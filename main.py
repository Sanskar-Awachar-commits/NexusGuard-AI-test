import subprocess

def execute_command(command, *args):
    try:
        # Use subprocess.run with a list of arguments to avoid shell injection
        result = subprocess.run([command, *args], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Handle the error if the command fails
        print(f"Error executing command: {e}")
        return None

# Example usage:
command = "echo"
args = ["Hello, World!"]
output = execute_command(command, *args)
print(output)