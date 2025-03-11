console.log('This site made by Voylin.');


document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.querySelector(".menu-toggle");
	const backToTopButton = document.getElementById("back-to-top");

    if (menuToggle) {
        menuToggle.addEventListener("click", function () {
            document.querySelector(".mobile-menu").classList.toggle("show");
        });
    }

    if (backToTopButton) {
        window.addEventListener("scroll", function () {
            if (window.scrollY > 300) {
                backToTopButton.style.display = "block";
            } else {
                backToTopButton.style.display = "none";
            }
        });

        backToTopButton.addEventListener("click", function () {
            window.scrollTo({top: 0, behavior: "smooth"});
        });
    }
});
