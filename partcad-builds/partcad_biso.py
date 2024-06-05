from mortised_frame.biso import mkMortiseProto, BuildConfig
import build123d as b3d
from yacv_server import show
from numpy import arcsin

config = BuildConfig(tolerence=5)
print(config)
mortise = mkMortiseProto(config)

show(mortise)
