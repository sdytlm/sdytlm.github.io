---
layout: post
title: "Best Time to Buy and Sell Stock III"
date: 2016-08-22
comments: true
categories: LeetCode
tag: LeetCode
---

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

#### Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

<!--more-->
### Solution
* DP
* F1[i]: 在prices[i]前进行一次交易获得的最大利益
`f1[i] = max(f1[i-1], prices[i]-minV)`
* F2[i]: 在prices[i]之后进行一次交易获得的最大利润
`f2[i] = max(f2[i+1], maxV-prices[i])`
* 结果就是f1[i] + f2[i]

{% include_code LeetCode/Python/Best-Time-to-Buy-and-Sell-Stock3.py %}
