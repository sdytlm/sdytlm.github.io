---
layout: post
title: "Play KVMGT (GPU Virtualization)"
date: 2016-11-16
comments: true
categories: virtualization
tag: virtualization
---



### Host (Opensuse 14.2)
* install libcheese

`sudo apt-get install libglew-dev libcheese7 libcheese-gtk23 libclutter-gst-2.0-0 libcogl15 libclutter-gtk-1.0-0 libclutter-1.0-0`

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


### Host Grub
Add `intel_iommu=igfx_off i915.hvm_boot_foreground=1 loglvl=all guest_loglvl=all conring_size=4M noreboot` on linux option.


### Host Driver
* Update all packages including x11-xorg


```
git clone git://anongit.freedesktop.org/git/xorg/driver/xf86-video-intel
cd xf86-video-intel
git checkout 2.99.917
./autogen.sh --prefix=/opt/hsw/usr
make && make install
cd /usr/lib64/xorg/modules/drivers/
ln -sf /opt/hsw/usr/lib64/xorg/modules/drivers/intel_drv.so intel_drv.so

```

### Guest 
