# {NN}_{stage-name} — {the job in five words}

One job: {the single thing this stage does}.

## Inputs
- Working (this run): ../{prev-stage-folder}/output/{run-id}/{file}, using the actual folder name and active run ID; update this path when renumbering
- Reference (every run): ../../_shared/{rules-file}.md
- Reference (every run): references/{stage-specific-guide}.md

Do NOT load: {anything an eager agent would wrongly pull in — other stages' references, prior runs, the whole _shared folder}.

## Process
1. {Read the inputs.}
2. {Transform, following the reference constraints.}
3. {Hard limits worth restating: length, count, format.}

## Outputs
- {artifact}.md → output/{run-id}/
- Ready when: {checks that establish the artifact is complete and usable}.

## Human check
Review record: {path for this run, recording approval and the reviewed artifact revision; invalidate approval if that artifact changes}.

{One concrete act: read it aloud / verify the numbers against X / confirm the order survived. Edit the output in place — the next stage reads whatever is here.}
