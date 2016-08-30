---
layout: post
title: "Candy"
date: 2016-08-21
comments: true
categories: LeetCode
tag: LeetCode
---



There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

* Each child must have at least one candy.
* Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

<!--more-->
### Solution
* 贪心算法，从左，从右扫描两次，当rating[i]大于相邻孩子j且糖果candies[i]少于candies[j]时，增加candies[i]
{% include_code LeetCode/Python/Candy.py %}
