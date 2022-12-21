---
tags: hardware, guide, tech
category: tech
subtitle: Useful Linux commands (installing software, networking, etc.)
---

Thanks to *clarkdonald413* on Pixabay for the [picture](https://pixabay.com/photos/linux-code-coding-program-computer-4259595/).

# Essential Linux commands you should know

## What lead me to creating this cheatsheet
I've often found myself looking up simple commands, such as how to display the current IP address.
So, I wanted to share my favorite general purposes Linux commands, no matter if they're distribution-dependent or not (I'll mention the distribution support for commands which are distribution-dependent, of course!)

## Package managers
### Install
    yay PACKAGE # AUR (Arch User Repository package installer wrapper) 
    pip install PACKAGE # Python
    npm install PACKAGE # NodeJS

    sudo pacman -S PACKAGE # Arch(-based distros)
    sudo apt install PACKAGE # "Advanced Packaging Tool" for Debian(-based distros)
    sudo snap install PACKAGE # Snap

### List
    snap list
    pip freeze
    pacman -Qm # AUR packages (yay/pacman/etc.)
    apt list --installed
    npm list -g --depth=0


### Uninstall
    npm remove PACKAGE
    pip uninstall PACKAGE

    sudo apt remove PACKAGE
    sudo pacman -Rdd PACKAGE # AUR packages (yay/pacman/etc.)
    sudo snap remove PACKAGE


## Screen Sessions
[GNU Screen](https://en.wikipedia.org/wiki/GNU_Screen) is a terminal multiplexer, which means you can easily manage different tasks on your server.

    screen -S NAME # start a screen session
    screen -ls # list all screen sessions
    screen -XS NAME quit # stop a screen session

## Networking
    kill -9 $(lsof -t -i:PORT) # kills a port
    curl api.ipify.org # get public IP (v4) address 
