import gdb
import os
import voltron

PACKAGE_DIR = os.path.dirname(voltron.__file__)

SCRIPT_PATH = [PACKAGE_DIR, 'entry.py']


def _abs_path(path):
    return os.path.abspath(os.path.join(*path))


def gdbundle_load():
    gdb.execute("source {}".format(_abs_path(SCRIPT_PATH)))
