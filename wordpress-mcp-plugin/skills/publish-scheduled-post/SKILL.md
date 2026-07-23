---
name: publish-scheduled-post
description: Publish a scheduled WordPress post immediately by post ID
keywords: [wordpress, publish, schedule, post, workflow, automation]
---

# Publish Scheduled Post

Publish a WordPress post that's currently in scheduled status. Useful for automating your publishing workflow.

## Usage

Call the WordPress MCP tool `publish_scheduled_post` with:

**post_id** (required): The ID of the scheduled post to publish immediately

## How to Use

1. First, retrieve your scheduled posts using the "get-posts" skill with status "scheduled"
2. Find the post ID you want to publish
3. Call this skill with that post ID to publish it immediately

## Examples

When the user says:
- "Publish post #42" — call with post_id 42
- "Publish my scheduled posts" — first get scheduled posts, then publish each by ID
- "Publish the article about X that's scheduled" — get scheduled posts, find the matching ID, then publish

Returns confirmation of publication with the post URL and new status.
