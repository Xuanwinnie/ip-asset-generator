---
name: ip-asset-generator
description: Generate consistent visual assets for a supplied IP character across different actions, scenes, mobile campaign covers, social graphics, stickers, and transparent character materials. Use when the user wants the same mascot, character, or branded IP to appear repeatedly without identity drift.
---

# IP Asset Generator

Create a new visual asset while preserving the identity of the supplied IP. The character may change action, expression, scene, prop, camera angle, season, and asset format, but its recognizable identity and visual language must remain stable.

## Input resolution

Use whichever character inputs the user provides. A dedicated IP folder is optional, but when supplied, inspect its structured files and reference images together. Supported input forms include:

- a direct character image or image set;
- an IP folder containing `ip_bible.yaml` or `ip_bible.yml` plus a `references/` directory;
- a character sheet or multi-view reference;
- a confirmed IP Bible or character description;
- a text-only description when no visual reference exists.

When a folder is supplied, read the IP Bible first, then inspect relevant files under `references/`; use [ip-folder-structure.md](references/ip-folder-structure.md) for the recommended organization and naming conventions. Do not modify, rename, or require the user to reorganize the source folder. Ignore system files such as `.DS_Store`. Treat filenames as hints only and use the image content to determine the view; if a view cannot be determined, mark it uncertain.

Resolve the available inputs into a Recipe Manifest. The following fields are required in the manifest when applicable; unavailable fields must be marked as unknown or `none`, not invented:

- `character_id`: the IP or character name;
- `identity_anchors`: 3-8 highest-priority recognizable features, ranked by importance;
- `fixed_rules`: features that must not change;
- `allowed_variations`: features that may change for the requested asset;
- `action`: one primary action;
- `emotion`: one primary emotional state;
- `scene`: one concrete setting;
- `asset_type`: the requested output format;
- `exact_text`: user-supplied wording, or none;
- `ratio`: user-specified ratio, otherwise choose the asset default;
- `output_requirements`: transparency, crop, count, and text-safe areas.

If no usable character reference exists, use the user's description but state that exact character consistency is limited. Do not invent permanent character features that were not provided.

Set reference confidence in the Recipe Manifest: `high` for a confirmed IP Bible with a useful multi-view pack, `medium` for a usable but incomplete reference, `low` for weak or ambiguous references, and `none` for text-only input. The quality of the input changes the confidence disclosure, not the identity rules.

Use the machine-readable catalogs in `design-system/` as the source of truth for identity locks, asset dimensions, composition, and variation budgets. Read only the catalog relevant to the current decision. Build the normalized request using [recipe-manifest.md](references/recipe-manifest.md); use [qa-checklist.md](references/qa-checklist.md) after generation. For a reusable IP reference structure, read [ip-bible-template.md](references/ip-bible-template.md) when the user is defining or documenting the character system.

Follow this workflow: resolve inputs → build and check the Recipe Manifest → select the catalog asset type and composition → compile the production prompt → generate → inspect and record QA → deliver or retry within the limits below. If the user asks to create or revise an IP Bible, stop after the IP Bible draft and wait for confirmation before generating formal assets.

## Identity lock

Before composing the generation prompt, lock the following:

1. Preserve the strongest applicable identity anchors and show at least three visible anchors in every image when the composition allows. The manifest's 3-8 anchors are a prioritized subset; `fixed_rules` may contain additional permanent details. Do not claim that an anchor was verified when it is hidden, cropped, or not supported by the reference.
2. Keep species, face shape, body proportions, signature colors, permanent markings, and signature accessories unchanged.
3. Permit only the variations explicitly requested or listed as allowed variations.
4. When a reference image is supplied, preserve identity and recognizable factual features; change only the requested action, setting, crop, or treatment.
5. Do not solve inconsistency by adding extra accessories, changing the costume design, or making the character more generic.

### 可數特徵確認

- 生成前實際查看參考圖，逐項確認腳趾、羽冠瓣數、尾羽瓣數及其他可數的固定特徵；左右部位分別記錄，不能只記總數。
- 建立本次生成的核對清單：特徵、每側／每部位的確切數量、形狀與朝向、依據（參考圖或已確認的角色設定）、本次構圖是否必須完整可見。
- 使用者明確修正的構造優先於舊圖。看不清、被遮擋或設定仍待確認的數量，不可猜測；先查其他可用參考圖，仍無法判定且本次畫面需要呈現時，請使用者補充確認。
- 把已確認的數量視為固定身份規則；不可因姿勢、透視或造型簡化而增減、合併。合理遮擋不等於構造改變，但不可把不可見部位宣稱為已驗證，也不可用遮擋迴避明確可見要求。

## Asset routing

Choose the first matching asset type in this order unless the user explicitly specifies another:

