document.addEventListener("DOMContentLoaded", keepScroll);


 function keepScroll(){
    var elem = document.getElementById("contenuto");
    var scrollpos = localStorage.getItem('scrollpos');
    var this_url = "{{this_url}}";
    var referer_view ="{{referer_view}}";
    console.log( this_url, ' e ', referer_view )
    console.log('keep scroll vive e scroll poss is ', scrollpos )

            
            if (this_url == referer_view){
            
            if (scrollpos) {
                
            document.getElementById("contenuto").style.top = scrollpos;
            window.scroll(0,scrollpos)
            // var x = elem.style.width;
            console.log('non so perche qui non ci andava ', scrollpos )
            
            }
            else{
                window.scrollTo(0, 0);
            console.log('e qui non se ci annava ', scrollpos )    
            }
            }



};




        