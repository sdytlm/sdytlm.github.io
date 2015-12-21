---
layout: post
title: "Longest Common Substring"
date: 2015-12-15
comments: true
categories: LintCode
tag: LintCode
---



### Longest Common Substring

Given two strings, find the longest common substring

Return the length of it.


#### Example
Given A = "ABCD", B = "CBCE", return 2.

#### Note
The characters in **substring** should occur continuously in original string. This is different with **subsequence**.

* substring: 必须是一个string中连续的一部分
* subsequence: 把一个string, 任意去掉一些字符后，得到的结果，不需要是连续的。

<!-- more -->

### Solution
假设两个字符串分别为`x1 ... xi ... xm` 和 `y1 ... yj ... yn`
假设二维dp数组 dp[i][j] 表示xi 和 yj 时，最大公共子串的长度.需要考虑如下两种情况

* 若 xi != yj 那么dp[i][j] = 0， 因为xi, yj一定不在任何公共子串中。

* 若 xi == yj 那么xi 与 yj 一定存在于一个公共子串中，但不一定是最大的那个，我们这时只知道dp[i][j] = d[i-1][j-1] + 1， 即前一个字符的公共子串长度+1.

{% include_code LintCode/Longest-Common-Substring.py %}


