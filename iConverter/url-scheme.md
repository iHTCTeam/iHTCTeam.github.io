---
layout: default
title: iConverter - URL Scheme Reference
---

# iConverter URL Scheme 深度链接文档

[Back to iConverter Support](./)

本文档列出 iConverter（爱计算）App 支持的全部 `iconverter://` URL Scheme，可从外部 App、网页、二维码、Safari、桌面快捷指令等途径一键打开指定工具，并可携带 query 参数自动预填输入框。

---

## 协议规范 | 協議規範 | Protocol Specification

```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```

- `<ToolItem.rawValue>` 与小组件深度链接共用同一套命名 | 與小組件深度連結共用同一套命名 | Shared naming with widget deep links
- 参数键名支持短键与同义别名二选一，例如 `text` 与 `input` 等效 | 參數鍵名支援短鍵與同義別名 | Short keys and aliases are interchangeable
- 布尔参数：`1/true/yes/on` → true；`0/false/no/off` → false
- 日期参数：支持 `yyyy-MM-dd`、ISO8601、Unix 时间戳（秒）| 支援多種日期格式 | Supports multiple date formats
- 单位换算通用：`v`=数值，`from`=源单位（rawValue 或 symbol，大小写不敏感），`to`=目标单位 | 單位換算通用格式 | Universal unit converter format

---

## 1. 计算器 | 計算器 | Calculator

**标准计算器 | 標準計算器 | Calculator** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/calculator
```

**科学计算器 | 科學計算器 | Scientific Calculator** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/scientific
```

**程序员计算器 | 程式設計師計算器 | Programmer Calculator** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/programmer
```

---

## 2. 财务 | 財務 | Finance

**房贷计算器 | 房貸計算器 | Mortgage Calculator**
`p`=贷款金额 | 貸款金額 | loan amount，`r`=年利率% | 年利率% | annual rate%，`y`=年数 | 年數 | years，`mode`=还款方式 0=等额本息/1=等额本金 | 0=等額本息/1=等額本金 | 0=equal installment/1=equal principal

```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```

**个人所得税 | 個人所得稅 | Income Tax**
`salary`=月工资 | 月薪 | monthly salary，`insurance`=社保公积金 | 社保公積金 | social insurance，`deduction`=专项扣除 | 專項扣除 | special deduction，`threshold`=起征点 | 起徵點 | threshold，`bonus`=年终奖 | 年終獎 | annual bonus

```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```

**复利计算 | 複利計算 | Compound Interest**
`p`=本金 | 本金 | principal，`m`=月定投 | 月定投 | monthly contribution，`r`=年利率% | 年利率% | annual rate%，`y`=年数 | 年數 | years，`freq`=复利频率 0=年/1=月/2=日 | 0=年/1=月/2=日 | 0=annual/1=monthly/2=daily，`i`=通胀率% | 通脹率% | inflation%

```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```

**折扣计算 | 折扣計算 | Discount Calculator**
`mode`=模式 0–4 | 模式 | mode，`p`=原价 | 原價 | original price，`r`=折扣率 | 折扣率 | discount ratio，`t`=满减门槛 | 滿減門檻 | threshold，`u`=减免金额 | 減免金額 | reduction amount

```
iconverter://tool/discount?mode=0&p=299&r=8.5
```

满减示例 | 滿減範例 | Full-minus example:

```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```

**小费/AA | 小費/AA | Tip & AA Split**
`mode`=0=小费/1=AA | 0=小費/1=AA | 0=tip/1=AA split，`bill`=账单 | 帳單 | bill，`tip`=小费% | 小費% | tip%，`tax`=税率% | 稅率% | tax%，`ppl`=人数 | 人數 | people count

```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```

**提前还款 | 提前還款 | Mortgage Prepayment**
`p`=原贷款额 | 原貸款額 | original loan，`r`=年利率% | 年利率% | annual rate%，`total`=总期数(年) | 總期數(年) | total term(years)，`paid`=已还期数 | 已還期數 | paid terms，`prepay`=提前还款额 | 提前還款額 | prepay amount，`mode`=方案 0=缩期/1=减月供/2=对比 | 0=縮期/1=減月供/2=對比 | 0=shorten/1=reduce/2=compare

```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```

**二手房税费 | 二手房稅費 | Real Estate Tax** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/realEstateTax
```

