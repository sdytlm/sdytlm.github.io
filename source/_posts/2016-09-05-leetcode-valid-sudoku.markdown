---
layout: post
title: "Valid Sudoku"
date: 2016-09-05
comments: true
categories: LeetCode
tag: LeetCode
---

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

#### Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

<!--more-->
### Solution

对于`9*9`矩阵中的每个元素
1. 检查他所在行是否和他重复
2. 检查他所在列是否和他重复
3. 检查他所在`3*3` 小矩阵是否和他重复

* Python
{% include_code LeetCode/Python/Valid-Sudoku.py %}

* Java

{% include_code LeetCode/Java/Valid-Sudoku.java %}


