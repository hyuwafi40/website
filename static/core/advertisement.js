document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('advertisementModal');
    const form = document.getElementById('advertisementForm');
    const modalTitle = document.getElementById('advertisementModalTitle');
    const typeInput = document.getElementById('id_type');
    const imageInput = document.getElementById('id_image');
    const linkInput = document.getElementById('id_link');
    const enddateInput = document.getElementById('id_enddate');
    const statusInput = document.getElementById('id_status');
    const formError = document.getElementById('advertisementFormError');

    if (
        !modal ||
        !form ||
        !modalTitle ||
        !typeInput ||
        !imageInput ||
        !linkInput ||
        !enddateInput ||
        !statusInput ||
        !formError
    ) return;

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const openModal = (mode, data = {}) => {
        if (mode === 'edit') {
            modalTitle.textContent = 'Edit Iklan';
            form.action = data.url || form.action;
            typeInput.value = data.type || '';
            imageInput.value = data.image || '';
            linkInput.value = data.link || '';
            enddateInput.value = data.enddate || '';
            statusInput.value = data.status || '';
        } else {
            modalTitle.textContent = 'Buat Iklan';
            form.action = form.dataset.createUrl;
            typeInput.value = '';
            imageInput.value = '';
            linkInput.value = '';
            enddateInput.value = '';
            statusInput.value = '';
        }
        formError.textContent = '';
        modal.classList.add('show');
    };

    document.querySelectorAll('.open-advertisement-modal').forEach((btn) => {
        btn.addEventListener('click', () => {
            openModal('create');
        });
    });

    document.querySelectorAll('.edit-advertisement-btn').forEach((btn) => {
        btn.addEventListener('click', () => {
            openModal('edit', {
                url: btn.getAttribute('data-url'),
                type: btn.getAttribute('data-type'),
                image: btn.getAttribute('data-image'),
                link: btn.getAttribute('data-link'),
                enddate: btn.getAttribute('data-enddate'),
                status: btn.getAttribute('data-status'),
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