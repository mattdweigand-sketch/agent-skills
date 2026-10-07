# ICM Provenance

Read when checking source history or upstream notices; routine workspace work uses [conventions](../conventions.md).

## Source record

Source: the user-supplied `Interpretable-Context-Methodology-main` snapshot, checked on 2026-10-01. No upstream commit ID was recorded. The source archive and full video captions are not bundled. These fingerprints identify the local source material, not a verified upstream release.

| Source paths, relative to that snapshot | SHA-256 group fingerprint |
|---|---|
| `_core/CONVENTIONS.md` | `14e97ef3f0bb838c17ae8a7cbb889fab39f0273674c8e2c05b414da717656c00` |
| `_core/templates/*.md and _core/placeholder-syntax.md` | `97d84535d07cf9023241b1026b5edd8261b24d22ee0a27d745917119f65ed16a` |
| `workspaces/workspace-builder/stages/*/CONTEXT.md` | `3eee615cbb618c40ef065e6edc705d9d313baf452ccf00ddb4c9083745c04a1c` |

Each fingerprint hashes a UTF-8 JSON object mapping relative POSIX file paths to their whole-file SHA-256 hashes, with sorted keys, no spaces, and no trailing newline.

Walkthrough evidence is paraphrased from English auto-generated captions retrieved on 2026-10-01:

- [Folder architecture, 1:11](https://www.youtube.com/watch?v=n1qE6NU7K_4&t=71s): entry map; [2:17](https://www.youtube.com/watch?v=n1qE6NU7K_4&t=137s): Input, Do, Output, Human check; [7:51](https://www.youtube.com/watch?v=n1qE6NU7K_4&t=471s): fresh-chat navigation check.
- [Reviewable stages, 2:34](https://www.youtube.com/watch?v=EhWlGingCl0&t=154s): workspace pipeline table; [4:11](https://www.youtube.com/watch?v=EhWlGingCl0&t=251s): review before downstream production.

Course-derived additions and the 2026-10-06 and 2026-10-07 source reviews are summarized with links in [lesson notes](lesson-notes.md); full source text is not distributed in this package. The [example index](../examples.md) contains compact authored adaptations.

Deliberate adaptations include task-sized workspaces, optional pipelines, concise local context, source coverage, explicit review roles, and comparable repair runs. These supersede earlier blanket pipeline and context-purity requirements. Safe-migration checks came from `mattdweigand-sketch/agent-skills` commit `ae2ae17`; they are local safeguards, not requirements attributed to the videos.

## Upstream notices

The supplied source names Model Workspace Protocol Contributors; the earlier skill package names Jake Van Clief. Both notices are retained here with their common MIT terms for the repository-derived material, not the course lessons.

```text
MIT License

Copyright (c) 2026 Model Workspace Protocol Contributors
Copyright (c) 2026 Jake Van Clief

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
