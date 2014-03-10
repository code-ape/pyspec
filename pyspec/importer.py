import inspect
import imp
import sys, os

def pyspec_import(target_name):
    stack = inspect.stack()
    frames = [frame_obj[0] for frame_obj in stack]
    last_frame = frames[1]

    abs_path_name = os.path.abspath('..')
    sys.path.append(abs_path_name)
    path_name = "../" + target_name + ".py"
    temp = imp.find_module(target_name)
    mod = imp.load_module(target_name, *temp)
    last_frame.f_globals[target_name] = mod
    last_frame.f_locals[target_name] = mod

