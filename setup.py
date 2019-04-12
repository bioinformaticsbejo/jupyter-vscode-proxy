import setuptools

setuptools.setup(
    name="jupyter-vscode-proxy",
    version='1.0dev',
    url="https://github.com/bioinformaticsbejo/jupyter-vscode-proxy",
    author="Ryan Lovett; Yuvi Panda; Saulo Alves @ Bejo Zaden BV",
    description="Jupyter extension to proxy VScode session",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'vscode = jupyter_vscode_proxy:setup_vscode'
        ]
    },
    package_data={
        'jupyter_vscode_proxy': ['icons/*'],
    },
)
