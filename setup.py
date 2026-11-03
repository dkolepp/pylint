from setuptools import setup

setup(
    name='pylint_shim',
    version='0.0.1',
    install_requires=['pylint==4.0.9','isort==4.3'],
    scripts=['pylint-shim.py'],
)

