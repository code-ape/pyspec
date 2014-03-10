    
import inspect    

def get_block_locals(depth = 0):
    stack = inspect.stack()
    frames = [frame_obj[0] for frame_obj in stack]
    targer_frame = frames[depth+1]
    return targer_frame.f_locals