---

## 3. 日期时间 | 日期時間 | Date & Time

**年龄/纪念日 | 年齡/紀念日 | Age & Anniversary**
`birth`=生日 yyyy-MM-dd | 生日 | birthday，`ref`=参考日期 | 參考日期 | reference date

```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```

**日期计算 | 日期計算 | Date Arithmetic**
`mode`=0=日期加减/1=两日期差 | 0=日期加減/1=兩日期差 | 0=add-subtract/1=difference

加减模式 | 加減模式 | Add-subtract mode（`d1`=起始日期，`d`=±天数，`w`=±周，`mo`=±月，`y`=±年）:

```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```

差值模式 | 差值模式 | Difference mode（`d1`=日期1，`d2`=日期2）:

```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```

**农历查询 | 農曆查詢 | Lunar Calendar**
`date`=公历日期 yyyy-MM-dd | 公曆日期 | Gregorian date

```
iconverter://tool/lunarCalendar?date=2026-05-17
```

**节气 | 節氣 | Solar Terms** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/solarTerms
```

**倒计时 | 倒計時 | Countdown**
`label`=事件名 | 事件名 | event name，`target`=目标日期 yyyy-MM-dd | 目標日期 | target date，`time`=含时分 0/1 | 含時分 | include time

```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```

**孕期计算 | 孕期計算 | Pregnancy Calculator**
`method`=方式 0=末次月经/1=受孕日/2=IVF | 0=末次月經/1=受孕日/2=IVF | 0=LMP/1=conception/2=IVF，`ref`=日期，`ivf`=IVF胚胎天数 0=D3/1=D5

```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```

```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```

**月经周期 | 月經週期 | Menstrual Cycle**
`lmp`=末次月经日期 | 末次月經日期 | LMP date，`cycle`=周期天数 | 週期天數 | cycle days，`period`=行经天数 | 行經天數 | period days

```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```

**世界时钟 | 世界時鐘 | World Clock**
`q`=城市搜索关键词 | 城市搜尋 | city search，`now`=使用当前时间 0/1 | 使用當前時間 | use current time，`ref`=自定义时间 | 自訂時間 | custom datetime

```
iconverter://tool/worldClock?q=Tokyo
```

```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```

**星座 | 星座 | Zodiac** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/zodiac
```

---

## 4. 数学 | 數學 | Math

**百分比计算 | 百分比計算 | Percentage Calculator**
`mode`=模式 0–4 | 模式 | mode，`a`=数值A | 數值A | value A，`b`=数值B | 數值B | value B

```
iconverter://tool/percentage?mode=0&a=75&b=120
```

**分数计算 | 分數計算 | Fraction Calculator** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/fraction
```

**质因数分解 | 質因數分解 | Prime Factorization** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/primeFactor
```

**一元二次方程 | 一元二次方程 | Quadratic Solver** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/quadraticSolver
```

**统计计算 | 統計計算 | Statistics**
`data`=数据集，空格/逗号/分号分隔 | 資料集，空格/逗號/分號分隔 | dataset, space/comma/semicolon separated

```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```

**排列组合 | 排列組合 | Combinations & Permutations** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/combinations
```

**几何计算 | 幾何計算 | Geometry**
`shape`=形状 | 形狀 | shape，`v1`/`v2`/`v3`=各边参数 | 各邊參數 | dimension params

可选形状 | 可選形狀 | Available shapes: `rectangle` · `square` · `circle` · `triangle` · `triangleSSS` · `parallelogram` · `trapezoid` · `sector` · `ellipse` · `regularPolygon` · `sphere` · `hemisphere` · `cylinder` · `cone` · `frustum` · `cube` · `cuboid`

圆形 | 圓形 | Circle（`v1`=半径 | 半徑 | radius）:

```
iconverter://tool/geometry?shape=circle&v1=5
```

矩形 | 矩形 | Rectangle（`v1`=长 | 長 | length，`v2`=宽 | 寬 | width）:

