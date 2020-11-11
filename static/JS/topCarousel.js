var myTimer;
var slideIndex = 1;
var slideshowContainer ;
window.addEventListener("load",function() {
    showSlides(slideIndex);
    myTimer = setInterval(function(){plusSlides(1)}, 4000);



})

slideshowContainer = document.getElementsByClassName('slidesContainer')[0];

slideshowContainer.addEventListener('mouseenter', pause);
slideshowContainer.addEventListener('mouseleave', resume);


showSlides(slideIndex);

function plusSlides(n) {

  showSlides(slideIndex += n);
}

function currentSlide(n) {
  clearInterval(myTimer);
  myTimer = setInterval(function(){plusSlides(n + 1)}, 4000);  
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
      

  };
  
  slides[slideIndex-1].style.display = "block";


};


function pause()  {
  clearInterval(myTimer);
  
}

function resume() {
  clearInterval(myTimer);
  myTimer = setInterval(function(){plusSlides(slideIndex)}, 4000);
  
} 

$(window).scroll(function(){
    $(".slidesContainer").css("opacity", 1 - $(window).scrollTop() / 250);
  });