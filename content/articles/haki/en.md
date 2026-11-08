---
title: Haki (حكي): push-to-talk dictation for the Mac menu bar, tuned for Arabic
short_title: Haki
seo_title: Haki: Arabic push-to-talk dictation for Mac (OpenAI)
description: Haki is an open-source macOS menu-bar dictation app. Hold Option+Space, speak Arabic, English, German or French, release, and the text is pasted at your cursor.
kicker: Open source tool
dek: Haki turns your voice into text anywhere on your Mac. Hold Option+Space, speak, release, and the transcribed text is pasted at your cursor. It is tuned for natural Arabic, including Levantine and Syrian speech, and also handles English, German and French. Transcription uses OpenAI models with your own API key, so your audio goes to OpenAI. The code is open under the MIT license.
keywords: Haki, حكي, Arabic dictation Mac, speech to text macOS, push-to-talk dictation, Levantine Arabic speech recognition, OpenAI transcription, gpt-4o-transcribe, voice typing menu bar app, Swift, MIT license
product_line: Open-source macOS menu-bar push-to-talk dictation: hold a hotkey, speak Arabic, English, German or French, and the text is pasted at your cursor. Uses OpenAI transcription with your own API key.
requirements: macOS 13 or later · OpenAI API key · Microphone and Accessibility permissions · MIT license
---

## What is Haki?

Haki (حكي, a Levantine Arabic word for talking) is a lightweight native macOS menu-bar app for speech-to-text dictation. Click into any text field in any app, hold the push-to-talk hotkey, speak, and let go. Haki transcribes what you said and pastes it at the cursor. Its tagline in Arabic is "احكي، وحكي بيكتبها", roughly "you talk, Haki writes it".

It is designed especially for natural Arabic and Levantine speech, with support for English, German, French and automatic language detection. It has no local speech model and no Python or Node.js runtime: the app is native Swift, and the transcription is done by OpenAI.

## How dictation works

1. Focus a text field in any application, such as Notes, TextEdit, a browser, a chat app or an editor.
2. Press and hold `⌥ Option + Space` and speak.
3. Release the keys. Haki sends the recording to OpenAI, receives the text and pastes it at your cursor.

Haki saves your clipboard before pasting and restores it afterwards, and it does this without stealing focus from the app you are typing in. A small floating indicator shows whether it is recording, transcribing or done. Accidental taps shorter than about a third of a second are discarded locally.

## Languages and models

- **Languages:** Arabic (with optimization for Levantine and Syrian speech), English, German, French, or automatic detection.
- **Models:** `gpt-transcribe` is the default and is aimed at fast, low-latency daily voice typing. `gpt-4o-transcribe` is the higher-accuracy option for complex phrases, dialects and technical terms. You can switch from Settings or from the menu bar.
- **Microphones:** pick the built-in microphone, a USB interface or AirPods. Haki handles reconnection through CoreAudio and can prefer AirPods when they connect. A live level meter lets you test the input.

## Privacy: what stays on your Mac and what goes to OpenAI

Be clear about the trade-off: **your voice recordings are sent to OpenAI.** According to the README they go directly from your Mac to OpenAI's transcription endpoint over TLS, with no intermediary servers, so dictation needs an internet connection and your own OpenAI API key, used under OpenAI's terms and pricing.

On your Mac, the README says Haki embeds no analytics, diagnostics, crash reporters or third-party SDKs. Audio is recorded to temporary files and deleted as soon as transcription finishes or fails, so no audio history is kept. Your API key is stored in the macOS Keychain and not in preferences, configuration files or logs.

## Permissions

- **Microphone:** to capture your voice, and only while you hold the hotkey or start dictation from the menu.
- **Accessibility:** for the global push-to-talk hotkey and to insert text by simulating `⌘V`. According to the README, Input Monitoring is not required separately.

## Set it up

1. Open Haki. Allow Microphone access when macOS asks, and enable Haki under System Settings, Privacy & Security, Accessibility.
2. Open Settings from the menu-bar icon or with `⌘,`. In the Transcription tab paste your OpenAI API key, choose Save, then Test API Key.
3. Choose a model, and in the Audio tab choose your microphone.

## Dictate from your iPhone with AirMouse

[AirMouse](https://github.com/Alhamou/AirMouse) is a separate open-source app that turns an iPhone into a trackpad for your Mac over your local Wi-Fi. Its voice tab records on the phone and hands the audio to Haki, which types the text on your Mac. Haki has to be installed and running, and it uses your normal API key, model and language settings.

The handoff is simple and open to other senders too. A recording (`m4a`, `mp4`, `webm`, `wav`, `mp3` or `ogg`, up to 25 MB) is written to `~/Library/Caches/Haki/Inbox/`, then the URL `haki://transcribe?file=<file name>` is opened. Haki transcribes the file, pastes the text and deletes the file. Only plain file names inside the inbox are accepted, so paths, hidden files and symlinks are rejected.

## Build it

Haki needs macOS 13 Ventura or later, on Apple silicon or Intel, and the Xcode Command Line Tools with Swift 6.0 or newer. Clone the repository from GitHub, run `swift test`, then `./scripts/build_app.sh`. The script builds the release binary, assembles `Haki.app`, signs it with your local Apple Development certificate or an ad-hoc signature, and installs it in `/Applications`.

## Open source

Haki is released under the MIT license. The contribution guide asks for no local models, no Python, no Node.js and no Electron, and for API keys never to be committed. Emad Alhamou, the author of this site, publishes Haki on [GitHub](https://github.com/Alhamou/Haki). Bug reports and pull requests are welcome, and security concerns go through the repository's security policy.

<!-- faq -->
## Frequently asked questions

### What is Haki?

Haki is an open-source macOS menu-bar app for push-to-talk dictation. Hold `⌥ Option + Space`, speak and release, and the transcribed text is pasted at your cursor in any app. It is tuned for Arabic and also supports English, German and French.

### How do I dictate with Haki?

Click into a text field, press and hold `⌥ Option + Space`, speak, then release. Haki sends the recording to OpenAI and pastes the text at your cursor.

### Which languages and models does Haki support?

Arabic (with Levantine and Syrian optimization), English, German, French and automatic detection. The models are `gpt-transcribe`, the default, and `gpt-4o-transcribe` for higher accuracy.

### Does Haki send my voice to OpenAI?

Yes. Transcription is done by OpenAI, so each recording is sent from your Mac directly to OpenAI over TLS. Haki deletes the temporary audio file as soon as transcription finishes or fails, and keeps no audio history.

### Do I need an OpenAI API key?

Yes. Haki uses your own OpenAI API key, which it stores in the macOS Keychain. Usage is under OpenAI's terms and pricing.

### Which permissions does Haki need?

Microphone, to capture your voice while you hold the hotkey, and Accessibility, for the global hotkey and for pasting with a simulated `⌘V`.

### Which Macs and macOS versions are supported?

macOS 13 Ventura or later, on Apple silicon or Intel. Building needs Swift 6.0 or newer.

### Can I dictate from my iPhone?

Yes, with AirMouse, a companion open-source app. Its voice tab records on the phone and Haki types the text on your Mac. Haki must be installed and running.
