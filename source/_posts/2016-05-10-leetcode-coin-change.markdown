---
layout: post
title: "Coin Change"
date: 2016-05-10
comments: true
categories: LeetCode
tag: LeetCode
---

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

#### Example

* Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

* Example 2:
coins = [2], amount = 3
return -1.

#### Note
You may assume that you have an infinite number of each kind of coin.

<!--more-->
### Solution

* Java 
{% include_code LeetCode/Java/Coin-Change.java %}

* Python
{% include_code LeetCode/Python/Coin-Change.py %}
