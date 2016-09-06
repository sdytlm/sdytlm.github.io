---
layout: post
title: "Find the Duplicate Number"
date: 2016-09-02
comments: true
categories: LeetCode
tag: LeetCode
---


Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

#### Note:
* You must not modify the array (assume the array is read only).
* You must use only constant, O(1) extra space.
* Your runtime complexity should be less than O(n2).
* There is only one duplicate number in the array, but it could be repeated more than once.

<!--more-->
### Solution
* 根据鸽笼原理，给定n + 1个范围[1, n]的整数，其中一定存在数字出现至少两次。

* 假设枚举的数字为 n / 2：

* 遍历数组，若数组中不大于n / 2的数字个数超过n / 2，则可以确定[1, n /2]范围内一定有解，

* 否则可以确定解落在(n / 2, n]范围内。

{% include_code LeetCode/Python/Find-the-Duplicate-Number.py %}
