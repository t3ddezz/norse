from setuptools import setup, find_packages
import glob
import os
import pkg_resources



setup(
      name='norse',
      version="0.3.0",
      packages=find_packages(),
      include_package_data=True,
      scripts=['norse/main_script.py'],
      description='na',
      url='https://github.com/t3ddezz/norse',
      author='anton',
      entry_points="""
      [console_scripts]
      norse = norse.main_script:main
      """,
      keywords=[],
      zip_safe=False)
