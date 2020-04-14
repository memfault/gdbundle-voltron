import lldb
import os
import voltron

PACKAGE_DIR = os.path.dirname(voltron.__file__)

SCRIPT_PATH = [PACKAGE_DIR, 'entry.py']


def _abs_path(path):
    return os.path.abspath(os.path.join(*path))


def gdbundle_load():
    lldb.debugger.HandleCommand("command script import {}".format(_abs_path(SCRIPT_PATH)))