```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```

球体 | 球體 | Sphere（`v1`=半径 | 半徑 | radius）:

```
iconverter://tool/geometry?shape=sphere&v1=3
```

圆柱 | 圓柱 | Cylinder（`v1`=半径，`v2`=高 | 高 | height）:

```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```

---

## 5. 编码 | 編碼 | Encoding

**罗马数字 | 羅馬數字 | Roman Numeral**
`n`=阿拉伯数字(1–3999) | 阿拉伯數字 | Arabic number；或 `roman`=罗马数字字符串 | 羅馬數字字串 | Roman numeral string

```
iconverter://tool/roman?n=2026
```

```
iconverter://tool/roman?roman=MMXXVI
```

**Base64 编解码 | Base64 編解碼 | Base64 Encoder / Decoder**
`mode`=encode/decode，`urlSafe`=URL安全模式 0/1 | URL安全模式 | URL-safe mode，`text`=输入文本 | 輸入文字 | input text

```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```

```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```

**URL 编解码 | URL 編解碼 | URL Encoder / Decoder**
`mode`=encode/decode，`comp`=component模式 0=全部/1=查询参数/2=路径 | 0=全部/1=查詢/2=路徑 | 0=full/1=query/2=path，`text`=输入 | 輸入 | input

```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```

```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```

**哈希计算 | 雜湊計算 | Hash Calculator**
`text`=输入文本 | 輸入文字 | input，`algo`=算法 md5/sha1/sha256/sha512 | 演算法 | algorithm，`upper`=大写输出 0/1 | 大寫輸出 | uppercase，`hmac`=启用HMAC 0/1 | 啟用HMAC | enable HMAC，`key`=HMAC密钥 | HMAC金鑰 | HMAC key

```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```

```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```

**字数统计 | 字數統計 | Word Count**
`text`=待统计文本 | 待統計文字 | text to analyze

```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```

**颜色换算 | 顏色換算 | Color Converter**
`hex`=十六进制颜色 | 十六進制顏色 | hex color；或 `r`/`g`/`b`=RGB分量(0–255) | RGB分量 | RGB components

```
iconverter://tool/colorConverter?hex=%23FF8800
```

```
iconverter://tool/colorConverter?r=255&g=136&b=0
```

**色板 | 色板 | Color Palette** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/colorPalette
```

**二维码 | 二維碼 | QR Code**
`text`=内容 | 內容 | content，`format`=格式 qr/aztec/code128/pdf417 等 | 格式 | format，`ecc`=纠错级别 L/M/Q/H | 糾錯等級 | error correction level

```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```

```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```

**JSON 格式化 | JSON 格式化 | JSON Formatter**
`text`=JSON字符串(需URL编码) | JSON字串(需URL編碼) | JSON string (URL-encoded)，`indent`=缩进空格数 2/4 | 縮排空格數 | indent spaces

```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```

**时间戳 | 時間戳 | Timestamp**
`ts`=Unix时间戳(秒) | Unix時間戳(秒) | Unix timestamp (seconds)，`u`=单位 0=秒/1=毫秒 | 0=秒/1=毫秒 | unit 0=sec/1=ms；或 `iso`=ISO8601日期字符串 | ISO8601日期字串 | ISO8601 date string

```
iconverter://tool/timestamp?ts=1747440000
```

```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```

**银行卡号 | 銀行卡號 | Bank Card Validator**
`num`=银行卡号 | 銀行卡號 | card number

```
iconverter://tool/bankCard?num=6214830172816734
```

**文本大小写 | 文字大小寫 | Text Case Converter**
`text`=输入文本 | 輸入文字 | input text

```
iconverter://tool/textCase?text=hello+world+from+iConverter
```

**文本对比 | 文字比對 | Text Diff** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/textDiff
```

