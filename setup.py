from setuptools import find_packages, setup
from setuptools.extension import Extension

setup(name='ProjectTemplate_Python',
      version='1',
      description='Template for starting Python projects',
      author='Orell Garten',
      author_email='orell.garten@rub.de',
      url='http://github.com/orgarten',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      )
