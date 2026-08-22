document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('accountModal');
    const form = document.getElementById('accountForm');
    const modalTitle = document.getElementById('accountModalTitle');
    const usernameInput = document.getElementById('id_username');
    const firstNameInput = document.getElementById('id_first_name');
    const lastNameInput = document.getElementById('id_last_name');
    const emailInput = document.getElementById('id_email');
    const jobInput = document.getElementById('id_job');
    const photoInput = document.getElementById('id_photo');
    const genderInput = document.getElementById('id_gender');
    const passwordInput = document.getElementById('id_password');
    const formError = document.getElementById('accountFormError');

    if (
        !modal ||
        !form ||
        !modalTitle ||
        !usernameInput ||
        !firstNameInput ||
        !lastNameInput ||
        !emailInput ||
        !jobInput ||
        !photoInput ||
        !genderInput ||
        !passwordInput ||
        !formError
    ) return;

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const openModal = (mode, data = {}) => {
        if (mode === 'edit') {
            modalTitle.textContent = 'Edit Pengguna';
            form.action = data.url || form.action;
            usernameInput.value = data.username || '';
            firstNameInput.value = data.first_name || '';
            lastNameInput.value = data.last_name || '';
            emailInput.value = data.email || '';
            jobInput.value = data.job || '';
            photoInput.value = data.photo || '';
            genderInput.value = data.gender || '';
            passwordInput.value = '';
            passwordInput.placeholder = 'Kosongkan jika tidak ingin mengubah';
        } else {
            modalTitle.textContent = 'Buat Pengguna';
            form.action = form.dataset.createUrl;
            usernameInput.value = '';
            firstNameInput.value = '';
            lastNameInput.value = '';
            emailInput.value = '';
            jobInput.value = '';
            photoInput.value = '';
            genderInput.value = '';
            passwordInput.value = '';
            passwordInput.placeholder = 'Password';
        }
        formError.textContent = '';
        modal.classList.add('show');
    };

    document.querySelectorAll('.open-account-modal').forEach((btn) => {
        btn.addEventListener('click', () => {
            openModal('create');
        });
    });

    document.querySelectorAll('.edit-account-btn').forEach((btn) => {
        btn.addEventListener('click', () => {
            openModal('edit', {
                url: btn.getAttribute('data-url'),
                username: btn.getAttribute('data-username'),
                first_name: btn.getAttribute('data-first_name'),
                last_name: btn.getAttribute('data-last_name'),
                email: btn.getAttribute('data-email'),
                job: btn.getAttribute('data-job'),
                photo: btn.getAttribute('data-photo'),
                gender: btn.getAttribute('data-gender'),
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