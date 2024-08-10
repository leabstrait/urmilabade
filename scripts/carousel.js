// carousel.js

class Carousel {
    constructor(element) {
        this.carousel = element;
        this.slides = this.carousel.querySelectorAll("li");
        this.totalSlides = this.slides.length;
        this.currentIndex = 0;
        this.buttons = {};
        this.touchStartX = 0;
        this.touchEndX = 0;

        // Create next and previous buttons
        this.createButtons();

        this.initTouchEvents();

        this.initLightbox();
    }
    createButtons() {
        const buttonNames = ["next", "prev"];
        buttonNames.forEach((name) => {
            const button = document.createElement("button");
            button.innerHTML =
                name === "next"
                    ? '<span class="icon is-large"><i class="material-icons">chevron_right</i></span>'
                    : '<span class="icon is-large"><i class="material-icons">chevron_left</i></span>';
            button.classList.add(`${name}-btn`);
            button.addEventListener("click", () =>
                this.handleButtonClick(name)
            );
            this.buttons[name] = button;
            this.carousel.appendChild(button);
        });
    }

    handleButtonClick(name) {
        if (name === "next") {
            this.nextSlide();
        } else if (name === "prev") {
            this.prevSlide();
        }
    }
    initTouchEvents() {
        this.carousel.addEventListener("touchstart", (event) => {
            this.touchStartX = event.touches[0].clientX;
        });

        this.carousel.addEventListener("touchend", (event) => {
            this.touchEndX = event.changedTouches[0].clientX;
            this.handleSwipe();
        });
    }
    handleSwipe() {
        const swipeThreshold = 100; // Adjust as needed
        const deltaX = this.touchEndX - this.touchStartX;

        if (deltaX > swipeThreshold) {
            this.prevSlide(); // Swipe right
        } else if (deltaX < -swipeThreshold) {
            this.nextSlide(); // Swipe left
        }
    }

    initLightbox() {
        const lightbox = document.createElement("div");
        lightbox.className = "lightbox";
        lightbox.innerHTML = `
        <span class="close">&times;</span>
        <div class="lightbox-content">
            <button class="prev-btn">
                <span class="icon is-large">
                    <i class="material-icons">chevron_left</i>
                </span>
            </button>
            <img src="" alt="" class="lightbox-image">
            <button class="next-btn">
                <span class="icon is-large">
                    <i class="material-icons">chevron_right</i>
                </span>
            </button>
        </div>
        `;
        document.body.appendChild(lightbox);

        this.lightbox = lightbox;
        this.lightboxImage = lightbox.querySelector(".lightbox-image");
        this.prevButton = lightbox.querySelector(".prev-btn");
        this.nextButton = lightbox.querySelector(".next-btn");
        this.closeButton = lightbox.querySelector(".close");

        // Close lightbox when close button is clicked
        this.closeButton.addEventListener("click", () => {
            this.lightbox.style.display = "none";
        });
        // Close lightbox when clicking outside the image
        lightbox.addEventListener("click", (event) => {
            if (event.target === lightbox) {
                this.lightbox.style.display = "none";
            }
        });

        // Show previous image in lightbox
        this.prevButton.addEventListener("click", () => {
            this.currentIndex =
                (this.currentIndex - 1 + this.totalSlides) % this.totalSlides;
            this.showImageInLightbox(this.currentIndex);
        });

        // Show next image in lightbox
        this.nextButton.addEventListener("click", () => {
            this.currentIndex = (this.currentIndex + 1) % this.totalSlides;
            this.showImageInLightbox(this.currentIndex);
        });

        // Show lightbox when image is clicked
        this.slides.forEach((slide, index) => {
            slide.addEventListener("click", () => {
                this.currentIndex = index;
                this.showImageInLightbox(index);
                this.lightbox.style.display = "flex";
            });
        });
    }

    showImageInLightbox(index) {
        this.lightboxImage.src = this.slides[index].querySelector("img").src;
        this.lightboxImage.alt = this.slides[index].querySelector("img").alt;
    }

    showSlide(index) {
        if (index < 0) {
            index = this.totalSlides - 1;
        } else if (index >= this.totalSlides) {
            index = 0;
        }

        const offset = -index * 100;
        this.carousel.querySelector(
            "ul"
        ).style.transform = `translateX(${offset}%)`;
        this.currentIndex = index;
    }

    nextSlide() {
        this.showSlide(this.currentIndex + 1);
    }

    prevSlide() {
        this.showSlide(this.currentIndex - 1);
    }

    startAutoSlide(interval = 3000) {
        this.stopAutoSlide();
        this.autoSlideInterval = setInterval(() => {
            this.nextSlide();
        }, interval);
    }

    stopAutoSlide() {
        clearInterval(this.autoSlideInterval);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const carousels = document.querySelectorAll(".carousel");
    carousels.forEach((carousel) => {
        new Carousel(carousel);
    });
});
