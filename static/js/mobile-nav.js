const hamburger = document.querySelector('.hamburger');
const menu = document.getElementById('mobile-menu');
const closeBtn = document.querySelector('.mobile-close');
const desktopNav = document.getElementById('desktop-nav');

function openMenu() {
  // Open mobile menu
  menu.classList.add('open');
  menu.removeAttribute('inert');
  menu.setAttribute('aria-hidden', 'false');

  // Disable desktop nav
  if (desktopNav) {
    desktopNav.setAttribute('inert', '');
    desktopNav.setAttribute('aria-hidden', 'true');
  }

  document.body.classList.add('menu-open');
  hamburger.setAttribute('aria-expanded', 'true');

  closeBtn.focus();
}

function closeMenu() {
  // Close mobile menu
  menu.classList.remove('open');
  menu.setAttribute('aria-hidden', 'true');
  menu.setAttribute('inert', '');

  // Re-enable desktop nav
  if (desktopNav) {
    desktopNav.removeAttribute('inert');
    desktopNav.setAttribute('aria-hidden', 'false');
  }

  document.body.classList.remove('menu-open');
  hamburger.setAttribute('aria-expanded', 'false');

  hamburger.focus();
}

hamburger.addEventListener('click', openMenu);
closeBtn.addEventListener('click', closeMenu);