**HTTP 请求 | HTTP 請求 | HTTP Request**
`url`=请求URL | 請求URL | request URL，`method`=GET/POST/PUT/PATCH/DELETE，`body`=请求体 | 請求體 | request body，`bodyKind`=body类型 json/form/text | body類型 | body kind，`headers`=请求头JSON | 請求頭JSON | headers JSON

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```

**文件下载 | 檔案下載 | File Download**
`url`=下载链接 | 下載連結 | download URL，`name`=保存文件名(可选) | 儲存檔名(可選) | filename (optional)

```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```

**HTTP 状态码 | HTTP 狀態碼 | HTTP Status Codes**
`code`=状态码 | 狀態碼 | status code；或 `q`=搜索关键词 | 搜尋關鍵詞 | search keyword

```
iconverter://tool/httpStatusCodes?code=404
```

```
iconverter://tool/httpStatusCodes?q=redirect
```

**IP 工具 | IP 工具 | IP Utility**
`mode`=subnet/cidr/range，`ip`=IP地址 | IP地址 | IP address，`mask`=子网掩码 | 子網路遮罩 | subnet mask；或 `prefix`=CIDR前缀长度 | CIDR前綴 | prefix length

```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```

```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```

**ASCII 码表 | ASCII 碼表 | ASCII Table**
`dec`=十进制码点 | 十進制碼點 | decimal codepoint；或 `hex`=十六进制 | 十六進制 | hex codepoint；或 `q`=搜索 | 搜尋 | search

```
iconverter://tool/asciiTable?dec=65
```

```
iconverter://tool/asciiTable?q=space
```

**密码生成器 | 密碼產生器 | Password Generator**
`length`=长度 | 長度 | length，`upper`=大写 0/1，`lower`=小写 0/1，`digits`=数字 0/1，`symbols`=符号 0/1，`unambiguous`=排除歧义字符 0/1 | 排除歧義字元 | no ambiguous chars，`go`=立即生成 1 | 立即產生 | generate immediately

```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```

**随机数生成 | 亂數產生 | Random Number Generator**
`min`=最小值，`max`=最大值，`n`=数量 | 數量 | count，`decimals`=小数位 | 小數位 | decimal places，`unique`=不重复 0/1 | 不重複 | unique，`sort`=排序 0=不排/1=升序/2=降序 | 0=不排/1=升序/2=降序 | 0=none/1=asc/2=desc，`go`=立即生成 1 | 立即產生 | generate immediately

```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```

```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```

**摩斯电码 | 摩斯電碼 | Morse Code**
`mode`=encode/decode，`text`=输入文本 | 輸入文字 | input text

```
iconverter://tool/morseCode?mode=encode&text=SOS
```

```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```

**JWT 解码 | JWT 解碼 | JWT Decoder**
`token`=JWT令牌字符串 | JWT令牌字串 | JWT token string

```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Cron 表达式 | Cron 表達式 | Cron Expression Parser**
`expr`=Cron表达式（空格可用 `+` 代替）| Cron表達式 | Cron expression (spaces as `+`)

```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```

```
iconverter://tool/cronParser?expr=0+0+*+*+*
```

**正则测试 | 正則測試 | Regex Tester**
`pattern`=正则表达式(需URL编码) | 正則表達式(需URL編碼) | regex pattern (URL-encoded)，`haystack`=测试文本 | 測試文字 | test text，`replacement`=替换内容 | 取代內容 | replacement，`i`=忽略大小写 0/1 | 忽略大小寫 | case-insensitive，`m`=多行 0/1 | 多行 | multiline，`s`=点匹配换行 0/1 | 點匹配換行 | dotall

```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```

```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```

**网页工具 | 網頁工具 | Web Browser**
`url`=直接打开URL | 直接開啟URL | open URL directly；或 `q`=搜索关键词（使用默认搜索引擎）| 搜尋關鍵詞（使用預設搜尋引擎）| search query (uses default search engine)

```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```

```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```

---

## 6. 生活 | 生活 | Lifestyle

**BMI 计算 | BMI 計算 | BMI Calculator**
`h`=身高cm | 身高cm | height cm，`w`=体重kg | 體重kg | weight kg，`std`=标准 0=中国成人/1=WHO | 0=中國成人/1=WHO | standard 0=Chinese/1=WHO

```
iconverter://tool/bmi?h=175&w=70&std=0
```

