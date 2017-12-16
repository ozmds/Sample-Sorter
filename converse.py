import sys, os.path
sys.path.insert(1, os.path.abspath("auger"))

import auger
import conversesorter, conversekeyword, report, sample

def main():
    conversesorter.PackLibrary().create(sys.argv)

if __name__ == '__main__':
    #with auger.magic([conversesorter, conversekeyword, report, sample]):
    main()
