from ww_joints.frame.biso import mkMortiseProto, BuildConfig
import build123d as b3d
from yacv_server import show

config = BuildConfig(tolerence=5)
mortise = mkMortiseProto(config)

show(mortise)
