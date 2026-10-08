#!/usr/bin/env python3
"""Check the countable writing rules, not full ASD-STE100 compliance.

Usage: check_text.py narration.txt | index.html

HTML requires data-ste="desc" (25 words/sentence) or data-ste="proc"
(20 words/sentence). Classification is inherited by child blocks. Paragraphs
allow six sentences. Mark non-prose labels data-ste="ui" and quoted source
blocks data-ste="quote" to exclude them explicitly. Exclusions are reported.
Unmarked legacy prose blocks are checked provisionally as descriptions AND
reported unclassified. Other unmarked text is reported uncovered.

Plain text uses blank-line paragraphs and the 25-word description limit.
Word counting preserves the original approximations: parenthetical text,
quoted text, formulas, numbers with units, and hyphenated words count as one;
parenthetical text is also checked separately. Warnings cover semicolons,
Latin abbreviations, passive voice with a named agent, HTML contractions, and
HTML main-path descriptions (outside <details>) above reading grade 4
(approximate Flesch-Kincaid, paragraphs of 10+ words). Reading grade is a
signal for the retell test in references/teaching.md, not a pass condition.
HTML main-path prose (desc and proc outside <details>) over about 250 words
also warns, as a signal for the idea budget. Pages with <main> also warn when
they lack an <h1> or an answer line (class="lead"), or when the main path has
more than one interactive part (distinct button data-group values outside
<details>). Leftover template placeholders such as [Topic title] outside
script, style, pre, and code are invalid structure (exit 2).

Exit codes: 0 = checked text passed (warnings/exclusions may remain);
1 = count violations with complete static coverage; 2 = incomplete coverage,
invalid classification/structure, or zero checked text (even with violations);
3 = usage/read error. All findings print regardless of exit precedence.

HTML parsing is static, not browser visibility analysis. CSS, generated text,
text-bearing attributes, external resources, canvas and runtime DOM changes
require browser review. Never treat exit 0 as full rendered-page coverage.
"""
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path

MAX_WORDS, MAX_SENTENCES = 25, 6
MAX_GRADE, MIN_GRADE_WORDS = 4.0, 10
MAX_MAIN_WORDS = 250
WORD = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)?")
UNITS = r"(?:%|°\s?[CF]?|mm|cm|km|m|kg|mg|g|ms|s|min|h|Hz|kHz|MHz|GHz|kW|W|V|A|KB|MB|GB|TB|px|ft|lb|psi|dB)\b"
LATIN = re.compile(r"\b(?:e\.g\.|i\.e\.|etc\.|viz\.|cf\.|et al\.)", re.I)
PASSIVE = re.compile(r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?"
                     r"(?:\w+ed|\w+en|\w+wn|built|made|held|sent|found|kept|set|put|done|led|told|paid|read)"
                     r"\s+by\b", re.I)
CONTRACTION = re.compile(r"\b\w+(?:n['’]t|['’](?:re|ve|ll|d|m))\b|\b(?:it|that|there|here|what|let)['’]s\b", re.I)
BLOCKS = {"p", "li", "dd", "dt", "td", "th", "figcaption", "blockquote", "caption", "summary"}
BOUNDARIES = BLOCKS | {
    "html", "body", "div", "section", "article", "main", "aside", "header",
    "footer", "nav", "ol", "ul", "table", "tr", "thead", "tbody", "tfoot",
    "h1", "h2", "h3", "h4", "h5", "h6", "button", "pre", "svg", "text",
}
SKIP = {"head", "script", "style", "noscript", "template", "title"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}
MODES = {"desc", "proc", "ui", "quote"}
PLACEHOLDER = re.compile(r"(?<!\\)\[[A-Za-z][^\]\n<>]{0,80}\]")
NON_PROSE = re.compile(r"<(script|style|pre|code)\b.*?</\1\s*>", re.S | re.I)


@dataclass
class TextBlock:
    text: str
    mode: str | None
    location: str
    provisional: bool = False
    excluded: str | None = None
    optional: bool = False


@dataclass
class Frame:
    tag: str
    mode: str | None
    excluded: str | None
    boundary: bool


