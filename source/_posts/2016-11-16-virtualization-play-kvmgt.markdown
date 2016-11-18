---
layout: post
title: "Play KVMGT (GPU Virtualization)"
date: 2016-11-16
comments: true
categories: virtualization
tag: virtualization
---



### Host (Opensuse 14.2)

udev-devel, 

* Download new host kernel

```
git clone https://github.com/01org/igvtg-kernel kernel_src
cd kernel_src
git checkout 2016q2-4.3.0 (linux kernel 4.3)
cp configure-file to ./.config
make ; make modules ; make modules_install ; make install; 

```


### QEMU (2.3)
In ./configure, Add `-lEGL` when vgt-egl-compositor is used.

```
git clone https://github.com/01org/igvtg-qemu qemu_src
cd qemu_src
git submodule update --init dtc
git submodule update --init roms/seabios
./configure --prefix=/usr \
            --enable-kvm \
            --enable-sdl \
            --disable-werror \
            --target-list=x86_64-softmmu
make 
cd roms/seabios
LC_ALL=C make -j8

```

