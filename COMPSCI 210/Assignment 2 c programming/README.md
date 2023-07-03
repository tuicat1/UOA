# Assignment 2

This program performs a convolution on a two-dimensional array of integers with a given two-dimensional array of integers as a filter. 

## Prerequisites

- `gcc` installed 
- data files and filter files

## Usage

1. Compile C source code to executables: e.g. `gcc ./convolution1.c -o ./convolution1`
2. Pass data files to the output executables: e.g. `./convolution2 ./data1.txt ./filter1.txt temp2 12` in which:
    - `./convolution2` is the executable file
    - `./data1.txt` is the data file for the data matrix
    - `./filter1.txt` is the filter file for the filter matrix
    - `temp2` is the output file for the output matrix
    - `12` is the number of convolutions
3. Timing the execution time of the programme[^0] : `time ./convolution2 ./data1.txt ./filter1.txt temp2 12`

[^0]: `#include <time.h>`