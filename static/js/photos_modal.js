document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modal-container");
    const modalImg = document.getElementById("modal-img");
    const closeBtn = document.querySelector(".modal-close");
    const images = document.querySelectorAll(".gallery-img");

    function openModal(img) {
        modalImg.src = img.src;
        modalImg.alt = img.alt;

        modal.classList.add("show");
        document.body.style.overflow = "hidden";
    }

    function closeModal() {
        modal.classList.remove("show");
        document.body.style.overflow = "";
    }

    // Open modal
    images.forEach(img => {
        img.addEventListener("click", () => openModal(img));
    });

    // Close with X
    closeBtn.addEventListener("click", closeModal);

    // Close on background click
    modal.addEventListener("click", (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Close with ESC
    window.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
            closeModal();
        }
    });
});