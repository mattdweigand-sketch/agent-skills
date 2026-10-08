"""Run with python -m unittest discover -s scripts -p 'test_check_text.py'."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest

import check_text


def words(count):
    return " ".join(["Word"] * count) + "."


class CheckTextTests(unittest.TestCase):
    def check(self, text, suffix=".html"):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / ("input" + suffix)
            path.write_text(text, encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                status = check_text.main([str(path)])
            return status, output.getvalue()

    def test_valid_description(self):
        status, output = self.check('<p data-ste="desc">This is clear.</p>')
        self.assertEqual(status, 0)
        self.assertIn("1 paragraphs checked", output)
        self.assertIn("0 unclassified/uncovered", output)

    def test_description_boundary(self):
        for count, expected in [(25, 0), (26, 1)]:
            with self.subTest(count=count):
                status, output = self.check(f'<p data-ste="desc">{words(count)}</p>')
                self.assertEqual(status, expected)
                if expected:
                    self.assertIn("26 words (max 25)", output)

    def test_procedure_boundary(self):
        for count, expected in [(20, 0), (21, 1)]:
            with self.subTest(count=count):
                status, output = self.check(f'<div data-ste="proc">{words(count)}</div>')
                self.assertEqual(status, expected)
                if expected:
                    self.assertIn("21 words (max 20)", output)

    def test_inherited_procedure_and_description_override(self):
        status, output = self.check(
            f'<section data-ste="proc"><p>{words(21)}</p>'
            f'<p data-ste="desc">{words(25)}</p></section>')
        self.assertEqual(status, 1)
        self.assertIn("2 paragraphs checked", output)
        self.assertIn("1 errors", output)

    def test_seven_sentences(self):
        for mode in ["desc", "proc"]:
            with self.subTest(mode=mode):
                status, output = self.check(f'<p data-ste="{mode}">' + "One. " * 7 + "</p>")
                self.assertEqual(status, 1)
                self.assertIn("7 sentences (max 6)", output)

    def test_six_sentences(self):
        self.assertEqual(self.check('<p data-ste="desc">' + "One. " * 6 + "</p>")[0], 0)

    def test_empty_input(self):
        for suffix in [".html", ".txt"]:
            with self.subTest(suffix=suffix):
                status, output = self.check(" \n ", suffix)
                self.assertEqual(status, 2)
                self.assertIn("zero paragraphs checked", output)

    def test_button_div_only(self):
        status, output = self.check("<button>Next</button><div>Visible text</div>")
        self.assertEqual(status, 2)
        self.assertIn("0 paragraphs checked", output)
        self.assertIn("2 unclassified/uncovered", output)
        self.assertIn("UNCOVERED <button>: Next", output)
        self.assertIn("UNCOVERED <div>: Visible text", output)

    def test_mixed_coverage(self):
        status, output = self.check('<p data-ste="desc">Clear.</p><button>Next</button>')
        self.assertEqual(status, 2)
        self.assertIn("1 paragraphs checked", output)
        self.assertIn("1 unclassified/uncovered", output)

    def test_unmarked_prose_checked_but_incomplete(self):
        status, output = self.check(f"<p>{words(26)}</p>")
        self.assertEqual(status, 2)
        self.assertIn("UNCLASSIFIED", output)
        self.assertIn("26 words (max 25)", output)
        self.assertIn("1 errors", output)

    def test_nested_inline_does_not_split_sentence(self):
        text = f'<p data-ste="proc">{words(19)[:-1]} <strong>one <em>two</em></strong>.</p>'
        status, output = self.check(text)
        self.assertEqual(status, 1)
        self.assertIn("21 words (max 20)", output)
        self.assertIn("1 paragraphs checked", output)

    def test_inline_adjacency_entities_and_break(self):
        parser = check_text.VisibleText()
        parser.feed('<p data-ste="desc">inter<strong>oper</strong>able &amp; useful<br>text.</p>')
        parser.finish()
        self.assertEqual(parser.blocks[0].text, "interoperable & useful text.")

    def test_repeated_inline_classification_does_not_split_sentence(self):
        status, output = self.check(
            f'<p data-ste="proc">{words(19)[:-1]} '
            '<span data-ste="proc">one two.</span></p>')
        self.assertEqual(status, 1)
        self.assertIn("21 words (max 20)", output)
        self.assertIn("1 paragraphs checked", output)

    def test_nested_blocks_not_double_counted(self):
        status, output = self.check(
            '<div data-ste="desc"><p>First.</p><p>Second.</p></div>')
        self.assertEqual(status, 0)
        self.assertIn("2 paragraphs checked", output)

    def test_malformed_classification(self):
        for marker in ['data-ste', 'data-ste=""', 'data-ste="unknown"',
                       'data-ste="PROC"', 'data-ste="proc" data-ste="desc"']:
            with self.subTest(marker=marker):
                status, output = self.check(f"<p {marker}>Text.</p>")
                self.assertEqual(status, 2)
                self.assertIn("invalid data-ste", output)

    def test_inline_mode_change_incomplete(self):
        status, output = self.check(
            '<p data-ste="desc">Start <span data-ste="proc">Do this.</span></p>')
        self.assertEqual(status, 2)
        self.assertIn("classification changes on inline markup", output)

    def test_malformed_structure(self):
        for text in ['<p data-ste="desc">Text.', '<p data-ste="desc"><b>Text.</p>']:
            with self.subTest(text=text):
                self.assertEqual(self.check(text)[0], 2)

    def test_warnings_remain_nonfatal(self):
        status, output = self.check(
            '<p data-ste="desc">It is made by users; it is useful, e.g. here. '
            "It's simple.</p>")
        self.assertEqual(status, 0)
        for warning in ["semicolon", "Latin abbreviation", "passive with a named agent", "contraction"]:
            self.assertIn(warning, output)

    def test_script_style_excluded_and_reported(self):
        status, output = self.check(
            f'<script>{words(40)}</script><style>{words(40)}</style>'
            '<p data-ste="desc">Clear.</p>')
        self.assertEqual(status, 0)
        self.assertIn("2 excluded text blocks", output)
        self.assertIn("non-rendered <script>", output)
        self.assertIn("non-rendered <style>", output)
        self.assertIn("JavaScript and dynamic DOM text", output)
        self.assertNotIn("40 words", output)

    def test_script_only_zero_checked(self):
        status, output = self.check("<script>document.body.innerText = 'Words';</script>")
        self.assertEqual(status, 2)
        self.assertIn("zero paragraphs checked", output)

    def test_ui_quote_exclusions(self):
        status, output = self.check(
            '<h1 data-ste="ui">Heading</h1><button data-ste="ui">Next</button>'
            f'<blockquote data-ste="quote">{words(50)}</blockquote>'
            '<p data-ste="desc">Clear.</p>')
        self.assertEqual(status, 0)
        self.assertIn("3 excluded text blocks", output)
        self.assertIn('data-ste="quote"', output)
        self.assertNotIn("50 words", output)

    def test_exclusions_only_incomplete(self):
        self.assertEqual(self.check('<h1 data-ste="ui">Heading</h1>')[0], 2)

    def test_svg_not_silently_skipped(self):
        status, output = self.check(
            '<p data-ste="desc">Clear.</p><svg><text>Chart label</text></svg>')
        self.assertEqual(status, 2)
        self.assertIn("Chart label", output)
        self.assertIn("1 unclassified/uncovered", output)

    def test_plain_text_paragraphs(self):
        status, output = self.check("First paragraph.\n\nSecond paragraph.", ".txt")
        self.assertEqual(status, 0)
        self.assertIn("2 paragraphs checked", output)

    def test_plain_text_word_limit(self):
        self.assertEqual(self.check(words(26), ".txt")[0], 1)

    def test_plain_text_contractions_not_warned(self):
        status, output = self.check("It's simple.", ".txt")
        self.assertEqual(status, 0)
        self.assertNotIn("contraction", output)

    def test_counting_preserved(self):
        masked, inner = check_text.mask(
            'Use "a long quoted phrase" (a parenthetical phrase) at 20 kg with state-of-the-art tools.')
        self.assertEqual(check_text.word_count(masked), 8)
        self.assertEqual(inner, ["a parenthetical phrase"])
        status, output = self.check(
            f'<p data-ste="proc">Use this ({words(21)}).</p>')
        self.assertEqual(status, 1)
        self.assertIn("21 words (max 20)", output)

    def test_simple_main_path_no_grade_warning(self):
        status, output = self.check(
            '<p data-ste="desc">The tool reads a review. It gives back a number. '
            'A high number means yes. You pick the cutoff.</p>')
        self.assertEqual(status, 0)
        self.assertNotIn("reading grade", output)

    def test_complex_main_path_grade_warning_is_nonfatal(self):
        status, output = self.check(
            '<p data-ste="desc">Probability-weighted aggregation of categorical '
            'classification distributions produces interpretable numerical '
            'evaluations for downstream automation.</p>')
        self.assertEqual(status, 0)
        self.assertIn("reading grade", output)

    def test_optional_details_skip_grade_warning(self):
        status, output = self.check(
            '<p data-ste="desc">The tool reads a review.</p>'
            '<details><summary data-ste="ui">More</summary>'
            '<p data-ste="desc">Probability-weighted aggregation of categorical '
            'classification distributions produces interpretable numerical '
            'evaluations for downstream automation.</p></details>')
        self.assertEqual(status, 0)
        self.assertNotIn("reading grade", output)

    def test_main_path_word_budget_warning(self):
        para = '<p data-ste="desc">' + "The tool reads a review. " * 5 + '</p>'
        status, output = self.check(para * 11)
        self.assertEqual(status, 0)
        self.assertIn("idea-budget target", output)

    def test_word_budget_ignores_optional_details(self):
        para = '<p data-ste="desc">' + "The tool reads a review. " * 5 + '</p>'
        status, output = self.check(
            '<p data-ste="desc">The tool reads a review.</p>'
            '<details><summary data-ste="ui">More</summary>' + para * 11 + '</details>')
        self.assertEqual(status, 0)
        self.assertNotIn("idea-budget target", output)

    def test_template_placeholder_is_incomplete(self):
        status, output = self.check('<main><h1 data-ste="ui">[Topic title]</h1></main>')
        self.assertEqual(status, 2)
        self.assertIn("template placeholder left in page: [Topic title]", output)

    def test_brackets_in_code_and_scripts_are_not_placeholders(self):
        status, output = self.check(
            '<p data-ste="desc">This is clear.</p><pre data-ste="quote">x[index]</pre>'
            '<p data-ste="desc">Use <code>items[first]</code> here.</p>'
            '<script>document.querySelector("[data-group]")</script>')
        self.assertEqual(status, 0)
        self.assertNotIn("placeholder", output)

    def test_page_top_warnings(self):
        status, output = self.check('<main><p data-ste="desc">This is clear.</p></main>')
        self.assertEqual(status, 0)
        self.assertIn("top: no <h1> title", output)
        self.assertIn("top: no answer line", output)
        status, output = self.check(
            '<main><h1 data-ste="ui">Topic</h1><p class="lead" data-ste="desc">This is clear.</p></main>')
        self.assertEqual(status, 0)
        self.assertIn("0 warnings", output)

    def test_interactive_part_budget(self):
        one = '<button data-group="a" data-ste="proc">A</button><button data-group="a" data-ste="proc">B</button>'
        two = one + '<button data-group="b" data-ste="proc">C</button>'
        optional = one + '<details><summary data-ste="proc">More</summary><button data-group="b" data-ste="proc">C</button></details>'
        for html, warned in [(one, False), (two, True), (optional, False)]:
            with self.subTest(warned=warned):
                status, output = self.check(f'<p data-ste="desc">This is clear.</p>{html}')
                self.assertEqual(status, 0)
                self.assertEqual("interactive parts" in output, warned)

    def test_input_errors(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(check_text.main([]), 3)
            self.assertEqual(check_text.main(["/missing/checker-test-input.txt"]), 3)
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "bad.txt"
                path.write_bytes(b"\xff")
                self.assertEqual(check_text.main([str(path)]), 3)

    def test_help_documents_statuses(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(check_text.main(["--help"]), 0)
        self.assertIn("Exit codes", output.getvalue())
        self.assertIn("3 = usage/read error", output.getvalue())


if __name__ == "__main__":
    unittest.main()
