import sys
import angr
import networkx as nx
import numpy as np
import pandas as pd
import os
import subprocess

files = os.listdir('/home/nimda/Documents/ml-sample-pack-small/benign/arm/')
malwy = '4eb6cb5191619d2d637beb4e6d4dde3aa58e7549b288f0d27916fe2ccd24be6a'

#Subprocess.PIPE = std.out messages go in a pipeline
#Subprocess.Popen = opens a terminal, and calls the first argument, and separate them with space
#process.communicate = Fetching (read and secure) the data to get out from the pipeline
for file in files:
	print(file)
	process = subprocess.Popen(["python3", "connect.py", file, malwy], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	stdout, err = process.communicate()
	print(stdout, err)
