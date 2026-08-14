/* =====================================================
   ARUN C S — Portfolio JavaScript
   ===================================================== */

'use strict';

// ── Theme ────────────────────────────────────────────
const ThemeManager = (() => {
  const btn = document.getElementById('theme-toggle');
  const root = document.documentElement;

  const icons = {
    dark:  '<i class="bi bi-moon-stars"></i>',
    light: '<i class="bi bi-sun"></i>',
  };

  function apply(theme) {
    root.setAttribute('data-theme', theme);
    if (btn) btn.innerHTML = theme === 'dark' ? icons.dark : icons.light;
    localStorage.setItem('theme', theme);
  }

  function init() {
    const saved = localStorage.getItem('theme') || 'dark';
    apply(saved);
    btn && btn.addEventListener('click', () => {
      apply(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
    });
  }

  return { init };
})();

// ── Scroll Progress ──────────────────────────────────
const ScrollProgress = (() => {
  const bar = document.getElementById('scroll-progress');

  function update() {
    if (!bar) return;
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + '%' : '0%';
  }

  return { init: () => window.addEventListener('scroll', update, { passive: true }) };
})();

// ── Navbar ───────────────────────────────────────────
const Navbar = (() => {
  const navbar = document.getElementById('navbar');
  const links  = document.querySelectorAll('.nav-link[data-section]');
  const sections = Array.from(document.querySelectorAll('section[id]'));

  function onScroll() {
    if (!navbar) return;
    navbar.classList.toggle('scrolled', window.scrollY > 30);

    // Active section highlight
    const scrollY = window.scrollY + 90;
    sections.forEach(sec => {
      if (scrollY >= sec.offsetTop && scrollY < sec.offsetTop + sec.offsetHeight) {
        links.forEach(l => {
          l.classList.toggle('active', l.dataset.section === sec.id);
        });
      }
    });
  }

  return { init: () => window.addEventListener('scroll', onScroll, { passive: true }) };
})();

// ── Scroll Reveal ────────────────────────────────────
const ScrollReveal = (() => {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px -40px 0px' });

  function init() {
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    document.querySelectorAll('.timeline-item').forEach(el => observer.observe(el));
  }

  return { init };
})();

// ── Custom Cursor ────────────────────────────────────
const Cursor = (() => {
  function init() {
    if (window.matchMedia('(pointer: coarse)').matches) return;

    const dot = document.createElement('div');
    dot.className = 'cursor-dot';
    document.body.appendChild(dot);

    let x = 0, y = 0;

    document.addEventListener('mousemove', e => {
      x = e.clientX; y = e.clientY;
      dot.style.left = x + 'px';
      dot.style.top  = y + 'px';
    });

    document.querySelectorAll('a, button, [role="button"], .skill-card, .project-card, .filter-btn').forEach(el => {
      el.addEventListener('mouseenter', () => dot.classList.add('expand'));
      el.addEventListener('mouseleave', () => dot.classList.remove('expand'));
    });
  }

  return { init };
})();

// ── Hero Terminal Typing ─────────────────────────────
const HeroTerminal = (() => {
  const lines = [
    { type: 'prompt', text: 'whoami' },
    { type: 'output', text: 'Arun C S', cls: 't-value' },
    { type: 'prompt', text: 'role' },
    { type: 'output', text: 'Backend / Full-Stack Developer', cls: 't-value' },
    { type: 'prompt', text: 'exploring' },
    { type: 'output', text: 'AI / Machine Learning', cls: 't-value' },
    { type: 'prompt', text: 'stack' },
    { type: 'output', text: 'Python  Django  DRF', cls: 't-key' },
    { type: 'output', text: 'HTML  CSS  JavaScript', cls: 't-key' },
    { type: 'prompt', text: 'status' },
    { type: 'output', text: '✦ Open to opportunities', cls: 't-success' },
  ];

  function init() {
    const body = document.getElementById('hero-terminal-body');
    if (!body) return;

    let i = 0;
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReduced) {
      lines.forEach(l => appendLine(body, l));
      return;
    }

    function next() {
      if (i >= lines.length) return;
      const line = lines[i++];
      appendLine(body, line);
      setTimeout(next, line.type === 'prompt' ? 320 : 160);
    }

    setTimeout(next, 400);
  }

  function appendLine(body, line) {
    const div = document.createElement('div');
    if (line.type === 'prompt') {
      div.innerHTML = `<span class="t-prompt">arun@portfolio</span><span class="t-comment">:~$</span> <span class="t-cmd">${line.text}</span>`;
    } else {
      div.innerHTML = `<span class="${line.cls || ''}">${line.text}</span>`;
    }
    // Remove blink cursor from previous last line
    const prev = body.querySelector('.cursor-blink');
    if (prev) prev.remove();
    body.appendChild(div);

    // Add blink cursor to last line
    const blink = document.createElement('span');
    blink.className = 'cursor-blink';
    body.appendChild(blink);
  }

  return { init };
})();

// ── Project Filters ──────────────────────────────────
const ProjectFilter = (() => {
  function init() {
    const btns  = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.project-item');

    btns.forEach(btn => {
      btn.addEventListener('click', () => {
        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.dataset.filter;
        cards.forEach(card => {
          const show = filter === 'all' || card.dataset.category === filter;
          card.style.display = show ? '' : 'none';
          // Re-trigger animation
          if (show) {
            card.classList.remove('visible');
            setTimeout(() => card.classList.add('visible'), 50);
          }
        });
      });
    });
  }

  return { init };
})();

