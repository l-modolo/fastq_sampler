#!/usr/bin/python3
# -*-coding:Utf-8 -*

#Copyright (C) 2013 Laurent Modolo

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU Lesser General Public
#License as published by the Free Software Foundation; either
#version 2.1 of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#Lesser General Public License for more details.

#You should have received a copy of the GNU Lesser General Public
#License along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
import time
import sys
import random
import argparse
import ntpath

def path_leaf(path) :
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)

parser = argparse.ArgumentParser(prog='fastq_sampler')
parser.add_argument('-i', action='store', dest='number', help='number of reads to sample')
parser.add_argument('-f', action='store', dest='fileName1', help='fastq')
parser.add_argument('-g', action='store', dest='fileName2', help='fastq paired')
args = parser.parse_args()

print( "number of reads to sample : ", args.number, "\nfastq : ", args.fileName1 )
k = int(args.number)
maxval = k
if len(args.fileName2) > 0 :
	print("fastq paired : ", args.fileName2)

sys.stdout.write("counting reads number ...")
sys.stdout.flush()
with open(args.fileName1, 'r') as file1 :
	np = sum(1 for line in file1)

np = int((np) / 4)
sys.stdout.write("\rtotal number of reads : "+str(np)+"\n")
sys.stdout.flush()

population = range(1,np)
tirages = random.sample(population, k)

tirages.sort()
i = 0
while i < len(tirages) :
	tirages[i] = ((tirages[i]-1) * 4)
	i += 1

sys.stdout.write(str(0)+"/"+str(maxval))
sys.stdout.flush()
# extraction des tirage pour le fichier 1
with open(args.fileName1, 'r') as file1 :
		i = 0
		j = 0
		with open("s_"+path_leaf(args.fileName1), 'w') as output :
			for line in file1 :
				if j < len(tirages) :
					if tirages[j] <= i and i <= (tirages[j]+3) :
						output.write(str(line))
					if i >= (tirages[j]+3) :
						j += 1
						if j % 100 == 0:
							sys.stdout.write("\r"+str(j)+"/"+str(maxval))
							sys.stdout.flush()
					i += 1
				else :
					break
sys.stdout.write("\r"+"s_"+path_leaf(args.fileName1)+" done.\n")

sys.stdout.write(str(0)+"/"+str(maxval))
sys.stdout.flush()
# extraction des tirage pour le fichier 2
with open(args.fileName2, 'r') as file2 :
		i = 0
		j = 0
		with open("s_"+path_leaf(args.fileName2), 'w') as output :
			for line in file2 :
				if j < len(tirages) :
					if tirages[j] <= i and i <= (tirages[j]+3) :
						output.write(str(line))
					if i >= (tirages[j]+3) :
						j += 1
						if j % 100 == 0:
							sys.stdout.write("\r"+str(j)+"/"+str(maxval))
							sys.stdout.flush()
					i += 1
				else :
					break
sys.stdout.write("\r"+"s_"+path_leaf(args.fileName2)+" done.\n")
sys.stdout.flush()
