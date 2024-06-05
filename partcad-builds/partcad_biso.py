from frame.biso import mkMortiseProto, BuildConfig
import build123d as b3d
from ocp_vscode import show_object

config = BuildConfig(tolerence=5)
mortise = mkMortiseProto(config)

show_object(mortise)
