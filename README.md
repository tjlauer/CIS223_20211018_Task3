# CIS223_Task3

In this practice, we will be implementing a the several sorting algorithms discussed in the class and experimenting with the runtime for these sorting algorithms.
- You are required to use python.
- For help you can use the lecture slides.

<br><hr>

## The Problem
1. Implement the insertion sort algorithm in python to sort in ascending order.
2. Implement the merge sort algorithm in python to sort in ascending order.
3. Implement the counting sort algorithm in python to sort in ascending order.
4. Compare the time for these implementations for the following cases. The code for recording the runtime is provided below.
5. Report your findings.

<b>Case A:</b> Input to the sort algorithm is a sorted list (ascending order)<br>
<b>Case B:</b> Input to the sort algorithm is a sorted list (descending order)<br>

Also vary the size of the input list for your experimentation:
1. 10,000
2. 100,000
3. 1000,000

[Note: There are 6 possible cases to run for each algorithm.]<br>
For each run take three readings and populate the table in the next section.

<br><hr>

## Recording the Runtime
To determine the sorting time, replace line 3 with appropriate function name.
1. <code>import time # Doc available @ https://docs.python.org/3/library/time.html</code>
2. <code>t = time.process_time()</code>
3. <code>a = my_insertion_sort(n)</code>
4. <code>elapsed_time = time.process_time() – t</code>
5. <code>print(elapsed_time) # Note down this time in the table</code>
