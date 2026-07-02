---
layout: doc
title: TwinPolarCam — FAQ
app_id: TwinPolarCam
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about TwinPolarCam.
---

<section lang="en" markdown="1">

### Which iPhones support TwinPolarCam?

TwinPolarCam requires a device with Apple's multi-camera capture capability (`AVCaptureMultiCamSession`). This includes iPhone XS, iPhone XR and all later models. Older devices that lack multi-camera hardware cannot run the app. A real device is required — the iOS Simulator does not support camera capture.

### What is the maximum recording resolution?

The maximum resolution depends on your device hardware. TwinPolarCam offers 720p, 1080p, 2K and 4K options. On newer iPhones (iPhone 12 and later), 4K dual-camera recording is generally available. On older supported models, the maximum may be limited to 1080p or 2K. The app automatically disables resolutions your device cannot support.

### Can I customize the PiP overlay?

Yes. You can:

- **Drag** the PiP window to any position on screen.
- **Pinch** to resize the PiP window.
- Adjust **border width**, **border color**, **corner radius**, **opacity** and **relative size** in the PiP settings.

All PiP customizations apply in real time during recording and are reflected in the final composited video.

### What happens if I receive a phone call during recording?

TwinPolarCam includes an Interruption Coordinator that monitors audio, capture and app-level events. When an interruption occurs (such as a phone call), the current recording segment is automatically finalized and saved. After the interruption ends, you can resume recording — a new segment will be created. All segments are composited together during export.

### How does crash recovery work?

If the app terminates unexpectedly during recording, any previously finalized segments are preserved on disk. When you relaunch TwinPolarCam, it detects these recovered segments and offers to export them. This ensures that even in the event of a crash, you do not lose all of your recorded footage.

### What export options are available?

TwinPolarCam offers two export modes:

- **Auto export** — The app automatically composites and saves the video to your photo library as soon as you stop recording.
- **Manual export** — After stopping, you can review the recording before choosing to export. This gives you a chance to discard unwanted takes.

The **Pending Exports Manager** lists exports waiting in the queue — retry a failed job, export when ready, or discard takes you no longer need.

Failure detection is built in: if export fails, the error is categorized and reported so you can retry or troubleshoot.

### What is preview pause?

**Preview pause** freezes the live camera preview while a recording session can continue (or while you adjust settings) — useful when you need a steady frame to reposition the PiP overlay or change zoom without the preview jumping around.

### How do zoom presets work?

Pinch or use the on-screen zoom control as usual, then save the current zoom level as a **preset**. Recall presets from the control panel to reframe quickly between front and back cameras during a session.

### Why is 60 fps not available?

Dual-camera simultaneous recording places extremely high demands on the device's ISP, CPU and thermal budget. Apple's `AVCaptureMultiCamSession` currently limits dual-camera capture to 30 fps maximum. To provide a stable and reliable recording experience, TwinPolarCam offers 24 fps and 30 fps. Supporting 60 fps would require future hardware or system-level improvements from Apple.

### Can I run TwinPolarCam on the iOS Simulator?

No. The iOS Simulator does not provide access to physical camera hardware and does not support `AVCaptureMultiCamSession`. TwinPolarCam requires a real iPhone to function. If you launch the app on a Simulator, camera initialization will fail.

### How do I switch which camera is the main view?

During recording or preview, tap the camera switch button on the control panel. This swaps the front and back camera roles — the current main camera becomes the PiP overlay and vice versa. The switch is seamless and does not interrupt recording.

### Still need help?

Contact us at [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) and we will get back to you within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

### 哪些 iPhone 支持太极双摄？

太极双摄需要支持 Apple 多摄像头采集功能（`AVCaptureMultiCamSession`）的设备，包括 iPhone XS、iPhone XR 及之后所有机型。缺少多摄像头硬件的旧设备无法运行本应用。需要真机——iOS 模拟器不支持相机采集。

### 最高录制分辨率是多少？

最高分辨率取决于你的设备硬件。太极双摄提供 720p、1080p、2K 和 4K 选项。较新的 iPhone（iPhone 12 及之后）通常可使用 4K 双摄录制。较旧的支持机型可能最高限制为 1080p 或 2K。应用会自动禁用你的设备不支持的分辨率。

### 可以自定义画中画吗？

可以。你可以：

- **拖拽**画中画窗口到屏幕任意位置。
- **双指缩放**调整画中画窗口大小。
- 在画中画设置中调整**边框宽度**、**边框颜色**、**圆角半径**、**不透明度**和**相对大小**。

所有画中画自定义都在录制过程中实时生效，并反映在最终合成视频中。

### 录制期间接到电话会怎样？

太极双摄内置中断协调器，监控音频、采集和应用层面事件。当发生中断（如来电）时，当前录制片段会自动定稿并保存。中断结束后，你可以继续录制——会创建一个新片段。导出时所有片段会一起合成。

### 崩溃恢复是怎么工作的？

如果应用在录制过程中意外终止，之前已定稿的片段会保留在磁盘上。重新启动太极双摄后，应用会检测到这些恢复的片段并提供导出选项。这确保即使发生崩溃，你也不会丢失所有已录制的素材。

### 有哪些导出选项？

太极双摄提供两种导出模式：

- **自动导出** — 停止录制后，应用自动合成并将视频保存到相册。
- **手动导出** — 停止后，你可以先预览录制内容再选择是否导出。这样可以丢弃不需要的素材。

