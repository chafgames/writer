# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()
with open('VERSION') as f:
    version = f.read()
with open('requirements.test.txt') as f:
    test_requirements = []
    for line in f.readlines():
        test_requirements.append(line)
with open('requirements.txt') as f:
    requirements = []
    for line in f.readlines():
        requirements.append(line)

setup(
    name='writer',
    version=version,
    description='A Chafnut game...',
    long_description=readme,
    author='Chafnut Games',
    author_email='chaf@chafnut.com',
    url='https://github.com/chafgames/writer',
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['setuptools', 'wheel', 'pytest-runner'],
    tests_require=test_requirements,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'paneltest = writer.main:panels_entrypoint',
            'ascitest = writer.main:ascii_entrypoint',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

)
