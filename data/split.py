# splits data for training, validation and testing

from pathlib import Path
import numpy as np
import math

import argparse

CATEGORIES = ['train','test']

def ratio2(string):
    input = tuple(int(i) for i in string.split(','))
    if len(input) != 2:
        raise TypeError('ratio must be a comma-separated list of length 2')
    output = tuple(i/sum(input) for i in input)
    return output
    

parser = argparse.ArgumentParser(description='split data for training and testing')
parser.add_argument('path', type=str,
                    help='path to the data')
parser.add_argument('--ratio', dest='ratio', metavar='train,test', default='90,10',
                    help='ratio to divide (default: "90,10")', type=ratio2)

args = parser.parse_args()

data = np.load(args.path, mmap_mode='r')

splits = [0] + list(math.ceil(elt) for elt in np.cumsum(args.ratio)*data.shape[0])

for i in range(2):
    np.save(str(Path(args.path).with_suffix('')) + '-%s.split' % CATEGORIES[i], range(splits[i],splits[i+1]))