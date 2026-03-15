document.querySelectorAll('nav a').forEach(anchor => {
	anchor.addEventListener('click', function(e) {
		const hash = this.hash;

		if (!hash) return;

		const target = document.querySelector(hash);
		if (!target) return;

		e.preventDefault();

		window.scrollTo({
			top: target.offsetTop - 80,
			behavior: 'smooth'
		});
	});
});

const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const navMenu = document.querySelector('nav ul');

mobileMenuBtn.addEventListener('click', function() {
	navMenu.classList.toggle('show');
});

document.addEventListener('click', function(e) {
	if (!e.target.closest('nav') && !e.target.closest('.mobile-menu-btn')) {
		navMenu.classList.remove('show');
	}
});
