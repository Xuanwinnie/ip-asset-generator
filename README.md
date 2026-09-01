# IP Asset Generator

[English](README.md) · [繁體中文](README.zh.md)

A reusable Skill for generating consistent visual assets from any user-provided IP character.

It keeps the same character recognizable across different actions, scenes, and formats while allowing each asset to have its own composition.

## What it does

Generate mobile campaign-page main visuals, social graphics, story illustrations, stickers, transparent character assets, and pose sets.

This is a public, reusable Skill. It does not include a private character. Each user supplies their own character reference images, description, or IP Bible.

## Quick start

### Install for Codex

```bash
git clone https://github.com/Xuanwinnie/ip-asset-generator.git \
  ~/.codex/skills/ip-asset-generator
```

### Install for Claude Code

```bash
git clone https://github.com/Xuanwinnie/ip-asset-generator.git \
  ~/.claude/skills/ip-asset-generator
```

Restart the relevant AI tool, then provide your own character reference.

```text
Use my supplied IP character to create a 1080x1920 mobile campaign-page main visual.
The character is holding an umbrella at a rainy train station.
Leave room for a headline and preserve the character's face, signature accessory, colors, and visual language.
```

Use the [IP Bible template](references/ip-bible-template.md) to document a character before generating a series.

## How to use an IP Bible

An IP Bible is a character specification document. It records the identity features that should remain stable across every asset, as well as the elements that may change with each request. Create and confirm the IP Bible before generating a series of assets.

### Create an IP Bible

Prepare a three-view character reference, ideally including front, side, and three-quarter views. Then provide the images to the agent with this prompt:

```text
Based on the three-view character references I provided, help me complete an IP Bible.

First analyze:
- Overall appearance
- Face shape, eyes, hairstyle, or fur color
- Body proportions
- Clothing and accessories
- Fixed color palette
- Distinctive identifying marks
- Possible personality and temperament
- Visual styles suitable for future extensions

Strictly separate:
1. Fixed features: must remain consistent in every image
2. Variable elements: may change with the action, scene, or emotion
3. Uncertain information: do not guess; mark it as "needs confirmation"

Use the format in references/ip-bible-template.md.
Do not generate an image yet. Let me review and confirm the IP Bible first.
```

When reviewing the result, check the face shape, clothing, colors, body proportions, signature accessories, and distinctive marks first. If a detail cannot be confirmed from the references, keep it marked as uncertain instead of inventing a new character rule.

### Use the IP Bible to generate assets

After confirming the IP Bible, provide these three things for each new asset:

1. The confirmed IP Bible
2. The three-view character reference or other character references
3. The requested action, situation, scene, emotion, and dimensions

```text
Use the confirmed IP Bible and the three-view character references.

Create a 1080x1080 square social post:
The character is flying a kite at the seaside during sunset, with a happy expression.

Keep every fixed identity feature consistent. Change only the action, scene, expression, and composition.
```

The IP Bible defines the character identity, the three-view references provide visual evidence, and the asset request defines the action, scene, and composition. Providing all three together gives the most reliable foundation for a consistent asset series.

## Supported assets

| Asset type | Default rules |
| --- | --- |
| Mobile campaign-page main visual | `1080x1920`, headline-safe area, mobile thumbnail readability |
| Square social post | `1080x1080`, clear hierarchy and short-copy space |
| Portrait social post | `1080x1350`, crop-safe identity and vertical composition |
| Story or short-form cover | `1080x1920`, central safe area |
| Link preview image | `1200x630`, landscape composition |
| Transparent character asset | Transparent background, clean silhouette, visible signature accessories |
| Pose set | Consistent scale, camera distance, line quality, and baseline |

## How it works

```text
Character reference or IP description
        ↓
Identify anchors and fixed rules
        ↓
Read action, emotion, scene, and asset purpose
        ↓
Build an IP Recipe Manifest
        ↓
Apply dimensions and composition rules
        ↓
Compile a production prompt
        ↓
Generate and inspect identity consistency
```

## Character consistency

The Skill separates fixed identity from controlled variation.

- Fixed: species, face shape, body proportions, age impression, signature colors, permanent markings, accessories, and visual language.
- Variable: action, emotion, scene, functional props, camera angle, seasonal details, and asset ratio.

For stronger consistency, provide front, side, three-quarter, full-body, expression, pose, and accessory references.

## Repository structure

```text
ip-asset-generator/
├── SKILL.md
├── agents/
├── design-system/
├── evals/
├── examples/
├── references/
├── scripts/
├── .github/workflows/
├── README.md
├── README.zh.md
└── CHANGELOG.md
```

## Limitations

Reference images, identity anchors, and inspection rules improve consistency, but no image model guarantees pixel-identical faces or details across every generation.

If identity drift continues, strengthen the character sheet and multi-angle references instead of adding unlimited prompt adjectives.

## License

Use the Skill instructions and templates according to the license configured for this repository. Check usage rights separately for character artwork, brand assets, and third-party references.
