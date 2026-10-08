# ASD-STE100 methods for visual lessons

Read before writing visible lesson text and again during final review.

## Source and scope

These methods paraphrase selected writing rules from the user-supplied ASD-STE100 Simplified Technical English, Issue 9, dated 2025-01-15, Part 1. Rule identifiers below provide traceability. The full standard and its controlled dictionary are not bundled.

Use these methods for any topic or situation. They govern explanation, not visual design. Use ordinary clear vocabulary without enforcing the controlled dictionary. This is a selected-methods adaptation, not full STE implementation. Do not describe a lesson as STE-compliant, certified, or approved by ASD.

## Explanation

- Give information gradually. Introduce prerequisites before dependent ideas. Use meaningful connecting words to make the sequence explicit. Rules 6.1, 6.2, and 4.4.
- Give each descriptive sentence one main idea and no more than 25 words. Keep necessary articles and other words instead of compressing the sentence into fragments. Avoid contractions. Rules 4.1, 4.2, and 6.3.
- Give each paragraph one topic and at most six sentences. Start with a topic sentence. Read the topic sentences together to check the explanation's outline. Rules 6.4–6.6.
- Use lists when several conditions, items, or alternatives would make a sentence hard to follow. Rule 4.3.
- Use active voice. In a description, use passive voice only when the actor is unknown. Describe actions with verbs rather than abstract action nouns. Rules 3.6 and 3.7.
- Use the same technical noun for the same item throughout. Keep terminology and wording consistent. Rules 1.11 and 9.4.
- Break up long noun strings. Prefer no more than three words in a technical noun group, but do not corrupt proper names or exact identifiers. Rule 2.1, adapted for general lessons.
- Do not use semicolons. Rule 8.1.

## Instructions

When the page asks the reader to perform an action, distinguish that instruction from the description.

- Use no more than 20 words in each instruction sentence. Rule 5.1.
- Give one instruction per sentence unless actions must occur together. Rule 5.2.
- Start commands with an action verb. Rule 5.3.
- Put a necessary condition before the command. For example, “If the request contains private information, select the private option.” Rule 5.4.
- Use notes to explain, not to hide required actions. Rule 5.5.

## User-specific style

These choices are not requirements of ASD-STE100. `teaching.md` owns explanation structure, examples, and optional depth.

- Avoid filler, sales language, emojis, em dashes, and colons inside prose sentences.
- Preserve source quotations, code, names, units, and identifiers exactly. Do not silently rewrite evidence to meet a style rule.

## Text classification

Mark visible HTML text with `data-ste`. Classification can be inherited from a parent, but override it on a containing block wherever the text's purpose changes. Changing classification inside inline markup returns incomplete. Use explicit closing tags because the checker conservatively flags unclosed or misnested elements.

- `desc` identifies descriptions and uses the 25-word sentence limit.
- `proc` identifies commands and instructions and uses the 20-word sentence limit. Mark action buttons as instructions too.
- `ui` identifies short headings and non-instruction interface labels. These are declared exclusions from prose counting, not verified prose.
- `quote` identifies exact source quotations and literal source material that must not be rewritten. These are declared exclusions too.

For example, use `<p data-ste="desc">The system checks access.</p>` and `<button data-ste="proc">Check access</button>`. Do not mark lesson prose as `ui` or `quote` to bypass checks.

## Review

1. Inspect the checker output from the hub's command. Fix count violations and review wording warnings, the outline, and the separate coverage and exclusion reports. A reading-grade warning flags a main-path description above about grade 4. Use it to find candidates for the retell test in `teaching.md`. Simplify the words or move detail to an optional section, but never drop a fact to lower the number. A main-path word warning flags more than about 250 words of main-path prose. Use it to check the idea budget in `teaching.md`. Top and interactive-part warnings check the page structure in `visual-direction.md`. A leftover template placeholder makes the result incomplete.
2. Treat exit 0 as a pass only for the reported static-text scope. Exit 1 means violations, 2 means incomplete coverage, and 3 means an input error. Incomplete coverage takes precedence over violations, which are still printed. Zero checked content cannot pass. Warnings can remain at exit 0 and still require review.
3. Classify uncovered text and correct invalid classifications. Review every declared `ui` and `quote` exclusion. Confirm that actual instructions use `proc`. The checker cannot determine the semantic truth of those labels.
4. Review rendered states and JavaScript-generated text through the shared browser-testing workflow. Static HTML checking does not execute scripts, resolve CSS visibility, or prove coverage of runtime text. Check new text in those states rather than treating a static pass as full-page verification.
5. Check active voice, consistent terminology, ambiguous pronouns, and the outline manually. Confirm that simplification preserved conditions, uncertainty, and meaning. Word and sentence counting remain heuristic, not complete STE parsing.
6. Record checks as passed, failed, or unverified with actual results and their checked scope. Do not claim that the script checked meaning, factual accuracy, or teaching quality.

## Original example

Before

“Authorization failure results in the prevention of document retrieval.”

After

“If access is denied, the system cannot retrieve the document.”

The revision states the condition first and replaces abstract action nouns with verbs.
