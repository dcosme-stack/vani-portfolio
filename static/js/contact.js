document.addEventListener("DOMContentLoaded", function() {
    const successMessage = document.querySelector('.contact .success');
    if (successMessage) {
        // Scroll smoothly to the contact section
        document.getElementById('contact-section').scrollIntoView({ behavior: 'smooth' });
    }
});