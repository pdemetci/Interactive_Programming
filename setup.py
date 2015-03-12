import os
import sys

ROOT_DIR = os.getenv('PUZZLE_PATH')

if not ROOT_DIR:
    print "please set PUZZLE_PATH to the project root directory\n"
    print "for example:"
    print "cd project_dir; export PUZZLE_PATH=`pwd`"
    exit()

sys.path.append(os.path.join(ROOT_DIR, "models"))
sys.path.append(os.path.join(ROOT_DIR, "controllers"))
sys.path.append(os.path.join(ROOT_DIR, "views"))
