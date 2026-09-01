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

Follow this workflow: resolve inputs → build and check the Recipe Manifest → select the catalog asset type and composition → compile the production prompt → generate → inspect and record QA → deliver or retry once. If the user asks to create or revise an IP Bible, stop after the IP Bible draft and wait for confirmation before generating formal assets.

## Identity lock

Before composing the generation prompt, lock the following:

1. Preserve the strongest applicable identity anchors and show at least three visible anchors in every image when the composition allows. The manifest's 3-8 anchors are a prioritized subset; `fixed_rules` may contain additional permanent details. Do not claim that an anchor was verified when it is hidden, cropped, or not supported by the reference.
2. Keep species, face shape, body proportions, signature colors, permanent markings, and signature accessories unchanged.
3. Permit only the variations explicitly requested or listed as allowed variations.
4. When a reference image is supplied, preserve identity and recognizable factual features; change only the requested action, setting, crop, or treatment.
5. Do not solve inconsistency by adding extra accessories, changing the costume design, or making the character more generic.

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

Do not turn a 2D IP into glossy 3D, photorealism, a different illustration medium, or a new branding style unless requested. Match the reference's level of simplification and visual weight.

Treat source character references as identity evidence. Treat files in an `approved-assets` or examples directory as quality and visual-treatment examples only; they must not override confirmed identity rules in the IP Bible.

## Prompt compiler

Compile the final image prompt in this order:

1. **Identity lock:** character name, reference usage, critical anchors, fixed features, and consistency requirement.
2. **Action and emotion:** one clear action and one emotional beat.
3. **Scene and props:** one concrete environment and only functional props.
4. **Asset composition:** ratio, character position, crop, focal action, safe zone, transparency, and output purpose.
5. **Visual language and exclusions:** line, color, texture, lighting, and hard avoids.

Use exact user-supplied text without translating it. If text is uncertain, reserve a safe area rather than inventing branding, campaign facts, URLs, or logos.

## Hard avoids

Always exclude the following unless explicitly requested:

- identity drift, redesigned face, changed species, or changed body proportions;
- missing or duplicated signature accessories;
- extra permanent markings;
- generic mascot expressions that erase the IP personality;
- extra characters or branded objects not supplied by the user;
- text over the face or critical identity anchors;
- cropped hands, feet, ears, tail, or other anchors when a reusable asset is requested;
- complex backgrounds in transparent assets;
- inconsistent camera scale or baseline within a pose set;
- glossy 3D rendering, photorealistic anatomy, or unrelated art styles;
- invented logos, sponsors, URLs, QR codes, or factual event information.

## Reference confidence

Assign `high`, `medium`, `low`, or `none` confidence in the Recipe Manifest. A text-only request has `none` confidence: do not invent permanent features or claim exact consistency. Mark ambiguous anchors as `needs_confirmation` and disclose that limitation.

## Inspection and retry

Inspect the result at full size and at the intended delivery size, and record the result using [qa-checklist.md](references/qa-checklist.md). Regenerate at most once, adjusting only the failed requirement, if any of these fail:

- three or more critical identity anchors are missing or visibly changed;
- the primary action is unclear;
- the requested asset ratio or transparency is wrong;
- a mobile campaign-page main visual lacks a usable text-safe zone;
- a reusable asset has an accidental background, crop, or extra character;
- the character's visual language has drifted from the reference;
- the composition is too busy to read at thumbnail size.

If the result remains inconsistent after one retry, explain the limitation and recommend a stronger character sheet or reference-driven generation. Do not claim identity consistency that the output does not demonstrate.

## Delivery

Return:

1. the generated raster image when image-generation capability is available;
2. the exact production prompt;
3. a short recipe naming the character anchors, action, scene, asset type, ratio, and visual treatment;
4. the QA result, including visible anchor count and any failed or uncertain checks;
5. any limitation affecting identity consistency, transparency, or text rendering.
