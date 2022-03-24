import time
import argparse
import pprint as pp
import os

import pandas as pd
import numpy as np
from concorde.tsp import TSPSolver

if __name__ == "__main__":
    file = open('raw_data.txt', 'r')
    Lines = file.readlines()
    max_coord=4000
    raw_data=[]
    norm_data=[]
    coords=[]
    for line in Lines:
        split_line=line.split(' ')
        if len(split_line)>1:
            raw_data.append([x.strip() for x in split_line])
    for line in raw_data:    
        norm_data.append([int(x)/max_coord for x in line])

    norm_data = np.array(norm_data)

    solver = TSPSolver.from_data(norm_data[:,0], norm_data[:,1], norm="GEO")  
    solution = solver.solve()
    write_file= f"tsp100_test_concorde.txt"
    with open(write_file, "w") as f:
        f.write( " ".join( str(x)+str(" ")+str(y) for x,y in norm_data) )
        f.write( str(" ") + str('output') + str(" ") )
        f.write( str(" ").join( str(node_idx+1) for node_idx in solution.tour) )
        f.write( str(" ") + str(solution.tour[0]+1) + str(" ") )
        f.write( "\n" )    