class VisibleText(HTMLParser):
    """Collect static text once, preserving inline adjacency and block breaks."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.blocks = []
        self.issues = []
        self.buf = []
        self.context = None
        self.has_main = self.has_h1 = self.has_lead = False
        self.groups = set()

    def handle_starttag(self, tag, attrs):
        parent = self.stack[-1] if self.stack else None
        attr = dict(attrs)
        self.has_main |= tag == "main"
        self.has_h1 |= tag == "h1"
        self.has_lead |= "lead" in (attr.get("class") or "").split()
        if tag == "button" and attr.get("data-group") and not any(f.tag == "details" for f in self.stack):
            self.groups.add(attr["data-group"])
        mode = parent.mode if parent else None
        excluded = parent.excluded if parent else None
        values = [value for key, value in attrs if key == "data-ste"]
        if values:
            if len(values) != 1 or values[0] not in MODES:
                self.issues.append(
                    f"line {self.getpos()[0]} <{tag}> invalid data-ste {values!r}"
                )
                mode = None
            else:
                mode = values[0]
            if tag not in BOUNDARIES and tag not in VOID and mode != (parent.mode if parent else None):
                self.issues.append(
                    f"line {self.getpos()[0]} <{tag}> classification changes on inline markup; "
                    "classify its containing block instead"
                )
        if tag in SKIP:
            excluded = excluded or f"non-rendered <{tag}>"
        if any(key == "hidden" for key, _ in attrs):
            excluded = excluded or "hidden attribute"
        boundary = tag in BOUNDARIES or bool(excluded)
        if boundary:
            self.flush()
        if tag == "br":
            self.handle_data(" ")
        if tag not in VOID:
            self.stack.append(Frame(tag, mode, excluded, boundary))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        match = next((i for i in range(len(self.stack) - 1, -1, -1)
                      if self.stack[i].tag == tag), None)
        if match is None:
            self.issues.append(f"line {self.getpos()[0]} unmatched </{tag}>")
            return
        if match != len(self.stack) - 1:
            self.issues.append(f"line {self.getpos()[0]} misnested </{tag}>")
        if any(frame.boundary for frame in self.stack[match:]):
            self.flush()
        del self.stack[match:]

    def handle_data(self, data):
        frame = self.stack[-1] if self.stack else Frame("document", None, None, False)
        location = next((f.tag for f in reversed(self.stack) if f.boundary), frame.tag)
        provisional = frame.mode is None and any(f.tag in BLOCKS for f in self.stack)
        optional = any(f.tag == "details" for f in self.stack)
        context = (frame.mode, location, provisional, frame.excluded, optional)
        if context != self.context:
            self.flush()
            self.context = context
        self.buf.append(data)

    def flush(self):
        text = " ".join("".join(self.buf).split())
        if text:
            mode, location, provisional, excluded, optional = self.context
            self.blocks.append(TextBlock(text, mode, location, provisional, excluded, optional))
        self.buf = []

    def finish(self):
        self.close()
        self.flush()
        if self.stack:
            self.issues.append("unclosed elements: " + ", ".join(f.tag for f in self.stack))


def mask(text):
    """Collapse one-word units. Return masked text and parenthetical sentences."""
    inner = []
    text = re.sub(r"\\\(.*?\\\)|\\\[.*?\\\]|\$\$.*?\$\$", " FORMULA ", text)
    text = re.sub(r"[“\"][^”\"]+[”\"]", " QUOTE ", text)

    def paren(m):
        inner.append(m.group(1))
        return " PAREN "
    text = re.sub(r"\(([^()]*)\)", paren, text)
    text = re.sub(r"\b\d[\d.,]*\s?" + UNITS, " NUM ", text)
    return text, inner


def sentences(paragraph):
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9“\"(])", paragraph.strip()) if s.strip()]


def syllables(word):
    """Approximate syllables: vowel groups, minus a silent final e, at least one."""
    w = word.lower().replace("’", "").replace("'", "")
    n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and n > 1:
        n -= 1
    return max(1, n)


def reading_grade(text):
    """Flesch-Kincaid grade level, or None when the text is too short to judge."""
    words = WORD.findall(text)
    n_sents = max(1, len(sentences(text)))
    if len(words) < MIN_GRADE_WORDS:
        return None
    syl = sum(syllables(w) for w in words)
    return 0.39 * len(words) / n_sents + 11.8 * syl / len(words) - 15.59


def word_count(sentence):
    return len(sentence.split())


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if args == ["--help"] or args == ["-h"]:
        print(__doc__)
        return 0
    if len(args) != 1:
        print("INPUT ERROR: expected one UTF-8 .txt or .html path", file=sys.stderr)
        return 3
    path = args[0]
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"INPUT ERROR: {exc}", file=sys.stderr)
        return 3
    html = path.lower().endswith((".html", ".htm"))
    issues = []
    if html:
        parser = VisibleText()
        parser.feed(raw)
        parser.finish()
        blocks, issues = parser.blocks, parser.issues
        for m in PLACEHOLDER.finditer(NON_PROSE.sub(" ", raw)):
            issues.append(f"template placeholder left in page: {m.group(0)}")
    else:
        blocks = [TextBlock(" ".join(p.split()), "desc", "plain text")
                  for p in re.split(r"\n\s*\n", raw) if p.strip()]

    excluded = [b for b in blocks if b.excluded or b.mode in {"ui", "quote"}]
    visible = [b for b in blocks if not b.excluded and b.mode not in {"ui", "quote"}]
    unclassified = [b for b in visible if b.mode is None]
    paragraphs = [b for b in visible if b.mode in {"desc", "proc"} or b.provisional]
    errors, warnings, outline = [], [], []
    for i, block in enumerate(paragraphs, 1):
        para = block.text
        max_words = 20 if block.mode == "proc" else MAX_WORDS
        masked, inner = mask(para)
        sents = sentences(masked)
        orig = sentences(para)
        if orig:
            outline.append(f"{i:>3}. {orig[0]}")
        if len(sents) > MAX_SENTENCES:
            errors.append(f"paragraph {i}: {len(sents)} sentences (max {MAX_SENTENCES})")
        for s in sents + inner:
            n = word_count(s)
            if n > max_words:
                errors.append(f"paragraph {i}: {n} words (max {max_words}): {s.strip()[:90]}")
        if ";" in para:
            warnings.append(f"paragraph {i}: semicolon")
        for m in LATIN.findall(para):
            warnings.append(f"paragraph {i}: Latin abbreviation '{m}'")
        for m in PASSIVE.finditer(para):
            warnings.append(f"paragraph {i}: passive with a named agent '{m.group(0)}'")
        if html:
            for m in CONTRACTION.findall(para):
                warnings.append(f"paragraph {i}: contraction '{m}'")
            if block.mode == "desc" and not block.optional:
                grade = reading_grade(para)
                if grade is not None and grade > MAX_GRADE:
                    warnings.append(f"paragraph {i}: reading grade {grade:.1f} (main-path target {MAX_GRADE:.0f}): {para[:70]}")

    if html:
        main_words = sum(len(WORD.findall(b.text)) for b in paragraphs if not b.optional)
        if main_words > MAX_MAIN_WORDS:
            warnings.append(f"main path: {main_words} words (idea-budget target about {MAX_MAIN_WORDS})")
        if parser.has_main and not parser.has_h1:
            warnings.append("top: no <h1> title that names the topic")
        if parser.has_main and not parser.has_lead:
            warnings.append('top: no answer line (class="lead") under the title')
        if len(parser.groups) > 1:
            warnings.append(f"main path: {len(parser.groups)} interactive parts (idea-budget target 1)")
    print(f"{len(paragraphs)} paragraphs checked in {path}")
    for e in errors:
        print("ERROR   ", e)
    for w in warnings:
        print("WARN    ", w)
    if html:
        print(f"COVERAGE: {len(unclassified)} unclassified/uncovered text blocks; "
              f"{len(excluded)} excluded text blocks")
        for b in unclassified:
            kind = "UNCLASSIFIED (provisional desc check)" if b.provisional else "UNCOVERED"
            print(f"{kind} <{b.location}>: {b.text[:120]}")
        for b in excluded:
            reason = b.excluded or f'data-ste="{b.mode}"'
            preview = "" if b.excluded else f": {b.text[:120]}"
            print(f"EXCLUDED <{b.location}> {reason}, {len(b.text)} characters{preview}")
        print("LIMIT: static HTML text only. CSS visibility/generated text, text-bearing "
              "attributes, external resources, canvas, JavaScript and dynamic DOM text "
              "are not checked. Browser review is required; no full rendered-page coverage claim.")
    for issue in issues:
        print("INCOMPLETE", issue)
    if not paragraphs:
        print("INCOMPLETE: zero paragraphs checked")
    print("\nOutline (first sentence of each paragraph). It should tell the story alone:")
    print("\n".join(outline))
    incomplete = bool(unclassified or issues or not paragraphs)
    status = 2 if incomplete else 1 if errors else 0
    labels = {0: "CHECKED TEXT PASSED", 1: "COUNT VIOLATIONS", 2: "INCOMPLETE"}
    print(f"\nSTATUS {status}: {labels[status]}; {len(errors)} errors; {len(warnings)} warnings")
    return status


if __name__ == "__main__":
    sys.exit(main())
