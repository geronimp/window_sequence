import sys
from Bio import SeqIO
fa = SeqIO.parse(sys.argv[1], 'fasta')

for record in fa:
    
    start = 0
    end = 100 # Window
    slide = 10 # Change
    
    seq = str(record.seq)
    seq_length = len(seq)
    while seq_length>end:
        print ">%s~%i~%i" % (record.name, start, end)
        print seq[start:end]
        start += slide
        end += slide
