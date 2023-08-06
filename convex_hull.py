import math
from random import uniform
from collections import namedtuple
from typing import List
from matplotlib import pyplot as plt

Point = namedtuple("Point", "x y")
n = 20


def generate_random_points(n) -> List[Point]:
    random_points: List[Point] = n * [None]
    for i in range(n):
        x = round(uniform(0, 10), 3)
        y = round(uniform(0, 10), 3)
        p = Point(x, y)
        random_points[i] = p
    return random_points


def is_counter_clockwise(a: Point, b: Point, c: Point) -> bool:
    prod = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    if prod > 0:
        return True
    else:
        return False


def polar_angle(point: Point, start_point: Point):
    dx = point.x - start_point.x
    dy = point.y - start_point.y
    return math.atan2(dy, dx)


def convex_hull(points: List[Point], start_point: Point = None) -> list[Point]:
    sorted_points = sorted(points, key=lambda p: polar_angle(start_point, p))
    result = [sorted_points[0], sorted_points[1]]

    for i in range(2, len(sorted_points)):
        while len(result) >= 2:
            if is_counter_clockwise(result[-2], result[-1], sorted_points[i]):
                break
            result.pop()
        result.append(sorted_points[i])
    result.append(sorted_points[0])
    return result


def plot_points(points: List[Point], color: str = 'black', start_point: Point = None):
    plt.style.use('seaborn-darkgrid')
    x_coords = [p.x for p in points]
    y_coords = [p.y for p in points]

    plt.scatter(x_coords, y_coords, color=color)
    if start_point:
        plt.scatter(start_point.x, start_point.y, color='gold')


def plot_hull(hull: List[Point], start_point: Point):
    x_coords = [p.x for p in hull]
    y_coords = [p.y for p in hull]
    plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='black')
    plt.plot(start_point.x, start_point.y, 'g*')


def plot_convex_hull(points: List[Point]):
    plt.style.use('seaborn-darkgrid')
    start_point = min(points, key=lambda p: p.y)
    hull = convex_hull(points, start_point)
    plot_points(points, start_point=start_point)
    plot_hull(hull, start_point)


if __name__ == '__main__':
    points = generate_random_points(n)
    plot_convex_hull(points)
    plt.show()
