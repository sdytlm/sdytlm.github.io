---
layout: post
title: "Distinct Subsequences"
date: 2016-08-24
comments: true
categories: LeetCode
tag: LeetCode
---


Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

<!--more-->
### Solution
* 把s删掉某个或者几个，得到t
* dp[i][j]:表示S[0...i-1]中有多少子串是T[0...j-1]

`dp[i][j] = dp[i][j - 1] + (T[i - 1] == S[j - 1] ? dp[i - 1][j - 1] : 0)`

dp[i][j] = dp[i][j - 1].就是说，假设S已经匹配了j - 1个字符，得到匹配个数为dp[i][j - 1].现在无论S[j]是不是和T[i]匹配，匹配的个数至少是dp[i][j - 1]。除此之外，当S[j]和T[i]相等时，我们可以让S[j]和T[i]匹配，然后让S[j - 1]和T[i - 1]去匹配。所以递推关系

{% include_code LeetCode/Python/Distinct-Subsequence.py %}
