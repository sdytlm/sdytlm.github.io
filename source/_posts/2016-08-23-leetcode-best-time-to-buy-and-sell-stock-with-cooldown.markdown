---
layout: post
title: "Best Time to Sell and Buy Stock with Cooldown"
date: 2016-08-23
comments: true
categories: LeetCode
tag: LeetCode
---

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

#### Example:

```
prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
```

<!--more-->
### Solution

* sell[i] 卖出操作的最大利润。它需要考虑的是，第i天是否卖出。（手上有stock在第i天所能获得的最大利润）

* buy[i] 买进操作的最大利润。它需要考虑的是，第i天是否买进。（手上没有stock在第i天所能获得的最大利润）

若没有卖出而只买入股票，相当于-prices[i]

`
buy[i] = max(buy[i-1] , sell[i-2] – prices[i])  // 休息一天在买入，所以是sell[i-2]在状态转移
sell[i] = max(sell[i-1], buy[i-1] + prices[i])`


{% include_code LeetCode/Python/Best-Time-to-Buy-and-Sell-Stock-with-cooldown.py %}
