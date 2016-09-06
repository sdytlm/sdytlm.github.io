---
layout: post
title: "Water and Jug Problem"
date: 2016-08-31
comments: true
categories: leetcode
tag: leetcode
---



You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

* Fill any of the jugs completely with water.
* Empty any of the jugs.
* Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

#### Example 1: (From the famous "Die Hard" example)

```
Input: x = 3, y = 5, z = 4
Output: True
```

#### Example 2:

```
Input: x = 2, y = 6, z = 5
Output: False
```

<!--more-->
### Solution
求最大公约数

如果x与y互质（最大公约数为1），则容量范围[1, x + y]之内的任意整数体积均可以通过适当的操作得到。

否则，记x与y的最大公约数为gcd，则可以获得的容量z只能为gcd的整数倍，且z <= x + y

{% include_code LeetCode/Python/Water-and-Jug-Problem.py %}
