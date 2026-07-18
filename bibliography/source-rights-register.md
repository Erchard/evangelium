# Source Rights Register

Status: release verification pass v0.2, updated 2026-07-18.

## Purpose

This register classifies each major source family by how it may be used in EUAGELIA.

Statuses:

- `PROJECT_COMMONS`: original EUAGELIA contribution governed by project commons / anti-ownership policy.
- `PRIMARY_WITNESS`: ancient witness; public reproduction depends on image/transcription/edition rights.
- `OPEN_WITH_ATTRIBUTION_VERIFIED`: usable with attribution under an open license checked against local or official evidence.
- `PUBLIC_DOMAIN_VERIFIED`: public-domain dedication checked against local or official evidence.
- `PROTECTED_CONTROL_ONLY`: cite or consult, but do not reproduce as base text.
- `NEEDS_PERMISSION_FOR_REDISTRIBUTION`: may be used privately as a research control, but may not be redistributed without permission or a stronger rights basis.
- `NOT_USED_IN_CURRENT_RELEASE`: excluded from the current print-release source apparatus unless a later pass selects a specific edition.

## Register

| Source family | Status | What may be used | What must not be done | Required final action |
| --- | --- | --- | --- | --- |
| EUAGELIA original reconstruction, translations, commentary, prompts, tables | `PROJECT_COMMONS` | May be shared, adapted, printed, and used commercially under anti-ownership notice. | Do not claim exclusive private ownership over the shared underlying project. | Include commons / anti-ownership notice in print and digital outputs. |
| NHC II,2 Coptic witness | `PRIMARY_WITNESS` | Cite as primary witness; use project transcription and lawful excerpts with source label. | Do not reproduce protected Brill / Layton text as open base text. | Perform final Coptic reading check against facsimile or critical edition before claiming critical-edition precision. |
| Linssen Coptic Unicode working text | `PUBLIC_DOMAIN_VERIFIED` | Use as working Coptic transcription control with attribution and source date. | Do not treat as final critical edition. | Public-domain notice verified locally in snapshot; cite as open working transcription, not as manuscript facsimile. |
| Grondin interlinear / facsimile snapshots | `NEEDS_PERMISSION_FOR_REDISTRIBUTION` | Use as local research snapshots and visual controls. | Do not redistribute images, interlinear pages, or bulk site content without permission. | Keep in digital audit only unless permission is obtained. |
| DCLP / Papyri.info XML for P.Oxy. 1 / 654 / 655 | `OPEN_WITH_ATTRIBUTION_VERIFIED` | Use XML as working open transcription layer with attribution. | Do not omit license attribution; do not treat restorations as certain. | Cite Digital Corpus of Literary Papyri / Papyri.info and CC BY 3.0. |
| Agraphos snapshots | `NEEDS_PERMISSION_FOR_REDISTRIBUTION` | Use as local working snapshots and comparison controls. | Do not reproduce site text or images in public package without rights clarity. | Keep as private/local research control unless terms or permission allow. |
| NASSCAL pages | `PROTECTED_CONTROL_ONLY` | Cite bibliographic data and public description. | Do not bulk reproduce site content. | Use as citation aid, especially for P.Oxy. 5575 bibliographic details. |
| Gnosis snapshots | `NEEDS_PERMISSION_FOR_REDISTRIBUTION` | Use as local comparison controls. | Do not reproduce protected translations or site collections as project base text. | Keep as research-only unless a specific permission/open source is identified. |
| P.Oxy. 5575 printed edition | `PROTECTED_CONTROL_ONLY` | Cite bibliographically and use as control. | Do not reproduce full edition text. | Citation now identified; page-specific quotation remains protected and should be minimal. |
| SBLGNT | `OPEN_WITH_ATTRIBUTION_VERIFIED` | Use as canonical Greek control with CC BY 4.0 attribution. | Do not present as Thomas witness; do not leave temporary cache paths as final source basis. | Cite official repository/license/version and access date. |
| Mattison / Gospels.net Thomas translation | `PUBLIC_DOMAIN_VERIFIED` | Use as open translation control with attribution. | Do not let it replace EUAGELIA's own translation base. | Public-domain notice verified locally and online. |
| Lambdin translation / Nag Hammadi Library in English | `PROTECTED_CONTROL_ONLY` | Consult and cite as modern control. | Do not reproduce as project base text. | Library-check exact edition and page references if used in print. |
| Layton editions / translations | `PROTECTED_CONTROL_ONLY` | Consult and cite as academic control. | Do not reproduce protected edition text. | Brill identity checked; library-check page references before final citation. |
| DeConick reconstruction / translation | `PROTECTED_CONTROL_ONLY` | Cite as scholarly reconstruction model. | Do not copy reconstructed text or translation as base. | Library-check exact imprint/year and page references. |
| Patterson / Meyer / Polebridge materials | `PROTECTED_CONTROL_ONLY` | Cite as scholarly translation/commentary controls. | Do not reproduce protected modern translation as base. | Library-check exact edition and page references. |
| Brill Coptic Gnostic Library | `PROTECTED_CONTROL_ONLY` | Use for verification and citation. | Do not reproduce protected text beyond lawful citation. | Use for final scholarly checking, not as redistributable source text. |
| NA / UBS Greek New Testament | `PROTECTED_CONTROL_ONLY` | Use for final scholarly checking only if needed. | Do not publish as open base text unless licensed. | Current release uses SBLGNT as public canonical base. |
| Q reconstructions | `NOT_USED_IN_CURRENT_RELEASE` | None in current release. | Do not cite generic Q without edition/model. | Select edition only if a later argument needs it. |
| Didache | `NOT_USED_IN_CURRENT_RELEASE` | None in current release. | Do not cite uncited Greek text. | Select edition only if a later argument needs it. |
| Paul / James Greek controls | `OPEN_WITH_ATTRIBUTION_VERIFIED` | Use under the same SBLGNT policy as other New Testament controls. | Do not mix editions silently. | Cite SBLGNT if these controls appear in final apparatus. |

## Final Safety Rule

When in doubt, classify a source as `PROTECTED_CONTROL_ONLY` or `NEEDS_PERMISSION_FOR_REDISTRIBUTION` until verification is complete.

The project may be bold in reconstruction, but must be conservative in rights claims.
