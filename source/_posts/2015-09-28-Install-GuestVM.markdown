---
layout: post
title: "QEMU-KVM Install Guest VM"
date: 2015-09-28
comments: true
categories: virtualization
tag: virtualization
---


#### Create a qcow2 disk image
```
qemu-img create -f qcow2 ./win7.img 10G
```

#### Install OS on the new image
```
qemu-system-xxx -hda win7.img -boot d -cdrom ./instal-image.iso -m 512
```

#### Boot after install
```
qemu-system-xxx -hda win7.img -m 512
```

> The above instructions only use most basic options to make it happen


