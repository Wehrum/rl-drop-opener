# rl-drop-opener

## Table of Contents

- [rl-drop-opener](#rl-drop-opener)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Usage](#usage)
    - [Downloading the release file](#downloading-the-release-file)
    - [Running the script directly](#running-the-script-directly)
      - [Setup](#setup)
  - [Building a release](#building-a-release)

## Overview

Simple bot that will automatically open Rocket League drops for you,
saving you from having to do it yourself.

## Usage

### Downloading the release file

For an easy to use/no setup nesseary approach, I created a release build of this project.

You can download the latest release [here](https://github.com/Wehrum/rl-drop-opener/releases/download/v0.1/rl_drop_opener.exe)

Simply run the `.exe` and follow the prompts.

### Running the script directly

While it is not needed to run the script directly, if you'd rather do this instead of
running the `.exe` this is for you.

#### Setup

- Make sure you have `Python 3.8.10` installed or higher.
- Clone the repostiory with `git clone https://github.com/Wehrum/rl-drop-opener.git`
- Navigate to the root of this reposistory
- Install the required python modules with `pip install -r requirements.txt`
- Run the program by executing `python3 main.py` while in the root of the repoistory.

## Building a release

A release is built by installing `pyinstaller` and running

```bash
pyinstaller --onefile main.py
```
