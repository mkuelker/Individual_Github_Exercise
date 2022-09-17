
import numpy as np
from random_word import RandomWords

#Driver Code. Use pip install Random-Words and Numpy
def main():
    list = words_list()
    merge_sort(list)
    print(list)
    
#generates a list of random words using the randomwords package by Vaibhav Singh
def words_list():
    list = []
    list = r.get_random_words()
    return list;

#simple mergesort algorithm. 
def merge_sort(list):
    if len(list) > 1:
        p = len(list)//2
        r = list[:p]
        l = list[p:]

        merge_sort(r)
        merge_sort(l)

        r_idx = l_idx = idx = 0

        while r_idx < len(r) and l_idx < len(l):
            if r[r_idx] < l[l_idx]:
                list[idx] = r[r_idx]
                r_idx += 1
            else:
                list[idx] = l[l_idx]
                l_idx += 1 
            idx += 1

        while r_idx < len(r):
            list[idx] = r[r_idx]
            r_idx += 1
            idx += 1

        while l_idx < len(l):
            list[idx] = l[l_idx]
            l_idx += 1
            idx += 1

#run. This worked in jupiter lab so hopefully it isn't bad. 
r =  RandomWords()
main();

     
