# Slides Remote Help (Android)

Slides Remote lets you change slides on your computer from your Android phone or Wear OS watch, see your notes for each slide and keep to time. Questions not answered here: {{EMAIL}}.

Slides Remote runs on **Mac** and **Windows**. Where a step on the computer differs, it's marked **On a Mac** or **On Windows**. The Windows app is newer: for now it connects over Wi-Fi only, and notes, timers and the computer's Settings are in the Mac app only (they're coming to Windows).

**Contents:** [Getting started](#getting-started) · [Pairing](#pairing) · [How the devices connect](#how-the-devices-connect) · [The remote](#the-remote) · [Wear OS watch](#wear-os-watch) · [Notes](#notes) · [Timers](#timers) · [The unlock, free trial and restoring](#the-unlock-free-trial-and-restoring) · [Settings on the phone](#settings-on-the-phone) · [Settings on the computer](#settings-on-the-computer) · [Troubleshooting](#troubleshooting) · [Privacy](#privacy)

---

## Getting started

You need:
- **A computer** with Slides Remote on it:
  - **On a Mac:** macOS 26 or later and the free **Slides Remote** app from the Mac App Store.
  - **On Windows:** Windows 10 (version 2004 or later) or Windows 11 and **Slides Remote for Windows**.
- **An Android phone** with Android 8.0 or later and the free **Slides Remote** app from Google Play.
- **A Wear OS watch** (optional) with Wear OS 3 or later. The watch app is the same Slides Remote on Google Play: install it from the Play Store on the watch, or from the app's page in the phone's Play Store.
- The computer and phone on **the same Wi-Fi network**, or (with a Mac) close enough for **Bluetooth** (about 10 metres). No internet connection is needed.

### 1. On the computer

**On a Mac:**
1. Open **Slides Remote**. It explains why it needs to press keys: that's how it changes slides in Keynote, PowerPoint and other apps.
2. Click **Open System Settings…**. macOS shows its own message; open System Settings and turn on **Slides Remote** under **Privacy & Security ▸ Accessibility**. Back in the app, the next screen comes by itself.
3. Click **Continue** and **Allow** Bluetooth, so your phone and watch can find the computer without Wi-Fi.

You can choose **Not Now** on either screen; the dashboard's Status section then shows what's missing, with a button to turn it on later.

**Why Accessibility?** macOS lets an app press keys for another app only with this permission. Slides Remote presses a key only when you choose a command (Next, Previous, Start Show…) on a remote or on the computer. It doesn't read your screen, other apps or what you type.

**On Windows:**
1. Open **Slides Remote**. Its dashboard opens, and its icon appears in the notification area at the right of the taskbar (Windows 11 may put it under **^**; drag it onto the taskbar to keep it in view). Closing the dashboard keeps Slides Remote running; open it again from the icon (**Open Dashboard…**).
2. **Windows Defender Firewall** asks the first time: allow Slides Remote on **private networks**, or phones can't connect. Your Wi-Fi network has to be set to **Private** (**Settings ▸ Network & internet ▸ Wi-Fi**, then your network). To change it later: **Windows Security ▸ Firewall & network protection ▸ Allow an app through firewall**.
3. Under **Status**, Wi-Fi says **On** when phones and watches can find the PC.

Windows needs no Accessibility permission. Slides Remote presses a key only when you choose a command on a remote or on the computer.

### 2. On the phone
1. Open **Slides Remote**. The first time, it explains why it uses Bluetooth (**Connect Without Wi-Fi**). Tap **Continue**, then **Allow** when Android asks:
   - on Android 12 and later, for **Nearby devices**;
   - on Android 8 to 11, for **Location**: on those versions Android counts looking for Bluetooth devices as using your location. Slides Remote never finds out or keeps where you are.

   You can tap **Not Now**: the phone then reaches the computer over Wi-Fi only. There's nothing to allow for Wi-Fi.
2. Your computer appears under **Computers Nearby**. Tap it and pair (next section).

### 3. Present
1. On the computer, open your presentation and click its window so it's in front. Start the slideshow there or with **Start Show** on the phone.
2. Tap **Next** and **Previous**, or press the phone's volume buttons. That's it.

Slides Remote works with **PowerPoint, Google Slides (in a browser)** and most other presentation apps, plus **Keynote and Preview** on a Mac and **PDF viewers** on Windows, by pressing the keys you would press yourself.

**Keep Slides Remote on screen while you present.** The phone keeps its link to the computer while the app is open; if you switch to another app, it lets go and reconnects when you come back. The screen stays on by itself while connected (see [Settings on the phone](#settings-on-the-phone)).

---

## Pairing

You pair each phone or watch with your computer once. It keeps others nearby from controlling your slides. The watch pairs with the computer itself, the same way; pairing the phone doesn't pair its watch.

1. On the computer, click **Pair New Device…** on the dashboard (on a Mac, also in the **Slides** menu; on Windows, also in the Slides Remote icon's menu in the notification area).
2. On the phone or watch, tap your computer.
3. **Both screens show the same 6-digit code.** Check they match, then tap **Confirm** on the phone (or watch) and click **Confirm** on the computer. If they don't match, tap **Cancel** on the phone or **Doesn't Match** on the watch (or choose **Doesn't Match** on the computer) and try again.

If **Pair New Device** isn't open on the computer, the phone or watch says so: open it, then try again.

After that, the phone and watch reconnect by themselves whenever the computer app is open.

**Removing a device:** on the computer, under **Paired Devices**, click **Revoke…** next to it. It has to pair again to connect: the phone or watch says the computer doesn't know it and offers **Pair Again**.

---

## How the devices connect

The badge at the top of the remote shows the link in use, with signal bars (on the watch, as an icon: Bluetooth, Wi-Fi or a phone):
- **Wi-Fi**: the computer and phone are on the same Wi-Fi network. Fastest; used whenever it's available. With a Windows PC, it's the only link for now.
- **Bluetooth** (with a Mac): used when there's no shared Wi-Fi (for example on a venue's network that blocks devices from seeing each other). The phone switches between Wi-Fi and Bluetooth by itself, and back to Wi-Fi when it returns. **Reconnecting…** shows while it switches; your slide stays on screen, and a Next you press meanwhile is sent once.
- **Via phone** (watch only): the watch talks to the computer directly over Bluetooth (with a Mac), or over Wi-Fi when the watch is on the computer's network. When it can't reach the computer itself, it goes through the Slides Remote app on your phone, which needs to be on the computer's Wi-Fi network, and switches back to Bluetooth when it can. The phone app doesn't need to be open: while it carries the watch's connection, the phone shows a **Connecting your watch** notification.

"No reply for 8 s" means the computer hasn't answered for a while; it usually recovers by itself. Everything between your devices is encrypted.

**The slide number** on the remote is counted from the commands sent (shown as **Tracked**). If you also press keys on the computer's keyboard, it can drift: use **Resync…** (More menu, ⋮) to tell it which slide is showing.

---

## The remote

- **Next** and **Previous**: the big buttons, or the **volume buttons** (volume down for the next slide, volume up for the previous one). Holding a volume button sends one command, not many. The phone taps (vibrates) when the computer has done it, and buzzes if it couldn't.
- **Start Show** / **End Show** and **Blank** are on the remote screen too.
- **More** (⋮, top right): **Go to Slide…**, **Resync…**, **Presentations…**, **Set Up Timer…** (or **Timer…**), **Reset Timer**, **Unlock Notes & Timers…**, **Restore Purchases**, **Settings** and **Disconnect**.

---

## Wear OS watch

- Open **Slides Remote** on the watch. The first time, it explains why it uses Bluetooth (**Connect to Your Computer**). Tap **Continue**, then **Allow** when the watch asks: for **Nearby devices** on Wear OS 4 and later, or for **Location** on Wear OS 3 (on that version, looking for Bluetooth devices counts as using your location; Slides Remote never finds out where you are). With **Not Now**, the watch reaches the computer only through your phone or over Wi-Fi.
- Tap your computer under **Computers** (pair with the code the first time, as above).
- **Change slides** with the big buttons, or by turning the **crown** or the **rotating bezel** (one step, one slide). On watches that let apps use their extra button, that button is **Next** while the slide page shows.
- **Swipe up** for the current slide's notes, then the **Show** page: Start or End Show, Blank, the timer's controls, **Keep in Front** and **Disconnect**.
- **Timer cues:** the watch taps your wrist at each warning, when time's up and when a section runs over.
- **With your wrist down** (Always On), the remote stays on screen, dimmed, showing the slide and the minutes left.

### Keep in Front
Normally a watch goes back to the watch face a little after you lower your wrist, and the app stops. During a talk, Slides Remote keeps going instead: while the slideshow or the timer is running, it stays connected to the computer and taps your wrist on time, and its icon on the watch face brings the remote back in one tap. A **pin** next to the link badge shows it's on. It stops when the show ends and the timer is paused or reset, and when you disconnect.

- To turn it off: **Show page ▸ Keep in Front**.
- It starts while the app is on screen. If you leave the app (press the crown), it carries on; tap its icon on the watch face, or open Slides Remote, to come back.
- **Wear OS 4 and later:** the icon shows on the watch face only if Slides Remote may show notifications. The Show page says so, with **Allow Notifications**.
- It keeps the watch working with the screen off, so it uses more battery than the watch face alone while your talk runs.

### Notes and timers on the watch
The watch reads the unlock from Google Play, for the Google account on the watch: unlock on your phone with the same account and the watch has notes and timers too. There's nothing to buy on the watch (**Unlock on your phone**). Your phone's 7-day free trial covers the watch as well: the phone tells the watch when it started.

---

## Notes

*Notes are part of the unlock (below); you can try them free for 7 days. They need the Mac app for now; they're coming to Windows.*

- **On the computer:** click **Edit Presentations and Notes…** on the dashboard. Add presentations with **+**, give each a name and its number of slides, pick a slide and type its notes. They save as you type.
- **On the phone:** the current slide's notes are on the remote screen; tap **Edit** to change them, then **Save** (or **Cancel**). If the same notes were changed on the computer at the same time, the phone shows the computer's and asks which to keep: **Use Mine** or **Use the computer's**.
- **On the watch:** swipe up from the controls to read them (read only).
- **Several presentations:** choose the one you're giving in the computer's **Presenting** menu or the phone's **More ▸ Presentations…**. Each has its own notes and timer.

Notes are plain text, up to about 16,000 characters per slide. They're kept on the computer and sent to your paired phone and watch.

---

## Timers

*Timers are part of the unlock (below). They need the Mac app for now; they're coming to Windows.*

- **Set up:** on the computer, **Edit Timer…** on the dashboard; on the phone, **More ▸ Set Up Timer…**. Enter the talk's length (for example 20 or 19:30), the warnings (times left, such as 5:00, 1:00, 0:00) and optionally **sections**: a range of slides with its own budget (Intro, slides 1–3, 2 minutes). You can also give a single slide its own time.
- **Run:** **Start Timer** on the computer, phone or watch; **Pause**, **Resume** and **Reset** from any of them (on the phone, Reset is in the More menu; on the watch, all are on the Show page).
- **Reading it:** time left, the current section and its time left, and whether you're **ahead** or **behind** the section plan. The phone buzzes and shows a banner at each warning, when time's up and when a section runs over; the watch taps.

---

## The unlock, free trial and restoring

- **Free:** remote control (changing slides, Start/End Show, Blank, Go to Slide, the connection) and creating presentations.
- **Unlock (one-time purchase on Google Play):** notes and timers. No subscription.
- **An unlocked device shares notes and timers with the devices connected to it.** A paid computer unlocks every phone and watch connected to it, and a paid phone or watch unlocks the computer it's connected to, for as long as they're connected (and for a minute after the connection drops, so a short drop doesn't lock anything). Settings ▸ Notes & Timers then says "Unlocked while *Studio Mac* is connected". Sharing doesn't pass on: a phone unlocked only by the computer doesn't unlock the computer's other phones. To have notes and timers away from that computer, buy the unlock on the phone.
- **Free trial:** tap **Unlock…** on a locked card, then **Start 7-Day Free Trial**. It unlocks everything for 7 days and then simply ends: nothing is charged and nothing renews. You can buy the unlock at any time during the trial. The trial can be started once on each phone, and covers its watch.
- **Restore Purchases:** after reinstalling, or on another Android phone signed in to Google Play with the same Google account. **More ▸ Restore Purchases**, or **Settings ▸ Notes & Timers ▸ Restore Purchases** (also in the unlock sheet).
- **The watch** reads the unlock from Google Play (the same Google account as the phone) and follows the phone's trial; there's nothing to buy on the watch ("Unlock on your phone"). An unlocked computer shares notes and timers with the watch while it's connected, as with the phone.
- **Purchase waiting for payment or approval** (some payment methods take a while): the sheet says so, and notes and timers unlock once Google Play completes it.
- **Refunds** are handled by Google Play: [support.google.com/googleplay/answer/2479637](https://support.google.com/googleplay/answer/2479637).

---

## Settings on the phone

Open **Settings** from the gear on the list of computers, or **More ▸ Settings** on the remote.

- **Volume buttons change slides** (on by default): while the remote is on screen, volume down goes to the next slide and volume up to the previous one. Turn it off to keep the volume buttons for volume.
- **Keep screen on** (on by default): while connected to a computer, and while waiting for it to come back, the phone doesn't turn its screen off.
- **Notes & Timers:** whether they're unlocked (or how many trial days are left, or "Unlocked while *your computer* is connected" when the computer shares its unlock), **Unlock…** and **Restore Purchases**.

---

## Settings on the computer

**On Windows**, Slides Remote has no Settings yet: it uses the usual keys for PowerPoint, Google Slides in a browser and PDF viewers, and keeps the PC's own sleep settings. Stop the PC sleeping during a talk in **Settings ▸ System ▸ Power & battery** (**Power & sleep** on Windows 10).

**On a Mac**, open **Slides Remote ▸ Settings…** (⌘,).

- **General:** show the menu bar item; **Keep Mac awake while remotes are connected** (on by default; the display also stays on during the slideshow; closing the lid still sleeps the Mac); Notes & Timers status, Unlock and Restore Purchases.
- **Presentation:** **Presentation app** (Automatic, or always a chosen app); **Control with** (Keystrokes); **Return to Slides Remote after Next or Previous** (off by default; see below).
- **Keys:** the key each command presses, for each app (Keynote, PowerPoint, Preview, Google Slides in a browser, Other Apps). Click a key and press a new one, choose **None**, or **Use Default**. Useful if your app uses different keys, for example W for a white screen in Keynote.
- **Shortcuts:** the Mac's own Next Slide and Previous Slide shortcuts (⌘] and ⌘[ by default).

### Next and Previous on the computer itself
The dashboard's buttons change slides too. **On a Mac**, so do the **Slides** menu, the **Dock** menu (right-click the Dock icon) and the **menu bar** item. **On Windows**, so do **Next Slide** and **Previous Slide** in the Slides Remote icon's menu in the notification area. If Slides Remote is in front, it first switches to your presentation (on a Mac, the app chosen in Settings ▸ Presentation; otherwise the one you were using before), then presses the key. On Windows, click your presentation's window once first so Slides Remote knows which it is. On a Mac, with **Return to Slides Remote after Next or Previous** on, it comes back to the front afterwards; handy while rehearsing at the computer.

---

## Troubleshooting

### The phone can't find my computer
- Is **Slides Remote open on the computer**? It has to be running (on a Mac it can be in the menu bar; on Windows, in the notification area).
- Is **Slides Remote open on the phone**, on screen? It looks for computers only while it's in front.
- Same **Wi-Fi network**? Many guest, hotel and conference networks stop devices seeing each other: with a Mac, turn Wi-Fi off on the phone and it uses Bluetooth instead.
- **On Windows:** is the Wi-Fi network set to **Private**, and is Slides Remote allowed through **Windows Defender Firewall** on private networks? See [On the computer](#1-on-the-computer). The dashboard's **Status** says whether phones can find the PC.
- **Bluetooth** not allowed? The list of computers says so. Tap **Open Settings**, or go to **Settings ▸ Apps ▸ Slides Remote ▸ Permissions** and allow **Nearby devices** (Android 12 and later) or **Location** (Android 8 to 11). If you chose Not Now at first, tap **Turn On Bluetooth** on the list. Wi-Fi still works without it.
- **Bluetooth off** on the phone? Turn it on in Quick Settings or **Settings ▸ Connected devices**. On a Mac, check **System Settings ▸ Privacy & Security ▸ Bluetooth**.
- **Android 8 to 11: Location off** on the phone? On those versions finding Bluetooth devices needs it: turn it on in Quick Settings or **Settings ▸ Location**. (Slides Remote still never reads where you are.)

### The watch can't find my computer
- Is **Slides Remote open on the computer**, and the watch within Bluetooth range (about 10 metres)? With a Windows PC, the watch connects over Wi-Fi or through your phone, not over Bluetooth.
- **Bluetooth** not allowed on the watch? The list of computers says so: tap **Open Settings**, or on the watch go to **Settings ▸ Apps ▸ Slides Remote ▸ Permissions** and allow **Nearby devices** (Wear OS 4 and later) or **Location** (Wear OS 3). If you chose Not Now at first, tap **Turn On Bluetooth** on the list.
- **Bluetooth off** on the watch? Turn it on in **Settings ▸ Connectivity ▸ Bluetooth**. **Wear OS 3: Location off?** Turn it on in **Settings ▸ Location**.
- **Through the phone:** the Slides Remote app has to be installed on your phone, and the phone on the computer's Wi-Fi network and near the watch. The phone app doesn't need to be open.

### "Waiting for <your computer>" / the computer went to sleep
When the computer sleeps, quits Slides Remote or goes out of range, the phone (or watch) waits and reconnects by itself when it's back. After 10 minutes it stops waiting and says so on the list of computers; tap the computer to connect again. **Stop Waiting** goes back to the list at once. To stop a Mac sleeping during a talk, leave **Settings ▸ General ▸ Keep Mac awake while remotes are connected** on, and keep the lid open. On Windows, set the PC not to sleep in **Settings ▸ System ▸ Power & battery** (**Power & sleep** on Windows 10).

### The remote says it worked but the slides don't move
- **Click your presentation's window on the computer** so it's the app in front. The keys go to whichever app is in front. If Slides Remote itself is in front, the remote says so.
- Is the **slideshow playing**? Some apps (PowerPoint, Google Slides) only use the arrow keys for slides while presenting.
- **"The computer can't change slides…"**: Slides Remote doesn't have permission to press keys in your presentation. **On a Mac**, turn it on in **System Settings ▸ Privacy & Security ▸ Accessibility** (if it's already on, turn it off and on again). **On Windows**, the slideshow is running as administrator, so Windows won't let Slides Remote press keys in it: run the slideshow normally, or run Slides Remote as administrator too. Notes and the timer still work meanwhile.
- **A particular app** ignores the keys or uses others: on a Mac, change them in **Settings ▸ Keys** for that app, or under **Other Apps**.
- **Google Slides:** the browser tab with the presentation has to be in front, and the presentation playing.
- The slide number is off by a few: use **Resync…** in the More menu.

### The volume buttons change the volume, not the slide
They change slides only while the remote is on screen and connected, and while **Settings ▸ Volume buttons change slides** is on.

### "Couldn't set up a secure connection" or "<your computer> doesn't know this phone"
Slides Remote was reinstalled on the computer, or the phone was revoked there. Open **Pair New Device…** on the computer, then tap **Pair Again** (or the computer) on the phone and confirm the code.

### The watch went back to the watch face during my talk
Check **Keep in Front** is on (Show page), and that the show or timer was running while the app was on screen (it starts with them). If Wear OS refused or ended it, the watch says so ("Wear OS won't keep the app in front"); open the app to bring it back. See [Keep in Front](#keep-in-front).

### Notes or the timer are locked
They're part of the unlock. Start the free trial, buy the unlock, or **Restore Purchases** if you already bought it. If the computer you're connected to is unlocked, they're unlocked on the phone too while it's connected. The watch follows the phone: its Play Store needs the same Google account, and Google Play may take a little while to show it the phone's purchase.

### "Couldn't reach Google Play"
The unlock needs Google Play: check the phone is online and signed in to the Play Store, then try again. Remote control doesn't need it.

### The phone's screen stays on
While connected to a computer, the phone doesn't turn its screen off, so the remote is ready mid-talk. Turn this off in **Settings ▸ Keep screen on**.

---

## Privacy

Slides Remote has no accounts, no servers, no analytics and no ads. Your presentations and notes are stored on your computer (Mac or Windows PC) and sent only to your own paired phone and watch, over an encrypted connection on your local network or Bluetooth (or, for the watch, through your phone). Purchases are handled by Google Play. Full policy: [Privacy Policy for Android and Wear OS]({{URL:privacy/android/}}).
