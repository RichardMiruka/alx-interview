# Making Change

> Algorithm
> Python

![image](https://github.com/RichardMiruka/alx-interview/assets/105627752/a227eb3b-5cbd-40c3-92ac-8cf6142b4857)

For the “0. Change comes from within” project, you will tackle a classic problem from the domain of dynamic programming and greedy algorithms: the coin change problem. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. This project challenges you to apply your understanding of algorithms to devise a solution that is not only correct but also efficient. Below are the key concepts and resources necessary to complete this project successfully.

## Concepts Needed:
### 1. Greedy Algorithms:

* Understanding how greedy algorithms work and why they are suitable for the coin change problem.
* Recognizing the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.

### 2. Dynamic Programming:

* Basic principles of dynamic programming as a method to solve optimization problems.
*  The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.

### 3. Algorithmic Complexity:

* Analyzing the time and space complexity of algorithms.
* Striving for solutions with lower complexity to meet runtime constraints.

### 4. Problem-Solving Strategies:

* Breaking down the problem into smaller, manageable sub-problems.
* Iterative vs recursive approaches to dynamic programming.
### 5. Python Programming:

* Manipulating lists and using list comprehensions.
* Implementing functions with efficient looping and conditional statements.

## Resources:

### Python Official Documentation:

* [More Control Flow Tools (for loops, if statements)](https://intranet.alxswe.com/rltoken/oVyaCk8erLwLPj96P-qlCw)

### GeeksforGeeks Articles:

* [Coin Change | DP-7](https://intranet.alxswe.com/rltoken/iQPaO5JhI-BtuZdm6HIVCQ)
* [Greedy Algorithm to find Minimum number of Coins](https://intranet.alxswe.com/rltoken/FsBN0oeRp0FpyU8sMd4UiA)

### YouTube Tutorials:

* [Dynamic Programming - Coin Change Problem](https://intranet.alxswe.com/rltoken/qFEdwwtAVyJr9NLHDZDsUQ) for a visual and step-by-step explanation of the dynamic programming approach.

By thoroughly understanding these concepts and utilizing the provided resources, you will be well-prepared to tackle the coin change problem. You will need to decide whether a greedy algorithm suffices for your particular set of coin denominations or if a more comprehensive dynamic programming approach is necessary to ensure correctness and efficiency. This project not only tests algorithmic skills but also reinforces the importance of choosing the right strategy based on problem constraints.

## Additional Resources

* [Mock Technical Interview](https://intranet.alxswe.com/rltoken/ktLaKIVRkq_-byFO-_-aGg)

## Tasks To Complete

+ [x] 0. **Change comes from within**<br/>[0-making_change.py](0-making_change.py) contains a module with a function that determines the fewest number of coins needed to meet a given amount `total` when given a pile of coins of different values, with the following requirements:
  + Prototype: `def makeChange(coins, total)`.
  + Return: fewest number of coins needed to meet `total`.
    + If `total` is `0` or less, return `0`.
    + If `total` cannot be met by any number of coins you have, return `-1`.
  + `coins` is a list of the values of the coins in your possession.
  + The value of a coin will always be an integer greater than `0`.
  + You can assume you have an infinite number of each denomination of coin in the list.
  + Your solution’s runtime will be evaluated in this task.
