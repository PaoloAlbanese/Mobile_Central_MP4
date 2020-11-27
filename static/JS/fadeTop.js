window.addEventListener("load", fadeTop);
window.addEventListener("resize", fadeTop);

// if the body's height is 1.8 times the viewport, there will be a fading effect as a window-wide strip (aka 'grad1') just under the sorting buttons.  
    

    function fadeTop() {
		var cbody = document.getElementById("contenuto").offsetHeight;
        var cviewHeight = window.innerHeight; 
        cviewHeight = 1.8*cviewHeight; 
        if (cbody > cviewHeight) {
          document.getElementById("grad1").style.visibility = "visible";
          
        
        } else {
          document.getElementById("grad1").style.visibility = "hidden";
           
        }
    };