window.addEventListener("load", fadeTop);
    window.addEventListener("resize", fadeTop);


    

    function fadeTop() {
		var cbody = document.getElementById("contenuto").offsetHeight;
        var cviewHeight = window.innerHeight; 
        cviewHeight = 1.4*cviewHeight; 
        if (cbody > cviewHeight) {
          document.getElementById("grad1").style.visibility = "visible";
          
        
        } else {
          document.getElementById("grad1").style.visibility = "hidden";
           
        }
    };