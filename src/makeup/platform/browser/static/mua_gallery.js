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
      slides[slideIndex-1].style.display = "block";
  }
  showSlides(slideIndex);

  document.getElementById ("prev").addEventListener ("click", function() {plusSlides(-1)}, false);
  document.getElementById ("next").addEventListener ("click", function() {plusSlides(1)}, false);
});
