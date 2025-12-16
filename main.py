from argparse import ArgumentParser
from pathlib import Path
import subprocess


def main(projectname):
    '''
    Create a project directory and initialize it with:
    1. Readme.md
    2. requirements.txt
    3. Create a virtual environment
    4. Create a .gitignore file
    '''
    project_dir = Path.cwd().absolute() / projectname
    project_dir.mkdir()

    #create a README.md and requirements.txt
    (project_dir / 'README.md').touch()
    (project_dir / 'requirements.txt').touch()

    #create .gitignore 
    (project_dir / '.gitignore').touch()
    with open(project_dir / '.gitignore',mode="w") as f:
        f.write("\n".join([".venv","__pycache__"]))
    
    #create virtual environment
    cmd = ["python3","-m","venv",f"{projectname}/.venv"]
    try:
        subprocess.run(cmd,check=True, timeout=60)
    except subprocess.CalledProcessError as e:
        print("Command failed with non-zero exit code.",e)
    except subprocess.TimeoutExpired as e:
        print("Command time out.",e)
    except FileNotFoundError as e:
        print("File doesn't exists.",e)
  

if __name__=="__main__":
    parser = ArgumentParser()
    parser.add_argument("--project","-p",type=str,help="Your project name.")
    args = parser.parse_args()
    print(args)
    main(args.project)