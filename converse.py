import sys, os.path
sys.path.insert(1, os.path.abspath("auger"))
sys.path.insert(2, os.path.abspath("scripts"))

import auger
import instrumentlibrary, packlibrary, packreport, report, sample, sortedlist

def main():
    packlibrary.PackLibrary().create(sys.argv)

if __name__ == '__main__':
    with auger.magic([instrumentlibrary, packlibrary, packreport, report, sample, sortedlist]):
        main()
