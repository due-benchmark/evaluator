# -*- coding: utf-8 -*-

import unittest

from due_evaluator.scorers.wtq_scorer import WtqScorer


class TestWtqScorer(unittest.TestCase):
    """Tests for AnlsScorer class."""

    def from_items(self, vals):
        anns = []
        for idx, key_vals in enumerate(vals):
            anns.append({
                'key': idx,
                'values': [{'value': [val], 'value_variants': [val]} for val in key_vals]
            })
        return {
            'name': 'test',
            'annotations': anns
        }

    @unittest.skip
    def test_all(self):
        """Test all methods together."""
        scorer = WtqScorer()
        out = self.from_items([
            ['university of california‘', 'university of virginia†‡*', str(10. + 1e-7)],
            ['aaa', 'bbb'],
        ])
        ref = self.from_items([
            ['university of california’', 'university of virginia', '10'],
            ['bbb'],
        ])
        scorer.add(out, ref)
        self.assertAlmostEqual(scorer.score(), 0.5)

    def test_empty_scorer(self):
        """Test empty scorer."""
        scorer = WtqScorer()
        self.assertAlmostEqual(scorer.score(), 0)

    @unittest.skip
    def test_wrong_answears(self):
        """Test all methods together."""
        scorer = WtqScorer()
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
        self.assertEqual(WtqScorer.metric_name(), 'WTQ')

    def test_support_feature_scores(self):
        self.assertEqual(WtqScorer.support_feature_scores(), False)
