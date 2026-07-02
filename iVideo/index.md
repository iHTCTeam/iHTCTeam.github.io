---
layout: app
title: iVideo — Support
app_id: iVideo
description: Professional video toolbox — screen recording, 31 editing tools, on-device subtitles, face blur, color grading, speed ramps, batch processing, filter & LUT support, all processed on-device.
---

<section lang="en" markdown="1">

iVideo is a **professional video toolbox** for iPhone, iPad and Mac. From screen recording to editing, subtitles to color grading — **31 powerful tools** handle everything in one app. Every frame is processed locally on your device. **No cloud, no account, no data upload.**

## Getting Started

1. **Record** — Tap the Record tab to start a screen recording (iOS: ReplayKit; macOS: ScreenCaptureKit). Auto-snapshots capture key moments during recording.
2. **Import** — Bring in videos from your Photo Library (zero transcoding), the Files app, or via remote URL download.
3. **Edit** — Open any video in the Workspace to access all 31 tools across 7 categories: capture, trim, speed, audio, visual, convert, and notes.
4. **Export** — Choose from 6 quality presets (Original / 4K / 2K / 1080p / 720p / 540p) in MP4 or MOV, or use custom export presets. The global export queue runs in the background.
5. **Share** — Share directly from the export toast, or revisit past exports from your session history.

## Features

### First-Launch Onboarding

A 5-page guided onboarding highlights four key pillars: professional workspace, frame-level precision, privacy-first design, and on-device subtitles. A built-in sample video is injected on first launch so you can try all tools immediately.

### Screen Recording

- **iOS Recording** — ReplayKit Broadcast Upload Extension with configurable auto-snapshot intervals during recording.
- **macOS Recording** — ScreenCaptureKit with multi-display and optional system audio capture.
- **Live Duration Badge** — The Record tab badge shows elapsed time in real-time while recording.

### Video Library

- **Smart Organization** — Search by filename, custom name, or tags. Filter by All / Favorites / Recorded / Imported / Exported / Has Notes.
- **Flexible Layout** — Grid or list view with adjustable column count (iPhone 1–4 / iPad & Mac 2–6).
- **Apple-Style Sorting** — Sort by date, name, size, kind, or favorites with ascending/descending direction — modeled after the Files app.
- **Batch Operations** — Multi-select for bulk share, save to Photos, favorite, merge, collage, batch processing, or delete (with storage size display).
- **Custom Thumbnails** — Set any frame as the video's cover image.

### Workspace — 31 Tools in 7 Categories

| Category | Tools |
|----------|-------|
| Capture | Screenshot, Frame Extraction, Video Info, Scene Detection, OCR, Waveform Scope, Annotation |
| Trim | Duration Trim, Aspect Crop, Rotate, Transcript Edit, Beat Sync, Silence Removal |
| Speed | Variable Speed (0.1–8×), Reverse Playback, Speed Ramp |
| Audio | Mute, Audio Extraction (M4A/WAV/CAF), On-Device Subtitles, Audio Denoise & Enhance |
| Visual | Watermark, Metadata Strip, Compression, Face Blur, Color Grading |
| Convert | Live Photo, GIF, Social Format, Before/After Compare |
| Notes | Video Notes, Frame Compare |

- **Favorite Tools Bar** — Long-press any tool to pin it to a quick-access bar at the top of the workspace (up to 5, synced via iCloud).
- **Immersive Preview** — Double-tap to enter full-screen immersive mode with large transport controls.
- **Export Toast** — Inline share button in the export notification; session export history for quick re-sharing.

### On-Device Auto Subtitles (Flagship)

- **Speech-to-Text** — Apple Speech framework with forced on-device recognition (`requiresOnDeviceRecognition`). Supports 60+ languages.
- **Sound Events** — SoundAnalysis detects music, applause, laughter and more, adding `[annotation]` captions.
- **Three Modes** — Speech only, sound events only, or combined speech + sound.
- **Language Selection** — Searchable language picker with 60+ languages, commonly-used pinned to top, offline download badge for unsupported languages.
- **Editable Results** — Edit, delete, or tap any subtitle segment to seek. Export as SRT or burn into video.
- **ASS Subtitle Export** — Standard ASS format with vertical per-character positioning.
- **Bilingual Translation** — Apple Translation framework for on-device secondary language line.
- **Subtitle Styling** — Horizontal alignment, vertical layout, secondary color, and burn-in rendering via CoreText.

