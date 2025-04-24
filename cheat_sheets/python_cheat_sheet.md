Okay, here are the Python code examples presented in the video, ordered by their appearance:

1.  **Variables - Dynamic Typing (01:15 - 01:42)**
    ```python
    # Variables are dynamically typed
    n = 0
    print('n =', n)

    n = "abc"
    print('n =', n)
    ```

2.  **Multiple Assignments (01:43 - 02:00)**
    ```python
    # Multiple assignments
    n, m = 0, "abc"

    n, m, z = 0.125, "abc", False
    ```

3.  **Incrementing (02:01 - 02:18)**
    ```python
    # Increment
    n = n + 1 # good
    n += 1    # good
    # n++     # bad (Syntax Error)
    ```

4.  **None/Null (02:24 - 02:39)**
    ```python
    # None is null (absence of value)
    n = 4
    n = None
    print("n =", n)
    ```

5.  **If Statements (02:40 - 03:20)**
    ```python
    # If statements don't need parentheses
    # or curly braces.
    n = 1
    if n > 2:
        n -= 1
    elif n == 2:
        n *= 2
    else:
        n += 2
    ```

6.  **Multi-line Conditions (03:24 - 03:51)**
    ```python
    # Parentheses needed for multi-line conditions.
    # and = &&
    # or = ||
    n, m = 1, 2
    if ((n > 2 and
        n != m) or n == m):
        n += 1
    ```

7.  **While Loops (04:00 - 04:16)**
    ```python
    # While loops are similar
    n = 0
    while n < 5:
        print(n)
        n += 1
    ```

8.  **For Loops / Range (04:17 - 05:46)**
    ```python
    # Looping from i = 0 to i = 4
    for i in range(5):
        print(i)

    # Looping from i = 2 to i = 5
    for i in range(2, 6):
        print(i)

    # Looping from i = 5 to i = 2
    for i in range(5, 1, -1):
        print(i)
    ```
    *(Note: The C-style `for (int i = 0; i < n; i++)` was shown for comparison only, not as a Python example)*

9.  **Math / Division (06:06 - 07:03)**
    ```python
    # Division is decimal by default
    print(5 / 2) # Output: 2.5

    # Double slash rounds down
    print(5 // 2) # Output: 2

    # CAREFUL: most languages round towards 0 by default
    # Python's // rounds down (towards negative infinity)
    print(-3 // 2) # Output: -2

    # A workaround for rounding towards zero is to
    # use decimal division and then convert to int.
    print(int(-3 / 2)) # Output: -1
    ```

10. **Modulo Operator (07:13 - 07:49)**
    ```python
    # Modding is similar to most languages
    print(10 % 3) # Output: 1

    # Except for negative values (result has same sign as divisor)
    print(-10 % 3) # Output: 2

    # To be consistent with other languages modulo (like C's %)
    import math
    print(math.fmod(-10, 3)) # Output: -1.0
    ```

11. **More Math Helpers (07:50 - 08:06)**
    ```python
    # More math helpers
    import math # Assumed imported from previous section
    print(math.floor(3 / 2)) # Output: 1
    print(math.ceil(3 / 2))  # Output: 2
    print(math.sqrt(2))      # Output: 1.414...
    print(math.pow(2, 3))    # Output: 8.0
    ```

12. **Max/Min Int - Infinity (08:07 - 08:39)**
    ```python
    # Max / Min Int representation using float
    float("inf")
    float("-inf")

    # Python numbers are infinite precision so they don't overflow in the traditional sense
    import math # Assumed imported
    print(math.pow(2, 200))

    # But still less than infinity representation
    print(math.pow(2, 200) < float("inf")) # Output: True
    ```

13. **Arrays/Lists - Basics, Stack Operations (08:40 - 09:17)**
    ```python
    # Arrays (called lists in python)
    arr = [1, 2, 3]
    print(arr)

    # Can be used as a stack (LIFO)
    arr.append(4) # Push
    arr.append(5) # Push
    print(arr)

    arr.pop()     # Pop (removes 5)
    print(arr)
    ```

