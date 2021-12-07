# -*- coding: utf-8 -*-

"""Tests for evaluate function."""

import argparse
import os
import unittest

from due_evaluator import cli_main


class TestMain(unittest.TestCase):
    """Tests for CLI main."""

    def test_main(self):
        """Test if a main is runnable."""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        ans_path = dir_path + '/out.jsonl'
        ref_path = dir_path + '/ref.jsonl'

        with open(ans_path) as ans_file, open(ref_path) as ref_file:
            args = argparse.Namespace()
            args.out_files = [ans_file]
            args.reference = ref_file
            args.normalize_dates = False
            args.properties = None
            args.print_format = 'text'
            args.line_by_line = False
            args.return_score = 'F1'
            args.ignore_case = False
            args.columns = ['Precision', 'Recall', 'F1']
            args.metric = 'F1'
            cli_main(args)

        self.assertTrue(True)
