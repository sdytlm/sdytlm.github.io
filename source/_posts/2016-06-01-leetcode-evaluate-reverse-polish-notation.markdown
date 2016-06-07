---
layout: post
title: "Evaluate Reverse Polish Notation"
date: 2016-06-01
comments: true
categories: LeetCode
tag: LeetCode
---

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, * , /. Each operand may be an integer or another expression.

#### Examples
```
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
```

<!--more-->

### Solution
* Use Stack
{% include_code LeetCode/Python/Evaluate-Reverse-Polish-Notation.py %}
