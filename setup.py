#!/usr/bin/env python
from setuptools import setup, find_packages

# avec ceci en place, nous pouvons installer 
# le package 'proprement' en faisant
# 
# pip install -e .
# 
# après quoi je pourrai utiliser le package 'snake'
# depuis n'importe où
# 
# $ cd /tmp
# $ cat > foo.py
# from snake import Game
# g = Game((10, 10), (5, 5))
# g.run()
# ˆD
# python3 foo.py
# ...

setup(
    name="snake",
    packages=find_packages(),
    install_requires=[
        "pygame",  # if needed we could have said
                   # "pygame==1.9.6"
    ],
)
