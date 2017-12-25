import sys, os.path
sys.path.insert(1, os.path.abspath("../../auger"))
sys.path.insert(2, os.path.abspath("../"))

import auger
import packlibrary, instrumentlibrary, packreport, sample, sortedlist

def main():
    packlibrary.PackLibrary('source files',
                            'sorted files',
                            'data/count.json',
                            'data/pack.json',
                            '../../css/main.css').create(sys.argv)

if __name__ == '__main__':
    with auger.magic([packlibrary,
                      instrumentlibrary,
                      packreport,
                      sample,
                      sortedlist]):
        main()
