# setup.py
from setuptools import setup, find_packages

setup(
    name='youtube_report',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tabulate>=0.9.0',
    ],
)