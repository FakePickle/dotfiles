#!/bin/sh

nitrogen --restore &
autorandr --load laptop_config
numlockx on &
emacs --daemon
xmodmap ~/.Xmodmap
