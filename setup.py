from setuptools import setup, find_packages
import os

install_requires = []
requirement_dir = os.path.dirname(os.path.realpath(__file__))
requirement_file = f'{requirement_dir}/requirements.txt'
with open(requirement_file) as f:
    install_requires = f.read().splitlines()

setup(
    name='merlol',
    version='0.0.0',
    packages=find_packages(),
    install_requires=install_requires
)
