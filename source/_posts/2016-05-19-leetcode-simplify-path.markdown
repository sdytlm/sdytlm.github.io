---
layout: post
title: "Simplify Path"
date: 2016-05-19
comments: true
categories: LeetCode
tag: LeetCode
---

Given an absolute path for a file (Unix-style), simplify it.

#### Example
* path = "/home/", => "/home"
* path = "/a/./b/../../c/", => "/c"

#### Corner Cases
* Did you consider the case where path = "/../"?
In this case, you should return "/".
* Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

<!--more-->

### Solution

* Java
{% include_code LeetCode/Java/Simplify-Path.java %}

* Python
{% include_code LeetCode/Python/Simplify-Path.py %}
