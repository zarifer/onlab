import csv
import os

files = os.listdir('/home/nimda/Documents/outputs/malset1/merged_sol/')
data = []

for file in files:
	with open(f'/home/nimda/Documents/outputs/malset1/merged_sol/{file}') as f:
		lines = f.readlines()
		try:
			data.append([int(float(l.split("\n")[0])*1000)/1000 for l in lines])
		except Exception as e:
			print(lines)
			continue
			
            
with open('dataset_merged.csv','w',newline = "") as f:
	spamwriter = csv.writer(f)
	spamwriter.writerows(data)
