import os
import csv
import numpy as np

TARGET_DIR = "/home/nimda/Documents/outputs/malset1/benign_arm_sol"

folders = os.listdir(TARGET_DIR)


all_lines = []
for folder in folders:
    if 'feature_vector.txt' in os.listdir(f"{TARGET_DIR}/{folder}"):
        try:
            with open(f'{TARGET_DIR}/{folder}/feature_vector.txt') as f:
                lines = f.readlines()
            
            lines = [int(float(l)*1000)/1000 for l in lines]
            all_lines.append(lines)
        except Exception as e:
            print(e)
            continue

with open('dataset_bn.csv','w') as f:
    spamwriter = csv.writer(f)
    spamwriter.writerows(all_lines)
