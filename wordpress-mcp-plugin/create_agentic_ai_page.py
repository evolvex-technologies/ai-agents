import json, urllib.request, base64, os, sys

env = {}
for line in open('.env'):
    line = line.strip()
    if line and not line.startswith('#') and '=' in line:
        k, v = line.split('=', 1)
        env[k] = v

content = """<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Agentic AI Automation</h1>
<!-- /wp:heading -->

<!-- wp:image -->
<figure class="wp-block-image"><img alt="Hero image"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2 class="wp-block-heading">How Does Agentic AI Automation Help Your Enterprise?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>[Add intro paragraph here]</p>
<!-- /wp:paragraph -->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">[Feature section 1]</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:image -->
<figure class="wp-block-image"><img alt="Section image"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:image -->
<figure class="wp-block-image"><img alt="Section image"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">[Feature section 2]</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">[Feature section 3]</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:image -->
<figure class="wp-block-image"><img alt="Section image"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:image -->
<figure class="wp-block-image"><img alt="Section image"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">[Feature section 4]</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">[Feature section 5]</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:image -->
<figure class="wp-block-image"><img alt="Section image"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:image -->
<figure class="wp-block-image"><img alt="Section image"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">[Feature section 6]</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --><!-- wp:list-item --><li>[Add point]</li><!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:heading -->
<h2 class="wp-block-heading">[Closing section: Intelligent Agentic AI for Connected Business Operations]</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>[Add closing paragraph here]</p>
<!-- /wp:paragraph -->"""

payload = json.dumps({"title": "Agentic AI Automation", "status": "draft", "content": content}).encode()
auth = base64.b64encode(f"{env['WORDPRESS_USERNAME']}:{env['WORDPRESS_PASSWORD']}".encode()).decode()
req = urllib.request.Request(
    env['WORDPRESS_URL'] + "/wp-json/wp/v2/pages",
    data=payload,
    headers={"Content-Type": "application/json", "Authorization": "Basic " + auth},
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
        print("SUCCESS")
        print("ID:", data["id"])
        print("Status:", data["status"])
        print("Link:", data["link"])
        print("Edit:", env['WORDPRESS_URL'] + f"/wp-admin/post.php?post={data['id']}&action=edit")
except Exception as e:
    print("FAILED:", e)
