---
layout: post
title: "Edit Distance"
date: 2016-08-10
comments: true
categories: LeetCode
tag: LeetCode
---

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

<!--more-->
### Solution

* dp[i][j]: 把单词word1[1:i] 转成 word2[1:j](单词从1开始)所用步数
* if word[i+1] == word[j+1]
`dp[i+1][j+1] = Min(dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j] + 0]`

* else
`dp[i+1][j+1] = Min(dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j] + 1]`

{% include_code LeetCode/Python/Edit-Distance.py %}