### Face Blur (Flagship)

- **Automatic Detection** — Vision framework detects faces in every frame.
- **Blur Styles** — Gaussian blur or mosaic with adjustable intensity.
- **Manual Region** — Draw custom blur rectangles for license plates, signs, or watermarks that face detection can't catch.
- **Pipeline** — AVAssetReader/Writer custom pipeline with soft-edge masks and original audio track muxing.

### Batch Processing

- **Recipe System** — Apply a chain of operations (rotate → speed → mute → watermark → metadata strip → compress) to multiple videos at once.
- **Sequential Execution** — Each video processed serially; individual failures don't block the batch. Completed videos added to the library incrementally.
- **Persistent Recipes** — Last-used recipe remembered for quick reuse.

### Scene Detection & Transcript Edit

- **Scene Chapters** — Vision feature fingerprints with adaptive threshold detect scene changes. Tap any chapter to jump to that point.
- **Transcript Edit** — Descript-style editing: transcribe locally, check/uncheck sentences, export with unchecked segments removed.

### OCR & Annotation

- **OCR** — Vision text recognition on the current frame with copy and share.
- **Frame Annotation** — Draw arrows, circles, rectangles, freehand, or text on any frame. Export as full-resolution PNG.

### Audio Enhancement

- **Denoise** — High-pass filter removes rumble, noise gate with adaptive floor estimation, peak normalization.
- **All On-Device** — Enhanced audio written to M4A and muxed back into the video.

### Color Grading & Filters

- **7-Parameter Grading** — Exposure, brightness, contrast, saturation, vibrance, white balance, tint via Core Image filter chain. Real-time preview with hold-to-compare.
- **Built-in LUT Pack** — 6 procedurally generated styles: Teal & Orange, Bleach Bypass, Vintage, Cool Shadow, Warm Shadow, High-Contrast B&W (17³ CIColorCube, zero resource files).
- **Filter Presets** — 11 built-in presets (8 CIPhotoEffect + warm/cool + teal-orange cinematic). Import `.cube` 3D LUT files from Adobe/Resolve.

### Speed Ramp & Silence Removal

- **Keyframe Speed Curves** — Split timeline into segments, assign different speeds per segment with a visual color-band editor.
- **Auto Jump Cut** — Detect silent segments via RMS windowing + adaptive threshold + morphological closing. Canvas visualization of kept/removed segments.

### Beat Sync Montage

- **Beat Detection** — Energy envelope onset analysis with adaptive threshold and BPM calculation.
- **Auto Montage** — Video cuts on every beat with continuous audio. Stackable transitions: zoom, slide, flash, black.

### Social Format & Before/After

- **Social Format Presets** — 9:16, 1:1, 4:5, 16:9 with blur background, solid color, or crop-to-fill. Real-time single-frame preview with safe area guides. Optional caption bar (top/bottom) with semi-transparent color band.
- **Before/After Compare** — Side-by-side or top-bottom split-screen with divider line and Before/After labels.

### Waveform Scope

- **RGB Histogram & Luma Waveform** — CPU-sampled analysis of the current frame, drawn with Canvas.

### Playback Experience

- **Keyboard Shortcuts** — Space (play/pause), Arrow keys (frame step / 10s skip), `,` `.` (frame step), **JKL** (FCP-style shuttle: 1× → 2× → 4× → 8× forward/reverse).
- **JKL HUD** — On-screen capsule overlay showing current speed and direction, auto-fading with duration adapted to speed tier.
- **JKL Live Activity** — Lock screen and Dynamic Island display of current JKL speed tier (iOS 16.1+).
- **Custom Speed** — Slider from 0.1× to 8× with 8 presets, 2 recently-used chips (LRU), and pinch-to-adjust on iPhone.
- **Speed Capsule** — Shows real-time playback speed with JKL +/- sign; long-press to jump to custom speed sheet.
- **Reverse Warning** — Scrubber tint turns red during reverse playback.
- **Scrubber Thumbnails** — Dragging the scrubber shows a floating thumbnail preview (60-segment bucketed, 3-level cache).
- **Audio Waveform** — Trim tool displays audio waveform visualization.
- **Horizontal Swipe Seek** — Swipe on the preview to seek with direction locking and adaptive span.
- **AirPlay & PiP** — Stream to external displays or continue playback in Picture-in-Picture.
- **Cross-Session Preferences** — Playback speed and mute state persist across sessions and sync via iCloud.

