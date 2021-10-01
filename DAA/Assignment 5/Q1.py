import math

def cross(o, a, b):
    """
    Calculates cross between two vectors.

    :param o, a: vector
    :param o, b: vector
    :return: cross product
    """
    ox, oy = o
    ax, ay = a
    bx, by = b

    return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox)


def convex(points):
    """
    Calculates the concave hull for a list of points. Each point is a tuple
    containing the x- and y-coordinate.

    :param points: list of points
    :return: convex hull
    """
    dataset = sorted(set(points))  # Remove duplicates
    if len(dataset) <= 1:
        return dataset

    # Build lower hull
    lower = []
    for p in dataset:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(dataset):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

points = [(1, 4), (4, 4), (7, 4), (1, 3), (3, 3), (6, 3), (8, 3), (1, 2), (3, 2), (5, 2), (7, 2), (9, 2), (2, 1), (4, 1), (6, 1), (8, 1)]

print(convex(points))