import logging
from typing import List
from operator import itemgetter

import textdistance

from due_evaluator.scorers.base_scorer import BaseScorer

logger = logging.getLogger(__name__)


class AnlsScorer(BaseScorer):
    """ANSL Scorer."""

    def __init__(self, threshold: float = 0.5):
        self.__scores: List[float] = []
        self.threshold = threshold

    @property
    def scores(self):
        return self.__scores

    def add(self, out_items: List[dict], ref_items: List[dict]):
        """Add more items for computing corpus level scores.

        Args:
            out_items: outs from a single document (line)
            ref_items: reference of the evaluated document (line)

        """
        out_ann = sorted(out_items['annotations'], key=itemgetter('key'))
        ref_ann = sorted(ref_items['annotations'], key=itemgetter('key'))
        assert [a['key'][:100] for a in out_ann] == [a['key'][:100] for a in ref_ann]

        for out, ref in zip(out_ann, ref_ann):            
            assert len(out['values']) == 1
            val = out['values'][0]['value']
            possible_vals = ref['values'][0]['value_variants']
            best_score = max([textdistance.levenshtein.normalized_similarity(val, pos)
                              for pos in possible_vals])
            if 1 - self.threshold >= best_score:
                best_score = 0.0            
            self.__scores.append(best_score)

    def score(self) -> float:
        if self.__scores:
            return sum(self.__scores) / len(self.__scores)
        return 0.0

    @classmethod
    def support_feature_scores(cls) -> bool:
        return False

    @classmethod
    def metric_name(cls) -> str:
        return "ANLS"
