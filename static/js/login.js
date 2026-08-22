window.addEventListener('load', () => {
    const loader = document.getElementById('page-loader');
    if (loader) {
        loader.classList.add('hidden');
    }
});

const loginForm = document.getElementById('login-form');
const loginBtn = document.getElementById('login-btn');

if (loginForm && loginBtn) {
    loginForm.addEventListener('submit', (e) => {
        if (loginForm.classList.contains('submitting')) {
            e.preventDefault();
            return;
        }

        loginForm.classList.add('submitting');
        loginBtn.classList.add('loading');
        loginBtn.disabled = true;

        const originalContent = loginBtn.innerHTML;
        setTimeout(() => {
            loginForm.submit();
        }, 400);
    });
}