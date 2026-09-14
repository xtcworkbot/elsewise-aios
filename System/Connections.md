# Connections

Every tool and account the assistant can reach. Filled by onboarding with the tools the owner uses. Updated every time a tool is connected, tested or removed.

Configured, signed in and tested are three different things. Only a test with a real result counts as working.

| Area | Tool | How the assistant reaches it | Status | Last tested | Detail |
|---|---|---|---|---|---|
| Email | Not set yet | Not connected | Not connected | Never | |
| Calendar | Not set yet | Not connected | Not connected | Never | |
| Files and documents | Not set yet | Not connected | Not connected | Never | |
| Customers and sales | Not set yet | Not connected | Not connected | Never | |
| Money and accounting | Not set yet | Not connected | Not connected | Never | |
| Marketing and social | Not set yet | Not connected | Not connected | Never | |
| Messaging | Not set yet | Not connected | Not connected | Never | |

Ways a tool can be reached: a connector built into Claude or Codex, a script in `Tools/` using a key in `.env`, or an export file the owner drops in. Status is one of: not connected, configured, signed in, tested.

The first two to connect, from onboarding: not set yet.

Key values never go in this file. Write only the name of the key, for example `GMAIL_APP_PASSWORD`.
