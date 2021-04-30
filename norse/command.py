#!/usr/bin/env python3
import argparse
from norse import __version__
from . import _program
import sys


"""def get_parser():
    
    #Creates a new argument parser.
    
    parser = argparse.ArgumentParser(prog = _program,
    description='NA',
    usage='''norse [options]''')
    
    parser.add_argument("-v","--version", action='version', version=f"norse {__version__}")

    return parser"""



"""def main(args=None):
    
    #Main entry point for your project.
    #Args:
    #    args : list
    #        A of arguments as if they were input in the command line. Leave it
    #        None to use sys.argv.
    

    parser = get_parser()
    args = parser.parse_args(args)"""


def main():

    parser = argparse.ArgumentParser(prog = _program,
    description='norse blablabla',
    usage='''norse [options]''')

    parser.add_argument("-v","--version", action='version', version=f"norse {__version__}")

    

if __name__ == '__main__':
    main() 



    