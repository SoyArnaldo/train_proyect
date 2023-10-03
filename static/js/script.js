let header = document.querySelector("header");

window.addEventListener("scroll", () => {
	header.classList.toggle("sticky", this.window.scrollY > 80);
});
