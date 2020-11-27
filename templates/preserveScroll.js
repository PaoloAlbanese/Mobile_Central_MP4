document.addEventListener("DOMContentLoaded", keepScroll);

// takes the local storage var scrollpos value and sets it as the page scrolling position if the current page and the refer are the same
 function keepScroll(){
    var elem = document.getElementById("contenuto");
    var scrollpos = localStorage.getItem('scrollpos');
    var this_url = "{{this_url}}";
    var referer_view ="{{referer_view}}";
    console.log( this_url, ' e ', referer_view )
    

            
            if (this_url == referer_view){
            
            if (scrollpos) {
                
            document.getElementById("contenuto").style.top = scrollpos;
            window.scroll(0,scrollpos)
           
            }
            else{
                window.scrollTo(0, 0);
             
            }
            }



};




        