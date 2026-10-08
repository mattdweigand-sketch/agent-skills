# Visual direction

Use the editorial design of the user's preferred [earlier fetch lesson](https://www.perplexity.ai/computer/a/8cd9a8b0-3794-4756-8550-e119710a1cc2), with the newer dark-teal/cyan and light-mode palette. The user selected this combination on 2026-10-06. This replaces the serif/keynote and fixed two-zone template, not the hub's teaching workflow or writing methods.

## Page structure

The user approved this structure on 2026-10-07. `templates/page.html` is a blank skeleton of it. Keep this order.

1. Title that names the topic, with one plain answer line below it.
2. Story sections that carry one example. Define each technical term inside the story.
3. One interactive part next to the story it shows. Label illustrative results as made up.
4. A short closing that restates the main idea.
5. One "More detail" area with collapsed sections for technical facts, then the source list.

## Layout and type

- Use the bundled Satoshi regular and bold fonts for headings and body text. Use system monospace for literal source text and code.
- Preserve the template's editorial hierarchy, large sans-serif title, thin dividing rules, restrained panels, and generous spacing.
- Use compact in-page navigation when it helps the reader follow the lesson.
- Put each section's conclusion close to its example or diagram.
- Preserve the responsive single-column layout on narrow screens. Do not make the reader scroll through decorative graphics before reaching the explanation.

## Palette

`assets/style.css` owns the exact values in both themes. Keep their roles consistent.

- Dark mode uses a deep teal background, lighter teal panels, off-white text, cyan emphasis, and blue selection states.
- Light mode uses white and light-gray surfaces, dark text, teal emphasis, and blue selection states.
- Keep the existing theme switch, visible focus indicators, and contrast between selected controls and their labels.

## Examples and interaction

- Reuse the simple input/operation/output flows, readable source panels, step lists, comparison toggles, and expandable details when they explain the subject.
- Use a timeline, chart, or plain text when it is clearer than the template's patterns.
- Put comparison controls next to the content they change. Captions should state what the reader should notice.
- When a diagram shows things that happen at the same time, keep them side by side at every width, including 375px. Shorten labels or shrink boxes instead of stacking them. A stacked layout reads as one after another.
- Preserve keyboard operation, selected-state feedback, and reduced-motion behavior. Essential information must remain available without animation.
- Use exact code-drawn labels and diagrams. Add no decorative imagery or invented brand mark.

## Build and review

1. Copy `templates/page.html` to the lesson's `index.html` and copy the complete `assets/` directory beside it. It includes `base.css`, `style.css`, `lesson.css`, `app.js`, and `fonts/satoshi-regular.woff2` plus `fonts/satoshi-bold.woff2`.
2. Replace every bracketed placeholder with lesson content. Add story paragraphs, options, or detail sections as the topic needs, within the idea budget.
3. Preserve the CSS system and reuse the small toggle/theme script as appropriate. Remove unused example panels, controls, and script handlers.
4. Apply the hub's teaching plan and all checks in `references/writing.md` to the new lesson, including retained labels and runtime text. A template's `data-ste` labels are not proof of correct language or exclusions.
5. Use the shared browser workflow to verify both themes, fonts, narrow-screen layout, every toggle and disclosure, keyboard operation, and source-link behavior.
