---
layout: post
title: "Shortest Palindrome"
date: 2016-09-04
comments: true
categories: LeetCode
tag: LeetCode
---

Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

#### Example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

<!--more-->
### Solution
记原始字符串为s，s的反转字符串为rev_s。

构造字符串l = s + '#' + rev_s，其中'#'为s中不会出现的字符，添加'#'是为了处理输入为空字符串的情形。

对字符串l执行KMP算法，可以得到“部分匹配数组”p（也称“失败函数”）

我们只关心p数组的最后一个值p[-1]，因为它表明了rev_s与s相互匹配的最大前缀长度。

最后只需要将rev_s的前k个字符与原始串s拼接即可，其中k是s的长度len(s)与p[-1]之差。

{% include_code LeetCode/Python/Shortest-Palindrome.py %}
