---
layout: post
title: "Longest Substring with At Least K Repeating Characters"
date: 2016-09-10
comments: true
categories: LeetCode
tag: LeetCode
---




Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

#### Example 1:
```
Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
```
### Example 2:
```
Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
```
<!--more-->
### Solution
* 以出现次数不到k的字符做split. 递归调用，返回最大值

{% include_code LeetCode/Python/Longest-Substring-with-at-least-k-repeating-character.py %}
