with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Capabilities: GenAI for Voice and Chatbots
content = content.replace(
    '<li>GenAI and agentic workflow architecture</li>',
    '<li>GenAI for Voice, Chatbots, and agentic workflows</li>'
)

# 2. Update Capabilities: Digital & AWS Connect
content = content.replace(
    '<li>CCaaS transformation: Avaya, Genesys, Amazon Connect</li>',
    '<li>Digital &amp; CCaaS transformation (AWS Connect, Avaya, Genesys)</li>'
)

# 3. Update Capabilities: Cloudflare
content = content.replace(
    '<li>Self-hosted infra: Hetzner, Fly.io, Supabase</li>',
    '<li>Edge &amp; Infra: Cloudflare, Hetzner, Fly.io, Supabase</li>'
)

# 4. Update Tools: Cloudflare
tool_target = """<h4 class="tool-name">Hetzner / Fly.io</h4>
          <p class="tool-opinion">"Where Magnis lives. Hetzner for the heavy stuff at Hetzner prices. Fly for the
            edge-deployed bits. AWS is for clients who can't say no to AWS."</p>"""
tool_replace = """<h4 class="tool-name">Cloudflare / Hetzner</h4>
          <p class="tool-opinion">"Where Magnis lives. Cloudflare for robust hosting and edge routing, Hetzner for the heavy compute. AWS is for clients who can't say no to AWS."</p>"""
content = content.replace(tool_target, tool_replace)

with open('index.html', 'w') as f:
    f.write(content)

print("Expertise added successfully!")
