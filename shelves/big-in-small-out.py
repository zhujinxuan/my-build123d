#!/usr/bin/env python3

from build123d import *
from build123d import export_stl
from yacv_server import show, export_all

length, thickness = 160, 40
gridSize = 10;

with BuildPart() as pillar0:
  Box(length, thickness, thickness)
  with Locations((gridSize, gridSize/2, 0)):
    Box(2*gridSize, gridSize, thickness, mode=Mode.SUBTRACT)
  with Locations((gridSize * 0.5, gridSize/2, -gridSize*1.5)):
    Box(3*gridSize, gridSize, gridSize, mode=Mode.SUBTRACT)
  with BuildSketch(pillar0.faces().sort_by(Axis.Y)[0]):
    with BuildLine():
        a,b,c = (-gridSize, -gridSize), (-gridSize * 2, -gridSize * 2), ( -gridSize * 2,0)
        Line(a,b)
        Line(b,c)
        Line(c,a)
    make_face()
  extrude(amount=-gridSize, mode=Mode.SUBTRACT)

q = mirror(mirror(pillar0.part, Plane.XZ), Plane.YZ)
pillar = pillar0.part & q.rotate(Axis.X, 90)
export_stl(pillar, 'test.stl')
# show(pillar)
