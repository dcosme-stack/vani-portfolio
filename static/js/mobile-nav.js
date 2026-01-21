  const hamburger = document.querySelector('.hamburger');
  const menu = document.getElementById('mobile-menu');
  const closeBtn = document.querySelector('.mobile-close');

  function openMenu() {
    menu.classList.add('open');
    document.body.classList.add('menu-open');
    hamburger.setAttribute('aria-expanded', 'true');
  }

  function closeMenu() {
    menu.classList.remove('open');
    document.body.classList.remove('menu-open');
    hamburger.setAttribute('aria-expanded', 'false');
  }

  hamburger.addEventListener('click', openMenu);
  closeBtn.addEventListener('click', closeMenu);