### Video Merge & Collage

- **Video Merge** — Concatenate multiple videos with optional crossfade transitions.
- **Video Collage** — Combine 2–4 videos in side-by-side, top-bottom, or 4-grid layout at 1920×1080.

### Live Photo Studio

- **Video to Live Photo** — Choose key frame and duration to create a Live Photo wallpaper.
- **Live Photo to Video/GIF/Still** — Batch conversion with original encoding preserved.
- **Batch Mode** — Multi-select Live Photos for bulk conversion.

### Export

| Preset | Resolution |
|--------|-----------|
| Original | Source resolution |
| Ultra HD | 4K |
| Super HD | 2K |
| HD | 1080p |
| Standard | 720p |
| Compact | 540p |

- Export in MP4 or MOV format.
- **Export Presets** — 4 built-in presets plus custom presets (quality + container). Switch globally from workspace menu or Settings.
- **Global Export Queue** — Background serial processing with progress tracking. Queue view shows pending, in-progress, completed, and failed items. iOS background task keeps exports alive.
- **Export Notification** — Optional local notification when export completes (configurable in Settings).

### Usage Guide

- **Built-in Help** — Settings → Help: hero card, getting-started steps, all tools reference, flagship features, permissions guide, and collapsible FAQ.
- **Replay Onboarding** — Re-watch the first-launch guide from Settings without resetting your data.

### Siri & Shortcuts

- **AppShortcuts** — Start recording, open video library, or launch Live Photo tool via Siri or the Shortcuts app.

### iCloud Sync

- Lightweight preference sync via `NSUbiquitousKeyValueStore`: theme, language, playback speed, mute state, custom speed history, and favorite tools bar — synced across all your devices.

### General

- **Privacy First** — All video processing happens on-device. No cloud, no analytics, no tracking, no account. Speech recognition, face detection, OCR, translation — all forced on-device.
- **Dark-First UI** — Dark-themed workspace designed for focused video editing.
- **3 Languages** — English, Simplified Chinese, Traditional Chinese. Switch in-app instantly without restart.
- **Tip Jar** — Optional in-app tip to support development.
- **About Page** — Hero card with app stats, product highlights, and quick links to rate, share, or send feedback.

## System Requirements

| Platform | Minimum Version |
|----------|-----------------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |

## Contact Us

If you have questions, feedback, or need help, please reach out:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

We typically respond within 48 hours.

[FAQ](faq) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱视频是一款面向 iPhone、iPad 和 Mac 的 **专业视频工具箱**。从录屏到剪辑，从字幕到调色——**31 种强大工具** 在一个应用内全搞定。每一帧画面都在设备本地处理。**无云端、无账号、零数据上传。**

## 快速上手

1. **录屏** — 点击「录屏」标签开始屏幕录制（iOS 使用 ReplayKit；macOS 使用 ScreenCaptureKit）。录制中自动按间隔截图。
2. **导入** — 从相册导入（零转码）、从文件 App 多选导入，或通过远程直链下载。
3. **编辑** — 在工作台中打开任意视频，使用全部 31 种工具，涵盖 7 大类别：截取、剪辑、速度、音频、视觉、转换与笔记。
4. **导出** — 从 6 档画质中选择（原画 / 4K / 2K / 1080p / 720p / 540p），支持 MP4 与 MOV 格式，也可使用自定义导出预设。全局导出队列后台串行处理。
5. **分享** — 导出完成的 Toast 中直接分享，或从本次会话的导出历史中一键再分享。

## 功能特性

### 首次启动引导

5 页走查式引导，呈现四大差异化支柱：专业工作台、逐帧级精准、隐私优先与本地字幕。首次启动时自动注入演示样片，让您立即体验所有工具。

### 录屏

- **iOS 录屏** — ReplayKit 广播上传扩展，可配置录屏中自动截图间隔。
- **macOS 录屏** — ScreenCaptureKit，支持多显示器与系统音频可选。
- **实时时长徽标** — 录制过程中录屏 Tab 图标实时显示已录制时长。

### 视频库

