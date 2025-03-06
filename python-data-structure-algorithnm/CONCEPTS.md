Big O notation helps describe the time complexity and space complexity of an algorithm in terms of how they scale with the size of the input. 

#### Definitions:
- Time Complexity: Measures the amount of time needed to execute an algorithm.
- Space Complexity: Measures the amount of memory or storage an algorithm requires.
- Both are analyzed asymptotically, meaning they focus on behavior as the input size grows significantly.

#### Big O Notation Purpose/ Describes algorithms based on:
- How fast they run → Time complexity
- How much space they take → Space complexity

The key idea is analyzing performance as the input size increases.


#### Metrics 

**O(1)**: Constant time. For exemple, accessing an element in an array by index and inserting/deleting in a hash table.

**O(n)**: Linear time: For example, finding max or min element in an array.

**O(log n)**: Logarithmic time: For example, a binary search on a sorted array.

**O(n^2)**: Quadratic time: For example, simple sorting algorithm, nested loops/

**O(n^3)** Cubic time: For example, multliplying two dense matrices.

**O(n log n)**: Linearithmic time: For example, efficient sortings algorithms.

**O(2 ^ n)**: Exponencial time: For example, recursive algoritms solve problems by dividing them into multiple subproblems.

**O(n!)**: Factorial time: 

**O(sqrt(n))** Square root time: 


#### Why is Big O Important?
- It helps understand how an algorithm scales as the input size increases.
- Allows comparison of different algorithms based on their efficiency.

### Algorithm Types Interview:

- Searching: Algorithms used to find an element in a data structure, such as **Binary Search** and **Linear Search**.
- Greedy: Algorithms that make locally optimal choices at each step, aiming for a globally optimal solution, such as Dijkstra's Algorithm.
- Recursive: Algorithms that solve problems by breaking them down into smaller instances of the same problem, like Factorial Calculation or Fibonacci Series.
- Backtracking: Algorithms that explore possible solutions incrementally and backtrack when a solution fails, such as the N-Queens Problem.
- Divide and Conquer – Algorithms that break a problem into smaller subproblems, solve them recursively, and combine their results, such as Merge Sort and Quick Sort.
- Dynamic Programming: An optimization technique that solves problems by breaking them into overlapping subproblems, like the Knapsack Problem or Fibonacci using Memoization.
- Brute-force: A straightforward approach that checks all possible solutions to find the correct one, such as String Matching Algorithms.
- Sorting: Algorithms that arrange data in a specific order, like Bubble Sort, Merge Sort, and Quick Sort.
- Hashing: A technique to map data to a fixed-size value using hash functions for fast access, used in Hash Tables and Cryptographic Applications.

### What is the "Two Pointer Technique"?

The Two Pointer Technique is an efficient algorithmic strategy used to solve problems involving arrays, strings, or linked lists. It involves using two pointers (or iterators) that traverse a data structure in a specific way to optimize the solution, typically reducing the time complexity compared to brute force approaches.

The two pointers can:

1. Move in opposite directions (e.g., one from the start and one from the end).
2. Move in the same direction but at different speeds.
3. Solve problems like searching, partitioning, or counting pairs with a certain condition.

Pseudocode

Here’s a generic pseudocode to illustrate the concept:

```
TwoPointerTechnique(arr, target):
    Initialize left pointer = 0
    Initialize right pointer = arr.length - 1

    while left < right:
        if condition_met_with(arr[left], arr[right], target):
            Perform desired action
        elif update_condition_for_left:
            Increment left pointer
        else:
            Decrement right pointer

    return result
```

##### Use Cases of the Two Pointer Technique

Finding Pairs with Specific Properties:

- Sum of two numbers equals a target.
- Difference between two numbers is a specific value.

Sorting and Searching:
- Merging two sorted arrays.
- Binary search optimizations.

Partitioning Arrays:
- Rearrange elements based on a condition (e.g., even and odd separation).

String Matching and Manipulation:

- Checking if a string is a palindrome.
- Sliding window problems.

Efficient Traversal:

- Removing duplicates from sorted arrays.
- Finding subarrays with a given sum.

### Pompts

```
What is "Two Pointer Technique" in the context of  data structure and algorithms?
Create a pseudocode illustrating the concept.
List some of the use cases of this technique.
```


### Algorithms Patterns

### Sliding Window Pattern

Explanation: The sliding window pattern is used to perform operations on a specific window (a contiguous subsequence) of data, typically in arrays or strings. You maintain a window that slides across the input, expanding or shrinking as needed, to compute results like maximum sums, minimum lengths, or counts of valid subarrays. It’s especially useful when you need to avoid reprocessing elements unnecessarily.

Fixed-size window: The window size stays constant, and you slide it across the data.
Variable-size window: The window grows or shrinks based on a condition (e.g., sum < target).

Key points:
- Used for problems involving contiguous subarrays or substrings.
- Optimizes brute-force approaches by dynamically adjusting the window size.
- Works best when dealing with fixed or variable-sized windows.

Pseudocode (Fixed-size Window - Maximum Sum Subarray of Size k):
```
function maxSumSubarray(arr, k):
    n = arr.length
    if n < k:
        return "Invalid"
    
    windowSum = sum(arr[0:k])  // Sum of first window
    maxSum = windowSum
    
    for i from k to n-1:
        windowSum = windowSum + arr[i] - arr[i-k]  // Slide window
        maxSum = max(maxSum, windowSum)
    
    return maxSum
```

### Two Pointer Pattern

Explanation: The two pointer pattern uses two indices (pointers) to traverse a data structure, often an array or string, to solve problems efficiently. The pointers can move toward each other, in the same direction, or be positioned strategically based on the problem’s constraints.

Common Uses: Finding pairs with a target sum, reversing strings, or partitioning arrays.

Key points:

- Used for problems that require searching pairs in sorted arrays.
- Reduces time complexity from O(N²) to O(N).

Pseudocode (Two Pointers - Pair with Target Sum in Sorted Array):
```
function findPair(arr, target):
    left = 0
    right = arr.length - 1
    
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == target:
            return [left, right]
        else if currentSum < target:
            left = left + 1
        else:
            right = right - 1
    
    return "No pair found"
```

### Top K Elements Pattern

Top K Elements Pattern
Explanation: This pattern finds the k largest or smallest elements in a dataset, often using a heap (min-heap or max-heap) or quickselect. It’s efficient for problems where sorting the entire array is overkill.

Key Idea: Maintain a heap of size k to track the top elements.

Key points:

- Used for problems requiring finding the largest, smallest, or most frequent elements.
- Often solved using heaps (priority queues).

Pseudocode (Find Top K Largest Elements with Min-Heap):
```
function topKElements(arr, k):
    heap = MinHeap()  // Min-heap to keep k largest elements
    
    for num in arr:
        heap.insert(num)
        if heap.size() > k:
            heap.extractMin()
    
    return heap.toArray()  // Remaining elements are top k
```