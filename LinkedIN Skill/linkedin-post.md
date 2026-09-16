# linkedin-post

Creates a complete EvolveX Technologies LinkedIn post: the text copy in EvolveX's brand voice plus a branded visual generated directly inside the template frame using Nano Banana 2 with the template as `image_input`.

**Company:** EvolveX Technologies Pvt. Ltd. — AI Automation & RPA Solutions ([evolvextechnologies.com](https://evolvextechnologies.com/))
**Mission:** Unlock limitless potential and lead the future with innovative technologies.
**Tagline:** Powered by People, Driven by Innovation.
**LinkedIn:** [linkedin.com/company/evolvextechnologies](https://www.linkedin.com/company/evolvextechnologies/)

---

## Project Directories

| Resource | Path |
|---|---|
| Root | `/Users/SAM/Downloads/repositories/ai-agents/LinkedIN Skill/` |
| Nano Banana 2 | `…/Nano Banana 2/` |
| Template PNG | `…/Linkedin Post Template.png` (1080×1080 px) |
| Scripts | `…/Nano Banana 2/scripts/` |
| Prompts | `…/Nano Banana 2/prompts/` |
| Image output | `…/Nano Banana 2/images/posts/` |
| Brand style ref | `…/Nano Banana 2/prompts/context_04_over_specified_md.json` |
| Logo assets | `…/Nano Banana 2/assets/logo/` (SVG + @2x/@4x PNG) |
| Template builder script | `…/Nano Banana 2/scripts/build_template.py` |

---

## STEP 1 — Ask for Topic

Ask the user exactly this:

> "What topic would you like to create a LinkedIn post about?"

Wait for the response before continuing.

---

## STEP 2 — Ensure Template is on GitHub

The Kie.ai API requires a **publicly accessible URL** for `image_input`. The template must be hosted in a public GitHub repo.

**Check if the template is already pushed:**
```bash
curl -s -o /dev/null -w "%{http_code}" \
  "https://raw.githubusercontent.com/evolvex-technologies/ai-agents/main/LinkedIN%20Skill/Linkedin%20Post%20Template.png"
```

If the response is **200**, the template is already there — skip to the URL assignment below.

**If not 200 (first time only):** the template lives in this repo — commit and push it:
```bash
cd "/Users/SAM/Downloads/repositories/ai-agents"
git add "LinkedIN Skill/Linkedin Post Template.png"
git commit -m "Add LinkedIn post template"
git push origin main
```

**Set the permanent raw URL:**
```
TEMPLATE_URL = https://raw.githubusercontent.com/evolvex-technologies/ai-agents/main/LinkedIN%20Skill/Linkedin%20Post%20Template.png
```

This URL never expires — no re-upload needed on subsequent runs.

---

## STEP 3 — Generate the Post Text

Write a LinkedIn post in EvolveX Technologies' brand voice — the collective voice of the EvolveX team, not a named individual. Follow every rule below.

### Structure (in order)
1. **Hook** (1 sentence) — Bold, direct, sometimes provocative. Can be a statement or question. Optional single emoji at the end.
2. **Relatability bridge** (1–2 sentences) — a common assumption/frustration the reader (an ops leader, founder, or department head) has about manual, repetitive work. NEVER open with "You know the drill." — that phrase is banned.
3. **Client/implementation story** (3–5 sentences) — Open with "We recently…" or "One of our clients was stuck with…". A specific, concrete example grounded in real automation work (RPA rollout, agentic AI workflow, document processing, CRM/ERP integration). Real detail, not generic.
4. **Revelation** (1–2 sentences) — "Here's where it got interesting…" or describe the measurable result (time saved, error rate down, hours reclaimed).
5. **Broader lesson** (2–3 sentences) — What does this mean for the reader's business? Draw the bigger implication about automation done right.
6. **CTA** (1 sentence) — Direct engagement question + 1 emoji. Examples: "Curious how this could work for your team? Let's talk! 😁" / "Dealing with something similar? Let's exchange."

### Tone & Format Rules
- Conversational and honest — sounds like a team sharing real client work, not a marketer
- Short paragraphs (1–3 sentences each), separated by a blank line
- Heavy use of "we" and "you" — personal, never corporate-speak
- Enthusiastic but grounded — never hype-y, never "game-changing" or "revolutionary"
- 180–200 words total. Shorter reads better than longer; never exceed 250.
- NO emojis anywhere in the post
- Simple, plain English a general LinkedIn audience understands, not industry insiders. Avoid unexplained jargon (DSO, cash application, remittance data, working capital, three-way matching); drop the term or say it plainly.
- Must read like a human wrote it, not like generated marketing copy
- No bullet lists, UNLESS the post is a "playbook" format — in that case numbered items are fine
- Never use: "synergy", "leverage", "innovative", "cutting-edge", "unlock", "game-changer"
- Never use em dashes (—). Use a comma, period, or "and" instead.
- Never open with "You know the drill."

### Core Themes (content pillars)
- Robotic Process Automation (RPA) capabilities and real-world use cases
- Agentic AI automation and what it actually delivers in production
- Intelligent Document Processing — accuracy, speed, and eliminating manual data entry
- CRM/ERP automation with practical business impact (sales, finance, operations)
- The honest limits of automation (what still needs a human in the loop)
- Industry-specific wins (Banking & Finance, Healthcare, Real Estate, Insurance, Logistics, Media & Entertainment)

### Voice Reference (3 example post structures)
- **Post 1 (RPA intro):** "Most 'automation' projects fail before they save a single hour." → "We know what you think — another automation vendor." → story about a mortgage firm's manual loan setup process automated in weeks, not months → they saved $200K and stopped drowning in paperwork → "THAT'S what automation should feel like."
- **Post 2 (Agentic AI for compliance):** Sell-off hook → "That's not completely true, but close." → built an agentic workflow that handles quarterly tax declarations end-to-end → "The system flags exceptions and routes them to a human — it doesn't just blindly execute."
- **Post 3 (Automation playbook):** "Stop automating the wrong things. 🛑" → numbered 3-rule playbook for choosing what to automate first → "The Hard Limit? Judgment calls that carry legal or reputational risk." → automation handles volume, people handle exceptions.

---

## STEP 4 — Choose a Visual Format

Read `context_04_over_specified_md.json` `_visual_formats` block and pick the best fit:

| Format | When to use |
|---|---|
| **A — Bold Text + Person** | Personal/inspirational posts. Large title text + photorealistic confident male figure. |
| **B — Tech Infographic** | Framework, system, or multi-part concept posts. Connected hexagonal nodes + orange lines. |
| **C — Split Layout** | Contrast/comparison posts. Two-column (e.g., AUTOMATE vs KEEP HUMAN) with central divider. |

Identify the 3–5 key concepts/elements that need to appear as labeled nodes or text in the visual.

---

## STEP 5 — Build the Nano Banana 2 Prompt

Use the **Dense Narrative Format** with `image_input`. Nano Banana 2 receives the template as a structural reference and generates the inner content directly inside it.

### How `image_input` changes the prompt strategy
- The template (light pink card, 1080×1080) provides: an `EVOLVEX · INSIGHT` label (top-left), a magenta heading placeholder `[ Your Heading Goes Here ]` between two vertical accent bars, a gray subheading placeholder `[ Optional subheading or supporting line goes here ]`, a large empty content panel in the middle, the `evolvextechnologies.com` footer (bottom-left), and the evolvex logo (bottom-right)
- The prompt must **explicitly replace both placeholder texts** with the real heading/subheading — instruct "replace the placeholder text '[ Your Heading Goes Here ]' with '<actual heading>' in the same magenta color, font style, size and position", and the same for the subheading. If you only say "keep everything", the placeholders are rendered literally.
- The prompt instructs the model to **fill the empty content panel** with the visual concept
- Explicitly tell the model to **preserve** the `EVOLVEX · INSIGHT` label, footer URL, and logo exactly — never alter, move, or duplicate them

### Mandatory Brand Rules (never skip)
These colors are lifted directly from the EvolveX logo mark — don't substitute other brand colors.
- **Primary accent**: Orange (#F1600A) — title glow, connecting lines, warm highlights (bottom-right glow)
- **Secondary accent**: Magenta/pink (#EE2A7B) — frame line, icon borders, connecting nodes
- **Tertiary accent**: Purple (#6228D7) — secondary glows, node fills (top-left glow)
- **Quaternary accent**: Gold (#F9CE34) — sparing use for highlight sparkle/metric callouts
- **Wordmark color**: Dark magenta (#9E166A) — only appears inside the logo itself, never reproduce it elsewhere in generated content
- **Text**: White labels (#ffffff), warm orange or pink glow on main title/headline
- **Icon style**: Hexagonal or circular floating nodes with dark plum interior + thin pink/purple border glow
- **Connections**: Thin pink-to-orange gradient lines with glowing dot endpoints between nodes
- **Bottom-right corner**: ALWAYS leave the EvolveX logo chip untouched — explicitly tell the model not to alter it
- **NO extra logos, NO added company text** — only preserve what the template already has

### JSON structure to use (nano-banana-2 `input` format):
```json
{
  "model": "nano-banana-2",
  "input": {
    "prompt": "Using the reference image as the exact layout template: replace the placeholder heading text '[ Your Heading Goes Here ]' with '<ACTUAL HEADING>' in the same magenta color, same bold font style, same size and position between the two vertical accent bars. Replace the placeholder line '[ Optional subheading or supporting line goes here ]' with '<ACTUAL SUBHEADING>' in the same gray color and size. Keep the 'EVOLVEX · INSIGHT' label, the light pink background, the evolvextechnologies.com footer text, and the evolvex logo in the bottom-right corner exactly as shown — do not alter, move, or duplicate them. Fill the large empty content panel in the middle with: <dense narrative of the visual concept — nodes, labels, icons, connecting lines>. Accents: orange #F1600A, magenta #EE2A7B, purple #6228D7, sparing gold #F9CE34. All text must be sharp, correctly spelled, and legible.",
    "negative_prompt": "placeholder text, bracket characters, '[' or ']' symbols, 'Your Heading Goes Here', 'Optional subheading', misspelled words, blurry text, dark background, teal tones, blue tones, added logos, added wordmarks, altering the footer, altering the logo, clutter",
    "image_input": [
      "https://raw.githubusercontent.com/evolvex-technologies/ai-agents/main/LinkedIN%20Skill/Linkedin%20Post%20Template.png"
    ],
    "aspect_ratio": "1:1",
    "resolution": "1K",
    "output_format": "jpg"
  }
}
```

**Note:** Use the `"model": "nano-banana-2"` + `"input": {}` wrapper format exactly as shown — the API key is authorized for `nano-banana-2` only (`nano-banana-pro` returns 401 "not authorized to use this model"). Verified working 2026-07-27.

---

## STEP 6 — Ensure .env is Configured

Check if `/Users/SAM/Downloads/repositories/ai-agents/LinkedIN Skill/Nano Banana 2/.env` exists.

**If it does NOT exist:**
1. Read `/Users/SAM/Downloads/repositories/ai-agents/LinkedIN Skill/.env`
2. Find the line starting with `Kie_AI_API_KEY=` and extract the value
3. Create `Nano Banana 2/.env` with exactly this content:
   ```
   KIE_API_KEY="<extracted_value>"
   ```

---

## STEP 7 — Save Prompt and Generate Image

1. Create a slug from the topic (lowercase, hyphens, max 30 chars). E.g. "AI agents for sales" → `ai-agents-for-sales`

2. Save the prompt JSON (with the GitHub raw URL already in `image_input`) to:
   ```
   …/Nano Banana 2/prompts/post_<slug>.json
   ```

3. Create output directory if needed:
   ```bash
   mkdir -p "/Users/SAM/Downloads/repositories/ai-agents/LinkedIN Skill/Nano Banana 2/images/posts"
   ```

4. Generate:
   ```bash
   cd "/Users/SAM/Downloads/repositories/ai-agents/LinkedIN Skill/Nano Banana 2"
   python3 scripts/generate_kie.py \
     "prompts/post_<slug>.json" \
     "images/posts/<slug>_final.jpg" \
     "1:1"
   ```

---

## STEP 8 — Deliver Results

Present in this order:

### 1. LinkedIn Post Text
Show the full post text, formatted exactly as it would appear on LinkedIn (blank lines between paragraphs, ready to copy-paste).

### 2. Final Visual
Read and display:
```
/Users/SAM/Downloads/repositories/ai-agents/LinkedIN Skill/Nano Banana 2/images/posts/<slug>_final.jpg
```

### 3. File Locations
- Final image: `…/Nano Banana 2/images/posts/<slug>_final.jpg`
- Prompt used: `…/Nano Banana 2/prompts/post_<slug>.json`

---

## STEP 9 — Ask for Approval and Post to LinkedIn

**CRITICAL RULES:**
- NEVER post without explicit approval
- Always show the post text and final image first (Step 8)
- Always ask: "Are you satisfied with the post and visual?" and wait for a clear "yes" before publishing

Once approved, post using the Python script at:
```
/Users/SAM/Downloads/repositories/ai-agents/LinkedIN Skill/linkedin_post.py
```

**Text-only post:**
```bash
python3 "/Users/SAM/Downloads/repositories/ai-agents/LinkedIN Skill/linkedin_post.py" "FULL POST TEXT HERE"
```

**Post with image** — pass the image path as a second argument:
```bash
python3 "/Users/SAM/Downloads/repositories/ai-agents/LinkedIN Skill/linkedin_post.py" \
  "FULL POST TEXT HERE" \
  "/Users/SAM/Downloads/repositories/ai-agents/LinkedIN Skill/Nano Banana 2/images/posts/<slug>_final.jpg"
```

**First-time / token expired:** The script opens a browser for LinkedIn OAuth and saves the token to `.linkedin_token.json` next to the script. All subsequent runs reuse the saved token silently.

**On success:** The script prints the post ID.

---

## Error Handling

| Error | Action |
|---|---|
| Template URL returns non-200 | Push the template to GitHub using the commands in Step 2. |
| GitHub push fails (auth) | Run `gh auth login` and retry the push. |
| `generate_kie.py` fails with auth error | Check `KIE_API_KEY` in `Nano Banana 2/.env`. |
| Task state goes to "fail" or API returns 500 | Likely temporary Kie.ai overload. Wait 30 seconds and retry. |
| `generate_kie.py` times out (60 polls) | Report the task ID and check the Kie.ai dashboard. |
| Output image looks off (border missing, colors wrong) | Offer to regenerate. Try reinforcing preservation language in the prompt: "Do not modify the outer frame, border, or logo in any way." |
