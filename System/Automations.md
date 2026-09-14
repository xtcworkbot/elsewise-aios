# Automations

Everything that runs on its own. A scheduled job is a tool, not an agent. It does one thing at a set time and must fail loudly.

Nothing runs automatically until a process has worked by hand first.

| Job | What it does | Where it runs | When | Output goes to | How to stop it | Last successful run |
|---|---|---|---|---|---|---|
| None yet | | | | | | |

Rules for adding one:

1. The process has already worked by hand, more than once.
2. One job per task. Check this table before creating one, so it never runs twice.
3. It says where it runs. A job on a laptop does not run when the laptop is closed.
4. It reports a failure somewhere the owner will see it.
5. Its row is added here the same session.
