---
layout: post
title: "Palindrome Number"
date: 2016-08-07
comments: true
categories: LeetCode
tag: LeetCode
---

Determine whether an integer is a palindrome. Do this without extra space.


Some hints:
* Could negative integers be palindromes? (ie, -1)

* If you are thinking of converting the integer to string, note the restriction of using extra space.

* You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

* There is a more generic way of solving this problem.

<!--more-->

### Solution
* 把x反转，除了最高位不要.
* p是反转以后的结果，ｑ是最高位

* Java Solution:
{% include_code LeetCode/Java/Palindrome-Number.java %}

{% include_code LeetCode/Python/Palindrome-Number.py %}