**基础代谢率 | 基礎代謝率 | BMR Calculator**
`h`=身高cm，`w`=体重kg，`age`=年龄 | 年齡 | age，`sex`=性别 m=男/f=女 | 性別 m/f | sex m=male/f=female，`act`=活动指数 0–4 | 活動指數 0–4 | activity level 0–4，`formula`=公式 0=Harris-Benedict/1=Mifflin-St Jeor | 公式 | formula

```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```

**服装尺码 | 服裝尺碼 | Clothing Size** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/clothingSize
```

**戒指尺码 | 戒指尺碼 | Ring Size** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/ringSize
```

**身高换算 | 身高換算 | Height Converter** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/heightConverter
```

**油费计算 | 油費計算 | Fuel Cost Calculator**
`unit`=单位 0=公制/1=英制 | 0=公制/1=英制 | 0=metric/1=imperial，`d`=行驶距离 | 行駛距離 | distance，`c`=百公里油耗 | 每百公里油耗 | consumption per 100km，`p`=油价 | 油價 | fuel price，`n`=人数 | 人數 | people

```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```

**运费计算 | 運費計算 | Shipping Fee Calculator**
`w`=实重kg | 實重kg | actual weight，`fw`=首重kg | 首重kg | first weight，`ff`=首重费用 | 首重費用 | first-weight fee，`sw`=续重步长kg | 續重步長kg | step weight，`sf`=续重费用 | 續重費用 | step fee

```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```

含体积重 | 含體積重 | With volumetric weight（`vol`=启用 0/1，`l`/`wd`/`h`=三边cm，`div`=抛比）:

```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```

**酒精血液浓度 | 酒精血液濃度 | Blood Alcohol Content (BAC)**
`sex`=性别 m=男/f=女 | 性別 m/f | sex，`w`=体重kg，`v`=饮酒量mL | 飲酒量mL | volume mL，`abv`=酒精度% | 酒精度% | ABV%，`h`=饮酒后小时数 | 飲酒後小時數 | hours since drinking

```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```

**亲戚称呼 | 親戚稱呼 | Relationship**
`chain`=关系链逗号分隔 | 關係鏈逗號分隔 | relationship chain (comma-separated)，`sex`=本人性别 0=男/1=女 | 0=男/1=女 | ego sex 0=male/1=female，`reverse`=显示互称 0/1 | 顯示互稱 | show reverse

```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```

```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```

**身份证查询 | 身份證查詢 | ID Card Parser**
`id`=身份证号码 | 身份證號碼 | ID card number

```
iconverter://tool/idCard?id=110101199003073010
```

**抛硬币 | 拋硬幣 | Coin Flip** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/coinFlip
```

**骰子模拟 | 骰子模擬 | Dice Roller** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/diceRoller
```

**随机抽签 | 隨機抽籤 | Random Draw** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/randomDraw
```

**转盘抽奖 | 轉盤抽獎 | Spin Wheel** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/spinWheel
```

**视频关键帧 | 視頻關鍵幀 | Video Frame Export** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/videoFrameExport
```

---

## 7. 传感器 | 感測器 | Sensors

**指南针 | 指南針 | Compass** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/compass
```

**水平仪 | 水平儀 | Level** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/level
```

**海拔仪 | 海拔儀 | Altitude** — 仅打开 | 僅開啟 | Open only

```
iconverter://tool/altitude
```

---

## 8. 中文 | 中文 | Chinese

**大写数字 | 大寫數字 | Chinese Number**
`n`=阿拉伯数字 | 阿拉伯數字 | number

```
iconverter://tool/chineseNumber?n=12345.67
```

**汉字数字反查 | 漢字數字反查 | Chinese Number Reverse**
`text`=汉字数字字符串 | 漢字數字字串 | Chinese numeral string

```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```

**金额大写 | 金額大寫 | Financial Amount**
`amount`=金额 | 金額 | amount，`zheng`=末尾「整」0/1 | 末尾「整」 | append 整 0/1

```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```

---

## 9. 单位换算 | 單位換算 | Unit Converters

通用格式 | 通用格式 | General format：`v`=数值 | 數值 | value，`from`=源单位（rawValue 或 symbol，大小写不敏感）| 來源單位 | source unit，`to`=目标单位 | 目標單位 | target unit

