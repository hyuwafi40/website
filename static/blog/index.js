document.addEventListener('DOMContentLoaded', initIndex);
document.addEventListener('htmx:afterSwap', initIndex);

function initIndex() {
    initStatCounters();
    initIndexHero();
}

function initStatCounters() {
    const counters = document.querySelectorAll('.stat-value[data-count]');
    if (!counters.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.3,
    });

    counters.forEach(counter => observer.observe(counter));
}

function animateCounter(counter) {
    if (counter.dataset.statAnimated === 'true') return;
    counter.dataset.statAnimated = 'true';

    const target = parseInt(counter.getAttribute('data-count'), 10) || 0;
    const duration = 1200;
    const start = performance.now();

    const update = (currentTime) => {
        const elapsed = currentTime - start;
        const progress = Math.min(elapsed / duration, 1);
        const value = Math.floor(progress * target);

        counter.textContent = value.toLocaleString('id-ID');

        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            counter.textContent = target.toLocaleString('id-ID');
        }
    };

    requestAnimationFrame(update);
}

function initIndexHero() {
    const carousel = document.getElementById('indexHeroCarousel');
    if (!carousel || carousel.dataset.indexHeroInitialized === 'true') return;

    carousel.dataset.indexHeroInitialized = 'true';

    const slides = carousel.querySelectorAll('.index-hero-slide');
    const dots = carousel.querySelectorAll('.index-hero-dot');
    const prevBtn = carousel.querySelector('[data-hero-prev]');
    const nextBtn = carousel.querySelector('[data-hero-next]');

    if (!slides.length) return;

    let currentIndex = 0;
    let autoplayInterval;

    const showSlide = (index) => {
        slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
        dots.forEach((dot, i) => dot.classList.toggle('active', i === index));
        currentIndex = index;
    };

    const nextSlide = () => showSlide((currentIndex + 1) % slides.length);
    const prevSlide = () => showSlide((currentIndex - 1 + slides.length) % slides.length);

    if (nextBtn) nextBtn.addEventListener('click', nextSlide);
    if (prevBtn) prevBtn.addEventListener('click', prevSlide);

    dots.forEach(dot => {
        dot.addEventListener('click', () => showSlide(Number(dot.getAttribute('data-hero-dot'))));
    });

    const startAutoplay = () => {
        if (autoplayInterval) clearInterval(autoplayInterval);
        autoplayInterval = setInterval(nextSlide, 5000);
    };

    const stopAutoplay = () => {
        if (autoplayInterval) clearInterval(autoplayInterval);
        autoplayInterval = null;
    };

    carousel.addEventListener('mouseenter', stopAutoplay);
    carousel.addEventListener('mouseleave', startAutoplay);

    startAutoplay();
}