1. `transparent_character_asset`: isolated character, sticker, pose, expression, or reusable material;
2. `h5_cover`: mobile campaign page or landing-page main visual;
3. `social_square` or `social_portrait`: square or feed graphic;
4. `story_cover`: character performing an action in a readable environment;
5. `link_preview`: landscape campaign or editorial share visual.

Do not use the mobile campaign-page layout for an isolated asset, and do not add a complex background to a transparent asset.

### 行動版活動頁主視覺

- Default to `9:16`; respect an explicit ratio.
- Prefer `1080x1920` for a standard mobile campaign-page main visual unless the user specifies another delivery size.
- Reserve a quiet text-safe zone in the upper or lower third, based on the user's content placement.
- Keep the character silhouette and primary action readable at mobile thumbnail size.
- Use one focal action and a controlled background hierarchy.
- Keep important identity anchors away from crop edges and text areas.
- Do not bake long, uncertain, or user-unspecified copy into the image; provide a safe area for layout text instead.

### Transparent character asset

- Use a transparent or plain neutral background as requested.
- Prefer a clean full-body or intentional half-body silhouette.
- Keep hands, feet, tail, ears, and signature accessories visible unless the user requests a crop.
- Do not include scene elements, logos, decorative text, or accidental extra characters.
- For a pose set, keep camera distance, character scale, line quality, and baseline consistent across the set.

### Social square and portrait

- Choose the exact delivery size from the requested platform when known.
- Use `1080x1080` for square posts, `1080x1350` for vertical feed posts, and `1080x1920` for stories or short-form vertical content.
- Use `1200x630` for link-preview or landscape share cards when a wide format is requested.
- Keep important identity anchors, headlines, and logos inside a central safe area so platform cropping does not remove them.
- Do not stretch one composition across every ratio. Recompose the character position and text-safe zone for each size while preserving the identity lock.

### Story cover and link preview

- Use `story_cover` for a readable character-in-scene cover and keep critical details away from top and bottom interface zones.
- Use `link_preview` for a landscape composition with a strong silhouette and a central horizontal text band.

### Scene content

- Use one primary action, one emotional beat, and one concrete scene.
- Let the environment support the action instead of competing with the character.
- Add only props that explain the activity or strengthen the story.
- Keep the character's silhouette and face readable even in a detailed scene.

## Variation budget

For one asset, vary no more than:

- one primary action;
- one primary emotion;
- one scene;
- one camera or composition change;
- one or two functional props;
- one small seasonal or situational costume variation.

Never vary identity anchors, character species, age impression, body proportions, or signature accessories unless the user explicitly requests a redesign. A series may vary actions and scenes while keeping the same identity lock, visual language, and scale logic.

## Visual language

Extract the IP's existing visual language from the reference material. If it is unspecified, use a restrained temporary default and keep it fixed across the run until the user confirms a style:

- one line treatment;
- one shading method;
- one material or texture treatment;
- one core palette with a small approved variation range;
- one expression vocabulary;
- one background density level per asset type.

For broad surfaces such as skin, fabric, walls, sky, or other smooth materials, prefer clean and naturally varied surfaces with gradual lighting transitions. Use concrete material and lighting language instead of stacking abstract quality terms such as `8K`, `hyper-detailed`, `micro texture`, or `sharp focus`; these terms are optional and should not be used when they add no meaningful visual requirement.

Do not turn a 2D IP into glossy 3D, photorealism, a different illustration medium, or a new branding style unless requested. Match the reference's level of simplification and visual weight.

Treat source character references as identity evidence. Treat files in an `approved-assets` or examples directory as quality and visual-treatment examples only; they must not override confirmed identity rules in the IP Bible.

## Prompt compiler

Compile the final image prompt in this order:

1. **Identity lock:** character name, reference usage, critical anchors, fixed features, and consistency requirement. 將核對清單中已確認的可數特徵逐項寫出確切數量、每側／每部位單位、形狀、朝向與必要的可見性，不能只寫「符合參考圖」。
2. **Action and emotion:** one clear action and one emotional beat.
3. **Scene and props:** one concrete environment and only functional props.
4. **Asset composition:** ratio, character position, crop, focal action, safe zone, transparency, and output purpose.
5. **Visual language and exclusions:** line, color, texture, lighting, clean-surface requirements where relevant, and hard avoids.

例如，若角色設定確認每隻腳三趾，提示詞應寫「每隻腳恰好三根短圓、朝前的腳趾；坐姿腳掌朝向鏡頭時，左腳三趾與右腳三趾都清楚分開可辨，不得缺趾、多趾或合併成兩趾」。其他角色須使用各自已確認的數量，不套用此範例；羽冠等特徵同樣逐項寫入。

Use exact user-supplied text without translating it. If text is uncertain, reserve a safe area rather than inventing branding, campaign facts, URLs, or logos.

## Hard avoids

Always exclude the following unless explicitly requested:

