# WordPress MCP Plugin - Setup Guide

Your plugin is configured to fetch credentials from the `.env` file. Here's how to set it up.

## Quick Start

### 1. Run the Setup Script

```bash
cd /Users/SAM/Downloads/repositories/claude/wordpress-mcp-plugin
./setup.sh
```

The script will:
- Attempt to retrieve your password from macOS Keychain (where you stored it earlier)
- If found, automatically populate `.env` with the password
- If not found, prompt you to enter it manually

### 2. Verify `.env` is Configured

Check that `.env` has your WordPress credentials:

```bash
cat .env
```

You should see:
```
WORDPRESS_URL=https://638331.us26.myftpupload.com
WORDPRESS_USERNAME=admin
WORDPRESS_PASSWORD=Os4e1BwsFQ9aXXXXXXXXXXXXXXXXX
```

### 3. Install the Plugin in Cowork

The plugin is ready to install in Cowork. The MCP server will read credentials from `.env` automatically.

## Manual Setup (if script fails)

If `setup.sh` doesn't find your password:

1. **Open Keychain Access:**
   ```bash
   open /Applications/Utilities/Keychain\ Access.app
   ```

2. **Search for your WordPress password** (search for "WordPress" or "claude")

3. **Copy the password** and paste into `.env`:
   ```
   WORDPRESS_PASSWORD=<your_password_here>
   ```

## Security Notes

- ✅ `.env` is in `.gitignore` — it won't be committed to Git
- ✅ Password is stored in a local file, not hardcoded in config
- ✅ Original password remains in macOS Keychain
- ⚠️ Never share or commit `.env` to version control
- ⚠️ If you share this repo, anyone with access to `.env` has your WordPress admin password

## Troubleshooting

**Script says "Password not found in Keychain":**
- Your password may be stored under a different name in Keychain
- Use manual setup: open Keychain Access and search for it
- Or enter it when prompted

**MCP connection fails:**
- Verify `.env` has correct URL, username, and password
- Check WordPress REST API is enabled on your site
- Confirm your WordPress site is accessible over HTTPS

**Need to update password:**
- Edit `.env` directly, or re-run `./setup.sh`
- Always keep `.env` secure and never commit it

## File Structure

```
wordpress-mcp-plugin/
├── .env              ← Your credentials (gitignored, never commit)
├── .env.template     ← Template reference
├── setup.sh          ← Automated setup script
├── .gitignore        ← Prevents accidental commits
├── .mcp.json         ← MCP server configuration
├── .claude-plugin/
│   └── plugin.json   ← Plugin manifest
├── skills/           ← 4 reusable skills
├── README.md         ← Full documentation
└── SETUP.md          ← This file
```
