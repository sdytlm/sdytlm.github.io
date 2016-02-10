---
layout: post
title: "Gas Station"
date: 2016-02-06
comments: true
categories: LintCode
tag: LintCode 
---

### Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

#### Example
Given 4 gas stations with gas[i]=[1,1,3,1], and the cost[i]=[2,2,1,1]. The starting gas station's index is 2.

#### Note
The solution is guaranteed to be unique.

#### Challenge
O(n) time and O(1) extra space

<!--more-->

### Solution
* Time:O(n)
* if sum(gas) >= sum(cost), there must be a solution
* From left to right, diff += gas[i]-cost[i], if diff<0, update the start index. A[0,index] can definitly be reached.
{% include_code LintCode/Gas-Station.py %}
