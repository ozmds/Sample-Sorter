#### Update: Archiving this repo as Converse Sample Library has been discontinued.

# Sample-Sorter
A small commandline tool that you can use to sort music samples from the [Converse Sample Library](https://www.conversesamplelibrary.com/).

## Usage
Running `converse.py` with a set of Converse Sample files in the `/source files` directory, seperated by Converse Pack, will sort the files into the `/sorted files` directory.

## Testing
Unit tests have been implemented using the [Auger Testing Framework](https://github.com/laffra/auger). The unit tests have already been created under the `scripts/tests folder`, but can be recreated by running the `scripts/testdata/test.py` with a subset of sample files present in the `scripts/testdata/source files`, seperated by Converse Pack.

## Credits

#### Converse Sample Library
[Converse Sample Library](https://www.conversesamplelibrary.com/) is a large collection of royalty-free samples from a wide variety of genres, recorded in Converse Rubber Tracks Studios across the world.

#### Auger
[Auger](https://github.com/laffra/auger) is a Python library that auto generates unit tests to aid in the development of any Python project. It currently cannot be installed with pip, and so it has been included in my repository and imported into my code.

#### Dominate
[Dominate](https://github.com/Knio/dominate) is a Python library that allows you to generate HTML code strictly with Python, eliminating the need to use a seperate templating language.
