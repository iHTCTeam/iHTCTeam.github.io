---
layout: app
title: Weber — Support
app_id: Weber
description: macOS Safari Web Extension for video speed control and Markdown copy.
---

<section lang="en" markdown="1">

Weber is a **macOS-only** Safari Web Extension that gives you precise control over HTML5 video playback speed and lets you copy any web page or link as Markdown with a single right-click. **Lightweight, privacy-friendly, and built for Safari on Mac.**

The **host app** from the Mac App Store registers the extension. Day-to-day controls — speed slider, presets, language and always-autospeed — live in the **Safari toolbar popup**, not inside the host app window.

## Getting Started

1. Download Weber from the Mac App Store and open the host app once to register the extension.
2. Open **Safari → Settings → Extensions** (or **Safari → Preferences → Extensions** on older macOS).
3. Check the box next to **Weber** to enable the extension.
4. Add the Weber icon to the Safari toolbar if needed (right-click the toolbar → Customize Toolbar).
5. If you want always-autospeed mode, grant the optional website access permission when prompted from the **toolbar popup**.
6. Click the **Weber icon in the Safari toolbar** to open the popup and control video speed or change extension settings.

## Features

- **Precise Speed Control** — Adjust playback from 0.1x to 100x using a slider, numeric input, or common presets (0.5x / 1x / 1.5x / 2x / 3x) from the toolbar popup.
- **Lazy Injection (Default)** — Content script is injected only when you open the popup. No broad website access is needed.
- **Always-Autospeed Mode** — Optionally grant website access permission so your preferred speed is auto-applied to every page on load.
- **Speed Memory** — Your chosen speed is saved via `browser.storage.local` and persists across pages and sessions.
- **Dynamic Video Detection** — Uses MutationObserver to detect newly-added `<video>` elements, so dynamically loaded players are covered automatically.
- **Copy as Markdown** — Right-click context menu "Copy as Markdown Format" for pages and links. Supports regular pages, selected text, and link targets.
- **Extension UI Languages** — Toolbar popup in **English** and **Simplified Chinese (简体中文)**.
- **Light & Dark Mode** — Adaptive popup UI that follows your macOS appearance setting.
- **Host App** — Minimal macOS companion to install and enable the extension in Safari (not the settings surface).
- **Modern Architecture** — Safari Web Extension built with Manifest V3 and Service Worker.

## Known Limitations

- Speed control works only with standard HTML5 `<video>` elements. Videos rendered via Canvas, WebGL, or inside closed Shadow DOM may not be detected.
- Some websites override playback speed programmatically, which may conflict with the extension's setting.
- The maximum speed factor is 100x; however, most browsers cap effective playback at lower rates depending on the media codec.
- **Mac only** — Weber is a Safari Web Extension for **macOS**. It does not run on iPhone, iPad, or other browsers.

## System Requirements

| Platform | Minimum Version |
|----------|-----------------|
| Mac (Safari) | macOS 12.0+ |

## Contact Us

If you have questions, feedback, or need help, please reach out:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

We typically respond within 48 hours.

[FAQ](faq) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

Weber 是一款 **仅限 macOS** 的 Safari 浏览器扩展，可精确控制 HTML5 视频播放速度，还能通过右键菜单一键将网页或链接复制为 Markdown 格式。**轻量、注重隐私、专为 Mac 版 Safari 打造。**

Mac App Store 中的 **宿主应用** 用于注册扩展。日常操作——速度滑块、预设、语言与始终自动调速——均在 **Safari 工具栏弹出窗口** 中完成，不在宿主应用窗口内。

## 快速上手

1. 从 Mac App Store 下载 Weber 并打开宿主应用一次以注册扩展。
2. 打开 **Safari → 设置 → 扩展**（旧版 macOS 为 **Safari → 偏好设置 → 扩展**）。
3. 勾选 **Weber** 以启用扩展。
4. 如需要，将 Weber 图标添加到 Safari 工具栏（右键工具栏 → 自定义工具栏）。
5. 如需始终自动调速模式，在 **工具栏弹出窗口** 提示时授予可选的网站访问权限。
6. 点击 **Safari 工具栏中的 Weber 图标**，打开弹出窗口控制视频速度或更改扩展设置。

## 功能特性

