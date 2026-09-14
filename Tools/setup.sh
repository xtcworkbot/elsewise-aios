#!/bin/bash
# Set up a Mac for this AI operating system.
#
# Run from the folder:   bash Tools/setup.sh
# Check only, no installs:   bash Tools/setup.sh --check
#
# Installs, only if missing: Apple command line tools (git and python3),
# Homebrew, Node, VS Code, Claude Code and Codex. Then creates .env from
# .env.example, runs the system check and prints what it found.
# Safe to run twice. It changes nothing that already works.

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHECK_ONLY=0
[ "$1" = "--check" ] && CHECK_ONLY=1
PROBLEMS=0

say()  { printf '\n== %s\n' "$1"; }
ok()   { printf '   ok    %s\n' "$1"; }
todo() { printf '   todo  %s\n' "$1"; PROBLEMS=$((PROBLEMS+1)); }
have() { command -v "$1" >/dev/null 2>&1; }

if [ "$(uname)" != "Darwin" ]; then
  echo "This script is for a Mac. On Windows run Tools\\setup.cmd instead."
  exit 1
fi

say "Apple command line tools (git and python3)"
if xcode-select -p >/dev/null 2>&1; then
  ok "installed"
else
  if [ $CHECK_ONLY = 1 ]; then todo "not installed"; else
    echo "   Apple will open a window. Click Install and wait, then run this script again."
    xcode-select --install
    exit 0
  fi
fi

say "Homebrew"
if have brew; then ok "$(brew --version | head -1)"; else
  if [ $CHECK_ONLY = 1 ]; then todo "not installed"; else
    echo "   Installing Homebrew. It asks for your Mac password once."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    if [ -x /opt/homebrew/bin/brew ]; then eval "$(/opt/homebrew/bin/brew shellenv)"; fi
    if [ -x /usr/local/bin/brew ]; then eval "$(/usr/local/bin/brew shellenv)"; fi
    if have brew; then
      grep -q 'brew shellenv' ~/.zprofile 2>/dev/null || echo 'eval "$('"$(command -v brew)"' shellenv)"' >> ~/.zprofile
      ok "$(brew --version | head -1)"
    else todo "Homebrew did not install"; fi
  fi
fi

say "Node"
if have node; then ok "$(node --version)"; else
  if [ $CHECK_ONLY = 1 ] || ! have brew; then todo "not installed"; else
    brew install node && ok "$(node --version)" || todo "Node did not install"
  fi
fi

say "Python 3"
if have python3 && python3 --version >/dev/null 2>&1; then ok "$(python3 --version)"; else todo "python3 missing. Install the Apple command line tools above."; fi

say "Git"
if have git; then ok "$(git --version)"; else todo "git missing. Install the Apple command line tools above."; fi

say "VS Code"
if [ -d "/Applications/Visual Studio Code.app" ] || have code; then ok "installed"; else
  if [ $CHECK_ONLY = 1 ] || ! have brew; then todo "not installed"; else
    brew install --cask visual-studio-code && ok "installed" || todo "VS Code did not install"
  fi
fi

say "Claude Code"
if have claude; then ok "$(claude --version 2>/dev/null | head -1)"; else
  if [ $CHECK_ONLY = 1 ]; then todo "not installed"; else
    curl -fsSL https://claude.ai/install.sh | bash
    export PATH="$HOME/.local/bin:$PATH"
    if have claude; then ok "$(claude --version 2>/dev/null | head -1)"; else todo "Claude Code did not install"; fi
  fi
fi

say "Codex"
if have codex; then ok "$(codex --version 2>/dev/null | head -1)"; else
  if [ $CHECK_ONLY = 1 ]; then todo "not installed (optional)"; else
    curl -fsSL https://chatgpt.com/codex/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
    if have codex; then ok "$(codex --version 2>/dev/null | head -1)"; else todo "Codex did not install (optional, Claude Code is enough to start)"; fi
  fi
fi

say "Key file"
if [ -f "$ROOT/.env" ]; then ok ".env exists"; else
  if [ $CHECK_ONLY = 1 ]; then todo ".env not created yet"; else
    cp "$ROOT/.env.example" "$ROOT/.env" && ok ".env created from .env.example. Keys go in there, never in chat."
  fi
fi
if git -C "$ROOT" check-ignore -q .env 2>/dev/null; then ok "git ignores .env"; elif [ -d "$ROOT/.git" ]; then todo "git does not ignore .env. Check .gitignore."; fi

say "System check"
if have python3 && python3 "$ROOT/Tools/check.py"; then :; else todo "the system check did not pass"; fi

echo
if [ $PROBLEMS = 0 ]; then
  echo "Everything is in place."
else
  echo "$PROBLEMS thing(s) still to do, marked todo above."
fi
echo
echo "Next: open this folder in VS Code or a terminal, run 'claude' to sign in,"
echo "then type /onboard. Claude Code needs a paid Claude plan to sign in."
