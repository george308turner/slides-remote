# Slides Remote for Android and Wear OS Privacy Policy

*Last updated: 17 October 2026*

This policy covers the Slides Remote app for Android phones and Wear OS watches ("Slides Remote", "the app"), made by George Turner ("we"). The Slides Remote apps for Mac, iPhone and Apple Watch have their own policy at [{{URL:privacy/}}]({{URL:privacy/}}); this one covers the Android and Wear OS apps and what they exchange with each other and with the Slides Remote app on your computer, a Mac or a Windows PC. Slides Remote for Windows, like the Mac app, keeps its data on the PC itself (pairing keys and its own identifier, in the PC's local app data folder), needs no account and sends nothing to us. In short: **we don't collect any of your data.** The app works entirely on your own devices, and nothing is sent to us.

## What the app stores, and where

- **Presentations, notes and timer plans** you create are stored on your computer, inside the computer app's own storage. They are sent to the Android phone and Wear OS watch you have paired with that computer, so you can read and edit them there (read them, on the watch), and nowhere else. The phone and watch keep them only while the app is connected; they don't save them.
- **Pairing keys:** the phone and the watch each keep their own key, and the public key of each computer they're paired with, in a file in the app's private storage on that device. They are used only to recognise your devices and encrypt the connection between them. This file is never included in Android backups or transfers to a new phone or watch.
- **Your phone's or watch's name and a random device identifier** made by the app are sent to the computer you pair with, so your computer can list the phone or watch ("Pixel 9", "Pixel Watch 3") and recognise it next time. The name is the one in the device's settings (or its model, if it has none).
- **Settings** are stored on the device they apply to: on the phone, Volume buttons change slides, Keep screen on, and whether you've already been asked about Bluetooth; on the watch, Keep in Front and whether you've already been asked about Bluetooth and notifications. They aren't backed up. Nothing on the watch is backed up.
- **The free trial's start date** is stored on the phone, and the phone shares it with your watch (below), so the watch shows notes and timers for the same 7 days. It is the one thing the app includes in **Android backup** and in transfers to a new phone, so a restored phone remembers that the trial was used. Android backup is a service of your phone's system: it is stored in your own Google account, under [Google's Privacy Policy](https://policies.google.com/privacy), and we can't see it. It holds only that date. You can turn backup off in your phone's settings (usually Settings ▸ System ▸ Backup, or Settings ▸ Google ▸ Backup).

None of this leaves your devices except to travel between your own phone, watch and computer, and the trial date in your own backup. You can delete it at any time: removing the phone under Paired Devices on the computer, deleting a presentation on the computer, clearing the app's storage on the phone or watch (Settings ▸ Apps ▸ Slides Remote ▸ Storage ▸ Clear storage, or as the watch names it), or uninstalling the app removes the data it holds on that device. Your backup of the trial date is managed, and can be deleted, in your Google account.

## How your devices talk to each other

Your phone, watch and computer connect directly over your local Wi-Fi network or Bluetooth (and, for the watch, through your phone). No internet connection and no server is involved; we don't run any servers. After you pair by comparing a 6-digit code on both screens, everything sent between your devices is **encrypted end to end**, so other devices on the network can't read it or send commands.

**Between your phone and watch**, the apps use the Wearable Data Layer of Google Play services, the part of your phone and watch that Wear OS uses to link them, for two things only:
- **The watch's connection to the computer, when it goes through your phone.** The watch encrypts it for the computer (as above) before it reaches the phone; the phone app passes it on to your computer over your Wi-Fi network without being able to read it, and passes the computer's replies back.
- **The free trial's start date**, which the phone publishes for its watch.

Google Play services carries these between your devices, directly over Bluetooth or Wi-Fi, and may carry them through Google's servers when your phone and watch aren't connected directly, under [Google's Privacy Policy](https://policies.google.com/privacy). We don't receive any of it, and this adds no data that we collect.

## What we don't do

- No accounts or sign-in.
- No analytics, usage statistics or crash reporting of our own.
- No advertising, no advertising ID and no tracking across apps or websites.
- No third-party software development kits (SDKs) other than Google's Play Billing Library for the in-app purchase (see Purchases).
- We don't sell, share or receive any personal information.

## Permissions

- **Nearby devices (Android 12 and later, Wear OS 4 and later):** to find and connect to your computer over Bluetooth without Wi-Fi. The app tells Android it never uses Bluetooth scans to work out your location.
- **Location (Android 8 to 11, and Wear OS 3, only):** on these versions, Android allows an app to look for Bluetooth devices only with the Location permission. Slides Remote asks for it only to find your computer over Bluetooth. It never reads, uses or keeps your location.
- **Network access:** to find your computer on your Wi-Fi network and connect to it. The app connects only to your computer on your local network, apart from Google Play's billing software (see Purchases) and Google Play services between your phone and watch (above). Android has no separate Local Network permission.
- **Vibration:** to tap when the computer has changed the slide, and at the timer's warnings.
- **Running in the background (foreground service):** on the phone, while your watch reaches the computer through it, with a notification saying so; on the watch, for **Keep in Front** while your show or timer runs, which also keeps the watch's processor awake so the link and the timer's taps stay on time. Neither collects anything.
- **Notifications (Wear OS 4 and later, watch only):** asked for only from the Show page, so Keep in Front can show its icon on the watch face.

The app explains Bluetooth before Android or Wear OS asks. You can turn these off at any time in Settings ▸ Apps ▸ Slides Remote ▸ Permissions; the app then works over Wi-Fi (and the watch through your phone).

## Purchases

The Notes & Timers unlock is bought through Google Play. Google handles the payment and your purchase history under [Google's Privacy Policy](https://policies.google.com/privacy). The app only asks Google Play whether your Google account owns the unlock; it receives no payment details and sends nothing to us. The watch asks Google Play on the watch in the same way and never sells anything. The free trial doesn't go through Google Play: it is the start date kept on the phone and shared with your watch (above).

Google Play's billing software, which is built into the app to make the purchase possible, sends Google its own technical information about how the billing service works (for example whether a request succeeded) so Google can run and improve it. We don't receive this information.

## Crash reports from Google

If you choose to share usage and diagnostics with Google in your phone's settings, Google may share crash and "app not responding" reports and performance statistics about the app with us (Android vitals in Google Play Console), without identifying you. This is Google's service, controlled by your phone's or watch's settings (usually Settings ▸ Google ▸ Usage & diagnostics on the phone).

## Children

The app collects no personal information from anyone, including children under 13.

## Changes

If the app ever starts collecting data (for example optional cloud sync of notes), we'll update this policy before that version is released and change the date above.

## Contact

Questions about privacy: {{EMAIL}}.
