const sidebar = document.getElementById('sidebar');
const sidebarBackdrop = document.getElementById('sidebarBackdrop');
const btnToggle = document.getElementById('btnToggle');

if (sidebar && sidebarBackdrop && btnToggle) {
    const toggleNav = () => {
        sidebar.classList.toggle('active');
        sidebarBackdrop.classList.toggle('active');
    };

    btnToggle.addEventListener('click', toggleNav);
    sidebarBackdrop.addEventListener('click', toggleNav);
}

const avatarTrigger = document.getElementById('avatarTrigger');
const profileDropdown = document.getElementById('profileDropdown');

if (avatarTrigger && profileDropdown) {
    avatarTrigger.addEventListener('click', (e) => {
        e.stopPropagation();
        profileDropdown.classList.toggle('show');
    });

    document.addEventListener('click', (e) => {
        if (!profileDropdown.contains(e.target)) {
            profileDropdown.classList.remove('show');
        }
    });
}

const toastContainer = document.querySelector('.toast-container');

if (toastContainer) {
    const toasts = toastContainer.querySelectorAll('.toast');
    toasts.forEach((toast, index) => {
        setTimeout(() => {
            toast.classList.add('toast-out');
            setTimeout(() => {
                toast.remove();
            }, 200);
        }, 4000 + index * 500);
    });
}

const deleteModal = document.getElementById('deleteModal');
const deleteForm = document.getElementById('deleteForm');
const deleteTitle = document.getElementById('deleteTitle');
const deleteButtons = document.querySelectorAll('.delete-btn');

if (deleteModal && deleteForm && deleteTitle) {
    const openDeleteModal = (e) => {
        e.preventDefault();
        const url = e.currentTarget.getAttribute('data-url');
        const title = e.currentTarget.getAttribute('data-title');
        deleteTitle.textContent = title || 'item';
        deleteForm.setAttribute('action', url);
        deleteModal.classList.add('show');
    };

    deleteButtons.forEach((btn) => {
        btn.addEventListener('click', openDeleteModal);
    });

    deleteModal.querySelectorAll('[data-close-modal]').forEach((btn) => {
        btn.addEventListener('click', () => {
            deleteModal.classList.remove('show');
        });
    });

    deleteModal.addEventListener('click', (e) => {
        if (e.target === deleteModal) {
            deleteModal.classList.remove('show');
        }
    });
}