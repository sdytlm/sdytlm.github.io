---
layout: post
title: "Interleaving String"
date: 2016-08-25
comments: true
categories: leetcode
tag: leetcode
---


Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

#### Example:
Given:
```
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

```

<!--more-->
### Solution
* dp[i][j]: 表示s1[0...i-1]和s2[0...j-1]是否可以拼接为s3[0...i+j-1]，可以拼接为true，不可以拼接为false

* 只有两种情况下dp[i][j] 是true:
1. dp[i-1][j] == True and s1[i-1]==s3[i+j-1]
2. dp[i][j-1] ==True and s2[j-1]==s3[i+j-1]

{% include_code LeetCode/Python/Interleaving-String.py %}
