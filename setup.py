from setuptools import setup
import glob
import os
import pkg_resources


setup(name='norse',
      version='0,1'
      scripts=['GUI/GUI.py'],
      install_requires=[
            "pandas==1.2.3",
            "PyQt5==5.15.3",
            "PyQt5-Qt==5.15.2",
            "PyQt5-sip==12.8.1",
            "qtwidgets==0.18",
            "requests==2.25.1",
            "paramiko==2.7.2"
        ],
      description='sequencing data transfer script as GUI',
      entry_points="""
      [console_scripts]
      {program} = norse.gui:MyWindow
      """.format(program = 'norse')
