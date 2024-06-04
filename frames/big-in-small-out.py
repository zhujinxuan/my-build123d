#!/usr/bin/env python3
from typing import Iterable, List, Tuple, Union
import build123d as b3d
from dataclasses import dataclass
from yacv_server import show


@dataclass
class BuildConfig:
    tolerence: float = 0.2
    gridUnit: float = 40
    chamferSize: float = 1


def mkFace(points: List[b3d.VectorLike]) -> b3d.Sketch:
    edges: List[b3d.Line] = [
        b3d.Line(points[i], points[i + 1]) for i in range(len(points) - 1)
    ]
    edges.append(b3d.Line(points[-1], points[0]))
    return b3d.make_face(edges)


def mkTriClap(
    config: BuildConfig,
):
    grid = config.gridUnit / 4
    pointsInt: List[Tuple[float, float]] = [(0.5, -0.5), (-1.0, -2.0), (2.0, -2.0)]
    points = [tuple(y * grid for y in x) for x in pointsInt]
    face = mkFace(points)
    return b3d.Plane.XY.offset(grid) * b3d.extrude(face, amount=grid)


def mkMidMort(config: BuildConfig):
    grid = config.gridUnit / 4
    pointsInt: List[Tuple[float, float]] = [
        (-2, -2),
        (2, -2),
        (2, 2),
        (1, 2),
        (1, 1),
        (0, 1),
        (0, -1),
        (-1, -1),
        (-2, -1),
    ]
    points = [tuple(y * grid for y in x) for x in pointsInt]
    return b3d.extrude(mkFace(points), amount=-grid)


config = BuildConfig()
mortise = mkTriClap(config) + mkMidMort(config)
show(mortise)
