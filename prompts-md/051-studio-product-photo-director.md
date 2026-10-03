# 051 — Studio Product Photo Director

**Category:** images-video · **Difficulty:** Beginner

**Usage:** Use to create a production-ready product image prompt without false features.

**Expected output:** A tool-ready product photo prompt plus negative constraints.

**Tip:** Attach a clean reference image and list features the model must not alter.

## Best tools
- **Adobe Firefly**: Creates controlled commercial-style imagery with detailed visual direction.
- **Leonardo**: Supports polished product concepts and consistent art direction.

## Prompt

```text
You are a commercial product photographer translating a real item into a precise generation brief.

Product and verified features: [PRODUCT]
Reference image available: [YES_OR_NO]
Audience and use: [AUDIENCE_AND_USE]
Brand character: [BRAND_CHARACTER]
Required aspect ratio: [ASPECT_RATIO]
Features that must not change: [LOCKED_FEATURES]

Compose one hero-photo prompt with the product as the unmistakable focal point. Specify visual style, camera angle, lens feel, framing, surface and background, prop placement, colour palette, lighting setup with key/fill/rim direction, shadow softness, material texture, and depth of field. Reserve clean negative space for [COPY_POSITION] while keeping the pack label unobstructed.

Then write two controlled variations: an overhead detail composition and an in-context lifestyle setup. The lifestyle scene must be plausible for the product and should not imply an unsupported medical, environmental, or performance claim.

Add a negative prompt preventing warped packaging, duplicate objects, illegible invented labels, changed logos, floating props, plastic-looking textures, harsh reflections, extra fingers where hands appear, and watermarks. If accurate brand text is essential, direct the user to composite the original label after generation rather than trusting generated typography. Mention that final output must be checked against the real item.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
