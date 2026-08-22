document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.resources-tab');
    const tabContents = document.querySelectorAll('.resources-tab-content');

    if (tabs.length && tabContents.length) {
        tabs.forEach((tab) => {
            tab.addEventListener('click', () => {
                const targetId = tab.getAttribute('data-tab');
                tabs.forEach((t) => t.classList.remove('active'));
                tabContents.forEach((content) => content.classList.remove('active'));
                tab.classList.add('active');
                const target = document.getElementById(targetId);
                if (target) {
                    target.classList.add('active');
                }
            });
        });
    }

    const radioCards = document.querySelectorAll('.resource-choice-card');
    radioCards.forEach((card) => {
        const radio = card.querySelector('input[type="radio"]');
        if (!radio) return;
        radio.addEventListener('change', () => {
            radioCards.forEach((c) => c.classList.remove('active'));
            if (radio.checked) {
                card.classList.add('active');
            }
        });
    });

    const loading = document.getElementById('resourcesLoading');
    if (!loading) return;

    const showLoading = () => loading.classList.add('show');
    const hideLoading = () => loading.classList.remove('show');

    document.querySelectorAll('[data-resource-form]').forEach((form) => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const confirmMessage = form.getAttribute('data-confirm');
            if (confirmMessage && !confirm(confirmMessage)) {
                return;
            }

            showLoading();

            try {
                const formData = new FormData(form);
                const response = await fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                });

                if (form.getAttribute('data-download') === 'true') {
                    if (!response.ok) {
                        const contentType = response.headers.get('content-type') || '';
                        const data = contentType.includes('application/json')
                            ? await response.json()
                            : null;
                        alert(data && data.message ? data.message : 'Terjadi kesalahan.');
                        return;
                    }

                    const blob = await response.blob();
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;

                    const contentDisposition = response.headers.get('Content-Disposition');
                    let filename = 'backup.json';
                    if (contentDisposition) {
                        const match = contentDisposition.match(/filename="?([^"]+)"?/);
                        if (match) {
                            filename = match[1];
                        }
                    }
                    a.download = filename;
                    document.body.appendChild(a);
                    a.click();
                    a.remove();
                    window.URL.revokeObjectURL(url);
                    window.location.reload();
                    return;
                }

                const contentType = response.headers.get('content-type') || '';
                const data = contentType.includes('application/json')
                    ? await response.json()
                    : null;

                if (response.ok && data && data.success) {
                    window.location.reload();
                } else {
                    alert(data && data.message ? data.message : 'Terjadi kesalahan.');
                }
            } catch (error) {
                alert('Terjadi kesalahan jaringan atau server.');
            } finally {
                hideLoading();
            }
        });
    });
});