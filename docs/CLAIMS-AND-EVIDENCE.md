# Claims and evidence

**What this public starter actually demonstrates:** a deterministic synthetic ledger, a lost acknowledgement, an idempotent retry, a deliberately unsafe retry and observable unit-test assertions.

**What it does NOT demonstrate:** production safety, real-model prompt-injection protection, independent third-party review, distributed delivery guarantees, real financial refunds or a million-case rerun.

A **reference PASS** and a **caught intentional failure** are different outcomes. Never sum them into a safety score.

Any proposed extension needs: source or contributor attribution, a runnable test, expected and observed behaviour, fault injection, a scoped receipt and an explicit limit on what the result means.

Leadership decisions remain with named humans. Code does not confer authority.

## Historical million-case statement versus this public starter

On Ricky Jones's LinkedIn post published around 1 November 2026 (owner-supplied screenshots, inspected 7 November), he describes **earlier local experiments totalling 1,000,000 synthetic AI agent test cases across 12 fault classes**. This is a *historical self-reported result*, distinct from this repository's currently runnable exercise. It does not mean a million unique failure modes, a million distinct software defects, or any production certification.

**What this repository contains today:** `lab.py` simulates a lost acknowledgement and a retry with/without an idempotency guard; `test_lab.py` defines two unit tests for the reference and intentionally broken scenarios. The GitHub Actions workflow runs only these public files. The 1 November 2026 run at https://github.com/LalaSkye/auntie-trinitys-workbench/actions/runs/41280089396 completed successfully at commit `bdc5d062c81f1d7e4e2f624f609747e999d17068`; it is **not** a rerun of the earlier million-case experiment.

**Outstanding original evidence:** the historical million-case runner/version, exact 12-class definitions, input generation/seeds, executed command, machine/log output, case counts, exceptions, result receipt, and any independent reproduction have not been linked or inspected in this repo. Those claims remain **UNRESOLVED pending a source-bound review**, not disproved. No uninspected private fixture is implicitly part of this public starter.

**Verification rule:** do not transfer a PASS or claim ceiling from the public two-test example to the historical million-case work, or vice versa. Preserve both source objects and their distinct provenance.
