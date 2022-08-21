#!/usr/bin/env python3
from data.raw_triplets import triplets
from scripts.pythagorean_triplets import *


def main():
   df = data_to_df(triplets)
   print (df)

if __name__ == '__main__':
   main()
