
import numpy as np
from numpy.linalg import norm

def line_circle_intersect(p1, p2, c, r):
    dis = p2 - p1
    diff = c - p1
    t = np.dot(diff, dis) / np.dot(dis, dis)
    if t < 0.0:
        t = 0.0
    if t > 1.0:
        t = 1.0
    closest = p1 + t * dis
    d = c - closest
    return np.dot(d, d) <= r * r
