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
| Root | `/path/to/linkedin-post-system/` |
| Nano Banana 2 | `…/Nano Banana 2/` |
| Template JPG | `…/Linkedin Post Template.jpg` (1200×1500 px) |
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
  "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_PUBLIC_REPO/main/Linkedin%20Post%20Template.jpg"
```

If the response is **200**, the template is already there — skip to the URL assignment below.

**If not 200 (first time only):** push the template to GitHub:
```bash
cd /tmp && git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_PUBLIC_REPO.git 2>/dev/null || true
cp "/path/to/linkedin-post-system/Linkedin Post Template.jpg" \
  /tmp/YOUR_PUBLIC_REPO/
cd /tmp/YOUR_PUBLIC_REPO
git add "Linkedin Post Template.jpg"
git commit -m "Add LinkedIn post template"
git push origin main
```

**Set the permanent raw URL:**
```
TEMPLATE_URL = https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_PUBLIC_REPO/main/Linkedin%20Post%20Template.jpg
```

This URL never expires — no re-upload needed on subsequent runs.

---

## STEP 3 — Generate the Post Text

Write a LinkedIn post in EvolveX Technologies' brand voice — the collective voice of the EvolveX team, not a named individual. Follow every rule below.

### Structure (in order)
1. **Hook** (1 sentence) — Bold, direct, sometimes provocative. Can be a statement or question. Optional single emoji at the end.
2. **Relatability bridge** (1–2 sentences) — "You know the drill." or a common assumption/frustration the reader (an ops leader, founder, or department head) has about manual, repetitive work.
3. **Client/implementation story** (3–5 sentences) — Open with "We recently…" or "One of our clients was stuck with…". A specific, concrete example grounded in real automation work (RPA rollout, agentic AI workflow, document processing, CRM/ERP integration). Real detail, not generic.
4. **Revelation** (1–2 sentences) — "Here's where it got interesting…" or describe the measurable result (time saved, error rate down, hours reclaimed).
5. **Broader lesson** (2–3 sentences) — What does this mean for the reader's business? Draw the bigger implication about automation done right.
6. **CTA** (1 sentence) — Direct engagement question + 1 emoji. Examples: "Curious how this could work for your team? Let's talk! 😁" / "Dealing with something similar? Let's exchange."

### Tone & Format Rules
- Conversational and honest — sounds like a team sharing real client work, not a marketer
- Short paragraphs (1–3 sentences each), separated by a blank line
- Heavy use of "we" and "you" — personal, never corporate-speak
- Enthusiastic but grounded — never hype-y, never "game-changing" or "revolutionary"
- 180–280 words total
- Maximum 2 emojis in the entire post
- No bullet lists, UNLESS the post is a "playbook" format — in that case numbered items are fine
- Never use: "synergy", "leverage", "innovative", "cutting-edge", "unlock", "game-changer"

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
- The template provides: outer rounded glow frame, dark purple-to-orange gradient background, EvolveX logo on a light chip (bottom-right)
- The prompt instructs the model to **fill the empty inner content area** with the visual concept
- Explicitly tell the model to **preserve** the frame, background gradient, and logo chip exactly
- **CRITICAL: the scene background inside the card must match the template gradient** — near-black plum (#0b0710) in the upper-left fading through deep magenta-plum (#2a0f30) toward a warm orange glow (#F1600A) in the lower-right. Never introduce a mismatched or flat-color background. When the inner background matches the card, the seam becomes invisible.

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

### JSON structure to use (flat format — routes to nano-banana-pro):
```json
{
  "prompt": "Keep the outer rounded glow frame, background gradient, and EvolveX logo chip in the bottom-right corner exactly as shown in the reference image — do not alter or remove them. Fill the empty inner content area of the card with: <dense narrative of the visual concept — layout, title text, node labels, connecting lines, brand colors>. The scene background must match the card gradient (near-black plum fading to warm orange), not a mismatched color. Primary accent: orange (#F1600A). Secondary accent: magenta/pink (#EE2A7B). Tertiary accent: purple (#6228D7). Sparing gold (#F9CE34) highlights. White sans-serif labels.",
  "negative_prompt": "white background, light background, pastel colors, blurry text, low contrast, excessive circuit board clutter, teal tones, blue tones, added logos, added wordmarks, removing the existing border, removing the existing logo, altering the background gradient, mismatched scene background",
  "image_input": [
    "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_PUBLIC_REPO/main/Linkedin%20Post%20Template.jpg"
  ],
  "api_parameters": {
    "aspect_ratio": "4:5",
    "resolution": "1K",
    "output_format": "jpg"
  },
  "settings": {
    "style": "premium tech infographic, preserve reference template frame, clean accent visuals",
    "lighting": "ambient glow from orange and magenta/pink accents, subtle purple depth, sparing gold highlights",
    "quality": "high detail, sharp legible text, vibrant accents on dark plum-to-orange background"
  }
}
```

**Note:** No `"model"` key, no `"input"` wrapper. The flat structure with `api_parameters` routes automatically to `nano-banana-pro`. Never use the `"input": {}` wrapper — it routes to nano-banana-2 which produces a flat overlaid look.

---

## STEP 6 — Ensure .env is Configured

Check if `/path/to/linkedin-post-system/Nano Banana 2/.env` exists.

**If it does NOT exist:**
1. Read `/path/to/linkedin-post-system/.env`
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
   mkdir -p "/path/to/linkedin-post-system/Nano Banana 2/images/posts"
   ```

4. Generate:
   ```bash
   cd "/path/to/linkedin-post-system/Nano Banana 2"
   python3 scripts/generate_kie.py \
     "prompts/post_<slug>.json" \
     "images/posts/<slug>_final.jpg" \
     "4:5"
   ```

---

## STEP 8 — Deliver Results

Present in this order:

### 1. LinkedIn Post Text
Show the full post text, formatted exactly as it would appear on LinkedIn (blank lines between paragraphs, ready to copy-paste).

### 2. Final Visual
Read and display:
```
/path/to/linkedin-post-system/Nano Banana 2/images/posts/<slug>_final.jpg
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
/path/to/linkedin-post-system/linkedin_post.py
```

**Text-only post:**
```bash
python3 "/path/to/linkedin-post-system/linkedin_post.py" "FULL POST TEXT HERE"
```

**Post with image** — pass the image path as a second argument:
```bash
python3 "/path/to/linkedin-post-system/linkedin_post.py" \
  "FULL POST TEXT HERE" \
  "/path/to/linkedin-post-system/Nano Banana 2/images/posts/<slug>_final.jpg"
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
