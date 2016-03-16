---
layout: post
title: "Topological Sorting"
date: 2016-03-08
comments: true
categories: LintCode
tag: LintCode 
---

Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph

#### Notice

You can assume that there is at least one topological order in the graph.

<!--more-->
### Solution
* Time: O(n)
{% include_code LintCode/Topological-Sorting.py %}
