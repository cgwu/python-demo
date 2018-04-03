#!/usr/bin/env python
# -*- coding: utf-8 -*-
import concurrent.futures
import time

number_list = [ i for i in range(1,11) ]

def evaluate_item(x):
    result_item = count(x)
    print("item " + str(x) + " result " + str(result_item))

def count(number):
    for i in range(0,10000000):
    #for i in range(0,100):
        i = i+1
    return i * number

if __name__ == '__main__':
    ## Sequential Execution
    start_time = time.clock()
    for item in number_list:
        evaluate_item(item)
    print("Sequential execution in " + str(time.clock() - start_time), "seconds")

    ## Thread pool Execution
    start_time_1 = time.clock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print("Thread execution in " + str(time.clock() - start_time_1), "seconds")

    ## Process pool Execution
    '''
    the ProcessPoolExecutor uses the multiprocessing module,
    which allows us to outflank the global interpreter lock and obtain a shorter execution time
    '''
    start_time_2 = time.clock()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print("Process execution in " + str(time.clock() - start_time_2), "seconds")

