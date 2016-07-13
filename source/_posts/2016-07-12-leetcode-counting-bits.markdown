---
layout: post
title: "Counting Bits"
date: 2016-07-12
comments: true
categories: LeetCode
tag: LeetCode
---


Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

#### Example:
For num = 5 you should return [0,1,1,2,1,2].

#### Follow up:

* It is very easy to come up with a solution with run time O(n * sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?

* Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function in c++ or in any other language.


#### Hint:

* You should make use of what you have produced already.
* Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
* Does the odd/even status of the number help you in calculating the number of 1s?

<!--more-->
### Solution

一个数 * 2 就是把它的二进制全部左移一位，也就是说 1的个数是相等的。

那么我们可以利用这个结论来做。

{% include_code LeetCode/Python/Counting-Bits.py %}

res[i /2] 然后看看最低位是否为1即可（上面*2一定是偶数，这边比如15和14除以2都是7，但是15时通过7左移一位并且+1得到，14则是直接左移）
