---
name: create-page-from-template
description: Create a new WordPress page by cloning an existing page and adapting its content to a new title/topic. Use whenever the user wants to duplicate a page, clone a page, create a page "like" or "based on" another page, or spin up a new page that mirrors an existing one but is about a different subject (e.g. "create an Agentic AI page based on the RPA Consulting page", "clone the Services page as a new Consulting page", "make a page like page 42 but for Pricing"). The template can be referenced by title, slug, ID, or URL.
keywords: [wordpress, page, template, clone, duplicate, copy, layout, create, adapt]
---

# Create WordPress Page from Template

Create a new WordPress page that clones an existing page in full — its complete layout AND its text — then rewrites the copied text so it fits the new title and topic. The new page is saved as a draft so the user can review before publishing.

## Why full-clone-and-adapt

The template's value is both its layout and its proven copy. A visitor-ready page needs real words, not empty placeholders. So copy everything — headings, sections, paragraphs, lists, buttons, image blocks — and then transform the wording from the template's topic to the new page's topic. The result is a complete, on-brand page the user can publish after a light review, not a blank skeleton they have to fill in from scratch.

## Workflow

1. **Resolve the template page.** The user gives a title, slug, ID, or URL.
   - By ID: `GET {WORDPRESS_URL}/wp-json/wp/v2/pages/{id}?context=edit`
   - By URL: extract the slug from the path and use `GET {WORDPRESS_URL}/wp-json/wp/v2/pages?slug={slug}`.
   - By title: `GET {WORDPRESS_URL}/wp-json/wp/v2/pages?search={title}&per_page=10`, then match the title (case-insensitive). If several match, list them with IDs and ask which to use.
   - If the title search finds nothing (or only body-text matches), try slug lookups: `?slug={kebab-case-title}` and common variants (e.g. "About" → `about`, `about-us`). Pages are often titled differently from how users refer to them. When a slug hit's title doesn't literally match what the user said, confirm before proceeding.
   - Prefer `context=edit` (authenticated) to get `content.raw` — the true block markup, which clones far more faithfully than rendered HTML. Fall back to `content.rendered` only if auth is unavailable.

2. **Clone the full content, then adapt it to the new title.** Take the template's entire content and transform it so it's about the new topic:
   - **Keep** the complete structure: every heading, paragraph, list, column, button, separator, and image block, in the same order.
   - **Rewrite the words** to match the new title. Swap the template's subject for the new one everywhere it appears — headings, body paragraphs, list items, button labels, calls to action. For example, cloning an "RPA Consulting & Integration" page into "Agentic AI Automation" means every "RPA"/"Robotic Process Automation" reference becomes the Agentic-AI equivalent, and the feature descriptions are re-expressed for AI agents rather than RPA bots.
   - **Preserve** each section's intent and length so the layout stays balanced — rewrite a 3-bullet list as a 3-bullet list about the new topic, not a single line.
   - **Images**: keep image blocks in place. Reuse the template's image URLs (they still render) unless the user asks to swap them; the user can replace visuals later. Don't invent image URLs.
   - Make the new title the page's main `<h1>`/hero heading.
   - Keep the writing consistent with the template's voice and the site's brand. Don't fabricate specific facts (client names, statistics, certifications) that wouldn't be true for the new topic — generalize or omit rather than invent.

3. **Create the new page.**
   `POST {WORDPRESS_URL}/wp-json/wp/v2/pages` with:
   - `title`: the new page title from the user
   - `content`: the cloned-and-adapted content
   - `status`: `draft` (always, unless the user explicitly asks to publish)
   - `parent`: copy from template only if the user asks for the same page hierarchy

4. **Confirm.** Report the new page's ID, title, edit link (`{WORDPRESS_URL}/wp-admin/post.php?post={id}&action=edit`), that it's a draft, and briefly note what you adapted so the user knows what to spot-check (e.g. "rewrote all six feature sections for Agentic AI; kept the original section images as placeholders").

## Authentication

Credentials come from the plugin's `.env` file (`WORDPRESS_URL`, `WORDPRESS_USERNAME`, `WORDPRESS_PASSWORD`). Use HTTP Basic Auth with the application password. Reading published pages works without auth; reading raw content (`context=edit`) and creating pages require it.

If a network sandbox blocks the authenticated POST (a 403 from a proxy on the write request while reads succeed), the request is fine but the environment is restricting it. Post it instead from a context with direct network access — the user's Chrome browser (a same-origin `fetch` to `/wp-json/wp/v2/pages` with the Basic Auth header) or by handing the user a ready-to-run script that reads `.env` and POSTs. Don't report this as a skill failure; it's an environment constraint with a known workaround.

## Examples

**"Create an 'Agentic AI Automation' page based on the RPA Consulting & Integration page"**
→ Resolve the RPA page → clone its full content → rewrite every RPA reference and feature description for Agentic AI → POST draft "Agentic AI Automation" → return edit link and note what changed.

**"Clone page 1187 as a new page called 'Enterprise Pricing'"**
→ GET page 1187 raw content → adapt the copy for Enterprise Pricing → POST draft → confirm.

**"Make a Training page like our Consulting page"**
→ Resolve Consulting → clone and re-topic the content for Training → POST draft → confirm.

## Edge cases

- **Template not found**: list the 10 most recent pages with titles and IDs so the user can pick.
- **Ambiguous title match**: show the candidates, ask.
- **Page-builder pages (Avada/Fusion, Elementor, WPBakery)**: raw content is builder shortcodes/HTML tied to the builder, and a REST clone won't reproduce the builder styling exactly. Tell the user, then offer the best available path: (a) clone the content as clean Gutenberg blocks adapted to the new topic (loses builder-specific styling but is fully editable), or (b) use the builder's own "Clone/Duplicate" in wp-admin and then rewrite the copy. Proceed with (a) unless they prefer (b).
- **Duplicate title**: WordPress allows it; create the page but mention the existing page with the same title.
- **Don't invent facts**: when adapting copy, keep claims generic for the new topic rather than fabricating specific metrics, client names, or certifications that were true only for the template's subject.
