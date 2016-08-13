---
layout: post
title: "Gas Station"
date: 2016-07-25
comments: true
categories: LeetCode
tag: LeetCode
---

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

#### Note:
The solution is guaranteed to be unique.

<!--more-->
### Solution
若储油量总和sum(gas) >= 耗油量总和sum(cost)，则问题一定有解

{% include_code LeetCode/Python/Gas-Station.py %}
