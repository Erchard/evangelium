# Structure Cleanup 2026-07-18 v0.1

## Scope

Reviewed the top-level project structure after the print/digital publication architecture pass.

## Removed As Unambiguously Unneeded

- `.DS_Store`
- `output/.DS_Store`
- `reconstruction/.DS_Store`
- empty `output/articles/`
- empty `output/book-draft/`
- empty `reconstruction/kernel-thomas/`

## Added / Aligned

- `output/print/uk/README.md`
- `output/print/en/README.md`
- `output/digital/scholarly/README.md`
- updated `output/README.md` to match the three-output publication architecture.
- updated root `README.md` to describe `output/` as generated Ukrainian print, English print, and digital scholarly companion outputs.

## Kept Intentionally

- `project/ide-codex-*.md` prompt files: kept as reproducibility trail for how major project passes were executed.
- `reconstruction/earliest-sayings-gospel/*-pass-*.md` and audit files: kept as decision history and quality-control evidence.
- `reconstruction/own-model/layer-model.md`: kept as active model material.
- `archive/`, `bibliography/`, `output/`: kept because they are documented functional top-level folders.

## Current Output Structure

```text
output/
  README.md
  print/
    uk/
      README.md
    en/
      README.md
  digital/
    scholarly/
      README.md
```

## Next Structural Step

No further deletion is recommended right now. The next useful structural improvement would be a later generated-output pipeline that writes book artifacts into `output/print/uk/`, `output/print/en/`, and `output/digital/scholarly/`.