14. **Array Insert and Indexing (09:18 - 09:52)**
    ```python
    # arr is [1, 2, 3, 4] from previous state
    arr.insert(1, 7) # Insert 7 at index 1 (O(n))
    print(arr) # Output: [1, 7, 2, 3, 4]

    # Indexing / Assignment (O(1))
    arr[0] = 0
    arr[3] = 0
    print(arr) # Output: [0, 7, 2, 0, 4]
    ```

15. **Initialize Array with Variable Size (09:53 - 10:10)**
    ```python
    # Initialize arr of size n with default value of 1
    n = 5
    arr = [1] * n
    print(arr)
    print(len(arr))
    ```

16. **Negative Indexing (10:11 - 10:27)**
    ```python
    # Careful: -1 is not out of bounds,
    # it's the last value
    arr = [1, 2, 3]
    print(arr[-1]) # Output: 3

    # Indexing -2 is the second to last value, etc.
    print(arr[-2]) # Output: 2
    ```

17. **Sublists / Slicing (10:32 - 10:54)**
    ```python
    # Sublists (aka slicing) - O(k) where k is slice size
    arr = [1, 2, 3, 4]
    print(arr[1:3]) # Elements index 1 up to (not including) 3. Output: [2, 3]

    # Similar to for-loop ranges, last index is non-inclusive
    print(arr[0:4]) # Output: [1, 2, 3, 4]
    ```

18. **Unpacking (10:55 - 11:17)**
    ```python
    # Unpacking
    a, b, c = [1, 2, 3]
    print(a, b, c)

    # Be careful though (ValueError: too many values to unpack if sizes don't match)
    # a, b = [1, 2, 3]
    ```

19. **Looping Through Arrays (11:18 - 12:06)**
    ```python
    # Loop through arrays
    nums = [1, 2, 3]

    # Using index
    for i in range(len(nums)):
        print(nums[i])

    # Without index (looping through values)
    for n in nums:
        print(n)

    # With index and value
    for i, n in enumerate(nums):
        print(i, n)
    ```

20. **Looping Through Multiple Arrays - Zip (12:07 - 12:28)**
    ```python
    # Loop through multiple arrays simultaneously
    # with unpacking using zip
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    for n1, n2 in zip(nums1, nums2):
        print(n1, n2)
    ```

21. **Array Reverse (12:29 - 12:36)**
    ```python
    # Reverse (in-place)
    nums = [1, 2, 3]
    nums.reverse()
    print(nums) # Output: [3, 2, 1]
    ```

22. **Sorting (12:37 - 13:34)**
    ```python
    # Sorting (in-place, usually O(N log N))
    arr = [5, 4, 7, 3, 8]
    arr.sort()
    print(arr) # Output: [3, 4, 5, 7, 8]

    arr.sort(reverse=True) # Sort descending
    print(arr) # Output: [8, 7, 5, 4, 3]

    arr = ["bob", "alice", "jane", "doe"]
    arr.sort() # Sorts alphabetically
    print(arr) # Output: ['alice', 'bob', 'doe', 'jane']

    # Custom sort (e.g., by length of string)
    arr.sort(key=lambda x: len(x))
    print(arr) # Output: ['bob', 'doe', 'jane', 'alice']
    ```

23. **List Comprehension (13:35 - 14:14)**
    ```python
    # List comprehension
    arr = [i for i in range(5)]
    print(arr) # Output: [0, 1, 2, 3, 4]

    arr = [i+i for i in range(5)] # Apply expression to each item
    print(arr) # Output: [0, 2, 4, 6, 8]
    ```

24. **2D Lists (Initialization) (14:15 - 14:47)**
    ```python
    # 2-D lists (correct way using list comprehension)
    arr = [[0] * 4 for i in range(4)]
    print(arr)

    # This common mistake creates rows referencing the same object
    # arr = [[0] * 4] * 4
    # Modifying arr[0][0] would change the first element of ALL rows.
    ```

