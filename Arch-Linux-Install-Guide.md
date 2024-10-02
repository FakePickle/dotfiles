# Before you Start (you can skip this if you want)
- The written setup guide is not for beginners.. It is meant for people who have already setup base arch linux before. You should also be following the [arch wiki](https://wiki.archlinux.org/).
- While the purpose of the guide is to replace the [wiki installation guide](https://wiki.archlinux.org/title/Installation_guide), it was made with personal use in mind only. This guide also goes slightly beyond the scope of the arch wiki installation guide which doesn't cover everything (like bootloader, user creation and drivers). I know it is there on other pages but again this was with personal use in mind so I don't have to search stuff that I already know.
# Base Install
## Internet Connection
- Use ethernet where possible.
- IIITD BONUS: our institution internet connection is setup in a very interesting way to say the least. You will not be able to use ethernet on archiso because it doesn't use NetworkManager. You could force it to work by editing configs but you're better off with the next option.
- Alternatively use USB tethering with your phone.
## Internet Connection (wifi)
```
iwctl
station wlan0 connect
station wlan0 scan
station wlan0 connect <SSID>
```
## archiso configs (optional)
```
setfont ter-232n
reflector --sort rate --verbose --save /etc/pacman.d/mirrorlist -l 30 -c Singapore -c India
```
## Partitions
### Making the partitions
```
lsblk
wipefs -a -t gpt -f /dev/nvme0n1
cfdisk /dev/nvme0n1
```
- Just delete the memory allocated then follow the next steps.
- Then write and quit
```
wipefs -a -t dos -f /dev/nvme0n1
cfdisk /dev/<drive>
```

Select the following
- gpt
- p1 - resize - 500M - Type - EFI system
- p2 - resize - 8G - Type - Linux swap
- p3 - resize - rest of the size - Type - Linux root (x86-64)
- Write
- Quit

### formatting the partitions
```
mkfs.ext4 /dev/<drive>p3
mkfs.fat -F 32 /dev/<drive>p1
mkswap /dev/<drive>p2
```
### mounting the partitions
```
mount /dev/<drive>p3 /mnt
mount --mkdir /dev/<drive>p1 /mnt/boot
lsblk
swapon /dev/nvme0n1p2
```
## Installing base arch
### pacstrap
> Enable parallel downloads in /etc/pacman.conf to speed up pacstrap
```
pacstrap -K /mnt base base-devel linux linux-firmware
```
### fstab
```
genfstab -U /mnt >> /mnt/etc/fstab
```
### Timezone
```
arch-chroot /mnt
pacman -S vim
ln -sf /usr/share/zoneinfo/Asia/Kolkata  /etc/localtime
hwclock --systohc
```
### Language
```
vim /etc/locale.gen
```
> uncomment `en_US.UTF-8 UTF-8`
```
locale-gen
```
#### `/etc/locale.conf`
```
LANG=en_US.UTF-8
```
### other config files
#### `/etc/vconsole.conf`
```
KEYMAP=us
```
#### `/etc/hostname
```
yourhostname
```
###  user and password
```
passwd
useradd -m -G wheel,audio,video,tty,input -s /bin/bash <username>
passwd <username>
```

```
EDITOR=vim visudo
```
> uncomment `%wheel ALL=(ALL:ALL) ALL`
## bootloader
```
bootctl --path=/boot install
```
#### `/boot/loader/loader.conf`
```
default arch-*
```
#### `/boot/loader/entries/arch.conf`
```
title Arch Linux
linux /vmlinuz-linux
initrd /initramfs-linux.img
options root=/dev/<drive>p3 rw
```

#### `Adding windows to bootloader`
```
mount /dev/<windows_drive>p1 /<new_dir>
cd /<new_dir>/EFI/
cp -r Microsoft/ /boot/EFI/
```

## Network Manager
```
pacman -S sof-firmware networkmanager
systemctl enable NetworkManager
```
## Reboot
```
exit
reboot
```
# Post Install
## Better pacman
```
vim /etc/pacman.conf
```
> uncomment `ParallelDownloads = 5`
## basic install
```
sudo pacman -Syu
sudo pacman -S linux-headers git
sudo pacman -S pipewire pipewire-pulse pipewire-jack pipewire-alsa
sudo pacman -S xorg-server xorg-apps
```
## graphics drivers (choose yours)
```
sudo pacman -S nvidia
sudo pacman -S xf86-video-amdgpu
sudo pacman -S xf86-intel-video
```
## AUR helper
```
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..
rm -rf yay
```
## Better pacman mirrors
```
yay -S rate-mirrors-bin
rate-mirrors arch
```
## Terminal, Display Manager and Window Manager
```
sudo pacman -S lightdm lightdm-gtk-greeter qtile kitty
sudo systemctl enable lightdm
```
## Bluetooth Setup

```
sudo pacman -S blueman bluez bluez-utils
```

## This is for newer Lenovo Laptop's
* WiFi Cards:- RTW89_8852CE
* And facing issues with monitor display with nvidia cards
```
sudo pacman -S nvidia envycontrol

sudo envycontrol -s integrated
reboot

sudo envycontrol -s hybrid
reboot

git clone https://aur.archlinux.org/rtw-dkms-git.git
cd rtw89-dkms-git
makepkg -sri
```
* IMPORTANT: Our BIOS does not handle PCIe interface correctly. To compensate we run this command below:-
```
sudo cp 70-rtw89.conf /etc/modprobe.d/
```
>This command is to be run in the git directory

## Manual Install of Custom Configurations
```
sudo pacman -S python-iwlib python-psutil
yay -S qtile-extras upower

sudo pacman -S dunst picom neovim rofi nitrogen betterlockscreen playerctl
yay -S ttf-cascadia-code-nerd
```
> You can select any wallpaper you like.
```
git clone https://github.com/FakePickle/dotfiles.git
cd dotfiles/Configs
cp -r nvim dunst picom qtile rofi ~/.confg/
```

## Automatic Install of Configs
```
git clone https://github.com/FakePickle/dotfiles.git
cd dotfiles/
chmod +x automatic_install.sh
./automatic_install.sh
```
