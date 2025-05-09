#!/bin/bash

BLANK='#00000000'
CLEAR='#ffffff22'
DEFAULT='#282a36'
KEY='#8a8ea8'
TEXT='#ffffff' # Changed for better contrast
VERIFYING='#414458'

i3lock -n -i ~/Downloads/optimized_fog_forest.png -L \
    --insidever-color=$CLEAR \
    --ringver-color=$VERIFYING \
    \
    --inside-color=$CLEAR \
    --ring-color=$DEFAULT \
    --line-color=$BLANK \
    --separator-color=$DEFAULT \
    \
    --verif-color=$TEXT \
    --wrong-color=$TEXT \
    --time-color=$TEXT \
    --date-color=$TEXT \
    --layout-color=$TEXT \
    --keyhl-color=$KEY \
    --bshl-color=$TEXT \
    \
    --screen 1 \
    --radius 95 \
    --clock \
    --time-str="%H:%M" \
    --indicator \