// ── Interactive Terminal ─────────────────────────────
const InteractiveTerminal = (() => {
  const commands = {
    help: () => [
      '<span class="t-info">Available commands:</span>',
      '  <span class="t-cmd">about</span>     — Who am I',
      '  <span class="t-cmd">skills</span>    — My tech stack',
      '  <span class="t-cmd">projects</span>  — What I have built',
      '  <span class="t-cmd">github</span>    — My GitHub profile',
      '  <span class="t-cmd">contact</span>   — Get in touch',
      '  <span class="t-cmd">clear</span>     — Clear terminal',
    ],
    about: () => [
      '<span class="t-info">Arun C S</span>',
      '4th Year B.Tech Computer Science & Engineering',
      'Backend / Full-Stack Developer',
      '<span class="t-dim">Currently exploring AI/ML</span>',
    ],
    skills: () => [
      '<span class="t-info">Tech Stack:</span>',
      '  Python  Django  Django REST Framework',
      '  HTML  CSS  Bootstrap  JavaScript  React',
      '  PostgreSQL  MySQL  SQLite',
      '  Git  GitHub  VS Code',
      '  <span class="t-dim">AI/ML: NumPy, Pandas, Matplotlib</span>',
    ],
    projects: () => [
      '<span class="t-info">Featured Projects:</span>',
      '  1. Sponsorship / Offers Platform  <span class="t-dim">[Full Stack]</span>',
      '  2. Contact Management API  <span class="t-dim">[Backend]</span>',
      '  3. AI Profession Image Generator  <span class="t-dim">[AI/ML]</span>',
      '  4. Skill Swap Hub  <span class="t-dim">[Frontend]</span>',
      '<span class="t-dim">→ Scroll up to see all projects</span>',
    ],
    github: () => [
      '<span class="t-info">GitHub:</span> github.com/arun-c-s-07',
      '<span class="t-dim">→ Check out my repositories</span>',
    ],
    contact: () => [
      '<span class="t-info">Contact:</span>',
      '  GitHub   → github.com/arun-c-s-07',
      '  <span class="t-dim">→ Scroll to the contact section below</span>',
    ],
    clear: () => '__clear__',
  };

  let history = [];
  let historyIdx = -1;

  function init() {
    const input  = document.getElementById('terminal-input');
    const output = document.getElementById('terminal-output');
    if (!input || !output) return;

    input.addEventListener('keydown', e => {
      if (e.key === 'Enter') {
        const cmd = input.value.trim().toLowerCase();
        if (cmd) {
          history.unshift(cmd);
          historyIdx = -1;
          run(cmd, output);
        }
        input.value = '';
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        if (historyIdx < history.length - 1) historyIdx++;
        input.value = history[historyIdx] || '';
      } else if (e.key === 'ArrowDown') {
        e.preventDefault();
        if (historyIdx > 0) historyIdx--;
        else { historyIdx = -1; input.value = ''; }
        input.value = history[historyIdx] || '';
      }
    });

    // Click anywhere in terminal to focus input
    document.getElementById('terminal-interactive') &&
      document.getElementById('terminal-interactive').addEventListener('click', () => input.focus());

    // Show initial help
    run('help', output, true);
  }

  function run(cmd, output, silent = false) {
    if (!silent) {
      appendOutput(output, `<span class="t-prompt">$</span> <span class="t-cmd">${escHtml(cmd)}</span>`);
    }

    const fn = commands[cmd];
    if (!fn) {
      appendOutput(output, `<span class="t-error">Command not found: ${escHtml(cmd)}. Type <span class="t-cmd">help</span> for commands.</span>`);
    } else {
      const result = fn();
      if (result === '__clear__') {
        output.innerHTML = '';
        return;
      }
      result.forEach(line => appendOutput(output, line));
    }
    appendOutput(output, '');
    output.scrollTop = output.scrollHeight;
  }

  function appendOutput(output, html) {
    const div = document.createElement('div');
    div.className = 'terminal-output';
    div.innerHTML = html;
    output.appendChild(div);
  }

  function escHtml(str) {
    return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  }

  return { init };
})();

// ── Contact Form ─────────────────────────────────────
const ContactForm = (() => {
  function init() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    // Auto-dismiss alerts
    document.querySelectorAll('.auto-dismiss').forEach(el => {
      setTimeout(() => {
        el.style.transition = 'opacity 0.5s';
        el.style.opacity = '0';
        setTimeout(() => el.remove(), 500);
      }, 5000);
    });
  }

  return { init };
})();

// ── Smooth Scroll for anchor links ───────────────────
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href').slice(1);
      const target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        const offset = target.getBoundingClientRect().top + window.scrollY - 70;
        window.scrollTo({ top: offset, behavior: 'smooth' });
        // Close mobile nav
        const collapse = document.getElementById('navbarNav');
        if (collapse && collapse.classList.contains('show')) {
          const toggle = document.querySelector('.navbar-toggler');
          toggle && toggle.click();
        }
      }
    });
  });
}

// ── Bootstrap Tooltips ───────────────────────────────
function initTooltips() {
  const tooltipEls = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  tooltipEls.forEach(el => new bootstrap.Tooltip(el));
}

// ── Init ─────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  ThemeManager.init();
  ScrollProgress.init();
  Navbar.init();
  ScrollReveal.init();
  Cursor.init();
  HeroTerminal.init();
  ProjectFilter.init();
  InteractiveTerminal.init();
  ContactForm.init();
  initSmoothScroll();
  initTooltips();
});
