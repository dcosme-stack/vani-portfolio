document.addEventListener("DOMContentLoaded", function() {
    const successMessage = document.querySelector('.contact .success');
    if (successMessage) {
        // Scroll smoothly to the contact section
        document.getElementById('contact-section').scrollIntoView({ behavior: 'smooth' });
    }
});

const textarea = document.querySelector("#id_message");
if (textarea) {
    const counter = document.createElement("small");
    counter.className = "char-counter";
    textarea.after(counter);

    const max = textarea.getAttribute("maxlength");

    const update = () => {
        counter.textContent = `${textarea.value.length} / ${max} characters`;
    };

    textarea.addEventListener("input", update);
    update();
}