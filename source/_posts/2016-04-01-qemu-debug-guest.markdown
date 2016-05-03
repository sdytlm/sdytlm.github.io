---
layout: post
title: "Display Guest's boot message in Host"
date: 2016-04-01
comments: true
categories: virtualization
tag: virtualization
---
### QEMU Commands
* virtualized serial port is directed to the host tcp port:1223
```
qemu-system-x86_64 -enable-kvm -rtc base=utc,clock=vm,driftfix=none -bios bios.bin -device piix3-usb-uhci -soundhw ac97,hda -m 1024 -serial tcp::1223,server,nowait -netdev tap,script=/data/images/qemu-image/qemu-ifup0.sh,id=net0 -device virtio-net-pci,netdev=net0 -hda /data/images/qemu-image/opensuse-50G.raw -name 23 -cpu core2duo -monitor stdio -smp sockets=1,cores=1,threads=1 -vnc :23
```

### Configure Guest GRUB
* `dmesg | grep ttyS` make sure virtualized serial port exists
 
* Make guest display boot message on serial

    1. /etc/default/grub/

```
GRUB_CMDLINE_LINUX_DEFAULT="console=tty0 console=ttyS0,9600n8 "
GRUB_TERMINAL=serial
GRUB_SERIAL_COMMAND="serial --speed=9600 -unit=0 --word=8 --parity=no --stop=1"    

```
    
    2. update grub config

### Host connection
* Turn of the VM
* Add `-S` in the qemu command to suspend the VM and you can telnet the port
* Boot the VM and `telnet localhost 1223` after VM is suspended.
* Resume the VM in qemu
