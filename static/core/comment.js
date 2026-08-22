document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('commentModal');
    const form = document.getElementById('commentForm');
    const modalTitle = document.getElementById('commentModalTitle');
    const statusSelect = document.getElementById('id_status');
    const formError = document.getElementById('commentFormError');

    if (!modal || !form || !modalTitle || !statusSelect || !formError) return;

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const openModal = (status, url) => {
        modalTitle.textContent = 'Ubah Status Komentar';
        form.action = url;
        statusSelect.value = status;
        formError.textContent = '';
        modal.classList.add('show');
    };

    document.querySelectorAll('.edit-comment-btn').forEach((btn) => {
        btn.addEventListener('click', () => {
            openModal(btn.getAttribute('data-status'), btn.getAttribute('data-url'));
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

            if (data && data.errors && data.errors.status) {
                formError.textContent = data.errors.status
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