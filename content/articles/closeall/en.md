---
title: closeAll: force-quit every Dock app from one menu-bar button on Mac
short_title: closeAll
seo_title: closeAll: force-quit all Mac apps from one menu-bar button
description: closeAll is an open-source macOS menu-bar app that force-quits every normal Dock app at once, after you review the list. Unsaved work in those apps is lost.
kicker: Open source tool
dek: closeAll force-quits every normal Dock app from one button in the menu bar. You review the list first, uncheck what should stay open and press Force Quit. Force Quit does not ask apps to save, so unsaved work is lost. The code is open under the MIT license.
keywords: closeAll, force quit all apps Mac, quit all apps macOS, close all Dock apps, menu bar app, Force Quit, Apple silicon, Swift, MIT license
product_line: Open-source macOS menu-bar app that force-quits every normal Dock app at once, with a review list and a keep-list. Unsaved work is lost.
requirements: macOS 14 or later · Apple silicon build · MIT license
---

## What is closeAll?

closeAll is a small open-source macOS menu-bar app with one job: close every normal app that is running, in one go. Its icon in the menu bar is a small stack of windows. Click it, review the list, then press **Force Quit**. The checked apps are closed with Force Quit.

Read this once before you use it: Force Quit does not ask an app to save. Unsaved work in the apps you close is lost.

## How you use it

1. Click the stack-of-windows icon at the top of the screen.
2. Leave a check on every app that should close. Remove the check to keep an app open; closeAll remembers that choice.
3. Under **Background apps**, check any menu-bar app that should close too.
4. Press **Force Quit**.

Each row shows the app's own icon, so you can recognize it before it closes. Close or uncheck anything that has unsaved work first.

## What closes

- **Every normal application,** the kind you would otherwise right-click in the Dock and quit. Editors, browsers and chat apps are included, so uncheck any you want to keep.
- **Background apps you check.** The Background apps section lists menu-bar apps that you installed in `/Applications` or `~/Applications`, such as a clipboard manager or a VPN client. They start unchecked, so nothing there closes unless you check it.

closeAll verifies that each app really exited. If an app survives Force Quit or comes straight back, it sends a hard kill (SIGKILL), up to three times. Any app it still could not close is named in red.

## What stays open

- **Finder,** so the desktop stays up, and **closeAll** itself, so the button is still there.
- The Dock, Control Center, WindowServer and the other processes that keep your login session alive.
- Any app you uncheck, and background apps you did not check.
- Apple's own menu-bar agents, helpers packed inside another app, updaters kept in Library folders, and processes with no window or menu are not listed at all. They usually close together with their parent app.

## Privacy and permissions

closeAll is not sandboxed, because the App Sandbox would block it from quitting other applications. According to the README it does not use the network and does not collect analytics. Your keep-list is stored only in your local preferences.

## Install

closeAll needs macOS 14 or later. The app that `make app` builds on an Apple silicon Mac is an Apple silicon app. Clone the repository from GitHub, run `make app`, and open `build/closeAll.app`. Copy it to `/Applications` if you want to keep it installed. It shows no Dock icon.

The build is signed ad hoc so it can launch on your Mac, and it is not notarized. If macOS blocks the first launch, Control-click `closeAll.app`, choose Open and confirm. To open it at login, add it under General in System Settings, then Login Items. To quit it, open the panel and choose Quit closeAll.

## Check the plan without closing anything

`swift run closeAll -- --dry-run` prints the quit plan as JSON and exits without closing any app. `make check` runs the unit tests and then prints the live plan, and it fails if that plan includes Finder, closeAll itself or another session process.

## Open source

closeAll is released under the MIT license. The quit rules live in a separate core module with no AppKit, covered by unit tests, and the menu-bar app is built on top of it. The repository also has an Arabic README.

Emad Alhamou, the author of this site, publishes closeAll on [GitHub](https://github.com/Alhamou/closeAll). Contribution guidelines, a code of conduct and a security policy are in the repository.

<!-- faq -->
## Frequently asked questions

### What is closeAll?

closeAll is an open-source macOS menu-bar app that force-quits every normal Dock app from one button, after you review the list and uncheck anything that should stay open.

### Will I lose unsaved work?

Yes. Force Quit does not ask apps to save. Close or uncheck anything with unsaved work before you press the button.

### Which apps does closeAll close, and which stay open?

It closes every normal application that macOS shows in the Dock, plus any background menu-bar apps you check. Finder, closeAll itself, the Dock, Control Center, WindowServer and other session processes always stay open, and so does any app you uncheck.

### Can I keep some apps open?

Yes. Uncheck an app in the list and closeAll keeps it open and remembers that choice.

### Does it close menu-bar apps such as a VPN client?

Only if you check them. The Background apps section lists menu-bar apps from `/Applications` and `~/Applications`, and they start unchecked.

### What if an app will not quit?

closeAll checks that each app really exited. If one survives or comes straight back, it sends a hard kill (SIGKILL), up to three times, and names any app it still could not close in red.

### Does closeAll use the network or collect data?

According to the README, no. It is not sandboxed, it does not use the network and it does not collect analytics. Your keep-list stays in local preferences.

### Which Macs and macOS versions are supported?

macOS 14 or later. The app that `make app` builds on an Apple silicon Mac is an Apple silicon app.
