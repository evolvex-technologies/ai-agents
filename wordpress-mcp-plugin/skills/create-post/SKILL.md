---
name: create-post
description: Create a new WordPress post — either from scratch or by cloning an existing post as a template and adapting its content to a new title/topic. Use whenever the user wants to write a new post, draft/publish/schedule a post, or duplicate a post ("create a post like this one but about X", "clone post 123 for a new topic", "write a post based on our last case study but for healthcare"). Set title, content, status, categories, and excerpt. The template can be referenced by title, slug, ID, or URL.
keywords: [wordpress, create, new post, draft, publish, clone, template, duplicate, writing, content]
---

# Create WordPress Post

Create a new post in WordPress. Two modes:

1. **From scratch** — the user gives a title and content (or a topic to write about).
2. **From a template post** — the user points at an existing post to clone, and the new post copies its full structure and copy, then rewrites the wording to fit the new title/topic.

Set title, content, status (draft/publish/scheduled), categories, and excerpt. Default to `draft` so the user reviews before it goes live.

## Mode 1 — From scratch

Call `POST {WORDPRESS_URL}/wp-json/wp/v2/posts` (or the `create_post` MCP tool) with:

**title** (required): Post title
**content** (required): Post content in HTML/Gutenberg blocks or plain text
**status** (optional): "draft" (default), "publish", or "future" (scheduled)
**categories** (optional): Array of category IDs
**excerpt** (optional): Short summary
**date** (optional): ISO 8601 date (e.g. "2026-07-25T15:00:00") — required when scheduling

## Mode 2 — Clone a template post and adapt to the new title

When the user references an existing post as the template ("based on", "like", "clone", "same format as"), reproduce its full structure and copy, then re-topic the words for the new title. The point is a publish-ready draft that mirrors a proven post, not an empty shell.

1. **Resolve the template post.** User gives a title, slug, ID, or URL.
   - By ID: `GET {WORDPRESS_URL}/wp-json/wp/v2/posts/{id}?context=edit`
   - By URL: extract the slug from the path → `GET .../posts?slug={slug}`
   - By title: `GET .../posts?search={title}&per_page=10`, match case-insensitively; if several match, list them with IDs and ask which one.
   - Prefer `context=edit` (authenticated) to get `content.raw` — the true block markup clones far more faithfully than rendered HTML. Fall back to `content.rendered` only if auth is unavailable.

2. **Clone the full content, then adapt it to the new title.**
   - **Keep** the complete structure: every heading, paragraph, list, quote, column, button, and image block, in the same order and roughly the same length, so the article stays balanced.
   - **Rewrite the words** to match the new title/topic. Swap the template's subject for the new one everywhere it appears — headline, intro hook, section headings, body copy, examples, list items, and any call to action. Re-express examples for the new domain rather than leaving the old ones.
   - **Preserve** the template's voice, tone, and rhythm — the whole reason to clone is to reuse a format that works.
   - **Images**: keep image blocks in place and reuse the template's image URLs (they still render) unless the user asks to swap them. Don't invent image URLs.
   - **Excerpt & SEO**: adapt the excerpt to the new topic too, if the template had one.
   - **Categories/tags**: reuse the template's unless the new topic clearly belongs elsewhere; when unsure, ask or default to the template's.
   - **Don't fabricate specifics.** Keep claims generic for the new topic rather than inventing client names, statistics, or certifications that were only true for the template's subject.

3. **Create the new post.** `POST .../posts` with the adapted `title`, `content`, `status` (`draft` unless told otherwise), and adapted `excerpt`/`categories`.

4. **Confirm.** Report the new post's ID, URL, edit link (`{WORDPRESS_URL}/wp-admin/post.php?post={id}&action=edit`), status, and a one-line note on what you adapted so the user knows what to spot-check.

## Authentication

Credentials come from the plugin's `.env` file (`WORDPRESS_URL`, `WORDPRESS_USERNAME`, `WORDPRESS_PASSWORD`). Use HTTP Basic Auth with the application password. Reading published posts works without auth; reading raw content (`context=edit`) and creating posts require it.

If a network sandbox blocks the authenticated POST (a 403 from a proxy on the write while reads succeed), the request is fine but the environment is restricting it. Post instead from a context with direct network access — the user's Chrome browser (a same-origin `fetch` to `/wp-json/wp/v2/posts` with the Basic Auth header) or a ready-to-run script that reads `.env` and POSTs. Don't report this as a skill failure; it's an environment constraint with a known workaround.

## Examples

**"Create a draft post titled 'New Article' about our Q3 results"** (from scratch)
→ Write the content → POST draft with title, content.

**"Write a post like our 'RPA saves $200K' case study, but about an Agentic AI project"** (clone + adapt)
→ Resolve the case-study post → clone its structure → rewrite the story, figures framing, and headings for the Agentic AI project (without inventing specific numbers) → POST draft → note what changed.

**"Clone post 11905 for the healthcare industry and schedule it for next Monday 9am"**
→ GET post 11905 raw content → re-topic for healthcare → POST with status "future" and the ISO date.

## Edge cases

- **Template not found**: list the 10 most recent posts with titles and IDs so the user can pick.
- **Ambiguous title match**: show candidates, ask.
- **Scheduling**: WordPress uses status `future` plus a future `date` (site timezone). Setting a future date with status `publish` still schedules it, but prefer `future` for clarity.
- **Duplicate title**: allowed; create it but mention the existing post with the same title.
