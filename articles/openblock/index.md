# OpenBlock: an open-source ad blocker for Safari on Mac, with no tracking

> OpenBlock blocks ads and trackers in Safari on your Mac. It downloads real filter lists, converts them into Safari's own rule format and lets Safari enforce them, so nothing sits between you and the web. The code is open under the GPL-3.0 license.

- Author: [Emad Alhamou](https://hamou.de/), Founder & Product Builder
- Published: 2026-11-08 (updated 2026-11-08)
- Language: English
- Web page: https://hamou.de/articles/openblock/
- Other languages: [Deutsch](https://hamou.de/de/articles/openblock/index.md), [العربية](https://hamou.de/ar/articles/openblock/index.md)
- Tool: [OpenBlock](https://github.com/Alhamou/OpenBlock) · macOS 15 Sequoia or later · Swift · GPL-3.0 license
- Source code: https://github.com/Alhamou/OpenBlock (GPL-3.0 license)

## What is OpenBlock?

OpenBlock is an open-source ad blocker for Safari on macOS. It follows the same recipe as AdGuard for Safari: filter lists go through a converter and become Safari content blockers. The app downloads the lists, converts them to Safari's native rule format and hands them to Safari, which compiles them into its own engine. Nothing sits between you and the web, and OpenBlock sends no data about your browsing anywhere.

It blocks only inside Safari. Other browsers and apps never see the rules. DNS-based blocking for every app on the Mac is the next feature on the project's roadmap.

## What it blocks with

- **Four Safari content blockers:** Ads, Privacy, Annoyances and Custom. Each has its own budget of 150,000 rules.
- **Real filter lists:** AdGuard Base, Tracking, Social, Cookie and Popups (the Safari builds), EasyList, EasyPrivacy, regional lists, or any list URL you add, in AdBlock syntax or as a hosts file.
- **Your own rules and an allowlist,** written in AdBlock syntax. Sites on the allowlist are left alone.
- **Automatic updates:** the lists refresh every 24 hours while OpenBlock is running, and the menu bar has an Update Filters Now command next to Pause Blocking and Launch at Login.

## OpenBlock Advanced

Safari's content blockers cannot express every rule. For the rest there is OpenBlock Advanced, a Safari web extension. It runs scriptlets (AdGuard's `#%#//scriptlet(...)` rules and uBlock Origin's `##+js(...)` rules), injects CSS (`#$#`), supports extended CSS selectors (`#?#`, `:has-text()`, `:remove()`) and handles rules for domains with a wildcard top-level domain such as `example.*`. The project names YouTube ads and anti-adblock walls as examples. Its toolbar button shows the status of the current site and lets you pause the advanced rules for that site.

## Privacy

The README describes OpenBlock as having no tracking, and its security policy says the only network traffic is the download of the filter lists you turned on. There is no telemetry, no analytics and no crash reporting, and OpenBlock does not read your browsing history. Because Safari compiles the rules itself, the app never sits in the path of your web traffic.

## Install

OpenBlock needs macOS 15 Sequoia or later. Download the DMG from the latest release on GitHub and drag OpenBlock to Applications. The build is signed with an Apple Development certificate and is not notarized, so macOS asks for confirmation the first time: open System Settings, go to Privacy & Security and choose Open Anyway next to OpenBlock.

Then open OpenBlock, pick your filter lists and wait for the first conversion to finish. In Safari, open Settings, then Extensions: enable the four OpenBlock content blockers and OpenBlock Advanced, and allow it on every website. Keep a single copy of the app on disk, because Safari gets confused when two builds register the same extensions.

To build it yourself you need Xcode 16 or later and XcodeGen. Safari only loads signed extensions, so an unsigned build does not block anything.

## Open source

OpenBlock is licensed under GPL-3.0, because OpenBlock Advanced bundles AdGuard's GPL-3 Scriptlets and ExtendedCss libraries. The filter lists are downloaded when the app runs and keep their own licenses. OpenBlock is not affiliated with AdGuard. The repository also includes a command-line converter that you can verify against WebKit's own rule compiler.

Emad Alhamou, the author of this site, publishes OpenBlock on [GitHub](https://github.com/Alhamou/OpenBlock). Bug reports and pull requests are welcome.

## Frequently asked questions

### What is OpenBlock?

OpenBlock is an open-source ad blocker for Safari on macOS. It converts real filter lists into Safari's native content blockers and adds a web extension for advanced rules.

### Does OpenBlock work in Chrome, Firefox or other apps?

No. OpenBlock blocks only inside Safari, because Safari compiles the rules into its own engine and other browsers and apps never see them. DNS-based blocking for every app is planned.

### Which filter lists does OpenBlock use?

AdGuard Base, Tracking, Social, Cookie and Popups, EasyList, EasyPrivacy and regional lists, plus any list URL you add. Lists can use AdBlock syntax or be hosts files.

### Does OpenBlock collect my data?

According to its README and security policy, no. It has no telemetry, analytics or crash reporting, and the only network traffic is the download of the filter lists you turned on.

### Which macOS version does OpenBlock need?

macOS 15 Sequoia or later.

### Why does macOS warn me when I open OpenBlock?

The release build is signed with an Apple Development certificate, not a Developer ID, and it is not notarized. Use Open Anyway in System Settings under Privacy & Security to open it. Signing with a Developer ID and notarization are on the project's roadmap.

### Is OpenBlock affiliated with AdGuard?

No. It is built the same way (filter lists, a converter, Safari content blockers) and bundles AdGuard's open-source Scriptlets and ExtendedCss libraries, which is why it is licensed under GPL-3.0.
