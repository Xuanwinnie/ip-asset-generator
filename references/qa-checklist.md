# Generation QA Checklist

Inspect the generated image at full size and at the intended delivery size. Record the result before delivery.

```yaml
qa:
  identity_anchors_visible: 0
  minimum_anchors_required: 3
  identity_drift: pass | fail | uncertain
  primary_action_clear: pass | fail
  ratio_and_dimensions: pass | fail
  transparency: pass | fail | not_applicable
  text_safe_zone: pass | fail | not_applicable
  accidental_extra_character: pass | fail
  unwanted_text_or_logo: pass | fail
  visual_language_match: pass | fail | uncertain
  retry_used: false
  limitation: none
```

Retry at most once, and adjust only the failed requirement. If the second result still fails, deliver the limitation rather than claiming consistency.
