import pathlib
# from datetime import datetime
""" SHORTCUTS TABLE 
r = reconstruction
b = batch
v = vertex
d = dict / dir 
s = string or split 
vn = vertex normals
f = face
fn = face normals 
gt = ground truth
tp = template
i = index 
fp = file path 
dp = directory path 
hp = hyper parameters 
ds = dataset 
You can also concatenate - gtrb = Ground Truth Reconstruction Batched  
"""
# ----------------------------------------------------------------------------------------------------------------------
#                                              COMPUTATION CONFIG
# ----------------------------------------------------------------------------------------------------------------------
# TODO: I think it's better to save the config file for hard coded constants, paths and similar.
#  Most of the variables defined here should be accessible from the experiment interface
#  (it is confusing to split the experiment paramters into different files). If the experiment interface gets long we can order in neatly in a new file (not config)
# TIP: Use CTRL + SHIFT + f in PyCharm to detect where these are used in the system

RANDOM_SEED = 2147483647  # The global random seed. Use datetime.now() For a truly random seed
DEF_COMPUTE_PRECISION = 'float32' # Default computation precision used through out the entire system
# Options are: float64,float32 or float16. PyTorch defaults to float32. VTK does not work with float16 [Can be fixed]

NORMAL_MAGNITUDE_THRESH = 10 ** (-6) # The minimal norm allowed for vertex normals to decide that they are too small

# Hyper parameters that were removed from main.py
DEF_LR_SCHED_COOLDOWN = 5 # Number of epoches to wait after reducing the step-size. Works only if LR sched is enabled # TODO: remove to experiment interface. This is a learning rate paramter!
DEF_MINIMAL_LR = 1e-6 # The smallest learning step allowed with LR sched. Works only if LR sched is enabled # TODO: remove to experiment interface. This is a learning rate paramter!
NON_BLOCKING = True # Transfer to GPU in a non-blocking method
REPORT_LOSS_PER_BATCH = False # If True - will output train loss to logger on every batch. Otherwise - on every epoch
MAX_EPOCHS = 1000
N_MESH_SETS = 2 # Parallel plot will plot 8 meshes for each mesh set - 4 from train, 4 from vald
# ----------------------------------------------------------------------------------------------------------------------
#                                               PATH CONFIG
# ----------------------------------------------------------------------------------------------------------------------

PRIMARY_RESULTS_DIR = (pathlib.Path(__file__).parents[0] / '..' / '..' / 'results').resolve()
PRIMARY_DATA_DIR = (pathlib.Path(__file__).parents[0] / '..' / '..' / 'data').resolve()

# ----------------------------------------------------------------------------------------------------------------------
#                                               ERROR CONFIG
# ----------------------------------------------------------------------------------------------------------------------
SUPPORTED_IN_CHANNELS = (3, 6, 12) # The possible supported input channels - either 3, 6 or 12
DANGEROUS_MASK_THRESH = 100 # The minimal length allowed for mask vertex indices.

# ----------------------------------------------------------------------------------------------------------------------
#                                               VISUALIZATION CONFIG
# ----------------------------------------------------------------------------------------------------------------------
# TODO: remove all to experiment interface
VIS_METHOD = 'spheres' # spheres,cloud,mesh  - Choose how to display the meshes
VIS_CMAP = 'summer' # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
# We use two colors: one for the mask verts [Right end of the spectrum] and one for the rest [Left end of the spectrum].
VIS_SHOW_GRID = False # Visualzie with grid?
VIS_SMOOTH_SHADING = False # Smooth out the mesh before visualization?  Applicable only for 'mesh' method
VIS_SHOW_EDGES = False # Visualize with edges? Applicable only for 'mesh' method

