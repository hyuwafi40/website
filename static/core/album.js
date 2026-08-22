document.addEventListener('DOMContentLoaded', () => {
    const previewModal = document.getElementById('photoPreviewModal');
    const previewImage = document.getElementById('previewImage');
    const previewTitle = document.getElementById('previewTitle');
    const previewCaption = document.getElementById('previewCaption');

    if (previewModal && previewImage && previewTitle && previewCaption) {
        const galleryImages = document.querySelectorAll('.gallery-image');
        const closeButtons = previewModal.querySelectorAll('[data-close-preview]');

        galleryImages.forEach((img) => {
            img.addEventListener('click', () => {
                previewImage.src = img.getAttribute('data-url');
                previewTitle.textContent = img.getAttribute('data-title') || 'Preview Foto';
                previewCaption.textContent = img.getAttribute('data-caption') || '';
                previewModal.classList.add('show');
            });
        });

        closeButtons.forEach((btn) => {
            btn.addEventListener('click', () => {
                previewModal.classList.remove('show');
            });
        });

        previewModal.addEventListener('click', (e) => {
            if (e.target === previewModal) {
                previewModal.classList.remove('show');
            }
        });
    }
});