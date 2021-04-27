from setuptools import setup
import glob
import os
import pkg_resources

from norse import __version__, _program


setup(name='norse',
      version=__version__,
      scripts=['norse/scripts/norse.py'],
      install_requires=[
            "pandas==1.2.3",
            "PyQt5==5.15.3",
            "PyQt5-Qt==5.15.2",
            "PyQt5-sip==12.8.1",
            "qtwidgets==0.18",
            "requests==2.25.1",
            "paramiko==2.7.2"],
      description='na',
      url='https://github.com/t3ddezz/norse',
      author='anton',
      entry_points={'console_scripts': 
      ['norse=norse.command:main']},
      zip_safe=False)
      