---
name: get-analytics
description: Get WordPress site analytics — post counts by status, recent activity, and publishing metrics
keywords: [wordpress, analytics, stats, metrics, dashboard, reporting]
---

# Get WordPress Analytics

Retrieve analytics and publishing metrics from your WordPress site. View post counts by status (published, draft, scheduled), recent activity, and publishing trends.

## Usage

Call the WordPress MCP tool `get_analytics` with:

**include_recent_days** (optional): Include post counts from the last N days (e.g., 7 for last week, 30 for last month)

## What You Get

- Total post counts by status: published, draft, scheduled, pending
- Posts created in the recent period (if specified)
- Posts by category
- Publishing trends and activity summary

## Examples

When the user says:
- "Show me my WordPress stats" — call without parameters for all-time totals
- "How many posts did I publish this week?" — call with include_recent_days 7
- "What's my posting activity this month?" — call with include_recent_days 30
- "How many drafts do I have?" — call without parameters to get status breakdown

Returns a summary dashboard of your WordPress site's content metrics.
