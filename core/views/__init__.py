import os, glob

# Get the current directory of this file
current_dir = os.path.dirname(__file__)

# find all the *_views.py  in the folder
modules = glob.glob(os.path.join(current_dir, "*_views.py"))

for m in modules:
    # Get the module name without the path and extension
    module_name = os.path.basename(m)[:-3]
    if not module_name.startswith("_"):
        exec(f"from .{module_name} import *")
        # print(f"from .{module_name} import *")