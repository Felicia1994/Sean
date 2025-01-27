let slideIndex = 0;
let num_instance = 1;
showSlides();

// Next/previous controls
function plusSlides(n) {
  slideIndex += n - 1;
  num_instance += 1;
  showSlides();
}

// Thumbnail image controls
function currentSlide(n) {
  slideIndex = n - 1;
  num_instance += 1;
  showSlides();
}

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  slideIndex = (slideIndex + slides.length) % slides.length + 1;

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" slideshow-active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " slideshow-active";

  if (num_instance == 1) {
    setTimeout(showSlides, 5000); // change image every 5 seconds
  }
  else {
    num_instance -= 1;
  }
} 