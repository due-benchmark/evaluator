# -*- coding: utf-8 -*-

import unittest

from due_evaluator.scorers import AnlsScorer


class TestAnlsScorer(unittest.TestCase):
    """Tests for AnlsScorer class."""

    def from_items(self, vals):
        anns = []
        for idx, val in enumerate(vals):
            anns.append({
                'key': idx,
                'values': [
                    {'value': val, 'value_variants': val}
                ]
            })
        return {
            'name': 'test',
            'annotations': anns
        }

    @unittest.skip
    def test_all(self):
        """Test all methods together."""
        scorer = AnlsScorer()
        out = self.from_items([
            ['university of california'],
            ['aashirvaad'],
        ])
        ref = self.from_items([
            ['university of california', 'University of California', 'university of california, san diego'],
            ['aashirvaad', 'Aashirvaad'],
        ])
        scorer.add(out, ref)
        self.assertAlmostEqual(scorer.score(), 1)

    def test_empty_fscorer(self):
        """Test empty scorer."""
        scorer = AnlsScorer()
        self.assertAlmostEqual(scorer.score(), 0)

    @unittest.skip
    def test_wrong_answears(self):
        """Test all methods together."""
        scorer = AnlsScorer()
        out = self.from_items([
            ['blabla'],
            ['bla'],
        ])
        ref = self.from_items([
            ['university of california', 'University of California', 'university of california, san diego'],
            ['aashirvaad', 'Aashirvaad'],
        ])
        scorer.add(out, ref)
        self.assertAlmostEqual(scorer.score(), 0)

    def test_metric_name(self):
        self.assertEqual(AnlsScorer.metric_name(), 'ANLS')

    def test_support_feature_scores(self):
        self.assertEqual(AnlsScorer.support_feature_scores(), False)
