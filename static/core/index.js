document.addEventListener('DOMContentLoaded', () => {
    const skeletonWrapper = document.getElementById('skeleton-wrapper');
    const dashboardContent = document.getElementById('dashboard-content');

    if (!skeletonWrapper || !dashboardContent) return;

    const showDashboard = () => {
        skeletonWrapper.classList.add('fade-out');
        setTimeout(() => {
            skeletonWrapper.style.display = 'none';
            dashboardContent.classList.remove('dashboard-content-hidden');
            dashboardContent.classList.add('dashboard-content-visible');
        }, 300);
    };

    setTimeout(showDashboard, 500);
});