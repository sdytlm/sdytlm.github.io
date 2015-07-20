---
layout: post
title: "Compile Linux Kernel"
date: 2015-04-06
comments: true
categories: Linux
tag: Linux
---


```
cp /boot/config-3.4-desktop ~/Download/linux-3.10/

```

```
make menuconfig

```

User a proper configuration file

```
make
```

```
make modules
```

```
make modules_install
```

```
make install
```

Update grub

```
grub2-mkconfig -o /boot/grub2/grub.cfg

```

Usually, you don't need to do this.
