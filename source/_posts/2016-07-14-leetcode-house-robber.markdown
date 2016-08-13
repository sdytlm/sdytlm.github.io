---
layout: post
title: "House Robber"
date: 2016-07-14
comments: true
categories: LeetCode
tag: LeetCode
---


You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

<!--more-->
### Solution
* dp[i]表示打劫到第i间房屋时累计取得的金钱最大值。
* dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])

{% include_code LeetCode/Python/House-Robber.py %}
