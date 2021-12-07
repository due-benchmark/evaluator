# -*- coding: utf-8 -*-

import unittest

from due_evaluator.scorers.fscorer import FScorer


class TestFscorer(unittest.TestCase):
    """Tests for FScorer class."""

    def from_items(self, vals):
        anns = []
        for key, val in vals:
            anns.append({
                'key': key,
                'values': [
                    {'value': val, 'value_variants': val}
                ]
            })
        return {
            'name': 'test',
            'annotations': anns
        }

    def test_all(self):
        """Test all methods together."""
        scorer = FScorer()
        ref = {
            'name': '01e707f2d8b8d070d1d8ee90e8b2e7d6',
            'extension': 'pdf',
            'annotations': [
                {'id': '0', 'key': 'effective_date', 'values': [{'value': '2017-02-24'}], 'score': None},
                {'id': '1', 'key': 'jurisdiction', 'values': [{'value': 'Ohio'}], 'score': None},
                {'id': '2', 'key': 'party', 'values': [{'value': 'Dennis W. Wells'}, {'value': 'Lsi Industries Inc.'}], 'score': None},
            ],
            'language': 'en',
        }
        pred = {
            'name': '01e707f2d8b8d070d1d8ee90e8b2e7d6',
            'extension': 'pdf',
            'annotations': [
                {'id': '0', 'key': 'effective_date', 'values': [{'value': '2017-02-24'}], 'score': '0.7924'},
                {'id': '1', 'key': 'jurisdiction', 'values': [{'value': 'Ohio'}], 'score': '0.8324'},
                {'id': '2', 'key': 'party', 'values': [{'value': 'Lsi Industries Inc.'}, {'value': 'DEnnis W. Wells'}], 'score': '0.5164'}
            ],
            'language': 'en'
        }
        scorer.add(pred, ref)
        self.assertAlmostEqual(scorer.precision(), 3/4)
        self.assertAlmostEqual(scorer.recall(), 3/4)
        self.assertAlmostEqual(scorer.f_score(), 3/4)

    def test_empty_fscorer(self):
        """Test empty scorer."""
        fscorer = FScorer()
        self.assertAlmostEqual(fscorer.precision(), 0)
        self.assertAlmostEqual(fscorer.recall(), 0)
        self.assertAlmostEqual(fscorer.f_score(), 0)