- **智能整理** — 按文件名、自定义名或标签搜索。按全部 / 收藏 / 录屏 / 导入 / 已导出 / 含笔记过滤。
- **灵活布局** — 网格或列表视图，可调整列数（iPhone 1–4 列 / iPad 与 Mac 2–6 列）。
- **Apple 风格排序** — 按日期、名称、大小、种类或收藏排序，支持升序与降序——参照「文件」App 交互风格。
- **批量操作** — 多选后批量分享、存相册、收藏、拼接、拼图、批处理或删除（显示占用空间大小）。
- **自定义封面** — 将任意帧设为视频的封面图。

### 工作台 — 7 大类 31 种工具

| 类别 | 工具 |
|------|------|
| 截取 | 截图、拆帧、视频信息、场景章节、文字识别 OCR、示波器、逐帧标注 |
| 剪辑 | 时长裁剪、画面裁剪、旋转、按文字剪辑、卡点混剪、去静音跳剪 |
| 速度 | 变速（0.1–8×）、倒放、变速曲线 |
| 音频 | 静音、音频分离（M4A/WAV/CAF）、设备端字幕、音频降噪增强 |
| 视觉 | 水印、元数据清除、压缩、人脸打码、调色 |
| 转换 | Live Photo、GIF、社媒画幅、前后对比拼屏 |
| 笔记 | 视频笔记、帧对比 |

- **常用工具快捷栏** — 长按任意工具将其钉在工作台顶部快捷栏（最多 5 个，通过 iCloud 跨设备同步）。
- **沉浸式预览** — 双击进入全屏沉浸模式，配备大号播放控件。
- **导出 Toast** — 导出通知内联「分享」按钮；本次会话的导出历史可一键再分享。

### 设备端自动字幕（旗舰功能）

- **语音转文字** — 使用 Apple Speech 框架，强制设备端识别（`requiresOnDeviceRecognition`），支持 60+ 种语言。
- **声音事件** — SoundAnalysis 检测音乐、掌声、笑声等，添加 `[标注]` 字幕。
- **三种模式** — 仅语音、仅声音事件、语音+声音合并。
- **语言选择** — 可搜索的语言选择器，60+ 种语言，常用语言置顶，不支持本地识别时显示「需下载」徽标。
- **可编辑结果** — 逐条编辑、删除文本，或点击字幕跳转至对应时间点。导出 SRT 或烧录进视频。
- **ASS 字幕导出** — 标准 ASS 格式，支持竖排逐字定位。
- **双语翻译** — 使用 Apple Translation 框架，设备端翻译生成副语言行。
- **字幕样式** — 水平对齐、竖排布局、副行颜色，通过 CoreText 烧录渲染。

### 人脸自动打码（旗舰功能）

- **自动检测** — Vision 框架逐帧检测人脸。
- **打码样式** — 高斯模糊或马赛克，强度可调。
- **手动框选** — 拖拽绘制矩形框，适合车牌、招牌或角标等人脸检测无法命中的固定区域。
- **处理管线** — AVAssetReader/Writer 自定义管线，柔化遮罩 + 原音轨 mux。

### 批处理

- **配方系统** — 对多个视频批量套用一组操作链（旋转 → 变速 → 去音轨 → 水印 → 清元数据 → 压缩）。
- **串行执行** — 逐个处理，单个失败不阻断整批，完成后增量入库。
- **记住配方** — 自动记住上次使用的配方，下次快速复用。

### 场景章节与文字剪辑

- **场景章节** — Vision 特征指纹 + 自适应阈值检测场景变化，点按章节即可跳转。
- **按文字剪辑** — Descript 风格编辑：本地转写 → 勾删句子 → 导出时移除已删段落。

### OCR 与逐帧标注

- **文字识别** — Vision 识别当前帧文字，支持复制与分享。
- **逐帧标注** — 在任意帧上绘制箭头、圆圈、矩形、自由笔触或文字，导出为全分辨率 PNG。

### 音频降噪增强

- **降噪** — 高通滤波去隆隆声 + 噪声门（本底自适应估计）+ 峰值归一化。
- **全程本地** — 增强后的音频写入 M4A 并 mux 回视频。

### 调色与滤镜

- **7 参数调色** — 曝光、亮度、对比度、饱和度、自然饱和度、色温、色调，通过 Core Image 滤镜链实现。实时预览 + 按住查看原图。
- **内置 LUT 包** — 6 种程序化生成的调色风格：青橙、漂白、复古、冷影、暖影、高反黑白（17³ CIColorCube，零资源文件）。
- **滤镜预设** — 11 种内建预设（CIPhotoEffect 8 种 + 暖色/冷色 + 青橙电影），支持导入 `.cube` 3D LUT 文件（Adobe/Resolve 格式）。