**待导出管理**会列出队列中的导出任务——可重试失败项、就绪后再导出，或丢弃不需要的素材。

内置故障检测：如果导出失败，错误会被分类并上报，便于重试或排查问题。

### 什么是预览暂停？

**预览暂停**会冻结实时相机预览（录制会话可继续进行，或便于你调整设置）——适合在调整画中画位置或变焦时保持画面稳定。

### 缩放预设怎么用？

双指捏合或使用屏幕缩放控件后，可将当前缩放级别保存为 **预设**。在控制面板中快速调用预设，在前后摄像头之间迅速重新构图。

### 为什么没有 60 fps？

双摄同时录制对设备的 ISP、CPU 和散热有极高要求。Apple 的 `AVCaptureMultiCamSession` 目前将双摄采集限制在最高 30 fps。为了提供稳定可靠的录制体验，太极双摄提供 24 fps 和 30 fps。60 fps 的支持需要未来 Apple 在硬件或系统层面的改进。

### 可以在 iOS 模拟器上运行太极双摄吗？

不可以。iOS 模拟器无法访问物理相机硬件，也不支持 `AVCaptureMultiCamSession`。太极双摄需要真实的 iPhone 才能运行。如果在模拟器上启动应用，相机初始化会失败。

### 如何切换主画面的摄像头？

在录制或预览期间，点按控制面板上的摄像头切换按钮。前后摄像头角色会互换——当前的主摄像头变为画中画，反之亦然。切换是无缝的，不会中断录制。

### 仍需帮助？

发邮件到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我们会在 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

### 哪些 iPhone 支援太極雙攝？

太極雙攝需要支援 Apple 多鏡頭擷取功能（`AVCaptureMultiCamSession`）的裝置，包括 iPhone XS、iPhone XR 及之後所有機型。缺少多鏡頭硬體的舊裝置無法執行本應用。需要實機——iOS 模擬器不支援相機擷取。

### 最高錄製解析度是多少？

最高解析度取決於你的裝置硬體。太極雙攝提供 720p、1080p、2K 和 4K 選項。較新的 iPhone（iPhone 12 及之後）通常可使用 4K 雙攝錄製。較舊的支援機型可能最高限制為 1080p 或 2K。應用會自動停用你的裝置不支援的解析度。

### 可以自訂子母畫面嗎？

可以。你可以：

- **拖曳**子母畫面窗口到螢幕任意位置。
- **雙指縮放**調整子母畫面窗口大小。
- 在子母畫面設定中調整**邊框寬度**、**邊框顏色**、**圓角半徑**、**不透明度**和**相對大小**。

所有子母畫面自訂都在錄製過程中即時生效，並反映在最終合成影片中。

### 錄製期間接到電話會怎樣？

太極雙攝內建中斷協調器，監控音訊、擷取和應用層面事件。當發生中斷（如來電）時，目前錄製片段會自動定稿並儲存。中斷結束後，你可以繼續錄製——會建立一個新片段。匯出時所有片段會一起合成。

### 當機恢復是怎麼運作的？

如果應用在錄製過程中意外終止，之前已定稿的片段會保留在磁碟上。重新啟動太極雙攝後，應用會偵測到這些恢復的片段並提供匯出選項。這確保即使發生當機，你也不會遺失所有已錄製的素材。

### 有哪些匯出選項？

太極雙攝提供兩種匯出模式：

- **自動匯出** — 停止錄製後，應用自動合成並將影片儲存到相簿。
- **手動匯出** — 停止後，你可以先預覽錄製內容再選擇是否匯出。這樣可以捨棄不需要的素材。

**待匯出管理**會列出佇列中的匯出任務——可重試失敗項、就緒後再匯出，或捨棄不需要的素材。

內建故障偵測：如果匯出失敗，錯誤會被分類並回報，便於重試或排查問題。

### 什麼是預覽暫停？

**預覽暫停**會凍結即時相機預覽（錄製工作階段可繼續進行，或便於你調整設定）——適合在調整子母畫面位置或縮放時保持畫面穩定。

### 縮放預設怎麼用？

雙指捏合或使用螢幕縮放控制元件後，可將目前縮放級別儲存為 **預設**。在控制面板中快速呼叫預設，在前後鏡頭之間迅速重新構圖。

### 應用內有繁體中文嗎？

沒有。太極雙攝 App 介面僅提供**英文**與**簡體中文**字串，不含繁體中文介面。本常見問題頁為繁體中文支援說明。

### 為什麼沒有 60 fps？

雙攝同時錄製對裝置的 ISP、CPU 和散熱有極高要求。Apple 的 `AVCaptureMultiCamSession` 目前將雙攝擷取限制在最高 30 fps。為了提供穩定可靠的錄製體驗，太極雙攝提供 24 fps 和 30 fps。60 fps 的支援需要未來 Apple 在硬體或系統層面的改進。

### 可以在 iOS 模擬器上執行太極雙攝嗎？

不可以。iOS 模擬器無法存取實體相機硬體，也不支援 `AVCaptureMultiCamSession`。太極雙攝需要真實的 iPhone 才能執行。如果在模擬器上啟動應用，相機初始化會失敗。

### 如何切換主畫面的鏡頭？

在錄製或預覽期間，點按控制面板上的鏡頭切換按鈕。前後鏡頭角色會互換——目前的主鏡頭變為子母畫面，反之亦然。切換是無縫的，不會中斷錄製。

### 仍需協助？

寄信到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我們會在 48 小時內回覆。

</section>
