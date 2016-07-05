---
layout: post
title: "Sort Colors"
date: 2016-07-01
comments: true
categories: LeetCode
tag: LeetCode
---


Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

#### Note
You are not suppose to use the library's sort function for this problem.

<!--more-->
### Solution
遍历两遍数组，第一遍对0，1，2计数，第二遍对数组进行赋值，这样是可以ac的。但题目的要求是只使用常数空间，而且只能遍历一遍。那么思路就比较巧妙了。设置两个头尾指针，头指针p0指向的位置是0该放置的位置，尾指针p2指向的位置是2该放置的位置。i用来遍历整个数组，碰到0把它和p0指向的数交换，碰到2把它和p2指向的数交换，碰到1继续向后遍历

{% include_code LeetCode/Python/Sort-Colors.py %}
