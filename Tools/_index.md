# Tools

Scripts that do real work. A script earns a place here when it will run more than once. One line per script saying what it does and how to run it.

- `check.py`: checks the system is wired correctly. Run `python3 Tools/check.py`. It changes nothing.
- `setup.sh`: sets up a Mac. Installs git, Homebrew, Node, VS Code, Claude Code and Codex if missing, creates `.env`, runs the check. Run `bash Tools/setup.sh`. Add `--check` to only report.
- `setup.ps1` and `setup.cmd`: the same for Windows. Double click `setup.cmd`, or run `powershell -ExecutionPolicy Bypass -File Tools\setup.ps1`. Add `-Check` to only report.
