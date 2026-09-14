# Set up a Windows computer for this AI operating system.
#
# Easiest: double click Tools\setup.cmd, which runs this file.
# Or in PowerShell from the folder:  powershell -ExecutionPolicy Bypass -File Tools\setup.ps1
# Check only, no installs:            powershell -ExecutionPolicy Bypass -File Tools\setup.ps1 -Check
#
# Installs, only if missing: Git for Windows, Python 3, Node, VS Code,
# Claude Code and Codex. Uses winget, which comes with Windows 10 and 11.
# Then creates .env from .env.example, runs the system check and prints
# what it found. Safe to run twice. It changes nothing that already works.
#
# No administrator needed. Windows may show one or two permission pop ups
# for the installers. Click Yes.

param([switch]$Check)

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Problems = 0

function Say($t)  { Write-Host "`n== $t" }
function Ok($t)   { Write-Host "   ok    $t" }
function Todo($t) { Write-Host "   todo  $t"; $script:Problems++ }
function Have($n) { return [bool](Get-Command $n -ErrorAction SilentlyContinue) }
function RefreshPath {
  $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" +
              [Environment]::GetEnvironmentVariable("Path", "User")
}
function InstallWith($id, $name) {
  if ($Check) { Todo "$name not installed"; return }
  if (-not (Have winget)) { Todo "$name not installed, and winget is missing. Install App Installer from the Microsoft Store, then run this again."; return }
  winget install --id $id -e --accept-package-agreements --accept-source-agreements --silent | Out-Null
  RefreshPath
}

Say "winget (the Windows installer)"
if (Have winget) { Ok "present" } else { Todo "missing. Open the Microsoft Store, install App Installer, then run this again." }

Say "Git for Windows"
if (Have git) { Ok (git --version) } else {
  InstallWith "Git.Git" "Git"
  if (Have git) { Ok (git --version) } elseif (-not $Check) { Todo "Git did not install" }
}

Say "Python 3"
$py = $null
foreach ($c in @("python", "python3", "py")) {
  if (Have $c) {
    $v = & $c --version 2>&1
    if ("$v" -match "^Python 3") { $py = $c; break }
  }
}
if ($py) { Ok "$(& $py --version) as '$py'" } else {
  InstallWith "Python.Python.3.12" "Python"
  if (Have python) { $py = "python"; Ok (python --version) } elseif (-not $Check) { Todo "Python did not install" }
}

Say "Node"
if (Have node) { Ok (node --version) } else {
  InstallWith "OpenJS.NodeJS.LTS" "Node"
  if (Have node) { Ok (node --version) } elseif (-not $Check) { Todo "Node did not install" }
}

Say "VS Code"
if (Have code) { Ok "installed" } else {
  InstallWith "Microsoft.VisualStudioCode" "VS Code"
  if (Have code) { Ok "installed" } elseif (-not $Check) { Todo "VS Code did not install" }
}

Say "Claude Code"
if (Have claude) { Ok (claude --version 2>&1 | Select-Object -First 1) } else {
  if ($Check) { Todo "not installed" } else {
    try { irm https://claude.ai/install.ps1 | iex } catch { }
    RefreshPath
    $bin = "$env:USERPROFILE\.local\bin"
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($userPath -notlike "*$bin*") { [Environment]::SetEnvironmentVariable("Path", "$userPath;$bin", "User") }
    $env:Path += ";$bin"
    if (Have claude) { Ok (claude --version 2>&1 | Select-Object -First 1) } else { Todo "Claude Code did not install" }
  }
}

Say "Codex"
if (Have codex) { Ok (codex --version 2>&1 | Select-Object -First 1) } else {
  if ($Check) { Todo "not installed (optional)" } else {
    if (Have npm) { npm install -g @openai/codex | Out-Null; RefreshPath }
    if (Have codex) { Ok (codex --version 2>&1 | Select-Object -First 1) } else { Todo "Codex did not install (optional, Claude Code is enough to start)" }
  }
}

Say "Key file"
$envFile = Join-Path $Root ".env"
if (Test-Path $envFile) { Ok ".env exists" } else {
  if ($Check) { Todo ".env not created yet" } else {
    Copy-Item (Join-Path $Root ".env.example") $envFile
    Ok ".env created from .env.example. Keys go in there, never in chat."
  }
}
if ((Have git) -and (Test-Path (Join-Path $Root ".git"))) {
  git -C $Root check-ignore -q .env 2>$null
  if ($LASTEXITCODE -eq 0) { Ok "git ignores .env" } else { Todo "git does not ignore .env. Check .gitignore." }
}

Say "System check"
if ($py) {
  & $py (Join-Path $Root "Tools\check.py")
  if ($LASTEXITCODE -ne 0) { Todo "the system check did not pass" }
} else { Todo "no Python, so the system check could not run" }

Write-Host ""
if ($Problems -eq 0) { Write-Host "Everything is in place." } else { Write-Host "$Problems thing(s) still to do, marked todo above." }
Write-Host ""
Write-Host "Next: close this window and open a new one so the new programs are found."
Write-Host "Open this folder in VS Code or a terminal, run 'claude' to sign in, then type /onboard."
Write-Host "Claude Code needs a paid Claude plan to sign in."
