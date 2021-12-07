# -*- coding: utf-8 -*-

"""Tests for the DueEvaluator class."""

import unittest

from due_evaluator import DueEvaluator


class Test(unittest.TestCase):
    """Tests for evaluate function."""

    def from_items(self, vals):
        anns = []
        for key, val in vals:
            anns.append({
                'key': key,
                'values': [
                    {'value': val, 'value_variants': val}
                ]
            })
        return [{
            'name': 'test',
            'annotations': anns,
        }]
    
        docs = []
        for idx, (key, val) in enumerate(vals):
            docs.append({
                'name': idx,
                'annotations': [{
                    'key': key,
                    'values': [
                        {'value': val, 'value_variants': val}
                    ]
                }]
            })
        return docs

    def test_init(self):
        """Test: read file and check answers."""
        answers = self.from_items([
            ('are_counterparts', 'yes'),
            ('effective_date', '2011-11-08'),
            ('jurisdiction', 'New York'),
            ('first_party', 'JDA Software Group, Inc.'),
            ('second_party', 'Red Prairie Holding, Inc.'),
        ])
        reference = self.from_items([
            ('are_counterparts', 'yes'),
            ('effective_date', '2012-09-04'),
            ('first_party', 'JDA Software Group, Inc.'),
            ('jurisdiction', 'Delaware'),
            ('second_party', 'Red Prairie Holding, Inc.'),
            ('term', '2 years'),
        ])
        due = DueEvaluator(reference, answers)
        fscorer = due.general_scorer

        self.assertAlmostEqual(fscorer.precision(), 3 / 5)
        self.assertAlmostEqual(fscorer.recall(), 3 / 6)
        self.assertAlmostEqual(fscorer.f_score(), 6 / 11)

        self.assertAlmostEqual(due.property_scorers['first_party'].f_score(), 1.0)

    def test_property_set(self):
        """Test: read file and check answers."""
        answers = self.from_items([
            ('are_counterparts', 'yes'),
            ('effective_date', '2011-11-08'),
            ('jurisdiction', 'New York'),
            ('first_party', 'JDA Software Group, Inc.'),
            ('second_party', 'Red Prairie Holding, Inc.'),
        ])
        reference = self.from_items([
            ('are_counterparts', 'yes'),
            ('effective_date', '2012-09-04'),
            ('first_party', 'JDA Software Group, Inc.'),
            ('jurisdiction', 'Delaware'),
            ('second_party', 'Red Prairie Holding, Inc.'),
            ('term', '2 years'),
        ])
        property_set = set(['first_party'])
        due = DueEvaluator(reference, answers, property_set=property_set)
        fscorer = due.general_scorer

        self.assertAlmostEqual(fscorer.precision(), 1.0)
        self.assertAlmostEqual(fscorer.recall(), 1.0)
        self.assertAlmostEqual(fscorer.f_score(), 1.0)

    def test_get_mean_f1_score(self):
        """Test: read file and check answers."""
        answers = self.from_items([
            ('are_counterparts', 'yes'),
            ('effective_date', '2011-11-08'),
            ('jurisdiction', 'New York'),
            ('first_party', 'JDA Software Group, Inc.'),
            ('second_party', 'Red Prairie Holding, Inc.'),
        ])
        reference = self.from_items([
            ('are_counterparts', 'yes'),
            ('effective_date', '2012-09-04'),
            ('first_party', 'JDA Software Group, Inc.'),
            ('jurisdiction', 'Delaware'),
            ('second_party', 'Red Prairie Holding, Inc.'),
            ('term', '2 years'),
        ])
        due = DueEvaluator(reference, answers, metric='MEAN-F1')
        self.assertAlmostEqual(due.general_scorer.score(), 6 / 11)

    def test_ignore_case(self):
        """Test: read file and check answers."""
        answers = self.from_items([
            ('are_counterparts', 'yes'),
            ('effective_date', '2011-11-08'),
            ('jurisdiction', 'New York'),
            ('first_party', 'JDA SOFTWARE GROUP, INC.'),
            ('second_party', 'Red Prairie Holding, Inc.'),
        ])
        reference = self.from_items([
            ('are_counterparts', 'yes'),
            ('effective_date', '8 November 2011'),
            ('first_party', 'JDA Software Group, Inc.'),
            ('jurisdiction', 'Delaware'),
            ('second_party', 'Red Prairie Holding, Inc.'),
            ('term', '2 years'),
        ])
        due = DueEvaluator(reference, answers, ignore_case=True)
        self.assertAlmostEqual(due.property_scorers['first_party'].f_score(), 1.0)
