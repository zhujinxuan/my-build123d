#!/usr/bin/env python3

from build123d import *
from build123d import export_stl
from yacv_server import show, export_all

radius = 30
baseHeight = 60
thickness = 4
connectHeight = 15

base2d = RegularPolygon(radius=radius, side_count=8)

def mkBase():
    base = extrude(base2d, baseHeight)
    topf = base.faces().sort_by(Axis.Z).last
    base = base.chamfer(2,2,base.edges().group_by(Axis.Z)[0])
    base = base.chamfer(2,2,base.edges().group_by(Axis.Z)[-1])
    innerSketch = Plane(topf) * RegularPolygon(radius=radius - thickness, side_count=8)
    trimTop = Plane(topf) * (base2d - RegularPolygon(radius=radius - thickness/2, side_count=8))
    return base - extrude(innerSketch, amount=thickness - baseHeight) -  extrude(trimTop, amount = -connectHeight)


def mkCover():
    cover = extrude(base2d, connectHeight+thickness)
    topf = cover.faces().sort_by(Axis.Z).last
    cover = cover.chamfer(2,2,cover.edges().group_by(Axis.Z)[0])
    cover = cover.chamfer(2,2,cover.edges().group_by(Axis.Z)[-1])
    innerSketch = Plane(topf) * RegularPolygon(radius= radius - thickness/2 + 0.5, side_count=8)
    polygons = Sketch() + [
        Plane.XY * loc * RegularPolygon(radius = 3, side_count=8)
        for loc in PolarLocations(radius = radius * 1/2, count = 8, start_angle=45/2)
        ]
    return cover - extrude(innerSketch, amount=-connectHeight) - extrude(polygons, thickness)

cover = mkCover()
base = mkBase()
export_stl(cover, 'cover.stl')
export_stl(base, 'base.stl')
