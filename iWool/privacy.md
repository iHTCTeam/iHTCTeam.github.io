---
layout: default
title: iWool - Privacy Policy
---

# Privacy Policy

**Last updated: May 17, 2026**

[Back to iWool Support](./)

---

iHTCTeam ("we", "us", or "our") built iWool (also known as "爱羊毛") as a paid app. This page informs you of our policies regarding the collection, use, and disclosure of personal data when you use our app.

---

## Summary

**iWool does not collect, store, or transmit any personal data.** The app operates entirely on your local device and requires no account, no internet connection, and no cloud services.

---

## Data Collection

We do not collect any data. Specifically:

- **No personal information** is collected (no name, email, phone number, or account).
- **No usage data** or analytics are collected.
- **No activities, earnings, or any content** you create in the app is accessible to us.
- **No cookies or tracking** technologies are used.
- **No third-party services** (advertising, analytics, crash reporting) are integrated.

---

## How the App Works

iWool stores all data — activities, reminders, earnings records, recurrence states, and templates — in a local SQLite database on your device:

- Data never leaves your device unless you explicitly export a backup and choose to share it yourself.
- No internet connection is required for any core feature of the app.
- Opening http/https links from within the app (in the built-in Safari view) follows standard iOS networking behavior; the linked page is loaded by your device directly from its host, not through any iHTCTeam server.

---

## Permissions

iWool requests the following device permissions, only when needed:

| Permission | Purpose |
|------------|---------|
| Notifications | Schedule and deliver local reminders for your activities |
| Camera | Scan QR codes and barcodes via the built-in scanner tool |
| Photo Library (Read) | Pick images for QR / barcode recognition |
| Live Activities | Display the Dynamic Island and Lock Screen Live Activity for upcoming activities (iOS 16.1+) |

These permissions are used solely for the stated purposes. No data accessed through these permissions is transmitted to any external server or third party.

---

## Data Storage

- **Activity data** (activities, reminders, earnings records, recurrence completion states, templates) is stored locally in a SQLite database file (`iWool.sqlite`) in the app's support directory on your device.
- **App preferences** (theme, language, currency, badge strategy, reminder settings, etc.) are stored locally using UserDefaults on your device.
- **Widget snapshot** — a lightweight JSON summary of your current activities and earnings — is written to an App Group container (`group.com.iHTCboy.iWool`) shared between the main app and the widget extension. This data never leaves your device.
- No data is stored on any external server or cloud service.

---

## Backup Files

When you use **Settings → Data → Export Full Backup**, iWool generates a CSV file on your device. The file contains your activities, reminders, earnings records, recurrence states and templates. This file is created locally and is only shared if you explicitly choose to share it (for example, saving to Files or sending via AirDrop or email). We have no access to this file.

---

## Children's Privacy

iWool does not knowingly collect any personal data from anyone, including children under 13. Since we do not collect any data at all, no special provisions are needed.

---

## Changes to This Policy

We may update this Privacy Policy from time to time. Any changes will be posted on this page with an updated date. We encourage you to review this page periodically.

---

## Contact Us

If you have any questions about this Privacy Policy, please contact us:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
- **GitHub:** [github.com/iHTCTeam/iApp/issues](https://github.com/iHTCTeam/iApp/issues)

---

Copyright 2026 iHTCTeam. All rights reserved.
