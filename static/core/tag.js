document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('tagModal');
    const form = document.getElementById('tagForm');
    const modalTitle = document.getElementById('tagModalTitle');
    const nameInput = document.getElementById('id_name');
    const formError = document.getElementById('tagFormError');

    if (!modal || !form || !modalTitle || !nameInput || !formError) return;

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const openModal = (mode, data = {}) => {
        if (mode === 'edit') {
            modalTitle.textContent = 'Edit Tag';
            form.action = data.url || form.action;
            nameInput.value = data.name || '';
        } else {
            modalTitle.textContent = 'Buat Tag';
            form.action = form.dataset.createUrl;
            nameInput.value = '';
        }
        formError.textContent = '';
        modal.classList.add('show');
    };

    document.querySelectorAll('.open-tag-modal').forEach((btn) => {
        btn.addEventListener('click', () => {
            openModal('create');
        });
    });

    document.querySelectorAll('.edit-tag-btn').forEach((btn) => {
        btn.addEventListener('click', () => {
            openModal('edit', {
                url: btn.getAttribute('data-url'),
                name: btn.getAttribute('data-name'),
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
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrfToken,
                'X-Requested-With': 'XMLHttpRequest',
            },
        });

        const data = await response.json();

        if (response.ok && data.success) {
            modal.classList.remove('show');
            window.location.reload();
            return;
        }

        if (data.errors && data.errors.name) {
            formError.textContent = data.errors.name.map((item) => item.message).join(', ');
        } else if (data.message) {
            formError.textContent = data.message;
        } else {
            formError.textContent = 'Terjadi kesalahan.';
        }
    });
});