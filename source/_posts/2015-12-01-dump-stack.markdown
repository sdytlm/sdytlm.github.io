---
layout: post
title: "Dump Stack in linux"
date: 2015-12-01
comments: true
categories: Linux
tag: Linux
---

`dump_stack()` is a useful tool to understand call procedure of a function. You can enable it in the kernel source.

### Enable dump_stack
Make sure the following flag is `y`

* CONFIG_PREEMPT
* CONFIG_DEBUG_KERNEL
* CONFIG_KALLSYMS
* CONFIG_SPINLOCK_SLEEP
* CONFIG_MAGIC_SYSRQ

### Use dump_stack in your code

``` c
printk(KERN_ERR, "%x", parameter);
dump_stack()

```

After that

You can watch the stack result in `dmesg`
