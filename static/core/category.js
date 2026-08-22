document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('categoryModal');
    const form = document.getElementById('categoryForm');
    const modalTitle = document.getElementById('categoryModalTitle');
    const nameInput = document.getElementById('id_name');
    const formError = document.getElementById('categoryFormError');

    if (!modal || !form || !modalTitle || !nameInput || !formError) return;

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const openModal = (mode, data = {}) => {
        if (mode === 'edit') {
            modalTitle.textContent = 'Edit Kategori';
            form.action = data.url || form.action;
            nameInput.value = data.name || '';
        } else {
            modalTitle.textContent = 'Buat Kategori';
            form.action = form.dataset.createUrl;
            nameInput.value = '';
        }
        formError.textContent = '';
        modal.classList.add('show');
    };

    document.querySelectorAll('.open-category-modal').forEach((btn) => {
        btn.addEventListener('click', () => {
            openModal('create');
        });
    });

    document.querySelectorAll('.edit-category-btn').forEach((btn) => {
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