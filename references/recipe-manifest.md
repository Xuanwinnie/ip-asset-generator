# IP Recipe Manifest

Use this manifest as the normalized plan for every generated asset or asset series. It is an internal working format: preserve user wording, but do not invent values that are not supported by the reference material. If the user is only creating or revising an IP Bible, stop before the asset fields and do not generate an image until the user confirms the Bible.

```yaml
character_id: <name-or-temporary-id>
reference_confidence: high | medium | low | none
reference_sources:
  - three-view-sheet

identity_anchors:
  - id: <anchor-id>
    description: <visible feature>
    priority: critical | high | supporting
    confidence: confirmed | needs_confirmation

fixed_rules:
  - <must remain unchanged>
allowed_variations:
  - <field allowed to change for this request>

asset_type: h5_cover | social_square | social_portrait | story_cover | link_preview | transparent_character_asset
action: <one primary action>
emotion: <one primary emotional beat>
scene: <one concrete setting>
functional_props: []
seasonal_variation: none
ratio: <requested ratio or catalog default>
dimensions: <requested dimensions or catalog default>
character_position: <composition decision>
text_safe_zone: <zone or none>
exact_text: none
transparency: false
series:
  enabled: false
  count: 1
  shared_rules: []

visual_language:
  line: <reference-derived treatment>
  shading: <reference-derived treatment>
  palette: []
  texture: <reference-derived treatment>
surface_quality:
  broad_surfaces: clean | natural_texture | intentional_pattern | unknown
  avoid_artifacts: []
hard_avoids: []
```

## Confidence rules

- `high`: confirmed IP Bible plus multi-angle reference pack.
- `medium`: usable reference image with some missing views or confirmed IP description.
- `low`: one weak, cropped, or ambiguous reference image.
- `none`: text-only description; do not claim exact identity consistency.

Any anchor marked `needs_confirmation` is not a permanent rule until the user confirms it. When the reference is missing, use temporary descriptive features only and disclose the limitation in delivery.

For a series, create one shared manifest and one per-asset manifest. The shared manifest locks identity, visual language, scale logic, and baseline; each asset manifest may change only the requested action, emotion, scene, functional props, or seasonal variation.
