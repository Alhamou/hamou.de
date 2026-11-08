# SafeShare: hide private apps while you share your Mac screen in Teams, Zoom or Meet

> SafeShare solves a screen-sharing dilemma: share the whole screen and risk leaking private chats and notifications, or share one window and lose multitasking. It builds a filtered Safe View window that leaves out the apps you protect. You share that window in Teams, Zoom or Meet and keep working on your real desktop. The code is open under the MIT license.

- Author: [Emad Alhamou](https://hamou.de/), Founder & Product Builder
- Published: 2026-11-08 (updated 2026-11-08)
- Language: English
- Web page: https://hamou.de/articles/safeshare/
- Other languages: [Deutsch](https://hamou.de/de/articles/safeshare/index.md), [العربية](https://hamou.de/ar/articles/safeshare/index.md)
- Tool: [SafeShare](https://github.com/Alhamou/SafeShare) · macOS 14 or later · Screen & System Audio Recording permission · MIT license
- Source code: https://github.com/Alhamou/SafeShare (MIT license)

## What is SafeShare?

SafeShare (also called ScreenGuard) is an open-source macOS utility for people who present their desktop in remote meetings. It hides the apps and windows you mark as private from what the meeting sees, while you keep working normally on your real screen.

## The problem it solves

When you present from a Mac, both built-in options have a cost. Share the entire screen and a private chat, a password manager, an inbox or a notification can leak into the meeting. Share a single application window and you lose the ability to multitask or to show a workflow that crosses apps.

## How it works

SafeShare adds a third option, a filtered preview called **Safe View**:

1. It captures your screen with Apple's ScreenCaptureKit.
2. It removes the apps and windows you protect from that capture, using a content filter.
3. It shows the cleaned-up desktop in its own window, Safe View.
4. In Teams, Zoom or Google Meet you share the Safe View window instead of your screen.

You see everything on your real desktop. Attendees see only what you allow.

## Use it with Teams, Zoom or Meet

First open SafeShare from the shield icon in the menu bar, mark the sensitive apps as protected and choose Start Safe View (while the SafeShare panel is open, `⌘⇧S` toggles it). Then, in your meeting app:

- **Microsoft Teams:** choose Share, then under Window select SafeShare — Safe View.
- **Zoom:** choose Share Screen, pick the SafeShare — Safe View window in the list and choose Share.
- **Google Meet:** choose Present now, then A window, and pick SafeShare — Safe View.

If you share your entire screen instead of the Safe View window, nothing is filtered, so always pick the window.

## Keep the Safe View window large

Meeting apps share a window at its on-screen size, so a Safe View window shrunk into a corner is unreadable for attendees. According to the README, SafeShare locks the window to the display's aspect ratio, refuses to go below half of the display size and shows a banner, with the exact resolution viewers receive, when it is downscaled. A Send to Back button in the menu parks the window behind your work at full size, and the stream keeps running while the window is covered.

## What it can do

- **One-click protection:** toggle any running app to protected from the menu bar.
- **Per-window and multi-instance control:** group apps with several windows, such as a browser or a terminal, and set each window to Visible, Protected or Inherit.
- **Fail-closed blanking:** the stream goes blank during a screen lock, sleep or a permission change, so no frame leaks through.
- **Multi-display support:** choose which physical display to capture.
- **Stream quality:** switch between 15, 30 and 60 frames per second without restarting the stream.
- **Notification auto-hiding:** Notification Center banners are kept out of the stream.
- **Launch at login, VoiceOver labels and keyboard shortcuts.**

## Privacy and permissions

SafeShare needs one permission, the standard Screen & System Audio Recording access, with no root privileges and no kernel extensions. According to the README it stores no video frames or window titles on disk, has no telemetry and makes no network calls. The repository includes a security policy with the details.

## Install

SafeShare needs macOS 14 Sonoma or later. Download the DMG from the latest release on GitHub, open it and drag SafeShare to Applications. To build it yourself you need Xcode 15 or later: clone the repository, run `swift test`, then `./scripts/build_app.sh`, and `./scripts/package_dmg.sh` if you want a DMG.

## Open source

SafeShare is released under the MIT license. Emad Alhamou, the author of this site, publishes it on [GitHub](https://github.com/Alhamou/SafeShare). The repository has a continuous integration workflow. Bug reports and pull requests are welcome.

## Frequently asked questions

### What is SafeShare?

SafeShare is an open-source macOS utility that hides private apps and windows while you share your screen in Teams, Zoom or Google Meet. It does this through a filtered preview window called Safe View.

### How does SafeShare hide apps during screen sharing?

It captures your screen with ScreenCaptureKit, filters out the apps and windows you marked as protected and shows the result in the Safe View window. You share that window in your meeting app instead of your whole screen.

### Does it work with Teams, Zoom and Google Meet?

Yes. In each of them you share the SafeShare — Safe View window: through Share and Window in Teams, Share Screen in Zoom, and Present now then A window in Google Meet.

### What if I share my entire screen instead of the Safe View window?

Then nothing is filtered and attendees see everything. The protection applies only to what appears in the Safe View window, so always choose that window in your meeting app.

### Why should the Safe View window stay large?

Meeting apps share a window at its on-screen size, so a tiny window is hard to read. SafeShare keeps the display's aspect ratio, will not go below half of the display size and has a Send to Back button that keeps the window out of your way at full size.

### Which permission does SafeShare need, and does it send data anywhere?

It needs Screen & System Audio Recording access. According to the README it has no telemetry, makes no network calls and stores no video frames or window titles on disk.

### What happens when the screen locks or the Mac sleeps?

The stream is blanked during screen lock, sleep and permission changes, which the README calls fail-closed blanking. Notification Center banners are also kept out of the stream.

### Which macOS version does SafeShare need?

macOS 14 Sonoma or later.
