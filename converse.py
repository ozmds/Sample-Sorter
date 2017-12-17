import sys, os.path
sys.path.insert(1, os.path.abspath("scripts"))

import packlibrary

def main():
    packlibrary.PackLibrary('source files',
                            'sorted files',
                            'data/count.json',
                            'data/pack.json').create(sys.argv)

if __name__ == '__main__':
    main()
