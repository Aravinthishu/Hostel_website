
    document.addEventListener('DOMContentLoaded', function() {
        const card = document.getElementById('static-card');
    
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Add the slide-up animation class when the card is half visible
                    card.classList.add('slide-up-card');
                    card.classList.remove('opacity-0');
                    observer.unobserve(card); // Remove the observer once the animation is triggered
                }
            });
        }, {
            threshold: 0.7 // Trigger when 50% of the card is visible
        });
    
        observer.observe(card);
    });
