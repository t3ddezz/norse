from setuptools import setup
import glob
import os
import pkg_resources



setup(name='norse',
      version="0.1",
      scripts=['norse/norse_script.py'],
      install_requires=[
            "pandas==1.2.3",
            "requests==2.25.1",
            "paramiko==2.7.2",
            "argparse==1.4.0",
            "openpyxl==3.0.7",
            "xlrd==2.0.1"],
      description='na',
      url='https://github.com/t3ddezz/norse',
      author='anton',
      entry_points="""
      [console_scripts]
      norse = norse_script:main
      """,
      keywords=[],
      zip_safe=False)
