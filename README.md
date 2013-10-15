fastq_sampler
=============

extract k reads from a fastq file or a pair of fastq files in the case of pairends reads without loading the files in memory:

example :
./fastq_sampler.py -h
./fastq_sampler.py -i number_of_reads -f file.fastq [ -g file2_pairends.fastq ]

As a drawback for the memory footprint, fastq_sampler.py as to read file.fastq from end to end two times: a first time to count the number of reads, and the second time to copy reads at uniformly random choosen positions (plus one time for file2_pairends.fastq at the same positions).

