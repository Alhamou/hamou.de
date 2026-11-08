---
title: RemoteDesk: an open-source Mac-to-Mac remote desktop for your local network
short_title: RemoteDesk
seo_title: RemoteDesk: open-source Mac-to-Mac remote desktop (LAN)
description: RemoteDesk is an open-source Mac-to-Mac remote desktop for local networks. It streams the screen with hardware H.264 and forwards input. For trusted networks only.
kicker: Open source tool
dek: RemoteDesk shares one Mac's screen and lets you control it from another Mac over your local network. It captures the screen with ScreenCaptureKit, compresses it with hardware H.264 and sends it over TCP. It has no encryption or login, so it is meant for trusted private networks only. The code is open under the MIT license.
keywords: RemoteDesk, Mac to Mac remote desktop, macOS screen sharing LAN, open source remote desktop Mac, ScreenCaptureKit, VideoToolbox H.264, Bonjour, control a Mac from another Mac, Swift, MIT license
product_line: Open-source Mac-to-Mac remote desktop for local networks: hardware H.264 streaming, full input forwarding and clipboard sync. Trusted LANs only.
requirements: macOS 14 or later on both Macs · same local network · MIT license
---

## What is RemoteDesk?

RemoteDesk is an open-source remote desktop for macOS that works between two Macs on the same local network. One Mac shares its screen, the other shows it and sends your mouse, keyboard, scroll and clipboard back. It is written in Swift and uses only Apple's own frameworks, with no third-party libraries.

It is a focused tool: Mac to Mac, over a local network. It is not a cloud service, there is no account, and it is not built for the open internet. Read the security section before you use it.

## How it works

- **The host** is the Mac being controlled. It captures the screen with ScreenCaptureKit, compresses it with VideoToolbox hardware H.264 and sends it through a length-prefixed TCP socket. Remote mouse and keyboard input is injected with `CGEvent`.
- **The client** is the Mac you sit at. It decodes the H.264 stream in hardware, draws it through a `CALayer`, and captures your mouse, keyboard, scroll and clipboard events.

The README describes a custom binary protocol with no B-frames and adaptive congestion control, aimed at low latency. The architecture notes in the repository explain the wire protocol and the concurrency model.

## What it can do

- **Full input forwarding:** precise pointer movement, left, right and middle clicks, pixel-accurate scrolling in both directions, and keyboard input.
- **Full-screen Capture All Input mode:** in full screen, system shortcuts such as Cmd+Tab, Cmd+Space and Mission Control go to the remote Mac instead of your own.
- **Trackpad gestures and Spaces:** in full screen, Spaces swipes, Mission Control, App Exposé and pinches act on the remote Mac, following your trackpad settings.
- **Match Remote Resolution to This Screen:** the host switches to the resolution that best fits the client's display so full screen fills it, and restores it when you disconnect.
- **Clean full-screen edges:** the local Dock stays hidden, and only the top edge reveals your local menu bar and window buttons.
- **Text clipboard sync in both directions,** with loop suppression.
- **Zero-configuration discovery:** hosts announce themselves over Bonjour (`_remotedesk._tcp`) on your Wi-Fi or Ethernet network, or you connect directly by IP address.

## Security: read this first

RemoteDesk is designed only for trusted private local networks, and its README is direct about the limits:

- **No encryption.** Traffic goes over plain TCP without TLS, so screen frames and typed keystrokes cross your network in plaintext.
- **No authentication.** Any device on the same network that reaches the host's port gets full control.
- **Clipboard broadcast.** Text you copy is sent automatically to the connected Mac.

Never run it on untrusted public Wi-Fi such as airports, hotels or cafes. To reach a Mac across the internet, tunnel the traffic through an encrypted channel such as Tailscale, WireGuard or SSH port forwarding. TLS with a pre-shared key and a PIN or one-time password prompt on the host are on the roadmap, not in the app yet.

## Permissions

- **Host:** Screen Recording and Accessibility, both in System Settings under Privacy & Security. Relaunch RemoteDesk after granting Screen Recording.
- **Client:** Accessibility, and only for full-screen Capture All Input mode.

## Install

RemoteDesk needs macOS 14 Sonoma or later on both Macs. The app is a universal binary, so it runs on Apple silicon and Intel. Download the DMG from the latest release on GitHub and drag RemoteDesk to Applications. The release is distributed without a paid Apple Developer ID, so macOS may refuse the first launch: Control-click the app, choose Open, then confirm. The README also gives a Terminal alternative that removes the quarantine attribute with `xattr -cr`.

To build it yourself you need the Swift toolchain (Xcode or the Command Line Tools). Clone the repository and run `./scripts/make-app.sh`.

## Using it

Open RemoteDesk on both Macs. On the host Mac choose **Share This Mac** and grant the permission prompts. On the client Mac choose **Connect to a Mac**, pick the host from the Bonjour list or type its local IP address (the default port is 8790), and choose **Connect**. The host window hides itself while a client is connected; click the Dock icon to see the status or disconnect.

Shortcuts on the client: Ctrl+Cmd+F toggles full screen, Ctrl+Opt+Cmd+G turns input capture on or off, and Ctrl+Opt+Cmd+Q disconnects at once and is never forwarded to the host.

RemoteDesk can also run from the command line, including a headless host with `--host --no-ui`.

## Open source

RemoteDesk is released under the MIT license. Emad Alhamou, the author of this site, publishes it on [GitHub](https://github.com/Alhamou/RemoteDesk). The roadmap lists TLS encryption, a PIN or one-time-password prompt, audio streaming and multi-monitor selection. Bug reports and pull requests are welcome.

<!-- faq -->
## Frequently asked questions

### What is RemoteDesk?

RemoteDesk is an open-source remote desktop for macOS. It shares one Mac's screen and lets you control it from another Mac on the same local network, using hardware H.264 streaming and full input forwarding.

### Is RemoteDesk safe to use?

Only on a trusted private network. It sends traffic over plain TCP without encryption, and it has no login: any device on the network that reaches the host's port gets full control. Do not use it on public Wi-Fi.

### Can I use RemoteDesk over the internet?

Not directly. The README says to tunnel the traffic through an encrypted channel such as Tailscale, WireGuard or SSH port forwarding, and to never expose it on untrusted networks.

### Which Macs and macOS versions does it support?

macOS 14 Sonoma or later on both the host and the client. The app is a universal binary for Apple silicon and Intel.

### Which permissions does RemoteDesk need?

The host needs Screen Recording and Accessibility. The client needs Accessibility only for full-screen Capture All Input mode.

### How do I connect two Macs?

Open RemoteDesk on both. On the host choose Share This Mac. On the client choose Connect to a Mac, pick the host from the Bonjour list or enter its local IP address, and choose Connect.

### What does RemoteDesk not do yet?

It does not encrypt traffic or ask for a PIN. Audio streaming and multi-monitor selection are on the roadmap too. Clipboard sync covers text only.

### Why does macOS warn me when I open RemoteDesk?

The release is distributed without a paid Apple Developer ID certificate. Control-click the app and choose Open, or remove the quarantine attribute with `xattr -cr`.
