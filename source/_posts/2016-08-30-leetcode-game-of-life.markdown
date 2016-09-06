---
layout: post
title: "Game of Life"
date: 2016-08-30
comments: true
categories: leetcode
tag: leetcode
---


According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

#### Follow up: 
* Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
* In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

<!--more-->
### Solution
每个点除了题目给出的２个状态，还可以有２个状态
我们假设有4个状态，比如2表示一开始为1，但是之后应该为0的状态，3表示一开始为0，但是之后为1 的状态，总结状态如下：

* 0 : 0 -> 0

* 1 : 1 -> 1

* 2 : 1 -> 0   这一轮这个点是１，下一轮这个点要是０

* 3 : 0 -> 1　　这一轮这个点是０，下一轮要是１

{% include_code LeetCode/Python/Game-of-Life.py %}
