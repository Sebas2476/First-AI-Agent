import os

def get_files_info(working_directory: str, directory: str = "."):
    working_directory_abs = os.path.abspath(working_directory)
    trg_directory = os.path.normpath(os.path.join(working_directory_abs, directory))
    valid_target_dir = os.path.commonpath([working_directory_abs, trg_directory]) == working_directory_abs
    try:
        if not valid_target_dir: 
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(trg_directory):
            return f'Error: "{directory}" is not a directory'
        else:
            return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"Error: {e}"