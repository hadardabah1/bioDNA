# Open the file with read only permit
import timeit
import numpy as np
# import SeqIO
# from Bio import SeqIO


def cut_dna(start_index):
    start = timeit.default_timer()
    # f = open('Daniel001-MAP-ZN_S66_L001_R1_001.fastq')
    f = open('minifastq.fastq')
    # use readline() to read the first line
    line = f.readline()
    # לא לשנות
    startIndex= start_index
    endIndex=startIndex+12
    bassDNA = ('A', 'G', 'T', 'C')
    linelist = []

    # function to get unique values
    def unique2(list1):
        x = np.array(list1)
        return (np.unique(x))

    def unique(list1):
        # intilize a null list
        unique_list = []

        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
                # print list
        return unique_list

    def unique1(list1):
        # insert the list to the set
        list_set = set(list1)
        # convert the set to the list
        unique_list = (list(list_set))
        return unique_list

    def lineValue(line):
        for char in line:
            if char not in "ATCG \n":
                return False
        return True

    while line:
        # if line.startswith((bassDNA)):
            # print(line.startswith(("A","G","T","c")))
        if lineValue(line):
            # print(line.strip())
            linelist.append(line[startIndex:endIndex])
            # print(line[startIndex:endIndex])
        line = f.readline()

    f.close()
    # print(linelist)
    # print(unique2(linelist))
    print(len(unique2(linelist)))
    stop = timeit.default_timer()

    # print('Time: ', stop - start)

    #Time:  4.1779972
    #Time1:  4.312221
    #Time2:  4.316538400000001

def def_range(y):
    for x in range(y):
        print('line num is', x)
        cut_dna(x)

