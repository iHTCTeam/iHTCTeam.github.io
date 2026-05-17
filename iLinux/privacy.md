---
layout: default
title: iLinux - Privacy Policy
---

# Privacy Policy

**Last updated: May 17, 2026**

[Back to iLinux Support](./)

---

iHTCTeam ("we", "us", or "our") built iLinux (also known as "爱 Linux") as a paid app. This page informs you of our policies regarding the collection, use, and disclosure of personal data when you use our app.

---

## Summary

**iLinux does not collect, store, or transmit any personal data.** The app operates entirely on your local device and requires no account, no internet connection, and no cloud services to function.

---

## Data Collection

We do not collect any data. Specifically:

- **No personal information** is collected (no name, email, phone number, or account).
- **No usage data** or analytics are collected.
- **No command history, quiz answers, or any content** you interact with in the app is accessible to us.
- **No cookies or tracking** technologies are used.
- **No third-party services** (advertising, analytics, crash reporting) are integrated.

---

## How the App Works

iLinux stores all user-generated data — favorites, recent views, quiz session results, wrong answer records, and app preferences — locally on your device:

- All command data (JSON summaries and Markdown documentation) is bundled inside the app and never fetched from any external server.
- No internet connection is required for any core feature of the app.
- Opening external links from within the app (e.g., tapping a URL in the Feedback section) uses standard iOS networking behavior; the linked page is loaded by your device directly from its host, not through any iHTCTeam server.
- The optional **App Store version check** (`AppStoreVersionChecker`) makes a single read-only request to the public iTunes Lookup API to compare the installed version with the latest release. No personal data is sent in this request.

---

## Permissions

iLinux does not request any special device permissions. No camera, microphone, location, contacts, or photo library access is required.

---

## Data Storage

| Data | Storage Location |
|------|-----------------|
| Favorites, recent views, wrong answer records | Local UserDefaults / app sandbox on your device |
| Quiz progress and daily session results | Local app sandbox on your device |
| Theme, language, and appearance preferences | Local UserDefaults on your device |
| Widget snapshot (theme color, language code, learning progress summary) | App Group container (`group.com.iHTCboy.iLinuxs`) shared between the main app and widget extension — stays on your device |

No data is stored on any external server or cloud service.

---

## App Group (Widget Extension)

iLinux uses an App Group (`group.com.iHTCboy.iLinuxs`) to share a small amount of data with its Home Screen widget extension. This data includes:

- The selected content language code (e.g. `en`, `zh-Hans`)
- A theme color snapshot (accent hex and gradient values)
- A summary of your learning progress (favorites count, quiz stats) for widget display

This data is written to a shared container on your device only, and is never transmitted anywhere.

---

## In-App Purchase

iLinux includes an optional tip/purchase option. All payment transactions are handled exclusively by **Apple's StoreKit framework**. iHTCTeam does not receive, process, or store any payment card information or billing details.

---

## Children's Privacy

iLinux does not knowingly collect any personal data from anyone, including children under 13. Since we do not collect any data at all, no special provisions are needed.

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
