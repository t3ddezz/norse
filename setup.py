from setuptools import setup
import glob
import os
import pkg_resources



setup(name='norse',
      version="0.3.0",
      scripts=['norse/norse_script.py'],
      description='na',
      url='https://github.com/t3ddezz/norse',
      author='anton',
      entry_points="""
      [console_scripts]
      norse = norse_script:main
      """,
      keywords=[],
      zip_safe=False)
