---
layout: post
title: "Decode Ways"
date: 2016-07-13
comments: true
categories: LeetCode
tag: LeetCode
---

A message containing letters from A-Z is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Given an encoded message containing digits, determine the total number of ways to decode it.

#### Example:
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

<!--more-->
### Solution

解码有多少种方法。一般求“多少”我们考虑使用dp。状态方程如下：

* 当s[i-2:i]这两个字符是10~26但不包括10和20这两个数时，比如21，那么可以有两种编码方式（BA，U），所以dp[i]=dp[i-1]+dp[i-2]

* 当s[i-2:i]等于10或者20时，由于10和20只有一种编码方式，所以dp[i]=dp[i-2]

* 当s[i-2:i]不在以上两个范围时，如09这种，编码方式为0，而31这种，dp[i]=dp[i-1]。

* 注意初始化时：dp[0]=1,dp[1]=1
{% include_code LeetCode/Python/Decode-Ways.py %}
