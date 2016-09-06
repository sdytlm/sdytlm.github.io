---
layout: post
title: "Best Time to Buy and Sell Stock"
date: 2016-09-06
comments: true
categories: LeetCode
tag: LeetCode
---

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

#### Example 1:
Input: [7, 1, 5, 3, 6, 4]

Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

#### Example 2:
Input: [7, 6, 4, 3, 1]

Output: 0

In this case, no transaction is done, i.e. max profit = 0.

<!--more-->
### Solution
* cur_min: 维护当前股价最低价
* dp: 每天卖出时最大利润，并更新cur_min

{% include_code LeetCode/Python/Best-Time-to-Buy-and-Sell-Stock.py %}
