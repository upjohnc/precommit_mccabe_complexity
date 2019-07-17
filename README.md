# Precommit Hook - Mccabe Complexity
Hook for checking McCabe complexity

- fails if the complexity is greater than 12


## Precommit project
[Link to Precommit Project](https://pre-commit.com/)

```yaml
  - repo: git://github.com/upjohnc/precommit_mccabe_complexity
    rev: 0.11.0
    hooks:
      - id: mccabe-complexity
        args: ['--base_branch=master']
```