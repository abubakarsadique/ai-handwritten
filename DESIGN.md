# Design System Specification: The Synthetic Ether

## 1. Overview & Creative North Star
**Creative North Star: "The Neon Neural"**
This design system moves away from the "SaaS-flat" aesthetic to embrace a deep, multi-dimensional workspace. It is designed to feel like a high-end command deck—sophisticated, responsive, and pulsing with the energy of live computation.

We break the "template" look by using **intentional asymmetry** and **tonal depth**. Instead of rigid, boxed-in grids, we use overlapping elements and light-refractive surfaces to create a sense of infinite space. This system doesn't just display information; it illuminates it through a high-contrast interplay of deep shadows and neon luminescence.

---

## 2. Colors
Our palette is rooted in the depth of space, punctuated by the vibrant energy of neural activity.

### The "No-Line" Rule
**Borders are prohibited for sectioning.** To define space, designers must use background color shifts (e.g., a `surface-container-low` section sitting atop a `surface` background). This forces a more organic, architectural feel rather than a spreadsheet-like structure.

### Surface Hierarchy & Nesting
Depth is achieved by stacking layers of increasing "lightness" or "transparency."
- **Base:** `surface` (#0b0e14)
- **Secondary Areas:** `surface-container-low` (#10131b)
- **Active Workspace:** `surface-container-high` (#1b202a)
- **Interactive Layers:** `surface-variant` (#202631)

### The "Glass & Gradient" Rule
To elevate the UI, floating panels (modals, popovers, dropdowns) must utilize **Glassmorphism**. Apply `surface-container` colors at 60-80% opacity with a `20px to 40px` backdrop blur.

**Signature Texture:** Main Action Buttons and Hero Headers should utilize a linear gradient from `primary` (#9093ff) to `primary-container` (#7073ff) at a 135-degree angle to create a "pulsing" visual soul.

---

## 3. Typography
We utilize a dual-font strategy to balance technical precision with futuristic character.

*   **Display & Headlines (Space Grotesk):** This is our "Technical Editorial" face. Its wide stance and geometric quirks feel engineered and high-tech. Use `display-lg` for impactful AI insights and `headline-md` for section entries.
*   **Body & Labels (Inter):** The workhorse. We use Inter for its unrivaled legibility in dark modes. High x-heights ensure that even `body-sm` remains crisp against neon accents.

**Hierarchy as Brand:** Use `tertiary` (#fface8) for small caps `label-md` to highlight AI-generated metadata. This creates a clear distinction between "System" text and "Machine-Generated" content.

---

## 4. Elevation & Depth
In this system, elevation is a physical property of light, not a structural line.

*   **The Layering Principle:** Rather than using a border, place a `surface-container-lowest` card on a `surface-container-low` background. The subtle 2-3% shift in HEX value creates a "soft lift" that feels premium and integrated.
*   **Ambient Shadows:** For floating elements, use extra-diffused shadows.
    *   *Values:* `0px 20px 50px rgba(0, 0, 0, 0.5)` mixed with a secondary glow: `0px 0px 15px rgba(144, 147, 255, 0.08)`. Shadows should feel like they are "tinted" by the surrounding neon environment.
*   **The "Ghost Border" Fallback:** If a container requires more definition (e.g., high-density data), use the `outline-variant` (#424855) at **15% opacity**. 100% opaque borders are strictly forbidden.

---

## 5. Components

### Buttons
*   **Primary:** Gradient fill (`primary` to `primary-container`), `xl` (1.5rem) rounded corners. White text (`on-primary`).
*   **Secondary:** Glass-effect. `surface-variant` at 40% opacity with a `secondary` (#00dce5) 1px ghost border at 20% opacity.
*   **Tertiary:** Text only in `secondary-fixed`, used for low-priority utility actions.

### Chips (Neural Tags)
*   Used for AI categories. High-contrast colors: `tertiary-container` fill with `on-tertiary-container` text. Always use `full` (9999px) roundedness to contrast with the `xl` corners of cards.

### Input Fields
*   **States:** Default state uses `surface-container-highest` fill. On focus, the container transitions to a `secondary` ghost border and a subtle internal glow (`surface-tint` at 5% opacity).
*   **Error:** Use `error_dim` (#c8475d) for the label text, never the entire box background.

### Cards & Lists
*   **No Dividers:** Lists are separated by `1rem` of vertical whitespace or a subtle background hover state using `surface-bright`.
*   **Nested Logic:** AI-suggested items should sit in a `surface-container-lowest` well to signify they are "processing" or different from the main surface.

### Additional AI Components
*   **The Pulse Loader:** A horizontal bar using a `secondary` to `tertiary` gradient that animates its width and opacity.
*   **The Confidence Meter:** A small `label-sm` tag utilizing `secondary` for high-confidence AI results and `error` for low-confidence flags.

---

## 6. Do's and Don'ts

### Do
*   **DO** use asymmetric padding. For example, give a container more bottom padding than top to create an "editorial" flow.
*   **DO** use `tertiary` (Magenta) sparingly as a "Notification" or "Insight" color to draw the eye to AI-specific updates.
*   **DO** ensure all glassmorphism layers have at least `20px` backdrop blur to maintain readability.

### Don't
*   **DON'T** use pure white (#FFFFFF). Always use `on-surface` (#e0e5f5) for body text to reduce eye strain in dark mode.
*   **DON'T** use 1px solid borders to separate the header from the body. Use a `surface-container` shift instead.
*   **DON'T** use standard "drop shadows" (black, high-opacity). They muddy the deep blues and purples of the background.