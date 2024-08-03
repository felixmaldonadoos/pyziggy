
# Intro

```
d8888b. db    db d88888D d888888b  d888b   d888b  db    db
88  `8D `8b  d8' YP  d8'   `88'   88' Y8b 88' Y8b `8b  d8'
88oodD'  `8bd8'     d8'     88    88      88       `8bd8'
88~~~      88      d8'      88    88  ooo 88  ooo    88
88         88     d8' db   .88.   88. ~8~ 88. ~8~    88
88         YP    d88888P Y888888P  Y888P   Y888P     YP
```

Simple python tool to install specific pre-built `zig` files compiler. 

## Missing: 

- Still need to add some functions to properly export paths to binary directory. I may do this in a `bash` script or `python`, not sure yet. `bash` would be easier for me. 

## Overview

I test this mainly on a Windows 11 machine with `WSL2 Ubuntu-22.04` and `python3.10`. 

`downloader.py` checks what platform you are working on, and uses `curl` or `winget` (for linux and windows, respectively) as the downloader of choice. Both, `curl` and `winget` are called using the `subprocess` python library. 

Development machine: 
- `WSL2 Ubuntu-22.04` and `Python3.10`

Tested and working on: 
- `WSL2 Ubuntu-24.04` and `Python3.12`
- Native `Ubuntu-22.04` and `Python3.10`

## Setup

1. Install dependencies

```
pip  install requirements.txt
```

2. That is it.

## Example Usage

### Run:

```
python3 main.py
```

### Output:

```

d8888b. db    db d88888D d888888b  d888b   d888b  db    db
88  `8D `8b  d8' YP  d8'   `88'   88' Y8b 88' Y8b `8b  d8'
88oodD'  `8bd8'     d8'     88    88      88       `8bd8'
88~~~      88      d8'      88    88  ooo 88  ooo    88
88         88     d8' db   .88.   88. ~8~ 88. ~8~    88
88         YP    d88888P Y888888P  Y888P   Y888P     YP


Welcome to the Zig downloader!
This program will help you download Zig for your system.
Let's get started!

Author: Alexander Maldonado (felixmaldonado2023@u.northwestern.edu)
Date: 08-02-2024

*** Select value to set ***
0) Use default values
1) os
2) architecture
3) has_signature
4) latest_version
5) Continue
6) Quit
Enter your choice: 0
Default values have been set.
*** Select value to set ***
0) Use default values
1) os (OK - linux)
2) architecture (OK - x86_64)
3) has_signature (OK - True)
4) latest_version (OK - True)
5) Continue
6) Quit
Enter your choice: 5
Continuing with current choices...
Final choices: {'os': 'linux', 'architecture': 'x86_64', 'has_signature': True, 'latest_version': True}
Status: Looking for download url for linux and x86_64:
Warning: url_list is None, using cached list
Found (18) downloadable files
NEED TO FIX THIS: breaks if we include the latest branch (unstable)
*** Select URL to download ***
1) https://ziglang.org/builds/zig-linux-x86_64-0.14.0-dev.829+2e26cf83c.tar.xz
2) https://ziglang.org/download/0.13.0/zig-linux-x86_64-0.13.0.tar.xz
3) https://ziglang.org/download/0.12.1/zig-linux-x86_64-0.12.1.tar.xz
4) https://ziglang.org/download/0.12.0/zig-linux-x86_64-0.12.0.tar.xz
5) https://ziglang.org/download/0.11.0/zig-linux-x86_64-0.11.0.tar.xz
6) https://ziglang.org/download/0.10.1/zig-linux-x86_64-0.10.1.tar.xz
7) https://ziglang.org/download/0.10.0/zig-linux-x86_64-0.10.0.tar.xz
8) https://ziglang.org/download/0.9.1/zig-linux-x86_64-0.9.1.tar.xz
9) https://ziglang.org/download/0.9.0/zig-linux-x86_64-0.9.0.tar.xz
10) https://ziglang.org/download/0.8.1/zig-linux-x86_64-0.8.1.tar.xz
11) https://ziglang.org/download/0.8.0/zig-linux-x86_64-0.8.0.tar.xz
12) https://ziglang.org/download/0.7.1/zig-linux-x86_64-0.7.1.tar.xz
13) https://ziglang.org/download/0.7.0/zig-linux-x86_64-0.7.0.tar.xz
14) https://ziglang.org/download/0.6.0/zig-linux-x86_64-0.6.0.tar.xz
15) https://ziglang.org/download/0.5.0/zig-linux-x86_64-0.5.0.tar.xz
16) https://ziglang.org/download/0.4.0/zig-linux-x86_64-0.4.0.tar.xz
17) https://ziglang.org/download/0.3.0/zig-linux-x86_64-0.3.0.tar.xz
18) https://ziglang.org/download/0.2.0/zig-linux-x86_64-0.2.0.tar.xz
19) Quit
Enter your choice: 1
Downloading https://ziglang.org/builds/zig-linux-x86_64-0.14.0-dev.829+2e26cf83c.tar.xz...
--2024-08-02 22:20:26--  https://ziglang.org/builds/zig-linux-x86_64-0.14.0-dev.829+2e26cf83c.tar.xz
Resolving ziglang.org (ziglang.org)... 108.159.227.36, 108.159.227.56, 108.159.227.113, ...
Connecting to ziglang.org (ziglang.org)|108.159.227.36|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 47266412 (45M) [application/x-xz]
Saving to: ‘/mnt/c/Users/famal/Documents/Projects/pyziggy/zig-linux-x86_64-0.14.0-dev.829+2e26cf83c.tar.xz.1’

zig-linux-x86_64-0.14.0-dev.829+2e26cf 100%[===========================================================================>]  45.08M  36.9MB/s    in 1.2s

2024-08-02 22:20:28 (36.9 MB/s) - ‘/mnt/c/Users/famal/Documents/Projects/pyziggy/zig-linux-x86_64-0.14.0-dev.829+2e26cf83c.tar.xz.1’ saved [47266412/47266412]

Download successful!
Thank you for using the Zig downloader!

```