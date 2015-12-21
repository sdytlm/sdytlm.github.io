---
layout: post
title: "Longest Common Prefix"
date: 2015-12-18
comments: true
categories: LintCode
tag: LintCode
---

### Longest Common Prefix
`Given k strings, find the longest common prefix (LCP).`

#### Example
For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"

For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"

<!-- more -->

### Solution
* Find the shortest string
* Compare each character of the shortest string with other strings. Return the result if any comparison returns false

{% include_code LintCode/Longest-Common-Prefix.py %}
