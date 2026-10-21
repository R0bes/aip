# AIP themes — semantic design tokens

AIP cards are ChatGPT-generated DIL/native UI and optional AppBlock HTML, **not** one shared browser DOM. Therefore a global CSS file cannot style every native card. Use this small semantic token specification as the single design reference, without building a renderer, settings service or CSS injection layer.

## Tokens

Each theme defines:
- `surface`, `surface_alt`, `text`, `muted`, `border`, `accent`, `accent_soft`, `glow`
- `radius` and `density` (compact spacing)
- Semantic statuses `done`, `active`, `open`, `blocked` keep readable icon + label, regardless of theme.

| Token | Pastel (default) | Cyberpunk | Neutral |
| --- | --- | --- | --- |
| surface | `#EEE5FA` | `#141824` | `#F4F5F7` |
| surface_alt | `#DFE9F6` | `#202838` | `#E8EBEF` |
| text | `#35374D` | `#EEF5FF` | `#232833` |
| muted | `#626B81` | `#A7B7C9` | `#626B76` |
| border | `#B8ACCE` | `#4D6075` | `#C5CAD2` |
| accent | `#866ACB` | `#50E4DD` | `#4B647D` |
| accent_soft | `#A58DE639` | `#50E4DD24` | `#4B647D20` |
| glow | `#8E78C650` | `#50E4DD50` | `#4B647D20` |
| radius | `14px` | `8px` | `10px` |
| density | compact | compact | compact |

These are **proposed visual presets**, not user-approved global defaults except the existing pastel direction. Validate legibility and contrast before treating any preset as final.

## Application

1. Choose a theme per user instruction or current conversation context. Otherwise use **Pastel**. Do not claim theme preference persists across chats.
2. For AppBlock HTML, apply the chosen values as scoped CSS custom properties on the AppBlock root (e.g. `--aip-surface`, `--aip-accent`) and use `var(...)` in card CSS. Multiple AppBlocks do not share one stylesheet automatically. If a host supports a shared CSS resource in a future runtime, reuse the same tokens there; do not assume it today.
3. For native DIL cards, map the same semantics to supported `background`, `border`, `color`, spacing and radius props. Use neutral host colors where custom token values aren't supported; never assume AppBlock CSS styles native components.
4. Keep selected Next Run glow distinct from status indicators. **Informational Plan/GitHub cards have no selection glow**. Never encode done/blocked with color alone.
5. Prefer compact content-aware layouts. Keep icon sizes around 20px and avoid artificial minimum heights. A horizontal group shares height; a vertical group shares width.
6. Theme is **presentation only**. It cannot change repository facts, plan status, handoff instructions, action keys or authorization.
7. A theme picker, if shown, affects the current rendered example or the explicitly selected next-run request. Persisting a user's theme requires an actual durable setting/source and must not be claimed otherwise.

## Future

If all cards eventually share a real browser host, a single scoped CSS file generated from these tokens could be useful. Until then, maintain **one token table**, not a parallel component library or runtime.