- **精确速度控制** — 在工具栏弹出窗口中通过滑块、数字输入或常用预设（0.5x / 1x / 1.5x / 2x / 3x）将播放速度调整为 0.1x 到 100x。
- **懒注入（默认）** — 内容脚本仅在你打开弹出窗口时注入，无需广泛的网站访问权限。
- **始终自动调速模式** — 可选授予网站访问权限，让你偏好的速度在每个页面加载时自动生效。
- **速度记忆** — 通过 `browser.storage.local` 保存你选择的速度，跨页面和跨会话持久保存。
- **动态视频检测** — 使用 MutationObserver 检测动态添加的 `<video>` 元素，自动覆盖动态加载的播放器。
- **复制为 Markdown** — 右键菜单「复制为 Markdown 格式」，支持普通页面、选中文本和链接目标三种场景。
- **扩展界面语言** — 工具栏弹出窗口支持 **英文** 与 **简体中文**。
- **亮色与深色模式** — 弹出窗口自适应界面，跟随 macOS 外观设置。
- **宿主应用** — 精简的 macOS 配套应用，用于在 Safari 中安装并启用扩展（非设置界面）。
- **现代架构** — 基于 Manifest V3 和 Service Worker 构建的 Safari Web Extension。

## 已知限制

- 速度控制仅适用于标准 HTML5 `<video>` 元素。通过 Canvas、WebGL 渲染或位于封闭 Shadow DOM 内的视频可能无法被检测到。
- 某些网站会以编程方式覆盖播放速度，可能与扩展的设置冲突。
- 最大速度倍率为 100x；但大多数浏览器会根据媒体编解码器将实际播放限制在更低的倍率。
- **仅限 Mac** — Weber 是 **macOS** 版 Safari Web Extension，不支持 iPhone、iPad 或其他浏览器。

## 系统要求

| 平台 | 最低版本 |
|----------|-----------------|
| Mac（Safari）| macOS 12.0+ |

## 联系我们

如有问题、反馈或需要帮助，请联系：

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我们通常在 48 小时内回复。

[常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

Weber 是一款 **僅限 macOS** 的 Safari 延伸功能，可精確控制 HTML5 影片播放速度，還能透過右鍵選單一鍵將網頁或連結複製為 Markdown 格式。**輕量、注重隱私、專為 Mac 版 Safari 打造。**

Mac App Store 中的 **宿主應用** 用於註冊延伸功能。日常操作——速度滑桿、預設、語言與始終自動調速——均在 **Safari 工具列彈出視窗** 中完成，不在宿主應用視窗內。

## 快速上手

1. 從 Mac App Store 下載 Weber 並開啟宿主應用一次以註冊延伸功能。
2. 開啟 **Safari → 設定 → 擴充功能**（舊版 macOS 為 **Safari → 偏好設定 → 擴充功能**）。
3. 勾選 **Weber** 以啟用延伸功能。
4. 如需要，將 Weber 圖示新增到 Safari 工具列（右鍵工具列 → 自訂工具列）。
5. 如需始終自動調速模式，在 **工具列彈出視窗** 提示時授予選用的網站存取權限。
6. 點按 **Safari 工具列中的 Weber 圖示**，開啟彈出視窗控制影片速度或變更延伸功能設定。

## 功能特色

- **精確速度控制** — 在工具列彈出視窗中透過滑桿、數字輸入或常用預設（0.5x / 1x / 1.5x / 2x / 3x）將播放速度調整為 0.1x 到 100x。
- **延遲注入（預設）** — 內容腳本僅在你開啟彈出視窗時注入，無需廣泛的網站存取權限。
- **始終自動調速模式** — 可選授予網站存取權限，讓你偏好的速度在每個頁面載入時自動生效。
- **速度記憶** — 透過 `browser.storage.local` 儲存你選擇的速度，跨頁面和跨工作階段持久保存。
- **動態影片偵測** — 使用 MutationObserver 偵測動態新增的 `<video>` 元素，自動涵蓋動態載入的播放器。
- **複製為 Markdown** — 右鍵選單「複製為 Markdown 格式」，支援一般頁面、選取文字和連結目標三種情境。
- **延伸功能介面語言** — 工具列彈出視窗支援 **英文** 與 **簡體中文**。
- **亮色與深色模式** — 彈出視窗自適應介面，跟隨 macOS 外觀設定。
- **宿主應用** — 精簡的 macOS 配套應用，用於在 Safari 中安裝並啟用延伸功能（非設定介面）。
- **現代架構** — 基於 Manifest V3 和 Service Worker 建構的 Safari Web Extension。

## 已知限制

- 速度控制僅適用於標準 HTML5 `<video>` 元素。透過 Canvas、WebGL 繪製或位於封閉 Shadow DOM 內的影片可能無法被偵測到。
- 某些網站會以程式方式覆蓋播放速度，可能與擴充功能的設定衝突。
- 最大速度倍率為 100x；但大多數瀏覽器會根據媒體編解碼器將實際播放限制在更低的倍率。
- **僅限 Mac** — Weber 是 **macOS** 版 Safari Web Extension，不支援 iPhone、iPad 或其他瀏覽器。

## 系統需求

| 平台 | 最低版本 |
|----------|-----------------|
| Mac（Safari）| macOS 12.0+ |

## 聯絡我們

如有問題、回饋或需要協助，請聯絡：

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我們通常在 48 小時內回覆。

[常見問題](faq) · [隱私政策](privacy)

</section>
