import numpy as np

from .._metric import Metric, Score, metric

@metric
def sum() -> Metric:
    """Compute sum of all scores.

    Returns:
       sum metric
    """

    def metric(scores: list[Score]) -> float:
        return np.sum([score.as_float() for score in scores]).item()

    return metric
