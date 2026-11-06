import numpy as np


def dot_product(
    a: list[float],
    b: list[float]
) -> float:

    a = np.array(a)
    b = np.array(b)

    return float(np.dot(a, b))


def vector_norm(
    vector: list[float]
) -> float:

    vector = np.array(vector)

    return float(np.linalg.norm(vector))


def cosine_similarity(
    a: list[float],
    b: list[float]
) -> float:

    a = np.array(a)
    b = np.array(b)

    denominator = (
        np.linalg.norm(a) *
        np.linalg.norm(b)
    )

    if denominator == 0:
        return 0.0

    return float(
        np.dot(a, b) / denominator
    )