- identity drift, redesigned face, changed species, or changed body proportions;
- missing or duplicated signature accessories;
- 可數固定特徵的數量錯誤、缺失、重複或合併，以及未符合要求的可見性；
- extra permanent markings;
- generic mascot expressions that erase the IP personality;
- extra characters or branded objects not supplied by the user;
- text over the face or critical identity anchors;
- cropped hands, feet, ears, tail, or other anchors when a reusable asset is requested;
- complex backgrounds in transparent assets;
- inconsistent camera scale or baseline within a pose set;
- repetitive scales, honeycomb/cellular patterns, procedural-looking grain, or unwanted micro-texture on broad surfaces;
- glossy 3D rendering, photorealistic anatomy, or unrelated art styles;
- invented logos, sponsors, URLs, QR codes, or factual event information.

## Reference confidence

Assign `high`, `medium`, `low`, or `none` confidence in the Recipe Manifest. A text-only request has `none` confidence: do not invent permanent features or claim exact consistency. Mark ambiguous anchors as `needs_confirmation` and disclose that limitation.

## 修圖來源與品質回退

- 每張素材區分並記錄：原始角色參考、未經局部修圖的場景初稿、通過整體驗收的版本、目前修正目標。保留原檔，不覆寫；最新版本不等於最佳底圖。
- 原始角色參考始終是身份、基礎色與表面材質的依據。局部編輯時明確標示哪張是編輯目標、哪張是角色參考；新場景各自從原始參考生成，不把上一張場景當成唯一身份來源。
- 修正前先整理目前所有已知問題與必須保留的特徵，選擇局部編輯或重新生成。只有問題局限在小範圍、且整體畫質與角色身份已通過時，才使用局部編輯。
- 若局部修正新增比例錯誤、色偏、濁化、鱗狀／碎片狀表面、線條或材質漂移，將該版標為失敗，禁止把它當成下一次修圖底圖。回到原始角色參考，彙整已知修正要求重新生成；必要時以通過驗收的場景版本輔助構圖，不能取代身份參考。
- 同一批修正預設最多一次局部編輯及一次從原始參考重新生成；若直接重生則重試一次。重生後仍不符合要求，明確交代未解決項目，不自動追加生成。使用者提出新的修正可另行處理，但仍須挑選乾淨底圖，不能延續失敗版本。
- 更換 session 不是畫質修復步驟。依實際成圖與來源版本判斷，不把劣化原因斷言為 session 或模型內部機制。

## Inspection and retry

Inspect the result at full size and at the intended delivery size, and record the result using [qa-checklist.md](references/qa-checklist.md). 依生成前的核對清單，逐張、逐部位檢查成圖；放大查看左右腳趾、羽冠、尾羽等，分別記錄「預期數量／實際可辨數量／通過、失敗或無法確認」。不可只憑整體像不像判斷。坐姿腳掌朝向鏡頭且設定每腳三趾時，須分別確認左腳三趾、右腳三趾均清楚可辨；兩趾加模糊隆起不能算通過。合理遮擋的項目記為無法確認；要求完整可見卻無法辨識則判定失敗。

每次生成與局部修正後都重新檢查整張圖，並與原始角色參考及同系列已通過的圖片比較：臉型、比例、配件、基礎色、材質、動作、文字、留白與畫面清晰度。不可因局部問題修好就忽略其他退化。夜景可有合理的環境光變化，但仍須保留角色基礎色的辨識度與原有表面質感；對原本光滑的角色，鱗片、重複斑塊、碎面或污濁紋理均判定失敗。

若以下任一項失敗，依「修圖來源與品質回退」選擇修正方式並遵守重試上限：

- any critical identity anchor or fixed rule is visibly violated;
- 任一已確認的可數特徵數量錯誤、合併，或未達必要的可見性；
- the primary action is unclear;
- the requested asset ratio or transparency is wrong;
- a mobile campaign-page main visual lacks a usable text-safe zone;
- a reusable asset has an accidental background, crop, or extra character;
- the character's visual language has drifted from the reference;
- broad surfaces contain obvious repetitive patterns, artificial grain, or plastic-looking texture;
- the composition is too busy to read at thumbnail size.

重試提示詞須指出出錯部位、預期數量與可見性，並在重試後重新逐項驗收。

若達重試上限仍未通過，明確說明限制與尚未通過的項目；只在參考不足時建議補強角色參考。不得把失敗版本當成完整成功交付，也不得宣稱成圖未能證明的一致性。

## Delivery

Return:

1. the generated raster image when image-generation capability is available;
2. the exact production prompt;
3. a short recipe naming the character anchors, action, scene, asset type, ratio, and visual treatment;
4. the QA result, including visible anchor count, per-feature count verification, and any failed or uncertain checks;
5. any limitation affecting identity consistency, transparency, or text rendering.
