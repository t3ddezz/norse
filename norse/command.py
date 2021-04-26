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


def main(sysargs = sys.argv[1:]):

    parser = argparse.ArgumentParser(prog = _program,
    description='norse blablabla',
    usage='''norse [options]''')


    parser.add_argument('--outfile', action="store",help="Optional output file name. Default: lineage_report.csv")
    parser.add_argument('--alignment', action="store_true",help="Optional alignment output.")
    parser.add_argument('-d', '--datadir', action='store',dest="datadir",help="Data directory minimally containing a fasta alignment and guide tree")
    parser.add_argument('--tempdir',action="store",help="Specify where you want the temp stuff to go. Default: $TMPDIR")
    parser.add_argument("--no-temp",action="store_true",help="Output all intermediate files, for dev purposes.")
    parser.add_argument('--decompress-model',action="store_true",dest="decompress",help="Permanently decompress the model file to save time running pangolin.")
    parser.add_argument('--max-ambig', action="store", default=0.5, type=float,help="Maximum proportion of Ns allowed for pangolin to attempt assignment. Default: 0.5",dest="maxambig")
    parser.add_argument('--min-length', action="store", default=10000, type=int,help="Minimum query length allowed for pangolin to attempt assignment. Default: 10000",dest="minlen")
    parser.add_argument('--panGUIlin', action='store_true',help="Run web-app version of pangolin",dest="panGUIlin")
    parser.add_argument("--verbose",action="store_true",help="Print lots of stuff to screen")
    parser.add_argument("-t","--threads",action="store",help="Number of threads")
    parser.add_argument("-v","--version", action='version', version=f"pangolin {__version__}")
    parser.add_argument("-pv","--pangoLEARN-version", action='version', version=f"pangoLEARN {pangoLEARN.__version__}",help="show pangoLEARN's version number and exit")
    parser.add_argument("--update", action='store_true', default=False, help="Automatically updates to latest release of pangolin and pangoLEARN, then exits")

if __name__ == '__main__':
    main()