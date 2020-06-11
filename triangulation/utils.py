import numpy as np


class Line():

    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    @property
    def length(self):
        return np.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)

    @property
    def gradient(self):
        return (self.y2 - self.y1)/(self.x2 - self.x1)

    @property
    def intersect(self):
        return self.y1 - (self.gradient * self.x1)

    def x_in_range(self, x, strict=True):

        # is the value inside the range
        in_bounds = x >= min(self.x1, self.x2) and x <= max(self.x1, self.x2)

        # as we are dealing with floats we get some variation so we want to be extra careful
        is_close = np.isclose(x, self.x1) or np.isclose(x, self.x2)

        if strict:
            # if strict ignore close
            return in_bounds and not is_close
        else:
            # otherwise allow it
            return in_bounds or is_close


def intersection(l1, l2):
    """
    Do these lines intersect
    """

    # If the gradients are the same then we assume they do not intersect
    if l1.gradient == l2.gradient:
        return False
    else:
        # Find the intersection point if they were both infinite lines
        ix = (l1.intersect - l2.intersect) / (l2.gradient - l1.gradient)

        # is the point of intersection on the actual line?
        if l1.x_in_range(ix) and l2.x_in_range(ix):
            return True
        else:
            return False