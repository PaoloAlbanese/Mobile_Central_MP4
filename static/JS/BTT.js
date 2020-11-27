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
      
    // from Code Institute, combined with Nick Ciliak's (modified) code to fade the products back in
      function winTop(){
          var pup = document.getElementsByClassName('pup');
        for (var i = 0; i < pup.length; i++) {
            $(pup[i]).css("opacity", 1 );
        }
        window.scrollTo({top: 0, behavior: 'smooth'});
        
        
        
        
    }