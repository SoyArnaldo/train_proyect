var swiper = new Swiper(".slide-content", {
	slidesPerView: 3,
	spaceBetween: 25,
	slidesPerGroupSkip: 1,
	grabCursor: true,
	keyboard: {
		enabled: true,
	},
	breakpoints: {
		0: {
		slidesPerView: 1,
		},
		520: {
			slidesPerView: 2,
			},
		950: {
			slidesPerView: 3,
			},
	},
	scrollbar: {
		el: ".swiper-scrollbar",
	},
	navigation: {
		nextEl: ".swiper-button-next",
		prevEl: ".swiper-button-prev",
	},
	pagination: {
		el: ".swiper-pagination",
		clickable: true,
		dynamicBullets: true,
	},
});
