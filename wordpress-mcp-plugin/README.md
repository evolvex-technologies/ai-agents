# WordPress REST API MCP Plugin

A Claude MCP plugin for managing your self-hosted WordPress site. Read, write, and automate your WordPress content directly from Claude.

## What It Does

- **Get Posts** — Retrieve posts filtered by status, date, or count
- **Create Posts** — Write new posts/pages as drafts, scheduled, or published
- **Publish Scheduled Posts** — Automate publishing workflow
- **Get Analytics** — View publishing metrics and content statistics

## Setup

### 1. Configure Environment Variables

Copy `.env.template` to `.env`:

```bash
cp .env.template .env
```

Edit `.env` with your WordPress details:

```
WORDPRESS_URL=https://638331.us26.myftpupload.com
WORDPRESS_USERNAME=admin
WORDPRESS_PASSWORD=<retrieve from macOS Keychain>
```

**Security:** 
- Retrieve your application password from macOS Keychain (don't hardcode it)
- Never commit `.env` to version control
- Add `.env` to `.gitignore`

### 2. Connect the Plugin

1. In Cowork, install this plugin
2. The MCP server will use the credentials in `.env` to authenticate with WordPress
3. The 4 skills will appear in your `/` menu

### 3. Use the Skills

Type `/` in Cowork to see available skills:

- `/get-posts` — Retrieve WordPress posts
- `/create-post` — Write a new post
- `/publish-scheduled-post` — Publish scheduled posts
- `/get-analytics` — View site metrics

## WordPress Requirements

- Self-hosted WordPress (wordpress.org, not wordpress.com)
- REST API enabled (enabled by default in modern WordPress)
- An admin account with an application password

### Create an Application Password

1. Log in to WordPress as admin
2. Go to Users → Your Profile
3. Scroll to "Application Passwords"
4. Enter a name (e.g., "Claude MCP") and click "Create"
5. Copy the password to macOS Keychain
6. Add to `.env` as `WORDPRESS_PASSWORD`

## MCP Configuration

The plugin uses WordPress REST API v2 with Basic Authentication:

- **Endpoint**: `https://your-site.com/wp-json/wp/v2`
- **Auth**: HTTP Basic Auth (username + application password)
- **Tools**: 4 core tools for posts, publishing, and analytics

## Project Structure

```
wordpress-mcp-plugin/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
├── .mcp.json                # WordPress REST API MCP config
├── .env.template            # Environment variable template
├── .env                      # Your actual credentials (gitignored)
├── skills/
│   ├── get-posts/
│   ├── create-post/
│   ├── publish-scheduled-post/
│   └── get-analytics/
└── README.md                # This file
```

## Security Notes

- Credentials are stored in `.env` and referenced by the MCP server
- Never share or commit `.env` to version control
- Use application passwords (not your WordPress password) for API access
- Store credentials in macOS Keychain for extra security

## Troubleshooting

**Plugin won't connect:**
- Verify `.env` is present and has correct values
- Check WordPress site URL is accessible
- Confirm REST API is enabled on your WordPress site
- Test credentials in Keychain

**Skills not appearing:**
- Restart Cowork
- Verify plugin is installed in Cowork settings
- Check plugin.json is valid JSON

## Version

v0.1.0 — Initial release

## Author

Somya
