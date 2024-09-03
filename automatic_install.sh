#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions to print messages
print_info() {
    echo -e "${YELLOW}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# Update and install packages
print_info "Updating system and installing packages..."
sudo pacman -Syu --noconfirm && print_success "System updated."
sudo pacman -S --noconfirm python-iwlib python-psutil dunst picom neovim rofi nitrogen betterlockscreen playerctl && print_success "Packages installed."

# Install AUR packages
print_info "Installing AUR packages..."
yay -S --noconfirm qtile-extras ttf-cascadia-code-nerd && print_success "AUR packages installed."

# Copy configurations
print_info "Copying configurations..."
cd Configs
cp -r nvim dunst picom qtile rofi ~/.config/ && print_success "Configurations copied."

print_success "Installation complete! Enjoy your setup!"

