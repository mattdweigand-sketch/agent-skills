---
name: explain
description: "Create beautiful HTML lessons about any topic or situation using selected ASD-STE100 writing methods. Invocation-only. Use for /explain, $explain, or an explicit request to use the explain skill. Not for generic HTML requests, videos, slide decks, or technical manuals."
---

# Explain

Build one polished, topic-specific HTML lesson. Apply selected ASD-STE100 Issue 9 writing methods, not the full standard or its controlled dictionary. Default to HTML without a format question. Keep this skill separate from `explainer`.

Use website-building only for technical implementation, its browser-testing workflow (visual, responsive, accessibility, and functional checks), and delivery. This skill owns the teaching approach and art direction.

## Workflow

1. Establish the learning goal in one sentence. Infer context and knowledge level. Default to an intelligent beginner. Ask for a missing topic, or one clarification if ambiguity would materially change the lesson.
2. Establish the facts. Use supplied material first. Verify changing facts and cite evidence near claims. Separate facts, interpretations, unknowns, and examples. For a situation, identify actors, sequence, constraints, and competing explanations without inventing motives or causes.
3. Plan the explanation. Read `references/teaching.md` before outlining and follow it.
4. Build one responsive scrolling page without placeholders. Read `references/writing.md` before writing visible text and `references/visual-direction.md` before designing. Keep literal evidence unchanged.
5. Verify and deliver. Run the simplicity review in `references/teaching.md` and the review steps in `references/writing.md`. Record actual results and limits. Never infer browser verification from code inspection. Never publish private material without explicit approval. Keep the handoff short. Never call output STE-compliant, certified, or ASD-approved.

## Teaching and writing

`references/writing.md` owns the selected writing methods, HTML classification, and review procedure. Before delivery, run `python scripts/check_text.py PAGE/index.html` from this skill directory. Fix violations and incomplete coverage. Review warnings. After checker edits, run `python scripts/test_check_text.py`.

## Visual direction

Start from `templates/page.html` and copy `assets/` as the visual reference directs. Keep design separate from writing methods.

## Example

Input: `/explain why this project missed its deadline` with meeting notes.

Output: A responsive HTML lesson. The title names the project and a line below gives the main cause. A short story follows one task through the notes. One interactive part changes one condition and shows the result. A short closing restates the answer. The timeline, other causes, and unknowns go in "More detail." Do not turn unverified statements from the notes into established causes.
