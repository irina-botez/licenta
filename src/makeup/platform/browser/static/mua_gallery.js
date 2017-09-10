document.addEventListener("DOMContentLoaded", function(event) {
  var slideIndex = 1;


  var plusSlides = function(n) {
      showSlides(slideIndex += n);
  }

  function currentSlide(n) {
      showSlides(slideIndex = n);
  }

  function showSlides(n) {
      var i;
      var slides = document.getElementsByClassName("img-container");
      if (n > slides.length) {slideIndex = 1}
      if (n < 1) {slideIndex = slides.length}
      for (i = 0; i < slides.length; i++) {
          slides[i].style.display = "none";
      }
      var previous_slide = slides[slideIndex-1];
      if(previous_slide)
        previous_slide.style.display = "block";
  }
  showSlides(slideIndex);

  var prev = $('#prev');
  var next = $('#next');

  if(prev) prev.on("click", function() {plusSlides(-1)});
  if(next) next.on("click", function() {plusSlides(1)});

});