### 变速曲线与去静音跳剪

- **关键帧变速曲线** — 将时间线分段，为每段设定不同速度，色带式可视化编辑器。
- **自动去静音跳剪** — 通过 RMS 窗口 + 自适应阈值 + 形态学闭运算检测静音段。Canvas 可视化展示保留/移除片段。

### 卡点混剪

- **节拍检测** — 能量包络 onset 差分 + 自适应阈值计算 BPM。
- **自动混剪** — 画面随节拍跳切，音乐连续。可叠加多种转场：缩放、滑入、闪白、黑场。

### 社媒画幅与前后对比

- **社媒画幅预设** — 9:16 / 1:1 / 4:5 / 16:9，支持模糊背景、纯色边或裁剪填满。实时单帧预览 + 安全区参考线。可选字幕条（顶/底）+ 半透明色条。
- **前后对比拼屏** — 左右或上下拼屏，分隔线 + Before/After 标签。

### 示波器

- **RGB 直方图与亮度波形** — 对当前帧进行 CPU 采样分析，Canvas 绘制展示。

### 播放体验

- **键盘快捷键** — Space（播放/暂停）、方向键（逐帧/跳 10 秒）、`,` `.`（逐帧）、**JKL**（FCP 风格快退快进：1× → 2× → 4× → 8×）。
- **JKL HUD** — 屏幕中央胶囊浮窗，显示当前速度与方向，按速度档差异化显示时长后自动淡出。
- **JKL 灵动岛** — 锁屏与灵动岛实时显示当前 JKL 速度档（iOS 16.1+）。
- **自定义速度** — 滑块 0.1×–8× + 8 档预设 + 最近用过 2 档（LRU）+ iPhone 双指捏合调速。
- **速度档胶囊** — 实时显示含 JKL 正负号的实际播放速度；长按 0.5 秒直达自定义速度面板。
- **反向警示** — 倒放时 scrubber 轨道由白变红。
- **Scrubber 缩略图** — 拖动进度条时悬浮缩略图预览（60 段分桶，三级缓存）。
- **音频波形** — 时长裁剪工具显示音频波形可视化。
- **水平滑动快进** — 在预览区左右滑动即可 seek，方向锁定 + 短长视频自适应覆盖时长。
- **AirPlay 与画中画** — 投屏至外部显示器或使用画中画继续播放。
- **跨会话偏好** — 播放速度与静音状态跨会话保留并通过 iCloud 同步。

### 视频拼接与拼图

- **视频拼接** — 多段视频首尾拼接，可选交叉淡化转场。
- **视频拼图** — 将 2–4 个视频合为一画面（左右 / 上下 / 四宫格），输出 1920×1080。

### Live Photo 工作室

- **视频转 Live Photo** — 选择关键帧与时长，创建 Live Photo 壁纸。
- **Live Photo 转视频/GIF/静图** — 批量转换，保留原始编码。
- **批量模式** — 多选 Live Photo 批量转换。

### 导出

| 档位 | 分辨率 |
|------|--------|
| 原画 | 源分辨率 |
| 超高清 | 4K |
| 超清 | 2K |
| 高清 | 1080p |
| 标清 | 720p |
| 省流 | 540p |

- 支持 MP4 与 MOV 格式导出。
- **导出预设** — 4 个内建预设 + 自定义预设（画质 + 容器），可在工作台菜单或设置中一键切换。
- **全局导出队列** — 后台串行处理，进度实时跟踪。队列视图展示排队中、进行中、已完成与失败的任务。iOS 后台任务保持导出持续运行。
- **导出完成通知** — 导出完成后可选本地通知提醒（在设置中配置）。

### 使用说明

- **内置帮助** — 设置 → 帮助：Hero 卡片 + 上手步骤 + 全部工具速查 + 旗舰能力 + 权限说明 + 折叠式 FAQ。
- **重看引导** — 在设置中重新查看首启引导，不会重置您的数据。

### Siri 与快捷指令

- **AppShortcuts** — 通过 Siri 或「快捷指令」App 直接开始录屏、打开视频库或启动 Live Photo 工具。

### iCloud 同步

