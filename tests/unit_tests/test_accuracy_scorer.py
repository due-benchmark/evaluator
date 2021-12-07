# -*- coding: utf-8 -*-

import unittest

from due_evaluator.scorers.accuracy_scorer import AccuracyScorer


class TestAccuracyScorer(unittest.TestCase):
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

    def test_all(self):
        """Test all methods together."""
        scorer = AccuracyScorer()
        out = self.from_items([
            ['university of california', 'university of virginia'],
            ['aaa', 'bbb'],
        ])
        ref = self.from_items([
            ['university of california', 'university of virginia'],
            ['bbb'],
        ])
        scorer.add(out, ref)
        self.assertAlmostEqual(scorer.score(), 0.5)

    def test_empty_scorer(self):
        """Test empty scorer."""
        scorer = AccuracyScorer()
        self.assertAlmostEqual(scorer.score(), 0)

    def test_wrong_answears(self):
        """Test all methods together."""
        scorer = AccuracyScorer()
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
        self.assertEqual(AccuracyScorer.metric_name(), 'Accuracy')

    def test_support_feature_scores(self):
        self.assertEqual(AccuracyScorer.support_feature_scores(), False)
