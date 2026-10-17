# Slides Remote Privacy Policy

*Last updated: 17 October 2026*

This policy covers the Slides Remote apps for Mac, Windows, iPhone and Apple Watch ("Slides Remote", "the app"), made by George Turner ("we"). The Android and Wear OS apps have [their own policy]({{URL:privacy/android/}}). What this policy says about "your computer" applies to a Mac and a Windows PC alike; [Slides Remote for Windows](#slides-remote-for-windows) has a section of its own for the few things that differ. In short: **we don't collect any of your data.** The app works entirely on your own devices, and nothing is sent to us or to anyone else.

## What the app stores, and where

- **Presentations, notes and timer plans** you create are stored on your computer, inside the app's own storage (its sandbox container). They are sent to the iPhone and Apple Watch you have paired with that computer, so you can read and edit them there, and nowhere else.
- **Pairing keys:** each device keeps its own key, and the public key of each device it's paired with, in a file in the app's storage on that device. They are used only to recognise your devices and encrypt the connection between them.
- **Device names and a random device identifier** made by the app are shared between your paired devices, so your computer can list them ("iPhone") and recognise them next time.
- **Settings** (for example your key map, Keep in Front and Keep Screen On) are stored on the device they apply to.

None of this leaves your devices except to travel directly between them. You can delete it at any time: removing a device under Paired Devices on the computer, deleting a presentation, or deleting the app removes the data it holds on that device.

## How your devices talk to each other

Your computer, iPhone and Apple Watch connect directly over your local Wi-Fi network or Bluetooth (and, for the watch, through your iPhone). No internet connection and no server is involved; we don't run any servers. After you pair by comparing a 6-digit code on both screens, everything sent between your devices is **encrypted end to end**, so other devices on the network can't read it or send commands.

## What we don't do

- No accounts or sign-in.
- No analytics, usage statistics or crash reporting of our own.
- No advertising and no tracking across apps or websites.
- No third-party software development kits (SDKs).
- We don't sell, share or receive any personal information.

## Permissions

- **Accessibility (Mac):** lets the app press keys (such as the Right Arrow) for your presentation app when you choose a command. The app doesn't read your screen, other apps' content or what you type.
- **Bluetooth (Mac, iPhone, Apple Watch):** to connect your devices to each other without Wi-Fi.
- **Local Network (iPhone, and the Mac if macOS asks):** to find your computer on your Wi-Fi network.

You can turn these off at any time in Settings; the app explains what still works.

## Purchases

The Notes & Timers unlock and its free trial are bought through Apple's App Store. Apple handles the payment and your purchase history under [Apple's Privacy Policy](https://www.apple.com/legal/privacy/). The app only asks the App Store whether you own the unlock; it receives no payment details and sends nothing to us.

## Crash reports from Apple

If you choose to share analytics with app developers in your device's settings, Apple may share crash reports and usage statistics about the app with us, without identifying you. This is Apple's service, controlled by your device's settings (iPhone: Settings ▸ Privacy & Security ▸ Analytics & Improvements; Mac: System Settings ▸ Privacy & Security ▸ Analytics & Improvements).

## Slides Remote for Windows

The Windows app works the same way as the Mac app, with these differences:

- **Where it keeps your data:** presentations, notes, timer plans, settings and pairing keys are stored in the app's own folder in your Windows user account on the PC. Its private pairing key is protected with Windows' data protection (DPAPI), so only your Windows account on that PC can use it.
- **What it talks to:** only your own paired phones and watches, over your local network or Bluetooth, and the Microsoft Store to check whether you own the unlock. It needs no account and sends nothing to us.
- **Pressing keys:** it presses keys for your presentation app (or controls PowerPoint's slideshow directly) only when you choose a command. It doesn't read your screen, other apps' content or what you type.
- **Permissions:** Windows may ask you to allow the app through Windows Defender Firewall on private networks, so your phone can find the PC on your Wi-Fi network, and Bluetooth may need to be turned on in Settings.
- **Purchases:** the Notes & Timers unlock and its free trial are bought through the Microsoft Store. Microsoft handles the payment and your purchase history under the [Microsoft Privacy Statement](https://privacy.microsoft.com/privacystatement). The app only asks the Microsoft Store whether your Microsoft account owns the unlock; it receives no payment details and sends nothing to us.
- **Crash reports from Microsoft:** if you allow Windows to send optional diagnostic data, Microsoft may share crash reports about the app with us, without identifying you. This is Microsoft's service, controlled in Settings ▸ Privacy & security ▸ Diagnostics & feedback.

## Children

The app collects no personal information from anyone, including children under 13.

## Changes

If the app ever starts collecting data (for example optional cloud sync of notes), we'll update this policy before that version is released and change the date above.

## Contact

Questions about privacy: {{EMAIL}}.
