document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initDropdowns();
    initPublicInteractions();
});

document.addEventListener('htmx:afterSwap', () => {
    initPublicInteractions();
});

function initNavbar() {
    const menuToggle = document.getElementById('publicMenuToggle');
    const navMenu = document.getElementById('publicNavMenu');
    const navOverlay = document.getElementById('navOverlay');
    const header = document.getElementById('app-header');

    if (menuToggle && navMenu && navOverlay) {
        const openMenu = () => {
            navMenu.classList.add('active');
            navOverlay.classList.add('show');
            menuToggle.setAttribute('aria-expanded', 'true');
        };

        const closeMenu = () => {
            navMenu.classList.remove('active');
            navOverlay.classList.remove('show');
            menuToggle.setAttribute('aria-expanded', 'false');
        };

        menuToggle.addEventListener('click', () => {
            const isOpen = navMenu.classList.contains('active');
            if (isOpen) {
                closeMenu();
            } else {
                openMenu();
            }
        });

        navOverlay.addEventListener('click', closeMenu);

        navMenu.querySelectorAll('a.nav-item, .nav-dropdown-item').forEach(link => {
            link.addEventListener('click', closeMenu);
        });

        document.addEventListener('htmx:beforeRequest', closeMenu);
    }

    if (header) {
        const handleScroll = () => {
            if (window.scrollY > 20) {
                header.style.background = 'var(--glass-bg-solid)';
                header.style.boxShadow = '0 10px 30px -10px rgba(0,0,0,0.1)';
                header.style.borderBottom = '1px solid transparent';
            } else {
                header.style.background = 'var(--glass-bg)';
                header.style.boxShadow = 'none';
                header.style.borderBottom = '1px solid var(--glass-border)';
            }
        };

        window.addEventListener('scroll', handleScroll);
        handleScroll();
    }
}

function initDropdowns() {
    document.addEventListener('click', (e) => {
        const toggle = e.target.closest('.nav-dropdown-toggle');
        const dropdown = e.target.closest('.nav-dropdown');

        if (toggle) {
            e.preventDefault();
            e.stopPropagation();

            const parent = toggle.closest('.nav-dropdown');
            const isOpen = parent.classList.contains('open');

            closeAllDropdowns(parent);
            parent.classList.toggle('open', !isOpen);
            toggle.setAttribute('aria-expanded', String(!isOpen));
            return;
        }

        if (!dropdown) {
            closeAllDropdowns();
        }
    });
}

function closeAllDropdowns(except = null) {
    document.querySelectorAll('.nav-dropdown.open').forEach(drop => {
        if (drop !== except) {
            drop.classList.remove('open');
            const toggle = drop.querySelector('.nav-dropdown-toggle');
            if (toggle) {
                toggle.setAttribute('aria-expanded', 'false');
            }
        }
    });
}

function initPublicInteractions() {
    initScrollSpy();
    initReveal();
    initPublicGallery();
    initArticleCopy();
}

function initScrollSpy() {
    const links = document.querySelectorAll('a.nav-item, .nav-dropdown-item');
    if (!links.length) return;

    const currentPath = window.location.pathname;

    const updateActiveLink = () => {
        links.forEach(link => {
            if (!link.href) return;

            const linkPath = new URL(link.href).pathname;
            const isActive = linkPath === currentPath;

            link.classList.toggle('active', isActive);

            if (isActive) {
                link.setAttribute('aria-current', 'page');
                const parent = link.closest('.nav-dropdown');
                if (parent) {
                    parent.classList.add('active');
                }
            } else {
                link.removeAttribute('aria-current');
            }
        });

        document.querySelectorAll('.nav-dropdown').forEach(drop => {
            const hasActiveChild = drop.querySelector('.nav-dropdown-item.active');
            if (!hasActiveChild) {
                drop.classList.remove('active');
            }
        });
    };

    updateActiveLink();

    if (!window.__scrollSpyInitialized) {
        window.__scrollSpyInitialized = true;
        window.addEventListener('popstate', updateActiveLink);
    }
}

function initReveal() {
    const revealElements = document.querySelectorAll('.reveal');
    if (!revealElements.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, {
        rootMargin: '0px 0px -20% 0px',
    });

    revealElements.forEach(el => observer.observe(el));
}

function initPublicGallery() {
    const modal = document.getElementById('publicPhotoModal');
    if (!modal) return;

    const modalImage = document.getElementById('publicPhotoImage');
    const modalTitle = document.getElementById('publicPhotoTitle');
    const modalCaption = document.getElementById('publicPhotoCaption');
    const closeButtons = modal.querySelectorAll('[data-close-preview]');

    const openModal = (e) => {
        const img = e.currentTarget;
        modalImage.src = img.getAttribute('data-url');
        modalTitle.textContent = img.getAttribute('data-title') || 'Preview Foto';
        modalCaption.textContent = img.getAttribute('data-caption') || '';
        modal.classList.add('show');
    };

    document.querySelectorAll('.public-gallery-image').forEach(img => {
        img.removeEventListener('click', openModal);
        img.addEventListener('click', openModal);
    });

    closeButtons.forEach(btn => {
        btn.removeEventListener('click', closeModal);
        btn.addEventListener('click', closeModal);
    });

    modal.removeEventListener('click', closeModalOnBackdrop);
    modal.addEventListener('click', closeModalOnBackdrop);
}

function closeModal() {
    const modal = document.getElementById('publicPhotoModal');
    if (modal) {
        modal.classList.remove('show');
    }
}

function closeModalOnBackdrop(e) {
    if (e.target === e.currentTarget) {
        closeModal();
    }
}

function initArticleCopy() {
    document.querySelectorAll('.share-copy').forEach(btn => {
        btn.removeEventListener('click', handleCopy);
        btn.addEventListener('click', handleCopy);
    });
}

function handleCopy(e) {
    const url = e.currentTarget.getAttribute('data-copy-url');
    if (!url) return;

    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(() => {
            alert('Tautan disalin.');
        }).catch(() => {
            fallbackCopy(url);
        });
    } else {
        fallbackCopy(url);
    }
}

function fallbackCopy(url) {
    const tempInput = document.createElement('input');
    tempInput.value = url;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    tempInput.remove();
    alert('Tautan disalin.');
}