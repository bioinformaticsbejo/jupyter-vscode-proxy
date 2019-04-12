import os
import tempfile
import subprocess
import getpass
import shutil
from textwrap import dedent

def setup_vscode():
    def _get_vscode_env(port):
        return {
            'NOTEBOOK_DIR': os.environ.get("NOTEBOOK_DIR", os.environ.get("HOME", "/home/jovyan")),
        }

    def _get_vscode_cmd(port):
        # Other paths rsession maybe in

        other_paths = []

        if shutil.which('vscode'):
            executable = 'vscode'
        else:
            for op in other_paths:
                if os.path.exists(op):
                    executable = op
                    break
            else:
                raise FileNotFoundError('Can not find rsession in PATH')

        envi = _get_vscode_env(port)

        return [
            executable,
            'code-server',
            '--allow-http',
            '--no-auth',
            '--host=0.0.0.0',
            '--port=' + str(port),
            '--user-data-dir=' + os.path.join(envi['NOTEBOOK_DIR'], ".vscode", "user_data"),
            '--extensions-dir=' + os.path.join(envi['NOTEBOOK_DIR'], ".vscode", "extensions"),
            envi['NOTEBOOK_DIR']
        ]

    return {
        'command': _get_vscode_cmd,
        'environment': _get_vscode_env,
        'launcher_entry': {
            'title': 'VScode',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'visual-studio-code.svg')
        }
    }
