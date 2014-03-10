from core import end, it
from importer import pyspec_import

import inspect
import imp
import sys, os

stack = inspect.stack()
frames = [frame_obj[0] for frame_obj in stack]
last_frame = frames[1]

for i in [end, it, pyspec_import]:
    last_frame.f_globals[i.__name__] = i
    last_frame.f_locals[i.__name__] = i

