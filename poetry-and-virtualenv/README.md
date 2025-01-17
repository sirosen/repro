# poetry + virtualenv crash reproducer

This reproduces a crash bug caused by a specific usage of poetry.

> [!NOTE]
> This crash bug reproducer uses `poetry` in a way that is not officially
> supported. Installing `poetry` into the same virtualenv as your
> application allows the dependencies for `poetry` to change when the
> application is installed, and causes the breakage.

## How to Run Me

`docker build .` should result in a crashfail within `poetry`, with a message
related to `isoduration` or `fqdn` failing install.

A full trace will be printed, showing the error as seen in `sample.log`.

A cleaned-up log has been provided in `sample.clean.log`.

## Minimal Requirements

Effort has been taken to make the requirements in the poetry config and lock
minimal.

The crash seems to require some specific parallel execution inside of `poetry`,
during which the `virtualenv` version gets downgraded.
This is why `virtualenv` is pinned.

Simultaneously, sdist builds with legacy setuptools metadata are run. This is
why the `fqdn` and `isoduration` dependencies are included and pinned to
specific sdist artifacts.

For reasons as-yet unknown, installation of `pre-commit<4` is required to get
the bug to trigger. It's possible that `pre-commit`'s own requirements has
important interplay, or else that it simply produces enough package
dependencies for enough parallelism to be triggered within `poetry`.
