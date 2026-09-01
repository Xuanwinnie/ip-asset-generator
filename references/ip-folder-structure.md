# 建議的 IP 資料夾結構

IP 資料夾不是必要條件。Skill 可以接受分散提供的檔案，但以下結構有助於後續檢查、版本管理與重複生成：

```text
dodo-cat/
├── ip_bible.yaml
├── references/
│   ├── front.png
│   ├── three-quarter.png
│   ├── side.png
│   ├── back.png
│   ├── expressions-neutral.png
│   ├── expressions-happy.png
│   ├── poses-standing.png
│   ├── accessory-neckerchief.png
│   └── palette.png
├── examples/
│   └── approved-assets/
└── README.md
```

## 建議檔案

- `ip_bible.yaml`：已確認的身份錨點、固定規則、可變元素、視覺語言與素材預設值。
- `references/`：IP 的視覺參考資料。建議依序提供正面、四分之三、側面與背面圖，再補充表情、姿勢、配件與色彩／材質參考。
- `examples/approved-assets/`：已核准的生成結果，用來示範品質與視覺處理方式。它們是範例，不可取代角色身份參考圖。
- `README.md`：可選的人類閱讀說明、來源註記、使用限制與待確認事項。

## 命名規則

資料夾名稱與檔案名稱建議使用英文，讓素材能在不同影像工具、腳本與作業系統中穩定使用。檔名使用小寫，以 hyphen 取代空格，並採用固定的視角或用途名稱：

```text
front.png
three-quarter.png
side.png
back.png
expression-neutral.png
pose-waving.png
accessory-neckerchief.png
palette.png
```

不要求使用者重新命名既有檔案。如果資料夾使用 `font.png`、`正面.png` 或任意匯出檔名，應檢查圖片內容；若無法確認視角，標記為不確定。不可只根據檔名推測缺少的固定特徵。

檔案內容不需要使用英文。角色描述、固定規則、視覺語言、README 說明與待確認事項都可以使用繁體中文或其他語言。

## 實務規則

- 每個視角盡量保留一份 canonical 參考圖；不同版本加上清楚的後綴，例如 `front-neutral.png` 或 `front-smile.png`。
- 將原始參考圖與生成結果分開存放。
- 角色參考圖與透明素材優先使用無損 PNG。
- 未確認的細節應在 IP Bible 中標記為 `needs_confirmation`。
- 不要將密鑰、私人憑證或無關的個人檔案放入 IP 資料夾。
- 資料夾結構是推薦規範，不是必要格式；單張圖片或獨立的 IP Bible 仍然是有效輸入。
