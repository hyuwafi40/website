document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('heroModal');
    const form = document.getElementById('heroForm');
    const modalTitle = document.getElementById('heroModalTitle');
    const nameInput = document.getElementById('id_name');
    const photoInput = document.getElementById('id_photo');
    const formError = document.getElementById('heroFormError');

    if (!modal || !form || !modalTitle || !nameInput || !photoInput || !formError) return;

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const openModal = (mode, data = {}) => {
        if (mode === 'edit') {
            modalTitle.textContent = 'Edit Hero';
            form.action = data.url || form.action;
            nameInput.value = data.name || '';
            photoInput.value = data.photo || '';
        } else {
            modalTitle.textContent = 'Buat Hero';
            form.action = form.dataset.createUrl;
            nameInput.value = '';
            photoInput.value = '';
        }
        formError.textContent = '';
        modal.classList.add('show');
    };

    document.querySelectorAll('.open-hero-modal').forEach((btn) => {
        btn.addEventListener('click', () => {
            openModal('create');
        });
    });

    document.querySelectorAll('.edit-hero-btn').forEach((btn) => {
        btn.addEventListener('click', () => {
            openModal('edit', {
                url: btn.getAttribute('data-url'),
                name: btn.getAttribute('data-name'),
                photo: btn.getAttribute('data-photo'),
            });
        });
    });

    modal.querySelectorAll('[data-close-modal]').forEach((btn) => {
        btn.addEventListener('click', () => {
            modal.classList.remove('show');
        });
    });

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('show');
        }
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        formError.textContent = '';

        const formData = new FormData(form);
        try {
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrfToken,
                    'X-Requested-With': 'XMLHttpRequest',
                },
            });

            const contentType = response.headers.get('content-type') || '';
            const data = contentType.includes('application/json')
                ? await response.json()
                : null;

            if (response.ok && data && data.success) {
                modal.classList.remove('show');
                window.location.reload();
                return;
            }

            if (data && data.errors) {
                const firstError = Object.values(data.errors)[0];
                formError.textContent = firstError
                    .map((item) => item.message)
                    .join(', ');
            } else if (data && data.message) {
                formError.textContent = data.message;
            } else {
                formError.textContent = 'Terjadi kesalahan.';
            }
        } catch (error) {
            formError.textContent = 'Terjadi kesalahan jaringan atau server.';
        }
    });
});