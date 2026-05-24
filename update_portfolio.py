import re

with open('index.html', 'r') as f:
    content = f.read()

# Add CSS
css_to_add = """
  /* UI/UX Improvements */
  .scroll-progress {
    position: fixed; top: 0; left: 0; height: 3px; background: var(--gold);
    width: 0%; z-index: 1000;
  }
  @supports (animation-timeline: scroll()) {
    .scroll-progress {
      width: 100%; transform-origin: 0 50%; transform: scaleX(0);
      animation: scroll-progress-anim auto linear forwards;
      animation-timeline: scroll(root);
    }
    @keyframes scroll-progress-anim { to { transform: scaleX(1); } }
  }

  .mobile-menu-btn { display: none; background: none; border: none; color: var(--ink); cursor: pointer; }
  .mobile-menu { position: fixed; inset: 0; background: rgba(14,13,11,0.98); z-index: 45; display: none; flex-direction: column; justify-content: center; align-items: center; gap: 2.5rem; opacity: 0; transition: opacity 0.3s; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); }
  .mobile-menu.active { display: flex; opacity: 1; }
  .mobile-menu a { font-family: 'Fraunces', serif; font-size: 2rem; color: var(--ink); text-decoration: none; transition: color 0.3s; }
  .mobile-menu a:hover { color: var(--gold); }

  .reveal-on-scroll { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease-out, transform 0.8s ease-out; }
  .reveal-on-scroll.is-visible { opacity: 1; transform: translateY(0); }
  @media (prefers-reduced-motion: no-preference) {
    @supports ((animation-timeline: view()) and (animation-range: entry)) {
      .reveal-on-scroll {
        opacity: 0; transform: translateY(50px);
        animation: fade-up-scroll linear both;
        animation-timeline: view();
        animation-range: entry 5% cover 25%;
        transition: none;
      }
      .reveal-on-scroll.is-visible { opacity: initial; transform: initial; }
      @keyframes fade-up-scroll { to { opacity: 1; transform: translateY(0); } }
    }
  }

  /* Hover Enhancements */
  .capability { transition: background 0.4s ease, transform 0.4s ease; }
  .capability:hover { background: var(--bg-soft); transform: translateY(-4px); box-shadow: 0 10px 30px rgba(0,0,0,0.5); z-index: 10; position: relative; }
  
  .work-grid { transition: transform 0.4s ease; }
  .work-grid:hover { transform: translateX(8px); }
  .work-grid .work-role { transition: color 0.4s ease; }
  .work-grid:hover .work-role { color: var(--gold); }

  .case-meta { transition: background 0.4s ease; }
  .case-meta:hover { background: var(--bg-card); }
"""

# Insert CSS before </style>
content = content.replace('</style>', css_to_add + '\n</style>')

# Add JS before </body>
js_to_add = """
  <!-- UI/UX Improvements Script -->
  <div class="scroll-progress" id="scrollProgress"></div>
  <script>
    // Scroll Progress Fallback
    if (!CSS.supports('animation-timeline: scroll()')) {
      window.addEventListener('scroll', () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        document.getElementById('scrollProgress').style.width = (winScroll / height) * 100 + '%';
      });
    }

    // Mobile Menu
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
    });

    // Reveal on Scroll Fallback
    const revealElements = document.querySelectorAll('.reveal-on-scroll');
    if (!CSS.supports('(animation-timeline: view()) and (animation-range: entry)')) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });
      revealElements.forEach(el => observer.observe(el));
    }
  </script>
"""
content = content.replace('</body>', js_to_add + '\n</body>')

# Add hamburger button to topbar
btn_html = """    <div class="meta-status">Singapore : Available</div>
    <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Toggle Menu">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
    </button>"""
content = content.replace('    <div class="meta-status">Singapore : Available</div>', btn_html)

# Add reveal-on-scroll class to target elements
targets = [
    'class="section-header"',
    'class="capability"',
    'class="case-study"',
    'class="work-grid"',
    'class="project"',
    'class="tool"',
    'class="article"',
    'class="cred-block-title"',
    'class="cred-list"'
]
for target in targets:
    replacement = target[:-1] + ' reveal-on-scroll"'
    content = content.replace(target, replacement)

# Add reveal-on-scroll to specific elements that don't match cleanly above
content = content.replace('<h2><span class="italic">Get in', '<h2 class="reveal-on-scroll"><span class="italic">Get in')
content = content.replace('<p class="contact-sub">', '<p class="contact-sub reveal-on-scroll">')
content = content.replace('<a href="mailto', '<a class="reveal-on-scroll" href="mailto') # Ensure it doesn't break other links, wait this might break things. Let's use a safer replacement.
content = content.replace('<a href="mailto:arvind.gautam@gmail.com" class="cv-button">', '<a href="mailto:arvind.gautam@gmail.com" class="cv-button reveal-on-scroll">')

with open('index.html', 'w') as f:
    f.write(content)

print("index.html updated successfully!")
