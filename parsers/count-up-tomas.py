import sys, os

def get_counts(file_in, i):
    l = []
    for line in open(file_in):
        dat = line.rstrip().split('\t')
        l.append(dat[i])
    return l

for n, f in enumerate(sys.argv[1:]): 
    if n == 0:
        fp = open("temp.tsv", 'w')
        list_of_counts = get_counts(f, 2)
        fp.write('DIRTY Name\t%s\n' % f)
        for n2, line in enumerate(open(f)):
            fp.write('%s' % line.rstrip().split('\t')[0])
            fp.write('\t%s' % list_of_counts[n2])
            fp.write('\n')
        fp.close()

    else:
        fp2 = open("temp.tsv", 'r')
        fp3 = open("summary-count.tsv", "w")
        list_of_counts = get_counts(f, 2)
        for n2, line in enumerate(fp2):
            if n2 == 0:
                fp3.write('%s' % line.rstrip())
                fp3.write('\t%s\n' % f)
            else:
                fp3.write('%s' % line.rstrip())
                fp3.write('\t%s' % list_of_counts[n2-1])
                fp3.write('\n')
        fp2.close()
        fp3.close()
        os.rename("summary-count.tsv", "temp.tsv")    

os.rename("temp.tsv", "summary-count.tsv")
