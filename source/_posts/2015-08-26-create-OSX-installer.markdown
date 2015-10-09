---
layout: post
title: "Make OSX installer (iso) by using install app"
date: 2015-08-26
comments: true
categories: geek
tag: geeks
---



*  so let's start with that:
```	
sudo -s
```
* Mount the installer image:
```
hdiutil attach /Applications/Install\ OS\ X\ Yosemite.app/Contents/SharedSupport/InstallESD.dmg -noverify -nobrowse -mountpoint /Volumes/install_app
```
* Convert the boot image to a sparse bundle:
```
hdiutil convert /Volumes/install_app/BaseSystem.dmg -format UDSP -o /tmp/Yosemite
```
<!--more-->
* Increase the sparse bundle capacity for packages, kernel, etc.:
```
hdiutil resize -size 8g /tmp/Yosemite.sparseimage
```
* Mount the sparse bundle target for further processing:
```	
hdiutil attach /tmp/Yosemite.sparseimage -noverify -nobrowse -mountpoint /Volumes/install_build
```
* Remove Package link and replace with actual files:
```	
rm /Volumes/install_build/System/Installation/Packages
cp -rp /Volumes/install_app/Packages /Volumes/install_build/System/Installation/
```
* ***Only Yosemite***, there are additional installer dependencies:
```	
cp -rp /Volumes/install_app/BaseSystem* /Volumes/install_build/
```
* ***Only Yosemite*** Assuming we're executing these steps on a Yosemite machine:
```
cp -rp /System/Library/Kernels /Volumes/install_build/System/Library/
```
* Unmount both the installer image and the target sparse bundle:
```	
hdiutil detach /Volumes/install_app
hdiutil detach /Volumes/install_build
```
* Resize the partition in the sparse bundle to remove any free space:
```	
hdiutil resize -size $(hdiutil resize -limits /tmp/Yosemite.sparseimage | tail -n 1 | awk '{ print $1 }')b /tmp/Yosemite.sparseimage
```
* Convert the sparse bundle to ISO/CD master:
```
hdiutil convert /tmp/Yosemite.sparseimage -format UDTO -o /tmp/Yosemite
```
* Remove the sparse bundle:
```
rm /tmp/Yosemite.sparseimage
```
* Rename the ISO and move it to the desktop:
```
mv /tmp/Yosemite.cdr ~/Desktop/Yosemite.iso
```
