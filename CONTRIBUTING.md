# Commit convention
This project follows the [conventional commits specification](https://www.conventionalcommits.org/en/v1.0.0/#specification) with the following tags:
- `feat`: Added new feature
- `enh`: Improvemed working code
- `fix`: Fixed broken code
- `refac`: Moving/reformatting code without (intentionally) changing how it works, excluded from release notes unless it's a breaking change (`!`)
- `doc`: Changes to package documentation
- `test`: Changes to test suite
- `sys`: Systems administration (e.g. GitHub actions, packaging, etc.), generally excluded from release notes

...and the following (optional) scopes:
- `[feat]`: Only affects code which has not yet been released, generally excluded from release notes
- `[silent]`: Always excluded release notes