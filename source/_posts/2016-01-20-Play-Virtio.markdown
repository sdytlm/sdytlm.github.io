---
layout: post
title: "Play Virtio on QEMU"
date: 2016-01-23
comments: true
categories: virtualization
tag: virtualization
---

* QEMU: 2.4
* Host: Linux3.10
* Guest: Opensuse 12.x with Linux3.10

### Original QEMU commands

```
qemu-system-x86_64 -enable-kvm -rtc base=utc,clock=vm,driftfix=none \
-bios bios.bin -device piix3-usb-uhci -soundhw ac97,hda -m 1024 \
-serial tcp::1223,server,nowait -net nic,macaddr=00:20:18:11:01:23,model=rtl8139,vlan=0 \
-net tap,vlan=0,script=/data/images/qemu-image/qemu-ifup0.sh \
-hda /data/images/qemu-image/opensuse-50G.img -name 23 -cpu core2duo \
-monitor stdio -smp sockets=1,cores=2,threads=1 -vnc :23

```
### virtio-gpu
Just standard VGA right now. Will suport 3D in the future.

```
qemu-system-x86_64 -enable-kvm -rtc base=utc,clock=vm,driftfix=none \
-bios bios.bin -device piix3-usb-uhci -soundhw ac97,hda -m 1024 \
-serial tcp::1223,server,nowait -net nic,macaddr=00:20:18:11:01:23,model=rtl8139,vlan=0 \
-net tap,vlan=0,script=/data/images/qemu-image/qemu-ifup0.sh \
-hda /data/images/qemu-image/opensuse-50G.img -name 23 -cpu core2duo \
-monitor stdio -smp sockets=1,cores=2,threads=1 -vnc :23 -vga virtio

```

### virtio-net
```
qemu-system-x86_64 -enable-kvm -rtc base=utc,clock=vm,driftfix=none \
-bios bios.bin -device piix3-usb-uhci -soundhw ac97,hda -m 1024 -serial tcp::1223,server,nowait \
-netdev tap,script=/data/images/qemu-image/qemu-ifup0.sh,id=net0 \
-device virtio-net-pci,netdev=net0 -hda /data/images/qemu-image/opensuse.img \
-name 23 -cpu core2duo -monitor stdio -smp sockets=1,cores=2,threads=1

```

### virtio-blk

```
qemu-system-x86_64 -enable-kvm -rtc base=utc,clock=vm,driftfix=none \
-bios bios.bin -device piix3-usb-uhci -soundhw ac97,hda -m 1024 -serial tcp::1223,server,nowait \
-net nic,macaddr=00:20:18:11:01:23,model=rtl8139,vlan=0 \
-net tap,vlan=0,script=/data/images/qemu-image/qemu-ifup0.sh \
-drive file=/data/images/qemu-image/opensuse.img,if=virtio,boot=on \
-name 23 -cpu core2duo -monitor stdio -smp sockets=1,cores=1,threads=1 -vnc :23
```

### virtio-scsi

```
qemu-system-x86_64 -enable-kvm -rtc base=utc,clock=vm,driftfix=none \
-bios bios.bin -device piix3-usb-uhci -soundhw ac97,hda -m 1024 \
-serial tcp::1223,server,nowait -net nic,macaddr=00:20:18:11:01:23,model=rtl8139,vlan=0 \
-net tap,vlan=0,script=/data/images/qemu-image/qemu-ifup0.sh \
-drive if=none,id=hd,file=/data/images/qemu-image/opensuse-50G.raw \
-device virtio-scsi-pci,id=scsi -device scsi-hd,drive=hd -name 23 \
-cpu core2duo -monitor stdio -smp sockets=1,cores=1,threads=1 -vnc :23
```

### virtio-input-pci
* Require:
    1. Guest Linux Kernel >= 4.1
    2. QEMU >=2.4
* keyboard: add `-device virtio-keyboard-pci`
* mouse: add `-device virtio-mouse-pci`
* tablet: add `-device virtio-tablet-pci`
