from setuptools import setup, find_packages

setup(
    name='pylint_shim',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
      'console_scripts': [
        'pylint-shim = pylint_shim:run_pylint'
      ]
    },
    install_requires=['pylint==2.1.1'],
)

