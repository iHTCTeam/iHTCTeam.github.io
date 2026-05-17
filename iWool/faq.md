---
layout: default
title: iWool - FAQ
---

# Frequently Asked Questions

[Back to iWool Support](./)

---

### Does iWool require an account or internet connection?

No. iWool works entirely offline. All data is stored locally on your device using SQLite. No account, no sign-up, and no network connection are required to use any feature (except opening http/https links inside the app).

---

### Where is my data stored? Is it safe?

All data — activities, reminders, earnings records, recurrence states — is stored in a local SQLite database on your device. Nothing is uploaded to any server. If you uninstall the app, your data will be deleted. Back up regularly using **Settings → Data → Export Full Backup**.

---

### How do I back up and restore my data?

Go to **Settings → Data → Export Full Backup** to generate a CSV file. Save it to Files, AirDrop it to your Mac, or send it by email.

To restore, go to **Settings → Data → Import Backup** and choose your file. You will be asked to choose between:

- **Replace all data** — clears everything and restores from backup. Use this when switching devices or reinstalling.
- **Append only (keep existing)** — inserts backup activities as new records without deleting anything on your device. Use this to merge data from another device.

---

### How do recurring activities work?

When you set a recurrence rule (daily, weekly, monthly, yearly, or a custom interval), iWool stores one master record and virtually expands it into individual occurrences on each day. The list and calendar always show today's occurrence for a recurring series.

To mark a specific day's occurrence as complete, use the long-press menu or the detail page bottom toolbar. That marks only that day; the series continues.

---

### Why is a reminder not showing up?

iOS limits each app to approximately 64 pending local notifications at a time. iWool prioritises non-recurring activities and schedules up to 120 days of future occurrences for recurring ones, but very large collections of recurring reminders may be trimmed.

Check **Settings → Notifications → Scheduled Local Reminders** to see exactly which reminders are currently registered.

Also verify:

- Notification permission is granted (iOS Settings → iWool → Notifications).
- The activity is not cancelled (cancelled activities have their reminders cleared automatically).
- The reminder time is in the future.

---

### What is the difference between "estimated earnings" and "recorded earnings"?

- **Estimated earnings** — entered in the activity form. Displayed on the activity card. Does not count in Statistics.
- **Recorded earnings** — entered in the activity detail page via the earnings form. These are the actual amounts counted in all Statistics totals, trend charts, and platform rankings.

---

### How do I record earnings for a specific day of a recurring activity?

Open the activity detail for that day's occurrence (tap the activity in the list or calendar on that day). In the detail page, tap **Record** in the earnings section. The record date will default to that day's occurrence date.

---

### Can I delete a single earnings entry without affecting the activity?

Yes. Open the activity detail, tap the earnings row you want to edit, and in the edit form scroll to the bottom. Tap **Delete this earnings record** and confirm. Only that one entry is removed; the activity and all other records remain untouched.

---

### The statistics chart is showing wrong amounts for Japanese Yen (JPY) / Korean Won (KRW).

These currencies have no decimal places by default, which may have caused amounts to appear as whole numbers in older versions. In the current version you can configure the number of decimal places independently:

- Go to **Settings → Appearance & Language → Amount Decimals** to set the number of decimal places for all amount displays (default: 2).
- Go to **Settings → Appearance & Language → Chart Amount Decimals** to set the decimal places for chart bar labels specifically (default: 0).

---

### How do I use the Dynamic Island / Live Activity feature?

The feature requires a supported iPhone model and iOS 16.1 or later. Enable it in **Settings → Notifications → Live Activity**. Use the slider to set how early (in minutes, 1 to 480) you want it to appear before an activity starts.

Activities are picked up automatically within the time window. You can also long-press any eligible activity on the home screen or calendar and choose **Add to Dynamic Island** from the menu.

---

### How do I add widgets to my Home Screen or Lock Screen?

Detailed step-by-step instructions are available in **Settings → Widgets → Widget Guide** inside the app. In short:

1. Long-press an empty area of your Home Screen and tap the **+** button.
2. Search for **iWool** in the widget gallery.
3. Choose a widget style and size, then tap **Add Widget**.

For Lock Screen widgets (iOS 16+): long-press your Lock Screen and tap **Customize**, then add iWool widgets to the Lock Screen widget row.

---

### Why does the widget show outdated data?

Widgets refresh when you open the app or when data changes. iOS also refreshes widget timelines periodically in the background (about every 15 minutes at best). If the widget is stale, open iWool once to force a refresh.

---

### How do I change the display language?

Go to **Settings → Appearance & Language → Display Language**. You can choose from 13 languages independently of your device's system language:

English, Simplified Chinese, Traditional Chinese, Japanese, Korean, Thai, Hindi, Spanish, French, German, Brazilian Portuguese, Russian, Arabic.

The change takes effect immediately throughout the app.

---

### Can I share an activity without sharing my earnings amounts?

Yes. By default, copying or sharing an activity does not include your earnings records. If you want to include them, go to **Settings → Appearance & Language** and enable **Include earnings when sharing**.

---

### How do I scan a QR code or barcode?

Go to **Settings → Tools → QR / Barcode Scanner**. Point your camera at a code or tap the album icon to pick an image. Results appear in a list you can copy or open in Safari.

You can also scan directly from the activity form: when filling in the Activity URL field, tap the scan icon next to it to scan a code and fill the URL automatically.

---

### What does "archive" mean? Is it the same as delete?

No. Archiving hides an activity from the main list without deleting it. Archived activities can be viewed, restored or deleted from **Settings → Activity Management → Archived Activities**.

Long-press a completed, expired or cancelled activity to see the Archive option. To archive all completed, expired and cancelled non-recurring activities at once, use **Settings → Activity Management → Archive All Completed**.

---

### Still need help?

Contact us at [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) or use the in-app **Settings → Send Feedback** option. We typically respond within 48 hours.
