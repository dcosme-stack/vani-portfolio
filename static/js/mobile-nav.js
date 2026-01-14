document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector(".hamburger");
    const menu = document.getElementById("mobile-menu");

    if (!button || !menu) return;

    button.addEventListener("click", () => {
        const isOpen = menu.classList.toggle("open");

        button.setAttribute("aria-expanded", isOpen);

        if (isOpen) {
            menu.removeAttribute("hidden");
        } else {
            menu.setAttribute("hidden", "");
        }
    });
});

document.addEventListener("click", (event) => {
    if (!menu.contains(event.target) && !button.contains(event.target)) {
        menu.classList.remove("open");
        menu.setAttribute("hidden", "");
        button.setAttribute("aria-expanded", "false");
    }
});

menu.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
        menu.classList.remove("open");
        menu.setAttribute("hidden", "");
        button.setAttribute("aria-expanded", "false");
    });
});