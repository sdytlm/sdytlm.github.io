---
layout: post
title: "Reconstruct Itinerary"
date: 2016-07-05
comments: true
categories: LeetCode
tag: LeetCode
---



Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

#### Note:
* If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, The itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

* All airports are represented by three capital letters (IATA code).

* You may assume all tickets form at least one valid itinerary.

#### Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

#### Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

Return ["JFK","ATL","JFK","SFO","ATL","SFO"].

Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

<!--more-->
### Solution
* 通过图（无向图或有向图）中所有边且每边仅通过一次的通路称为欧拉通路，相应的回路称为欧拉回路。具有欧拉回路的图称为欧拉图（Euler Graph），具有欧拉通路而无欧拉回路的图称为半欧拉图。
* 因此题目的实质就是从JFK顶点出发寻找欧拉通路，可以利用Hierholzer算法。

{% include_code LeetCode/Python/Reconstruct-Itinerary.py %}