- 基于 `NSUbiquitousKeyValueStore` 的轻量偏好同步：主题、语言、播放速度、静音状态、自定义速度档历史与常用工具快捷栏——在所有设备间自动同步。

### 其他

- **隐私优先** — 所有视频处理在设备本地完成。无云端、无分析、无追踪、无账号。语音识别、人脸检测、OCR、翻译——全部强制设备端运行。
- **暗色优先** — 工作台采用暗色主题，专为沉浸式视频编辑设计。
- **3 种语言** — 英文、简体中文、繁体中文，应用内实时切换无需重启。
- **打赏** — 可选应用内打赏支持开发。
- **关于页面** — Hero 卡片展示应用数据、产品亮点，一键评分、分享或反馈。

## 系统要求

| 平台 | 最低版本 |
|------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |

## 联系我们

如有问题、反馈或需要帮助，请联系：

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我们通常在 48 小时内回复。

[常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛視頻是一款面向 iPhone、iPad 和 Mac 的 **專業影片工具箱**。從錄屏到剪輯，從字幕到調色——**31 種強大工具** 在一個應用程式內全搞定。每一幀畫面都在裝置本地處理。**無雲端、無帳號、零資料上傳。**

## 快速上手

1. **錄屏** — 點擊「錄屏」標籤開始螢幕錄製（iOS 使用 ReplayKit；macOS 使用 ScreenCaptureKit）。錄製中自動按間隔截圖。
2. **匯入** — 從相簿匯入（零轉碼）、從檔案 App 多選匯入，或透過遠端直連下載。
3. **編輯** — 在工作台中開啟任意影片，使用全部 31 種工具，涵蓋 7 大類別：擷取、剪輯、速度、音訊、視覺、轉換與筆記。
4. **匯出** — 從 6 檔畫質中選擇（原畫 / 4K / 2K / 1080p / 720p / 540p），支援 MP4 與 MOV 格式，也可使用自訂匯出預設。全域匯出佇列後台串行處理。
5. **分享** — 匯出完成的 Toast 中直接分享，或從本次工作階段的匯出歷史中一鍵再分享。

## 功能特色

### 首次啟動引導

5 頁走查式引導，呈現四大差異化支柱：專業工作台、逐幀級精準、隱私優先與本地字幕。首次啟動時自動注入示範樣片，讓您立即體驗所有工具。

### 錄屏

- **iOS 錄屏** — ReplayKit 廣播上傳延伸功能，可設定錄屏中自動截圖間隔。
- **macOS 錄屏** — ScreenCaptureKit，支援多顯示器與系統音訊可選。
- **即時時長徽標** — 錄製過程中錄屏 Tab 圖示即時顯示已錄製時長。

### 影片庫

- **智慧整理** — 按檔案名稱、自訂名稱或標籤搜尋。按全部 / 收藏 / 錄屏 / 匯入 / 已匯出 / 含筆記過濾。
- **靈活佈局** — 網格或列表檢視，可調整欄數（iPhone 1–4 欄 / iPad 與 Mac 2–6 欄）。
- **Apple 風格排序** — 按日期、名稱、大小、種類或收藏排序，支援升序與降序——參照「檔案」App 互動風格。
- **批次操作** — 多選後批次分享、存相簿、收藏、拼接、拼圖、批次處理或刪除（顯示佔用空間大小）。
- **自訂封面** — 將任意幀設為影片的封面圖。

### 工作台 — 7 大類 31 種工具

| 類別 | 工具 |
|------|------|
| 擷取 | 截圖、拆幀、影片資訊、場景章節、文字辨識 OCR、示波器、逐幀標註 |
| 剪輯 | 時長裁剪、畫面裁剪、旋轉、按文字剪輯、卡點混剪、去靜音跳剪 |
| 速度 | 變速（0.1–8×）、倒放、變速曲線 |
| 音訊 | 靜音、音訊分離（M4A/WAV/CAF）、裝置端字幕、音訊降噪增強 |
| 視覺 | 浮水印、中繼資料清除、壓縮、人臉打碼、調色 |
| 轉換 | Live Photo、GIF、社媒畫幅、前後對比拼屏 |
| 筆記 | 影片筆記、幀對比 |

- **常用工具快捷列** — 長按任意工具將其釘在工作台頂部快捷列（最多 5 個，透過 iCloud 跨裝置同步）。
- **沉浸式預覽** — 雙擊進入全螢幕沉浸模式，配備大型播放控制項。
- **匯出 Toast** — 匯出通知內嵌「分享」按鈕；本次工作階段的匯出歷史可一鍵再分享。

### 裝置端自動字幕（旗艦功能）

- **語音轉文字** — 使用 Apple Speech 框架，強制裝置端辨識（`requiresOnDeviceRecognition`），支援 60+ 種語言。
- **聲音事件** — SoundAnalysis 偵測音樂、掌聲、笑聲等，新增 `[標註]` 字幕。
- **三種模式** — 僅語音、僅聲音事件、語音+聲音合併。
- **語言選擇** — 可搜尋的語言選擇器，60+ 種語言，常用語言置頂，不支援本地辨識時顯示「需下載」徽標。
- **可編輯結果** — 逐條編輯、刪除文字，或點擊字幕跳轉至對應時間點。匯出 SRT 或燒錄進影片。
- **ASS 字幕匯出** — 標準 ASS 格式，支援直排逐字定位。
- **雙語翻譯** — 使用 Apple Translation 框架，裝置端翻譯產生副語言行。
- **字幕樣式** — 水平對齊、直排佈局、副行顏色，透過 CoreText 燒錄渲染。

### 人臉自動打碼（旗艦功能）

- **自動偵測** — Vision 框架逐幀偵測人臉。
- **打碼樣式** — 高斯模糊或馬賽克，強度可調。
- **手動框選** — 拖曳繪製矩形框，適合車牌、招牌或角標等人臉偵測無法命中的固定區域。
- **處理管線** — AVAssetReader/Writer 自訂管線，柔化遮罩 + 原音軌 mux。

### 批次處理

- **配方系統** — 對多個影片批次套用一組操作鏈（旋轉 → 變速 → 去音軌 → 浮水印 → 清中繼資料 → 壓縮）。
- **串行執行** — 逐個處理，單個失敗不阻斷整批，完成後增量入庫。
- **記住配方** — 自動記住上次使用的配方，下次快速複用。

### 場景章節與文字剪輯

- **場景章節** — Vision 特徵指紋 + 自適應閾值偵測場景變化，點按章節即可跳轉。
- **按文字剪輯** — Descript 風格編輯：本地轉寫 → 勾刪句子 → 匯出時移除已刪段落。

### OCR 與逐幀標註

- **文字辨識** — Vision 辨識當前幀文字，支援複製與分享。
- **逐幀標註** — 在任意幀上繪製箭頭、圓圈、矩形、自由筆觸或文字，匯出為全解析度 PNG。

### 音訊降噪增強

- **降噪** — 高通濾波去隆隆聲 + 噪聲門（本底自適應估計）+ 峰值歸一化。
- **全程本地** — 增強後的音訊寫入 M4A 並 mux 回影片。

### 調色與濾鏡

- **7 參數調色** — 曝光、亮度、對比度、飽和度、自然飽和度、色溫、色調，透過 Core Image 濾鏡鏈實現。即時預覽 + 按住查看原圖。
- **內建 LUT 包** — 6 種程式化生成的調色風格：青橙、漂白、復古、冷影、暖影、高反黑白（17³ CIColorCube，零資源檔案）。
- **濾鏡預設** — 11 種內建預設（CIPhotoEffect 8 種 + 暖色/冷色 + 青橙電影），支援匯入 `.cube` 3D LUT 檔案（Adobe/Resolve 格式）。

### 變速曲線與去靜音跳剪

- **關鍵幀變速曲線** — 將時間線分段，為每段設定不同速度，色帶式視覺化編輯器。
- **自動去靜音跳剪** — 透過 RMS 窗口 + 自適應閾值 + 形態學閉運算偵測靜音段。Canvas 視覺化展示保留/移除片段。

### 卡點混剪

- **節拍偵測** — 能量包絡 onset 差分 + 自適應閾值計算 BPM。
- **自動混剪** — 畫面隨節拍跳切，音樂連續。可疊加多種轉場：縮放、滑入、閃白、黑場。

### 社媒畫幅與前後對比

- **社媒畫幅預設** — 9:16 / 1:1 / 4:5 / 16:9，支援模糊背景、純色邊或裁剪填滿。即時單幀預覽 + 安全區參考線。可選字幕條（頂/底）+ 半透明色條。
- **前後對比拼屏** — 左右或上下拼屏，分隔線 + Before/After 標籤。

### 示波器

- **RGB 直方圖與亮度波形** — 對當前幀進行 CPU 取樣分析，Canvas 繪製展示。

### 播放體驗

- **鍵盤快捷鍵** — Space（播放/暫停）、方向鍵（逐幀/跳 10 秒）、`,` `.`（逐幀）、**JKL**（FCP 風格快退快進：1× → 2× → 4× → 8×）。
- **JKL HUD** — 螢幕中央膠囊浮窗，顯示目前速度與方向，按速度檔差異化顯示時長後自動淡出。
- **JKL 靈動島** — 鎖定畫面與靈動島即時顯示目前 JKL 速度檔（iOS 16.1+）。
- **自訂速度** — 滑桿 0.1×–8× + 8 檔預設 + 最近用過 2 檔（LRU）+ iPhone 雙指捏合調速。
- **速度檔膠囊** — 即時顯示含 JKL 正負號的實際播放速度；長按 0.5 秒直達自訂速度面板。
- **反向警示** — 倒放時 scrubber 軌道由白轉紅。
- **Scrubber 縮圖** — 拖動進度條時懸浮縮圖預覽（60 段分桶，三級快取）。
- **音訊波形** — 時長裁剪工具顯示音訊波形視覺化。
- **水平滑動快進** — 在預覽區左右滑動即可 seek，方向鎖定 + 短長影片自適應覆蓋時長。
- **AirPlay 與子母畫面** — 投放至外部顯示器或使用子母畫面繼續播放。
- **跨工作階段偏好** — 播放速度與靜音狀態跨工作階段保留並透過 iCloud 同步。

### 影片拼接與拼圖

- **影片拼接** — 多段影片首尾拼接，可選交叉淡化轉場。
- **影片拼圖** — 將 2–4 個影片合為一畫面（左右 / 上下 / 四宮格），輸出 1920×1080。

### Live Photo 工作室

- **影片轉 Live Photo** — 選擇關鍵幀與時長，建立 Live Photo 桌布。
- **Live Photo 轉影片/GIF/靜圖** — 批次轉換，保留原始編碼。
- **批次模式** — 多選 Live Photo 批次轉換。

### 匯出

| 檔位 | 解析度 |
|------|--------|
| 原畫 | 來源解析度 |
| 超高清 | 4K |
| 超清 | 2K |
| 高清 | 1080p |
| 標清 | 720p |
| 省流 | 540p |

- 支援 MP4 與 MOV 格式匯出。
- **匯出預設** — 4 個內建預設 + 自訂預設（畫質 + 容器），可在工作台選單或設定中一鍵切換。
- **全域匯出佇列** — 後台串行處理，進度即時追蹤。佇列檢視展示排隊中、進行中、已完成與失敗的任務。iOS 後台任務保持匯出持續運行。
- **匯出完成通知** — 匯出完成後可選本地通知提醒（在設定中配置）。

### 使用說明

- **內建幫助** — 設定 → 幫助：Hero 卡片 + 上手步驟 + 全部工具速查 + 旗艦能力 + 權限說明 + 摺疊式 FAQ。
- **重看引導** — 在設定中重新查看首啟引導，不會重設您的資料。

### Siri 與捷徑

- **AppShortcuts** — 透過 Siri 或「捷徑」App 直接開始錄屏、開啟影片庫或啟動 Live Photo 工具。

### iCloud 同步

- 基於 `NSUbiquitousKeyValueStore` 的輕量偏好同步：主題、語言、播放速度、靜音狀態、自訂速度檔歷史與常用工具快捷列——在所有裝置間自動同步。

### 其他

- **隱私優先** — 所有影片處理在裝置本地完成。無雲端、無分析、無追蹤、無帳號。語音辨識、人臉偵測、OCR、翻譯——全部強制裝置端運行。
- **暗色優先** — 工作台採用暗色主題，專為沉浸式影片編輯設計。
- **3 種語言** — 英文、簡體中文、繁體中文，應用內即時切換無需重新啟動。
- **打賞** — 可選應用內打賞支持開發。
- **關於頁面** — Hero 卡片展示應用資料、產品亮點，一鍵評分、分享或回饋。

## 系統需求

| 平台 | 最低版本 |
|------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |

## 聯絡我們

如有問題、回饋或需要協助，請聯絡：

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我們通常在 48 小時內回覆。

[常見問題](faq) · [隱私政策](privacy)

</section>
