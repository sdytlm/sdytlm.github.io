---
layout: post
title: "Make Opensuse Installation USB on MacOS"
date: 2015-04-07
comments: true
categories: Geek
tag: Geek
---

1. Convert opensuse installtion ios to dmg

``` 
hdiutil convert -format UDRW -o opensuse-13.01.img opensuse-13.01.iso
```

2. Get the current device lists

```
diskutil list

```
Remeber the current existing device number

3. Insert USB

```
diskutil list 

```

again and find the device node assigned to your usb ( e.g. /dev/disk1)

4. Unmount your USB

```
diskutil unmountDisk /dev/disk1
```

5. Burn the flash

```
sudo dd if=/your_img_location/opensuse-13.01.img of=/dev/rdisk1 bs=1m
```

6. Ignore the pop-up window and run

```
diskutil eject /dev/disk1
```

7. Enjory it
