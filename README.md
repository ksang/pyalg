Fibonacci Heap
=============

A Fibonacci Heap implementation in Python, kaitoy@qq.com

Fibonacci Heap is a great data structure and works perfectly for graph algorithms like Dijkstra, I find it's necessary to write a python version during study.
It's majorly based on the original pseudo code and take advantage of some of python features.
Also there is a test available for study.
Anything you want to discuss please email.

Interface:
-------------

    minimun()
        - Get the node with minimun key value.
    merge(heap)
        - Merge another Fibonacci Heap into this one.
    insert(key, data)
        - Insert a new node with (key, data) pair.
    extract_min()
        - Extract the node in heap with minmun key value.
    decrease_key(node, key)
        - Decrease the key value of node provided.
    delete(node)
        - Delete the node from heap.

Reference:
-------------
Wiki:

[http://en.wikipedia.org/wiki/Fibonacci_heap](http://en.wikipedia.org/wiki/Fibonacci_heap)

Pseudo code:

[http://www.cs.princeton.edu/~wayne/cs423/fibonacci/FibonacciHeapAlgorithm.html](http://www.cs.princeton.edu/~wayne/cs423/fibonacci/FibonacciHeapAlgorithm.html)

Java code:

[http://keithschwarz.com/interesting/code/?dir=fibonacci-heap](http://keithschwarz.com/interesting/code/?dir=fibonacci-heap)

