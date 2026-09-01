# IP Bible Template

Use this template when documenting a character before generating a series of assets. Replace examples with facts from the user's supplied IP. Do not invent missing identity facts.

```yaml
character_id: <name>
species_or_role: <species, object, person, or mascot role>
personality: [<trait>, <trait>]

identity_anchors:
  - id: <anchor>
    description: <visible feature>
    priority: critical

fixed_rules:
  - <feature that must never change>

allowed_variations:
  - actions
  - facial_expressions
  - scenes
  - functional_props
  - seasonal_accessories

visual_language:
  line: <line quality>
  shape: <shape language>
  palette: [<color>, <color>, <color>]
  shading: <shading method>
  texture: <material treatment>
  background_density: <low, medium, or high>

asset_defaults:
  h5_cover:
    ratio: 9:16
    text_safe_zone: upper-third
  transparent_character_asset:
    ratio: 1:1
    background: transparent
  social_card:
    ratio: 1:1
    text_safe_zone: upper-left
```

## Reference sheet checklist

Prefer a reference pack containing:

- front, side, and three-quarter views;
- neutral expression plus four to six common expressions;
- full-body silhouette and several useful poses;
- close-up of permanent markings and accessories;
- approved color and material references.

The reference pack improves identity consistency, but it does not guarantee pixel-identical results across image models. The Skill should preserve anchors and report failures instead of hiding them.
