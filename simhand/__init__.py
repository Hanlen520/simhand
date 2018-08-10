import subprocess
import os
from simhand.config import AQUBE_PATH, AQUBE_URL


def get_aqube():
    if os.path.exists(AQUBE_PATH):
        old_cwd = os.getcwd()
        os.chdir(AQUBE_PATH)
        subprocess.run(['git', 'pull', '--rebase'])
        os.chdir(old_cwd)
    else:
        subprocess.run(['git', 'clone', AQUBE_URL])


get_aqube()
