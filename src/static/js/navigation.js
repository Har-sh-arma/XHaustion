document.addEventListener('DOMContentLoaded', () => {
    // Get DOM elements
    const sidebar = document.querySelector('.sidebar');
    const mobileNavTrigger = document.querySelector('.mobile-nav-trigger');
    const navLinks = document.querySelectorAll('.nav-link');
    const mainContent = document.querySelector('.main-content');

    // Mobile navigation toggle
    if (mobileNavTrigger) {
        mobileNavTrigger.addEventListener('click', () => {
            sidebar.classList.toggle('mobile-open');
        });
    }

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
            if (!sidebar.contains(e.target) && !mobileNavTrigger.contains(e.target)) {
                sidebar.classList.remove('mobile-open');
            }
        }
    });

    // Handle navigation
    navLinks.forEach(link => {
        link.addEventListener('click', async (e) => {
            e.preventDefault();
            const href = link.getAttribute('href');

            // Update active state
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');

            // Close mobile menu
            if (window.innerWidth <= 768) {
                sidebar.classList.remove('mobile-open');
            }

            try {
                // Animate content out
                mainContent.style.opacity = '0';
                mainContent.style.transform = 'translateY(20px)';
                
                // Wait for animation
                await new Promise(resolve => setTimeout(resolve, 300));

                // Navigate to new page
                window.location.href = href;
            } catch (error) {
                console.error('Navigation error:', error);
                mainContent.style.opacity = '1';
                mainContent.style.transform = 'translateY(0)';
            }
        });

        // Add hover effect for navigation items
        link.addEventListener('mouseenter', () => {
            const icon = link.querySelector('svg');
            if (icon) {
                icon.style.transform = 'scale(1.1) rotate(5deg)';
            }
        });

        link.addEventListener('mouseleave', () => {
            const icon = link.querySelector('svg');
            if (icon) {
                icon.style.transform = 'scale(1) rotate(0deg)';
            }
        });
    });

    // Initialize page content animation
    if (mainContent) {
        mainContent.style.opacity = '0';
        mainContent.style.transform = 'translateY(20px)';
        setTimeout(() => {
            mainContent.style.opacity = '1';
            mainContent.style.transform = 'translateY(0)';
        }, 100);
    }

    // Handle window resize
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            sidebar.classList.remove('mobile-open');
        }
    });

    // Set active state based on current URL
    const currentPath = window.location.pathname;
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.style.opacity = '0.8';
        } else {
            link.classList.remove('active');
        }
    });
}); 