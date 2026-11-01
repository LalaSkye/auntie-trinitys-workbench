# ▲ AUNTIE TRINITY'S WORKBENCH

**BUILD IT. BREAK IT. PROVE WHERE IT STOPS.**

An accessible, open-source AI agent failure-testing laboratory for engineers, reviewers and leaders.

**Status:** Educational / synthetic · **Authority:** Human-controlled · **Deployment certification:** Not claimed.

## Start here

Run the first exercise with Python 3.10+ (no external packages or API keys):

```bash
python lab.py
python -m unittest discover -v
```

The lab demonstrates a lost acknowledgement: an authorised transaction succeeds but its response disappears. An unsafe retry duplicates it; the guarded workflow uses an idempotency key to prevent a second commit.

## The engineering ladder

| Level | Question | Evidence |
|---|---|---|
| Beginner | What actually happened? | Observable event trace |
| Engineer | Can the action safely be repeated? | Asserted state invariants |
| Reviewer | Can a deliberately broken workflow be detected? | Mutation test |
| Leader | What can a human authorise? | Named owner, scope and release decision |

## Release gates

- **UNDERSTAND:** Check the person's actual request, not just fluent wording.
- **VERIFY:** Keep evidence origin and uncertainty visible.
- **AUTHORISE:** No consequential action without suitable current permission.
- **EXECUTE:** Make retries, timeouts and partial failures explicit.
- **PROVE:** Record what the test executed, what it asserted and what remains untested.
- **STOP:** A successful test never grants standing permission.

## Claims and evidence

The earlier Agent Failure Lab v0.7 workbench was prepared with twelve synthetic fault categories, recovery lessons, beginner learning paths and separate-path verification fixtures. **Those historical runs are not a certification.** This repository is being imported in stages: the files and checks visible here are the only ones currently available to GitHub users. Never claim that earlier million-case executions have been rerun by the repository's CI.

Please use synthetic data only. Never put secrets, private records or live customer transactions in tests, issues or receipts.

## Leadership challenge

> A million passing test cases still cannot tell a leader who authorised the million-and-first action.

**Owner:** Ricky Jones · **Licence:** MIT · **Public contribution:** Welcome, with review before merge.

*Auntie Trinity keeps the torch. Gerald is not an independent auditor of the sheep.* 🫖🐑
