---
title: pinFiy: colored sticky notes for the Mac, with a small pin in the menu bar
short_title: pinFiy
seo_title: pinFiy: colored sticky notes for Mac in the menu bar
description: pinFiy is an open-source macOS sticky notes app. Each note is its own window, Arabic runs right to left, and there is no account, cloud sync or network access.
kicker: Open source tool
dek: pinFiy gives your Mac colored sticky notes that live behind a small pin in the menu bar. Each note is its own window, Arabic text runs right to left and English left to right, and a pinned note stays above your other windows. There is no account, no cloud sync and no network access. The code is open under the MIT license.
keywords: pinFiy, sticky notes Mac, menu bar notes app, macOS sticky notes, Arabic right-to-left notes app, pinned notes, open source notes app Mac, Swift, MIT license
product_line: Open-source macOS sticky notes app: colored notes in their own windows, automatic right-to-left text, pin to keep on top, local storage only.
requirements: macOS 13 or later · Swift 5.9 or later to build · MIT license
---

## What is pinFiy?

pinFiy is an open-source sticky notes app for macOS. Each note is its own colored window. The app itself is a small pin in the menu bar and does not appear in the Dock, so it stays out of the way until you need a note.

It handles Arabic and English side by side. Text direction follows the first strong character of what you type: Arabic runs right to left and English runs left to right, in the same app and even on neighboring notes.

## What it does

- **One window per note,** so you can place each note where you need it.
- **Pin keeps a note on top.** A pinned note stays above normal windows and does not cover the menu bar. The pin corner follows the text direction: right for Arabic, left for English.
- **Twenty colors:** ten light and ten dark. The default is a warm amber (`#F3C15B`). Dark text sits on light colors and light text on dark ones.
- **Font size from 12 to 36** for each note, and from Settings for new notes or for every note.
- **Lock a note** to block changes to its text, color, size and position, and to stop it from being closed.
- **A safety net:** closing a note that has text asks for confirmation first.
- **Open at login,** from Settings or from the pin menu.

## Where your notes live

Notes are stored on your Mac, in `~/Library/Application Support/pinFiy/notes.json`, with a backup file. According to the README there is no account, no cloud sync and no network access. The repository includes a privacy policy and a security policy.

## Shortcuts

- **New note:** the plus button, `⌘N`, or the pin menu.
- **Close a note:** the close button or `⌘W`.
- **Keep above windows:** the pin button or `⌘P`.
- **Settings:** `⌘,` or the pin menu.
- **Quit:** `⌘Q` or the pin menu.

## Install

pinFiy needs macOS 13 or later and Swift 5.9 or later, which the toolchain that ships with Xcode includes. Clone the repository from GitHub, run `swift test`, then `./scripts/build-app.sh`, and open `PinFiy.app`. The script signs the app ad hoc. That is not an Apple Developer signature and not an App Store release.

## Open source

pinFiy is released under the MIT license. The code is split into a core library for the model and storage, with no AppKit in it, and an app target for the note windows and the menu bar. The core has XCTest tests.

Emad Alhamou, the author of this site, publishes pinFiy on [GitHub](https://github.com/Alhamou/pinFiy). The repository has contribution guidelines and a code of conduct, and security issues are reported privately as its security policy describes.

<!-- faq -->
## Frequently asked questions

### What is pinFiy?

pinFiy is an open-source sticky notes app for macOS. It gives you colored notes, each in its own window, controlled from a small pin in the menu bar.

### Does pinFiy support Arabic and right-to-left text?

Yes. Text direction follows the first strong character: Arabic runs right to left and English runs left to right. The pin corner of a note follows the direction too.

### What does Pin do?

Pin keeps a note above normal windows without covering the menu bar. Use the pin button on the note or press `⌘P`.

### Where are my notes stored, and does pinFiy use the network?

Notes are stored locally in `~/Library/Application Support/pinFiy/notes.json`, with a backup. According to the README there is no account, no cloud sync and no network access.

### What does locking a note do?

A locked note cannot be edited, recolored, resized or moved, and it cannot be closed, until you unlock it.

### Which macOS version does pinFiy need?

macOS 13 or later. Building it needs Swift 5.9 or later.

### How do I install pinFiy?

Clone the repository, run `swift test` and `./scripts/build-app.sh`, then open `PinFiy.app`. The build is signed ad hoc, not with an Apple Developer certificate.

### Can I change the font size and colors?

Yes. Each note has color swatches and font size buttons, from 12 to 36. Settings sets the size for new notes or for every note.
