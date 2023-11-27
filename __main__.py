from subprocess import run, CalledProcessError, PIPE
import shlex
from sys import executable, exit

    
# Check if a given tool is installed by running its '--version' command.
def is_tool_installed(tool):
    try:
        run([tool, "--version"], stdout=PIPE, stderr=PIPE, check=True)
        return True
    except CalledProcessError:
        return False


# Install 'pipx' if it is not already installed.
def install_pipx():
    try:
        if is_tool_installed("pipx"):
            print("pipx is already installed.")
        else:
            run([executable, "-m", "pip", "install", "--user", "pipx"], check=True)
            print("pipx installed successfully.")
    except CalledProcessError as e:
        print(f"Error installing pipx: {e}")
        exit(1)


# Install 'poetry' if it is not already installed.
def install_poetry():
    try:
        if is_tool_installed("poetry"):
            print("poetry is already installed.")
        else:
            run(["pipx", "install", "poetry"], check=True)
            print("poetry installed successfully.")
    except CalledProcessError as e:
        print(f"Error installing poetry: {e}")
        exit(1)
        

# Set up the package using 'poetry'.
def setup_package():
    try:
        # Check the version of poetry
        run(shlex.split("poetry -V"))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Commands to set up the package
        run(shlex.split("poetry install"))
        run(shlex.split("poetry update"))
        run(shlex.split("poetry shell"))


# Main function to execute the installation and setup process.
def main():
    install_pipx()
    install_poetry()
    setup_package()


if __name__ == "__main__":
    main()
