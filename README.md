# agent-harness CI template test (scratch)

Scratch repo for a real GitHub Actions verification of the agent-harness
CI template gate. No secrets, no real project code — a minimal gated
example only.

- Template source: `templates/ci-gate-check.yml` from
  [xusofty-cyber/agent-harness](https://github.com/xusofty-cyber/agent-harness),
  main `5fd31c7`, copied verbatim to `.github/workflows/gate-check.yml`.
- Checker source: `templates/pre-push-gate/gate-prepush-check.py` from the
  same main, copied verbatim to `scripts/gate-prepush-check.py`.
- Gate script: `gate/pass-gate.py` from the same main, copied verbatim.
- Workflow triggers (per the template header): push to `main` and any
  pull request. Steps: (1) `python3 scripts/gate-prepush-check.py --root .`
  re-verifies passing items; (2) `python3 gate/pass-gate.py --root .
  check-clean` runs the five clean-state dimensions.

## Layout

- `.github/workflows/gate-check.yml` — template copy (verbatim)
- `scripts/gate-prepush-check.py` — template checker (verbatim)
- `gate/pass-gate.py` — gate script (verbatim)
- `gate/feature_list.json` — one gated item
- `gate/clean-state.json` — minimal build/test/start commands for this example
- `example.py`, `tests/test_example.py` — the minimal example under test
- `.gitignore` — `__pycache__/` and `*.pyc` (needed so the build step's
  `py_compile` output does not trip check-clean dimension 4)

## Round 1 (intentionally failing)

The single passing item claims a verification command that cannot pass
(`test -f does-not-exist.txt`) with evidence `exit_code 0`. The workflow
is expected to FAIL at step 1 (re-verification) and therefore block.

## Results

(Updated after round 2; see commit history and Actions runs.)
