---
layout: post
title: "Linked List Random Node"
date: 2016-08-12
comments: true
categories: LeetCode
tag: LeetCode
---

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

#### Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

#### Example:

```
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
```

<!--more-->
### Solution
* 我们以第2个数为例（就是head.next.val）

* 在从[0,n]遍历一边的过程中被选取的概率为`(1/2)* （2/3）*（3/4）* ……….. (n-1) / n = 1/n`   （选取第2个数在长度为2的时候为1/2，其他的都不要选)

* 此一类推，任何一个数x在遍历一边中被选到的概率都是1/n
{% include_code LeetCode/Python/Linked-List-Random-Note.py %}
