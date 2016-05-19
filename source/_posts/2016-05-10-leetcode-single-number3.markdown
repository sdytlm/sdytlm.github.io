---
layout: post
title: "Single Number III"
date: 2016-05-10
comments: true
categories: LeetCode
tag: LeetCode
---


Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

#### Example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

#### Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

<!--more-->
### Solution

* 首先计算nums数组中所有数字的异或，记为xor

* 接下来计算xor从右起第一个不为０的数字lowbit
**  令lowbit = xor & -xor，lowbit的含义为xor从低位向高位，第一个非0位所对应的数字

**  例如假设xor = 6（二进制：0110），则-xor为（二进制：1010，-6的补码，two's complement, 则lowbit = 2（二进制：0010）

**  根据异或运算的性质，“同0异1” 记只出现一次的两个数字分别为a与b 可知a & lowbit与b & lowbit的结果一定不同

**  通过这种方式，即可将a与b拆分开来


