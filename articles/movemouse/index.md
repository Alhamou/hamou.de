# moveMouse: a Mac menu-bar app that helps keep your RDP connection from dropping

> moveMouse helps keep a remote desktop (RDP) connection open. It moves the pointer at an interval you choose and stops the Mac from sleeping while it runs, so a quiet session is less likely to be cut off. It lives in the menu bar and its code is open under the MIT license.

- Author: [Emad Alhamou](https://hamou.de/), Founder & Product Builder
- Published: 2026-11-08 (updated 2026-11-08)
- Language: English
- Web page: https://hamou.de/articles/movemouse/
- Other languages: [Deutsch](https://hamou.de/de/articles/movemouse/index.md), [العربية](https://hamou.de/ar/articles/movemouse/index.md)
- Tool: [moveMouse](https://github.com/Alhamou/moveMouse) · macOS 11 or later · Apple silicon build · Accessibility permission · MIT license
- Source code: https://github.com/Alhamou/moveMouse (MIT license)

## What is moveMouse?

moveMouse is a small open-source app for the macOS menu bar. At an interval you choose it moves the mouse pointer by itself, and while it runs it keeps the Mac from going to sleep because of inactivity. It was made for one practical problem: a remote desktop (RDP) connection that drops when you are not touching the Mac. The app's own menu-bar tooltip says so, in Arabic: it is there to prevent RDP connections from being cut.

The README describes it more broadly, as automatic pointer movement on your schedule: useful for desktop demonstrations, for testing mouse interactions, or for keeping a Mac active during a task. It is written in Swift and AppKit and runs without a Dock icon.

## Why an RDP connection drops

Remote desktop sessions usually end for dull reasons. The Mac you connect from goes to sleep and takes the network connection with it, or the remote side treats a session with no input as idle and ends or locks it. moveMouse works from your Mac and tackles both: it prevents idle system sleep while it runs, and it produces pointer activity at the interval you set.

Two honest limits. The app does not know about your RDP client: it moves the pointer on your Mac, so the activity only reaches the remote session while the RDP window is under the pointer. In practice, keep the remote desktop window where the pointer moves, which with the default pattern is the middle of the screen. And moveMouse changes nothing on the remote machine, so a session limit enforced there stays in force.

## What it does

- **Six intervals:** every 15, 30 or 45 seconds, or every 1, 2 or 5 minutes. The first-launch default is 30 seconds.
- **Two movement patterns:** Screen center moves the pointer to the middle of the screen, then right and left, and ends at the center. Current pointer position moves it a short distance right and left and returns it to where it started.
- **An optional left click** after each movement, with an optional sound. The click happens at the final pointer position and lands on whatever is underneath it.
- **Simple menu-bar controls:** Start or Pause, Move Now (it also works while paused), and Quit. A status line shows whether movement is running and when the last operation happened.
- **Saved preferences:** interval, pattern, click and sound settings are kept between launches.
- **Sleep prevention:** idle system sleep is blocked while automatic movement runs. Pausing or quitting releases it.

moveMouse starts moving as soon as it launches, using your saved settings. The menu labels are in Arabic, with English labels for several controls: Start, Pause, Move Now, Interval and Left Click.

## Permissions

Simulated mouse input needs the Accessibility permission. On first launch macOS may ask you to allow it: open System Settings, go to Privacy & Security, then Accessibility, and enable moveMouse. The Accessibility item in the app's menu opens that page for you. According to the README, clicking is the part that needs it most. If clicking stops working after you rebuild or move the app, remove its Accessibility entry, add the app again and relaunch it.

## Install

moveMouse needs macOS 11 Big Sur or later. The included app and the build script target Apple silicon (arm64). Clone the repository from GitHub, then run `./build.sh` and `./run.sh`. Building needs the Xcode Command Line Tools, which `xcode-select --install` installs. The script signs the app locally with an ad-hoc signature.

To start moveMouse when you sign in, add `MoveMouse.app` to your Login Items in System Settings, under General. To stop it, choose Quit in the menu or run `./stop.sh` from the project folder.

## Open source

moveMouse is released under the MIT license. It uses only native macOS frameworks and builds directly with `swiftc`, with no third-party dependencies and no Xcode project. The code is a handful of Swift files: the menu-bar interface, the movement timer with pointer input and saved preferences, and the sleep prevention.

Emad Alhamou, the author of this site, publishes moveMouse on [GitHub](https://github.com/Alhamou/moveMouse). Bug reports, ideas and pull requests are welcome; include your macOS version, the steps to reproduce and what you expected.

## Frequently asked questions

### What is moveMouse?

moveMouse is an open-source macOS menu-bar app that moves the pointer automatically at an interval you choose and keeps the Mac from sleeping while it runs. It was made to help keep an RDP connection from dropping.

### How does moveMouse help with an RDP connection?

It works from your Mac. It prevents idle system sleep, which would otherwise take the connection down, and it creates pointer activity at your chosen interval so a session is not left completely quiet. The activity reaches the remote session only while the RDP window is under the pointer, and moveMouse does not change any setting on the remote machine.

### Will the click land on something I did not intend?

It can. The optional left click happens at the final pointer position and interacts with whatever is underneath it. If you only want movement, turn off Left Click in the menu. It is on by default.

### Which intervals and movement patterns are available?

Intervals are 15, 30 and 45 seconds and 1, 2 and 5 minutes, with 30 seconds as the default. The two patterns are Screen center (center, right, left, back to center) and Current pointer position (a small right and left wiggle, then back to the start).

### Which permission does moveMouse need?

Accessibility, for simulated mouse input, especially clicking. Enable moveMouse under Privacy & Security, then Accessibility, in System Settings.

### Which Macs and macOS versions are supported?

macOS 11 Big Sur or later. The included app and the build script target Apple silicon (arm64).

### How do I pause or stop moveMouse?

Choose Pause in the menu-bar menu to stop scheduled movement and release sleep prevention, or Quit to close the app. Move Now performs one movement on demand, even while paused.

### Is moveMouse open source?

Yes. It is released under the MIT license, and the source is on GitHub.
