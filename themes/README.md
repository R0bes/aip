# AIP themes — semantic design tokens

The theme applies to the minimal identity header, Next Run, GitHub, Plan and Proposal cards. The accepted Next Run input is a real morphing textarea: an idle 40px circle containing the agreed waveform/I-beam/arrow SVG, expanding on focus or when nonempty. Its shell may use theme accent, border and glow; expanded text remains fully editable. The native DIL pressable uses the custom circular-arrow/play SVG and must retain its working dispatch. Native ChatGPT UI and the actual chat composer cannot be restyled through AppBlock CSS.

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

## Cyberpunk consistency rules\n\nFor Cyberpunk, use `surface` (#141824) for the header, GitHub result and unselected Next Run cards. Use `surface_alt` (#202838) only for nested controls or a restrained secondary surface, not as a separate competing card palette. All primary headings use `text` (#EEF5FF), including **HTML AppBlock headings**; do not inherit a dark text color from the host or Pastel examples. Secondary copy uses `muted` (#A7B7C9). Borders use `border` (#4D6075); reserve `accent` (#50E4DD) and `glow` for selected actions and interactive focus. Keep informational cards unglowing. In AppBlock CSS, explicitly set foreground on the root and on title/description elements, since the host and HTML controls can otherwise supply conflicting defaults. Match corner radii and density across native and HTML surfaces.\n\n## Application

1. Choose a theme per user instruction or current conversation context. Otherwise use **Pastel**. Do not claim theme preference persists across chats.
2. For AppBlock HTML, apply the chosen values as scoped CSS custom properties on the AppBlock root (e.g. `--aip-surface`, `--aip-accent`) and use `var(...)` in card CSS. Multiple AppBlocks do not share one stylesheet automatically. If a host supports a shared CSS resource in a future runtime, reuse the same tokens there; do not assume it today.
3. For native DIL cards, map the same semantics to supported `background`, `border`, `color`, spacing and radius props. Use neutral host colors where custom token values aren't supported; never assume AppBlock CSS styles native components.
4. Style the minimal identity header using the same `surface`, `border`, `text`, `muted` and `radius` tokens; no selection glow or status badge. The morphing textarea's SVG and circular shell use theme accents. Keep the native pressable functional and use the same accent, border and surface tokens for its circular shell. Keep selected Next Run glow distinct from status indicators. **Informational Plan/GitHub cards have no selection glow**. Never encode done/blocked with color alone.
5. Prefer compact content-aware layouts. Keep icon sizes around 20px and avoid artificial minimum heights. A horizontal group shares height; a vertical group shares width.
6. Theme is **presentation only**. It cannot change repository facts, plan status, handoff instructions, action keys or authorization.
7. A theme picker, if shown, affects the current rendered example or the explicitly selected next-run request. Persisting a user's theme requires an actual durable setting/source and must not be claimed otherwise.

## Future

If all cards eventually share a real browser host, a single scoped CSS file generated from these tokens could be useful. Until then, maintain **one token table**, not a parallel component library or runtime.
