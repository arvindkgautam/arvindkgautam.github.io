import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Replace remaining "venture" text
content = content.replace('Agentic AI &amp; venture initiatives', 'Agentic AI &amp; advisory initiatives')
content = content.replace('id="magnis-venture"', 'id="magnis"')
content = content.replace('Independent AI Venture', 'Independent AI SaaS')

# 2. Inject Meta Tags and Favicon
meta_tags = """  <meta name="description" content="Arvind K Gautam - CX & AI Transformation Leader helping enterprises design and scale AI adoption, Agentic AI use cases, and customer-led growth strategies.">
  <meta property="og:title" content="Arvind K Gautam | AI & CX Transformation">
  <meta property="og:description" content="CX & AI Transformation Leader helping enterprises design and scale AI adoption.">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90' font-family='serif' fill='%23c9a55a'>AG</text></svg>">
"""
content = content.replace('<title>Arvind K Gautam', meta_tags + '<title>Arvind K Gautam')

# 3. Inject Premium Polish CSS
css_polishes = """
  /* Premium Polishes */
  ::selection { background: var(--gold-soft); color: var(--ink); }
  ::-moz-selection { background: var(--gold-soft); color: var(--ink); }
  
  ::-webkit-scrollbar { width: 10px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.1); border-radius: 5px; }
  ::-webkit-scrollbar-thumb:hover { background: var(--gold-soft); }

  @media print {
    body { background: white; color: black; }
    body::before { display: none; }
    .topbar, .bottom-nav, .terminal-section, .cv-button, .mobile-menu-btn, .project-arrow, .scroll-progress { display: none !important; }
    .hero, .content, .capability, .project, .article { border: none !important; box-shadow: none !important; margin: 0 !important; padding: 1rem 0 !important; page-break-inside: avoid; }
    .name, .section-title, .project-title, .work-role { color: black !important; }
    a { text-decoration: underline; color: black; }
    .project-tag, .section-num { color: #555; }
    .work-grid { display: block; border-bottom: 1px solid #ccc; padding-bottom: 1rem; margin-bottom: 1rem; }
    .work-meta { float: left; width: 30%; margin-bottom: 1rem; }
    .reveal-on-scroll { opacity: 1 !important; transform: none !important; }
  }
"""
content = content.replace('</style>', css_polishes + '\n</style>')

with open('index.html', 'w') as f:
    f.write(content)

print("Final polishes applied successfully.")
