"""Filesystem regression tests; all fixtures live in a temporary directory."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

from migration_preflight import check_migration


class MigrationPreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / "source"
        self.destination = self.root / "destination"
        self.source.mkdir()
        (self.source / "empty").mkdir()
        (self.source / "data.bin").write_bytes(b"\x00original\xff")

    def copy(self):
        shutil.copytree(self.source, self.destination)

    def test_preflight_reads_without_creating_destination_or_changing_source(self):
        before = (self.source / "data.bin").read_bytes()
        report = check_migration(self.source, self.destination)
        self.assertTrue(report["passed"], report)
        self.assertEqual(report["source_files"], 1)
        self.assertFalse(self.destination.exists())
        self.assertEqual((self.source / "data.bin").read_bytes(), before)

    def test_exact_tree_copy_passes_but_existing_destination_blocks_preflight(self):
        self.copy()
        self.assertFalse(check_migration(self.source, self.destination)["passed"])
        self.assertTrue(check_migration(self.source, self.destination, verify=True)["passed"])

    def test_changed_bytes_missing_directory_and_extra_file_are_reported(self):
        self.copy()
        (self.destination / "data.bin").write_bytes(b"\x00modified\xff")
        (self.destination / "empty").rmdir()
        (self.destination / "stale.md").write_text("old run")
        report = check_migration(self.source, self.destination, verify=True)
        self.assertFalse(report["passed"])
        self.assertEqual(report["changed"], ["data.bin"])
        self.assertEqual(report["missing"], ["empty"])
        self.assertEqual(report["extra"], ["stale.md"])

    def test_case_variant_destination_or_ancestor_blocks_copy(self):
        occupied = self.root / "Destination"
        occupied.mkdir()
        for destination in (self.destination, self.destination / "child"):
            with self.subTest(destination=destination):
                report = check_migration(self.source, destination)
                self.assertFalse(report["passed"])
                self.assertIn("collision", report["error"])

    def test_case_collisions_inside_source_block_copy(self):
        first = self.source / "Card.md"
        second = self.source / "card.md"
        first.write_text("one")
        if second.exists():
            self.skipTest("Filesystem cannot hold case-distinct siblings")
        second.write_text("two")
        report = check_migration(self.source, self.destination)
        self.assertFalse(report["passed"])
        self.assertIn("collision", report["error"])

    def test_file_copy_and_root_type_mismatch(self):
        file_source = self.source / "data.bin"
        shutil.copyfile(file_source, self.destination)
        self.assertTrue(check_migration(file_source, self.destination, verify=True)["passed"])
        report = check_migration(self.source, self.destination, verify=True)
        self.assertFalse(report["passed"])
        self.assertIn(".", report["changed"])

    def test_zip_copy_checks_archive_bytes_even_when_members_match(self):
        source = self.source / "document.docx"
        for path, year in ((source, 2025), (self.destination, 2026)):
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr(zipfile.ZipInfo("word/document.xml", (year, 1, 1, 0, 0, 0)), b"<doc/>")
        report = check_migration(source, self.destination, verify=True)
        self.assertFalse(report["passed"])
        self.assertEqual(report["changed"], ["."])

    def test_missing_inputs_report_errors(self):
        for source, verify in ((self.root / "missing", False), (self.source, True)):
            with self.subTest(source=source, verify=verify):
                report = check_migration(source, self.destination, verify=verify)
                self.assertFalse(report["passed"])
                self.assertIn("error", report)

    def test_same_and_nested_paths_are_rejected(self):
        for destination in (self.source, self.source / "nested", self.root):
            with self.subTest(destination=destination):
                report = check_migration(self.source, destination)
                self.assertFalse(report["passed"])
                self.assertIn("non-overlapping", report["error"])

    def test_symlink_in_source_is_rejected_without_following(self):
        (self.source / "link").symlink_to(self.source / "data.bin")
        report = check_migration(self.source, self.destination)
        self.assertFalse(report["passed"])
        self.assertIn("unsupported", report["error"])

    def test_symlink_destination_ancestor_and_parent_traversal_are_rejected(self):
        alias = self.root / "alias"
        alias.symlink_to(self.source, target_is_directory=True)
        for destination in (alias / "child", alias / ".." / "copy"):
            with self.subTest(destination=destination):
                self.assertFalse(check_migration(self.source, destination)["passed"])

    def test_non_directory_ancestor_is_rejected(self):
        report = check_migration(self.source, self.source / "data.bin" / "child")
        self.assertFalse(report["passed"])
        self.assertIn("not a directory", report["error"])

    def test_cli_json_and_exit_status(self):
        script = Path(__file__).with_name("migration_preflight.py")
        command = [sys.executable, "-B", str(script), str(self.source), str(self.destination)]
        success = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertTrue(json.loads(success.stdout)["passed"])
        failure = subprocess.run(command + ["--verify"], capture_output=True, text=True)
        self.assertEqual(failure.returncode, 1, failure.stderr)
        self.assertFalse(json.loads(failure.stdout)["passed"])


if __name__ == "__main__":
    unittest.main()