25. **Strings (Similarities & Immutability) (15:20 - 15:55)**
    ```python
    # Strings are similar to arrays
    s = "abc"
    print(s[0:2]) # Slicing works. Output: ab

    # But they are immutable
    # s[0] = "A" # TypeError: 'str' object does not support item assignment

    # Concatenation creates a new string
    s += "def"
    print(s) # Output: abcdef
    ```

26. **String/Int Conversion (15:56 - 16:14)**
    ```python
    # Valid numeric strings can be converted to integers
    print(int("123") + int("123")) # Output: 246

    # And numbers can be converted to strings
    print(str(123) + str(123)) # Output: 123123
    ```

27. **Ord Function (ASCII Value) (16:15 - 16:27)**
    ```python
    # In rare cases you may need the ASCII value of a char
    print(ord("a")) # Output: 97
    print(ord("b")) # Output: 98
    ```

28. **Joining Strings (16:28 - 16:47)**
    ```python
    # Combine a list of strings (with an empty string delimiter)
    strings = ["ab", "cd", "ef"]
    print("".join(strings)) # Output: abcdef

    # Example with a space delimiter:
    # print(" ".join(strings)) # Output: ab cd ef
    ```

29. **Queues (Deque) (16:48 - 17:23)**
    ```python
    # Queues (using double ended queue for O(1) popleft)
    from collections import deque

    queue = deque()
    queue.append(1) # Add to right
    queue.append(2) # Add to right
    print(queue)

    queue.popleft() # Remove from left (O(1))
    print(queue)

    queue.appendleft(1) # Add to left (O(1))
    print(queue)

    queue.pop() # Remove from right (O(1))
    print(queue)
    ```

30. **Hash Sets (17:24 - 18:01)**
    ```python
    # HashSet (O(1) lookup, insertion, deletion on average)
    mySet = set()

    mySet.add(1)
    mySet.add(2)
    print(mySet) # Output: {1, 2} (order not guaranteed)

    print(len(mySet)) # Output: 2

    # Check membership (O(1) average)
    print(1 in mySet) # Output: True
    print(2 in mySet) # Output: True
    print(3 in mySet) # Output: False

    mySet.remove(2) # O(1) average
    print(2 in mySet) # Output: False
    ```

31. **Set Initialization (List/Comprehension) (18:02 - 18:22)**
    ```python
    # Initialize set from list (removes duplicates)
    print(set([1, 2, 3])) # Output: {1, 2, 3}

    # Set comprehension
    mySet = { i for i in range(5) }
    print(mySet) # Output: {0, 1, 2, 3, 4}
    ```

32. **Hash Maps / Dictionaries (18:23 - 19:16)**
    ```python
    # HashMap (aka dict) (O(1) lookup, insertion, deletion on average)
    myMap = {}
    myMap["alice"] = 88
    myMap["bob"] = 77
    print(myMap)
    print(len(myMap))

    myMap["alice"] = 80 # Update value
    print(myMap["alice"])

    # Check key membership (O(1) average)
    print("alice" in myMap) # Output: True

    myMap.pop("alice") # Remove key-value pair (O(1) average)
    print("alice" in myMap) # Output: False

    # Initialize dict directly
    myMap = { "alice": 90, "bob": 70 }
    print(myMap)
    ```

33. **Dict Comprehension (19:17 - 19:42)**
    ```python
    # Dict comprehension
    myMap = { i: 2*i for i in range(3) }
    print(myMap) # Output: {0: 0, 1: 2, 2: 4}
    ```

34. **Looping Through Maps (19:43 - 20:11)**
    ```python
    # Looping through maps
    myMap = { "alice": 90, "bob": 70 }

    # Looping through keys (default iteration)
    for key in myMap:
        print(key, myMap[key])

    # Looping through values
    for val in myMap.values():
        print(val)

    # Looping through key-value pairs (items)
    for key, val in myMap.items():
        print(key, val)
    ```

