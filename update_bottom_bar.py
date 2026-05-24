import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Remove Hamburger Menu Button from topbar
content = re.sub(r'<button class="mobile-menu-btn" id="mobileMenuBtn".*?</button>', '', content, flags=re.DOTALL)

# 2. Add Bottom Bar HTML before the UI/UX script
bottom_bar_html = """
  <!-- Bottom Mobile Navigation Bar -->
  <nav class="bottom-nav">
    <a href="#work" class="bottom-nav-item">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>
      <span>Exp</span>
    </a>
    <a href="#ventures" class="bottom-nav-item">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
      <span>Ventures</span>
    </a>
    <a href="#contact" class="bottom-nav-item">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
      <span>Contact</span>
    </a>
    <a href="mailto:arvind.gautam@gmail.com?subject=Book%20an%20Appointment" class="bottom-nav-item highlight">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
      <span>Book Call</span>
    </a>
  </nav>
"""
if '<nav class="bottom-nav">' not in content:
    content = content.replace('  <!-- UI/UX Improvements Script -->', bottom_bar_html + '\n  <!-- UI/UX Improvements Script -->')

# 3. Add CSS for Bottom Bar
css_to_replace = """  .mobile-menu-btn { display: none; background: none; border: none; color: var(--ink); cursor: pointer; }
  .mobile-menu { position: fixed; inset: 0; background: rgba(14,13,11,0.98); z-index: 45; display: none; flex-direction: column; justify-content: center; align-items: center; gap: 2.5rem; opacity: 0; transition: opacity 0.3s; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); }
  .mobile-menu.active { display: flex; opacity: 1; }
  .mobile-menu a { font-family: 'Fraunces', serif; font-size: 2rem; color: var(--ink); text-decoration: none; transition: color 0.3s; }
  .mobile-menu a:hover { color: var(--gold); }"""

new_css = """  /* Bottom Nav */
  .bottom-nav { display: none; position: fixed; bottom: 0; left: 0; right: 0; background: rgba(14,13,11,0.95); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border-top: 1px solid var(--rule-strong); z-index: 60; padding-bottom: env(safe-area-inset-bottom); }
  .bottom-nav-item { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.3rem; padding: 0.8rem 0; color: var(--ink-dim); text-decoration: none; font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.1em; transition: color 0.3s; }
  .bottom-nav-item:hover, .bottom-nav-item:active { color: var(--gold); }
  .bottom-nav-item.highlight { color: var(--gold); background: rgba(201, 165, 90, 0.05); }
  .bottom-nav-item svg { margin-bottom: 0.2rem; opacity: 0.8; }
  
  @media (max-width: 900px) {
    .bottom-nav { display: flex; }
    .meta-status { display: none; }
    body { padding-bottom: 5rem; } /* Extra space so content isn't hidden */
  }"""
content = content.replace(css_to_replace, new_css)

# 4. Remove JS for Mobile Menu
js_to_remove = """    // Mobile Menu
    const menuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.createElement('div');
    mobileMenu.className = 'mobile-menu';
    mobileMenu.innerHTML = `
      <a href="#capabilities" class="mobile-link">Capabilities</a>
      <a href="#case-study" class="mobile-link">Case study</a>
      <a href="#work" class="mobile-link">Experience</a>
      <a href="#ventures" class="mobile-link">Ventures</a>
      <a href="#contact" class="mobile-link">Contact</a>
    `;
    document.body.appendChild(mobileMenu);

    menuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('active');
      if (mobileMenu.classList.contains('active')) {
        menuBtn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>';
        document.body.style.overflow = 'hidden';
      } else {
        menuBtn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
        document.body.style.overflow = '';
      }
    });

    document.querySelectorAll('.mobile-link').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('active');
        menuBtn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
        document.body.style.overflow = '';
      });
    });"""
content = content.replace(js_to_remove, "")

# 5. Add Desktop "Book Call" button to the topbar
desktop_button_html = """    <nav class="nav-links">
      <a href="#capabilities">Capabilities</a>
      <a href="#work">Experience</a>
      <a href="#ventures">Ventures</a>
      <a href="#contact">Contact</a>
      <a href="mailto:arvind.gautam@gmail.com?subject=Book%20an%20Appointment" style="color: var(--gold); border: 1px solid var(--gold-soft); padding: 0.3rem 0.8rem; border-radius: 4px; margin-top: -0.4rem;">Book Call</a>
    </nav>"""
# Find the existing nav-links and replace
content = re.sub(r'<nav class="nav-links">.*?</nav>', desktop_button_html, content, flags=re.DOTALL)


with open('index.html', 'w') as f:
    f.write(content)

print("index.html updated successfully!")
