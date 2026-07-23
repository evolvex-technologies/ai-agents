---
name: create-post
description: Create a new post or page in WordPress with title, content, status, categories, and more
keywords: [wordpress, create, new post, draft, publish, writing, content]
---

# Create WordPress Post

Create a new post in WordPress. Set title, content, status (draft/published/scheduled), categories, tags, and excerpt.

## Usage

Call the WordPress MCP tool `create_post` with these parameters:

**title** (required): Post title

**content** (required): Post content in HTML or plain text

**status** (optional): "draft" (default), "publish", or "scheduled"

**categories** (optional): Array of category IDs

**excerpt** (optional): Short summary of the post

**date** (optional): Publish date in ISO 8601 format (e.g., "2026-07-25T15:00:00") for scheduling

## Examples

When the user says:
- "Create a draft post titled 'New Article'" — call with title, content, status "draft"
- "Publish a post about X" — call with status "publish"
- "Schedule a post for July 25th" — call with date in ISO 8601 format, status "scheduled"
- "Create a post in the 'News' category" — call with categories array containing category ID

Returns the new post's ID, URL, and confirmation of status.