35. **Tuples (Immutability, Hashing) (20:12 - 20:50)**
    ```python
    # Tuples are like arrays but immutable
    tup = (1, 2, 3)
    print(tup)
    print(tup[0])
    print(tup[-1])

    # Can't modify
    # tup[0] = 0 # TypeError

    # Can be used as key for hash map/set because they are immutable
    myMap = { (1,2): 3 } # Tuple (1, 2) is the key
    print(myMap[(1,2)])

    mySet = set()
    mySet.add((1, 2)) # Add tuple to set
    print((1, 2) in mySet) # Check if tuple is in set

    # Lists can't be keys because they are mutable
    # myMap[[3, 4]] = 5 # TypeError: unhashable type: 'list'
    ```

36. **Heaps (Min & Max Workaround) (20:51 - 22:09)**
    ```python
    # Heaps (Priority Queue)
    import heapq

    # Min Heap (default in Python)
    minHeap = []
    heapq.heappush(minHeap, 3)
    heapq.heappush(minHeap, 2)
    heapq.heappush(minHeap, 4)

    # Min is always at index 0
    print(minHeap[0]) # Output: 2

    while len(minHeap):
        print(heapq.heappop(minHeap)) # Pops 2, 3, 4

    # Max Heap (workaround: store negated values in a min-heap)
    maxHeap = []
    heapq.heappush(maxHeap, -3) # Push -3 (represents 3)
    heapq.heappush(maxHeap, -2) # Push -2 (represents 2)
    heapq.heappush(maxHeap, -4) # Push -4 (represents 4)

    # Max is always at index 0 (after negating back)
    print(-1 * maxHeap[0]) # Output: 4

    while len(maxHeap):
        # Pop smallest (most negative) and negate back to get largest original
        print(-1 * heapq.heappop(maxHeap)) # Pops 4, 3, 2
    ```

37. **Heapify (Build Heap) (22:10 - 22:27)**
    ```python
    # Build heap from initial values (O(N) time)
    import heapq # Assumed imported
    arr = [2, 1, 8, 4, 5]
    heapq.heapify(arr) # Turns arr into a valid heap in-place

    while arr:
        print(heapq.heappop(arr)) # Pops 1, 2, 4, 5, 8
    ```

38. **Functions (Basic Definition) (22:28 - 22:49)**
    ```python
    # Functions
    def myFunc(n, m):
        return n * m

    print(myFunc(3, 4)) # Output: 12
    ```

39. **Nested Functions (Scope, Nonlocal) (22:50 - 24:14)**
    ```python
    # Nested functions have access to outer variables
    def outer(a, b):
        c = "c" # Variable in outer scope
        def inner():
            # inner() can access a, b, c from outer scope
            return a + b + c
        return inner()

    print(outer("a", "b")) # Output: abc

    # Modifying objects vs reassigning primitives in nested functions
    def double(arr, val): # arr is mutable (list), val is immutable (int)
        def helper():
            # Modifying elements of the mutable object 'arr' works
            for i, n in enumerate(arr):
                arr[i] *= 2

            # Trying to reassign 'val' creates a new local variable 'val' inside helper
            # val *= 2 # This would NOT change the 'val' from the 'double' scope

            # To modify the 'val' from the 'double' scope, use 'nonlocal'
            nonlocal val
            val *= 2

        helper() # Call the nested helper function
        print(arr, val) # Print the results after modification

    nums = [1, 2]
    val = 3
    double(nums, val) # Output: [2, 4] 6
    ```

40. **Classes (Constructor, Methods, Self) (24:20 - 25:26)**
    ```python
    # Class definition
    class MyClass:
        # Constructor (initializer)
        def __init__(self, nums):
            # self refers to the instance of the class
            # Create member variables (instance attributes)
            self.nums = nums
            self.size = len(nums)

        # Method definition - 'self' must be the first parameter
        def getLength(self):
            return self.size

        # Method calling another method of the same object
        def getDoubleLength(self):
            return 2 * self.getLength() # Use self to call other methods

    # Example Usage (not explicitly run in the video for this part)
    # my_obj = MyClass([1, 2, 3])
    # print(my_obj.getLength())        # Output: 3
    # print(my_obj.getDoubleLength())  # Output: 6
    ```