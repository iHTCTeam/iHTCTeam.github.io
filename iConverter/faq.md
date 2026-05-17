---
layout: default
title: iConverter - FAQ
---

# Frequently Asked Questions

[Back to iConverter Support](./)

---

### How do I find a specific tool?

Use the search bar at the top of the tool menu. You can search in English, Simplified Chinese, or Traditional Chinese. Results match tool names, subtitles, and keywords simultaneously.

---

### Can I pin tools to the home screen?

Yes. Tap the ⋯ menu button in any tool's toolbar, or go to **Settings → Pinned Tools** to add up to 8 tools to the quick-access row on the home screen.

---

### How do I add iConverter widgets?

Long-press your Home Screen or Lock Screen to enter edit mode, tap the **＋** button, search for "iConverter," and choose the widget size and tool you want. Interactive widgets (tap to update values directly on the widget) require iOS 17 or later.

---

### Can I change the app language independently of my iPhone's language?

Yes. Go to **Settings → Language** inside the app. You can choose Simplified Chinese, Traditional Chinese, or English regardless of your system language.

---

### How do I restore the last session when opening a tool?

Go to **Settings → Calculator History → Restore Last Session**. When enabled, opening a supported tool will automatically restore the most recent values from history.

---

### How do I share a calculation result?

Tap any result value to copy it to the clipboard. A brief toast confirms the copy. You can then paste it anywhere. For QR codes, use the Share or Save buttons directly in the QR Code tool.

---

### What is the URL Scheme / Deep Link feature?

iConverter supports the `iconverter://` URL scheme, which lets you open any of the 98 tools from Safari, Apple Shortcuts, another app, or a scanned QR code. Many tools also accept URL parameters to pre-fill input fields automatically.

See the full [URL Scheme Reference](url-scheme) for all supported tools and parameters.

---

### How do I use iConverter with Apple Shortcuts?

1. Open the **Shortcuts** app and create a new shortcut.
2. Add an **Open URLs** action.
3. Enter an `iconverter://` URL, for example:
   `iconverter://tool/bmi?h=175&w=70`
4. Run the shortcut to open iConverter and pre-fill the BMI tool.

---

### Can I open iConverter from a QR code?

Yes. Use any QR code generator to create a code for an `iconverter://` URL. When scanned with the iPhone Camera or QR Code tool, it opens the corresponding tool directly — optionally with pre-filled values.

---

### How do I change the accent color?

Go to **Settings → Accent Color**. Choose from 12 preset colors or tap the color wheel icon to pick any custom color with the system color picker.

---

### Can I change the app icon?

Yes. Go to **Settings → App Icon** to switch between the default icon and several alternate designs.

---

### What are "Home Screen Shortcuts"?

Home Screen Shortcuts let you add up to 4 specific tools as icon-sized shortcuts directly on your iOS Home Screen (using `UIApplicationShortcutItem`). Configure them in **Settings → Home Screen Shortcuts**.

---

### How does the Calculator History work?

All three calculators (Standard, Scientific, Programmer) share one history log. Each entry shows the expression and result. Tap an entry in the history sheet to restore it. History recording can be toggled in **Settings → Calculator History**. You can delete individual entries by swiping left, or clear all entries at once.

---

### The web browser tool can't open a URL — what's wrong?

- Make sure the URL starts with `http://` or `https://`. If you type a plain domain, the browser will auto-add `https://`.
- If the URL looks like a search query, the browser will search using your selected search engine.
- `iconverter://` links opened inside the web browser are passed back to the system to handle — they will open the corresponding iConverter tool.

---

### How do I export a video frame?

1. Open **Video Frame Export** from the Lifestyle category.
2. Tap the video icon to pick a video from Photos.
3. Use the slider and step buttons to navigate to the exact frame.
4. Tap **Save to Photos** or the share icon to export the frame.
5. For batch export, tap ⋯ and choose **Burst Export**.

---

### Are all tools available offline?

Yes — all 98 tools work fully offline. The only exception is the **Web Browser** tool, which requires an internet connection to load web pages. The Web Browser's own features (bookmarks, history, JS injection, etc.) work locally.

---

### Does iConverter collect any personal data?

No. See the [Privacy Policy](privacy) for details.

---

### Still need help?

Contact us at [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) and we will get back to you within 48 hours.
