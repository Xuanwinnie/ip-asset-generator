# Generation QA Checklist

Inspect the generated image at full size and at the intended delivery size. Record the result before delivery.

```yaml
qa:
  identity_anchors_visible: 0
  minimum_anchors_required: 3
  identity_drift: pass | fail | uncertain
  countable_features:
    - feature: <特徵與左右部位>
      expected_count: <預期數量或 unknown>
      distinguishable_count: <實際可辨數量或 unknown>
      visibility_required: true
      result: pass | fail | uncertain
      note: <數量、形狀、朝向、合併或遮擋情況>
  primary_action_clear: pass | fail
  ratio_and_dimensions: pass | fail
  transparency: pass | fail | not_applicable
  text_safe_zone: pass | fail | not_applicable
  accidental_extra_character: pass | fail
  unwanted_text_or_logo: pass | fail
  surface_artifacts: pass | fail | uncertain
  visual_language_match: pass | fail | uncertain
  retry_used: false
  limitation: none
```

Retry at most once, and adjust only the failed requirement. If the second result still fails, deliver the limitation rather than claiming consistency.

For `surface_artifacts`, inspect broad surfaces at full size for repetitive scales, honeycomb/cellular patterns, procedural-looking grain, or plastic-looking texture. Do not fail a result merely because it has intentional material texture that matches the requested visual language.

依 Recipe Manifest 逐項核對可數特徵，左右部位分開驗收。任一固定數量錯誤、合併或必要可見性不符即判定失敗並觸發一次重試；不能等到三項身份錨點出錯才重試。合理遮擋記為 `uncertain`，不可宣稱已通過；要求完整可見卻無法辨識則為 `fail`。重試後再次逐項檢查。
