---
name: get-posts
description: Retrieve posts from your WordPress site, filtered by status, date range, or count
keywords: [wordpress, posts, content, retrieve, blog, read]
---

# Get WordPress Posts

Retrieve posts from your WordPress site with optional filters by status (published, draft, scheduled, pending), limit results, and sort order.

## Usage

Call the WordPress MCP tool `get_posts` with these parameters:

**status** (optional): Filter by post status — "publish", "draft", "scheduled", or "pending"

**per_page** (optional): Number of posts to return — defaults to 20, max 100

**orderby** (optional): Sort results by "date" (newest first), "title", or "id"

## Examples

When the user asks:
- "Show me my recent posts" — call with status "publish", per_page 10
- "What drafts do I have?" — call with status "draft"
- "List all scheduled posts" — call with status "scheduled"
- "Get 5 oldest posts" — call with orderby "date", per_page 5

Returns for each post: ID, title, status, publish date, excerpt, categories, and URL.
