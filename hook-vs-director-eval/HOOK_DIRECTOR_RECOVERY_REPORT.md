# Recovery report: hook-director

Date: 2026-10-20. **Result: NOT RECOVERED. No file, folder, archive, Git object or public repository containing the original was found.** No replacement was written. Nothing outside this directory was modified.

## 1. Environment (verified)
- OS: Linux 6.18.44 x86_64 (cloud VM, ephemeral container). User: root. HOME=/root. CWD=/home/user/Cloud.
- Git repositories found by `find / -name .git` (depth 6): /home/user/Cloud (the only project repo), /root/.cache/uv/sdists-v9/.git, /opt/rbenv (+ruby-build), /opt/nvm. Tooling only, not project roots.
- GitHub repositories reachable from the account: 2i8o/Cloud, 2i8o/GPH (private), 2i8o/PPPwn (fork), 2i8o/MagiskOnWSA (fork, disabled). 2i8o/GPH was attached read-only and shallow-cloned to /home/user/gph; PPPwn and MagiskOnWSA were not cloned (unrelated forks, listed only).
- Only one disk is writable (/dev/vda); no other drives or backup mounts exist. /mnt/attach, /mnt/user-data/{uploads,outputs,working} are empty.
- Historical path .claude/skills/hook-director/SKILL.md: does not exist in /home/user/Cloud, /home/user/gph, ~/.claude, or /home/claude/.claude.
- Recovery directory: /home/user/hook-director-recovery (outside project files).

## 2. Local searches performed
| Method | Scope | Result |
|---|---|---|
| `find / -iname '*hook-director*' / '*hook_director*' / '*hookdirector*'` (excluding proc, sys, node_modules, nix, node/gcloud dirs) | whole filesystem | 0 matches |
| grep for `hook-director`, `hook storyboard`, `punch-in`, `kinetic type` | /home /root /mnt /opt/env-runner /tmp /srv | matches only in: skills-catalog.md (below), my own earlier reports (hook-vs-director-eval, hook-engine-pack/validation/phase2/*) and this session's transcript. None is the skill. |
| `find` for .zip .skill .tar* .tgz (excluding system trees) | whole filesystem except /usr, /var/lib, toolchains | 0 files outside /mnt/skills |
| .skill archives in /mnt/skills/examples (35 packages) | listing of each | none contains a "hook" or "director" entry |
| `.claude/skills` directories | ~/.claude, /home/claude/.claude | only session-start-hook and the synced account skills |
| Synced account skills (abbas-personal-operating-system, abbas-work-profile, professional-video-editing-intelligence, orwellian-writer-skill, etc.) | full text grep for remotion, kinetic, punch, storyboard, hook | mentions of generic hooks/storyboards only; no hook-director |
| Plugin dirs, backups (~/.claude/backups holds only .claude.json copies), sessions, state | listed | no skill content |
| Project bible | searched filesystem and Notion | no local copy. Notion has one page, "OptiNest - نظام تشغيل مشروع صناعة المحتوى البصري" (id 3e723da4-2a6f-81ce-9ddf-d7ec449eebe5, unverified, edited 2026-09-28). I then fetched and read it in full: it is a project operating plan (MINE/BUILD/PUBLISH cycle, script template HOOK→PROBLEM→SURPRISE→EXPLANATION→PAYOFF→NEXT CURIOSITY, 90-day plan). It never mentions hook-director, Remotion, or a hook storyboard, and says "no advanced Motion Graphics at the start". It is not the historical bible with the skill manifest. It uses the OptiNest name, which conflicts with the current identity, so treat it as legacy. |

## 3. Git forensics
- /home/user/Cloud: branches main, claude/hook-engine-video-skills-xl849h (+ remote counterparts). 6 commits on all refs. `git log --all -S'hook-director'` hits only my commit 77d8eea (it names the missing skill). No path matching hook-director in any commit; no rename/move/delete records. Initial commit a71cd20 contains only README.md. `git fsck --lost-found --no-reflogs` printed nothing. Stash empty.
- /home/user/gph (HEAD ab64e3b, history deepened to 65 commits via bounded fetch): `git log --all -S'hook-director'` returned 0 commits; `git grep -il hook-director` over every fetched revision returned 0 files. (An earlier filename grep matched three "Delete ... directory" commits only because the word "directory" contains "director"; I opened them: they delete functions/, public/, scripts/ of the booking app. Not related.) Tracked content is a booking web app plus ZenMux skills (.agents/skills), none relevant. Only the fetched 65 commits were checked; older history, if any, was not.
- Dangling objects/reflogs: reflogs of these fresh clones are empty by construction; fsck on Cloud found nothing.

## 4. External search (only after local failure)
Two public web searches for the exact name plus the description produced no repository, file or page named hook-director. Hits were unrelated (superimg Remotion-like library with a "director" API, marketing blogs). None of them is the skill, none was installed or downloaded, none counts even as a probable match. Public GitHub code search was not used (outside this session's repository scope).

## 5. The only trace found
`/root/.claude/skills/synced/aed4cda1-.../abbas-work-profile/references/skills-catalog.md` line 56 (sha256 prefix 96c98fd8a797627a): "`hook-director` - Design or evaluate the opening seconds of a short video." The file says it is a Codex-environment snapshot dated 2026-10-13 and an inventory, not software. This matches the name but **does not** carry the description in your brief (first 3-5 seconds as a production phase, second-by-second storyboard, Remotion). The Remotion skills are listed separately in the same catalog as `remotion:*`; that is plugin routing, not evidence about hook-director.

## 6. Candidates and comparison
None. Candidate count: 0. No hashes, duplicates or provenance to compare.

## 7. Validation
Not applicable: nothing recovered, nothing to read, run or check for Remotion dependencies. I did not test anything operational.

## 8. Remaining uncertainty and where it may still live (guess, not evidence)
- مرجح: it exists only in the Codex environment (the catalog says so) or in a project folder on your own computer that was never synced here. This VM is a fresh clone with only one commit-history of your Cloud repo.
- Open leads: (a) older GPH history if any; (b) your local machine's `.claude/skills/hook-director/` or `~/.codex/skills/hook-director/`; (c) the Codex skill folder in whatever backup or cloud drive you used.
- Commands you can run locally: `find ~ -ipath '*hook-director*' 2>/dev/null` and `git -C <project> log --all --oneline -- '*hook-director*'`.

## 9. Recommendation
Do not recreate it from the one-line description and label it the original. If you locate it, put it in `.claude/skills/hook-director/` of a project (not user-level) so it cannot shadow other skills, and hash it before use. Restoration was not performed; no skill was installed, overwritten, or modified.
