---
layout: post
title: "Lowest Common Ancestor of BST"
date: 2016-09-06
comments: true
categories: LeetCode
tag: LeetCode
---


Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

```
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
```

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

<!--more-->
### Solution
递归寻找两个带查询LCA的节点p和q，当找到后，返回给它们的父亲。如果某个节点的左右子树分别包括这两个节点，那么这个节点必然是所求的解，返回该节点。否则，返回左或者右子树


{% include_code LeetCode/Python/Lowest-Common-Ancestor-of-BST.py %}
