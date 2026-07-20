import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    abs_path_for_dir = os.path.abspath(working_directory) 
    abs_file_path = os.path.normpath(os.path.join(abs_path_for_dir, file_path))
    command = ["python", abs_file_path] #command will be used to run a sub-process

    try:
        if not abs_file_path.startswith(abs_path_for_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        elif args:
            command.extend(args)
        
        CompletedProcess = subprocess.run(command, cwd=abs_path_for_dir, text=True, timeout=30, capture_output=True)
        output = f"STDOUT: {CompletedProcess.stdout}\nSTDERR: {CompletedProcess.stderr}"


        if CompletedProcess.stdout == "" and CompletedProcess.stderr == "":
            return "No output produced"
        elif CompletedProcess.returncode != 0:
            output += f"Process exited with code {CompletedProcess.returncode}"
            return output
        else:
            return output
       

    except Exception as e:
        return f"Error: {e}"