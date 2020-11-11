window.addEventListener("load", toggleArrow);
window.addEventListener("resize", toggleArrow);


      function toggleArrow() {
        var bbody = document.getElementById("contenuto").offsetHeight;
        var viewHeight = window.innerHeight; 
        viewHeight = 1.5*viewHeight;
        if (bbody > viewHeight) {
          document.getElementById("backtotop").style.visibility = "visible";
        
        } else {
          document.getElementById("backtotop").style.visibility = "hidden";
        
        }
      }
        
      function winTop(){
          var pup = document.getElementsByClassName('pup');
        for (var i = 0; i < pup.length; i++) {
            $(pup[i]).css("opacity", 1 );
        }
        window.scrollTo({top: 0, behavior: 'smooth'});
        
        
        
        
    }