---

**长度 | 長度 | Length**
常用单位 | 常用單位 | Common units：`meter`(m) · `kilometer`(km) · `centimeter`(cm) · `millimeter`(mm) · `foot`(ft) · `inch`(in) · `mile`(mi) · `yard`(yd) · `nauticalMile`(nmi) · `chineseLi`(里) · `chineseChi`(尺)

```
iconverter://tool/length?v=100&from=meter&to=foot
```

```
iconverter://tool/length?v=1&from=mile&to=kilometer
```

**面积 | 面積 | Area**
常用单位 | 常用單位 | Common units：`squareMeter`(m²) · `hectare`(ha) · `acre`(acre) · `squareFoot`(ft²) · `squareMile`(mile²) · `mu`(亩) · `squareKilometer`(km²)

```
iconverter://tool/area?v=1&from=hectare&to=mu
```

```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```

**体积 | 體積 | Volume**
常用单位 | 常用單位 | Common units：`liter`(L) · `milliliter`(mL) · `cubicMeter`(m³) · `gallon`(gal) · `fluidOunce`(fl oz) · `cup`(cup) · `ukGallon`(gal (UK)) · `oilBarrel`(bbl)

```
iconverter://tool/volume?v=1&from=gallon&to=liter
```

```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```

**重量/质量 | 重量/質量 | Weight / Mass**
常用单位 | 常用單位 | Common units：`kilogram`(kg) · `gram`(g) · `pound`(lb) · `ounce`(oz) · `tonne`(t) · `jin`(斤) · `liang`(两) · `carat`(ct)

```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```

```
iconverter://tool/weight?v=1&from=jin&to=gram
```

**温度 | 溫度 | Temperature**
单位 | 單位 | Units：`celsius`(°C) · `fahrenheit`(°F) · `kelvin`(K) · `rankine`(°R) · `reaumur`(°Re)

```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```

```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```

**时间 | 時間 | Time**
常用单位 | 常用單位 | Common units：`second`(s) · `minute`(min) · `hour`(h) · `day`(day) · `week`(wk) · `month`(mo) · `year`(yr) · `millisecond`(ms) · `microsecond`(μs)

```
iconverter://tool/time?v=1&from=hour&to=second
```

```
iconverter://tool/time?v=7&from=day&to=hour
```

**速度 | 速度 | Speed**
单位 | 單位 | Units：`meterPerSecond`(m/s) · `kmPerHour`(km/h) · `milePerHour`(mph) · `knot`(kn) · `mach`(Ma)

```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```

```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```

**压强 | 壓強 | Pressure**
单位 | 單位 | Units：`pascal`(Pa) · `kilopascal`(kPa) · `bar`(bar) · `atmosphere`(atm) · `psi`(psi) · `mmHg`(mmHg)

```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```

```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```

**能量 | 能量 | Energy**
单位 | 單位 | Units：`joule`(J) · `kilojoule`(kJ) · `calorie`(cal) · `kilocalorie`(kcal) · `kilowattHour`(kWh) · `btu`(BTU)

```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```

```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```

**功率 | 功率 | Power**
单位 | 單位 | Units：`watt`(W) · `kilowatt`(kW) · `hpMechanical`(hp) · `hpMetric`(PS) · `btuPerHour`(BTU/h)

```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```

```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```

**力 | 力 | Force**
单位 | 單位 | Units：`newton`(N) · `kilonewton`(kN) · `kgf`(kgf) · `lbf`(lbf) · `dyne`(dyn)

```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```

```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```

**扭矩 | 扭矩 | Torque**
单位 | 單位 | Units：`newtonMeter`(N·m) · `newtonCentimeter`(N·cm) · `kgfMeter`(kgf·m) · `footPound`(ft·lb) · `inchPound`(in·lb)

```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```

**频率 | 頻率 | Frequency**
单位 | 單位 | Units：`hertz`(Hz) · `kilohertz`(kHz) · `megahertz`(MHz) · `gigahertz`(GHz) · `terahertz`(THz) · `rpm`(rpm)

```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```

```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```

