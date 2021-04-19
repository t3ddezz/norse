from setuptools import setup
import glob
import os
import pkg_resources


setup(name='norse',
      version='0,1'
      scripts=['GUI/GUI.py'],
      install_requires=[
            "biopython>=1.70",
            'pandas>=1.0.1',
            "wheel>=0.34",
            'joblib>=0.11',
            'pysam>=0.16.0',
            'scikit-learn==0.23.1',
            "PuLP>=2"
        ],
      description='sequencing data transfer script as GUI',
      url='https://github.com/cov-lineages/pangolin',
      entry_points="""
      [console_scripts]
      {program} = norse.gui:MyWindow
      """.format(program = 'norse')
