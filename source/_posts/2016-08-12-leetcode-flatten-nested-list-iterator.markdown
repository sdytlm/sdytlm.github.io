---
layout: post
title: "Flatten Nested List Iterator"
date: 2016-08-12
comments: true
categories: LeetCode
tag: LeetCode
---


Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

#### Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

#### Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

<!--more-->
### Solution

* nestedList: List[NestedInteger]. NestedInteger有可能是integer也有可能还是一个List[NestedInteger]
{% include_code LeetCode/Python/Flatten-Nested-List-Iterator.py %}