**角度 | 角度 | Angle**
单位 | 單位 | Units：`degree`(°) · `radian`(rad) · `gradian`(grad) · `arcminute`(') · `arcsecond`(") · `turn`(turn)

```
iconverter://tool/angle?v=180&from=degree&to=radian
```

```
iconverter://tool/angle?v=1&from=turn&to=degree
```

**数据存储 | 數據儲存 | Data Storage**
单位 | 單位 | Units：`byte`(B) · `kilobyte`(KB) · `megabyte`(MB) · `gigabyte`(GB) · `terabyte`(TB) · `kibibyte`(KiB) · `mebibyte`(MiB) · `gibibyte`(GiB)

```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```

```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```

**数据速率 | 數據速率 | Data Rate**
单位 | 單位 | Units：`bps`(bps) · `kbps`(Kbps) · `mbps`(Mbps) · `gbps`(Gbps) · `kBps`(KB/s) · `mBps`(MB/s) · `gBps`(GB/s)

```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```

```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```

**光照强度 | 照度 | Illuminance**
单位 | 單位 | Units：`lux`(lx) · `footCandle`(fc) · `phot`(ph) · `nox`(nx)

```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```

**磁感应强度 | 磁感應強度 | Magnetic Flux Density**
单位 | 單位 | Units：`tesla`(T) · `millitesla`(mT) · `microtesla`(μT) · `gauss`(G) · `milligauss`(mG)

```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```

**放射性活度 | 放射性活度 | Radioactivity**
单位 | 單位 | Units：`becquerel`(Bq) · `kilobecquerel`(kBq) · `megabecquerel`(MBq) · `curie`(Ci) · `millicurie`(mCi) · `microcurie`(μCi)

```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```

**黏度 | 黏度 | Viscosity**
单位 | 單位 | Units：`pascalSecond`(Pa·s) · `millipascalSecond`(mPa·s) · `poise`(P) · `centipoise`(cP)

```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```

**燃油经济性 | 燃油經濟性 | Fuel Economy**
单位 | 單位 | Units：`lPer100km`(L/100km) · `kmPerL`(km/L) · `mpgUS`(MPG (US)) · `mpgUK`(MPG (UK))

```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```

```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```

**流量 | 流量 | Flow Rate**
单位 | 單位 | Units：`cubicMeterPerSecond`(m³/s) · `cubicMeterPerHour`(m³/h) · `literPerSecond`(L/s) · `literPerMinute`(L/min) · `literPerHour`(L/h) · `usGallonPerMinute`(gpm (US)) · `cubicFootPerMinute`(cfm)

```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```

**密度 | 密度 | Density**
单位 | 單位 | Units：`kgPerCubicMeter`(kg/m³) · `gramPerCubicCentimeter`(g/cm³) · `gramPerLiter`(g/L) · `kgPerLiter`(kg/L) · `poundPerCubicFoot`(lb/ft³)

```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```

**磁通量 | 磁通量 | Magnetic Flux (Wb)**
单位 | 單位 | Units：`weber`(Wb) · `milliweber`(mWb) · `microweber`(μWb) · `kiloweber`(kWb) · `maxwell`(Mx)

```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```

**吸收剂量 | 吸收劑量 | Absorbed Dose**
单位 | 單位 | Units：`gray`(Gy) · `milligray`(mGy) · `microgray`(μGy) · `kilogray`(kGy) · `rad`(rad) · `millirad`(mrad)

```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```

**等效剂量 | 等效劑量 | Equivalent Dose**
单位 | 單位 | Units：`sievert`(Sv) · `millisievert`(mSv) · `microsievert`(μSv) · `rem`(rem) · `millirem`(mrem)

```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```

```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```

**物质的量 | 物質的量 | Amount of Substance**
单位 | 單位 | Units：`mole`(mol) · `millimole`(mmol) · `micromole`(μmol) · `kilomole`(kmol) · `nanomole`(nmol) · `picomole`(pmol)

```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```

```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```

---

[Back to iConverter Support](./) &middot; [FAQ](faq) &middot; [Privacy Policy](privacy)

---

Copyright 2026 iHTCTeam. All rights reserved.
