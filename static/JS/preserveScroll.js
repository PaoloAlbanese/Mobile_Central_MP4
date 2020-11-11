document.addEventListener("DOMContentLoaded", keepScroll);

 function keepScroll(){
    var elem = document.getElementById("contenuto");
    var scrollpos = localStorage.getItem('scrollpos');
    var this_url = "{{this_url}}";
    var referer_view ="{{referer_view}}";
    
            
            if (this_url == referer_view){
            
            if (scrollpos) {
                
            document.getElementById("contenuto").style.top = scrollpos;
            window.scroll(0,scrollpos)
            // var x = elem.style.width;
            
            }
            else{
                window.scrollTo(0, 0);
            }
            }



};




        window.addEventListener("scroll", SetScrollY);
        
        function SetScrollY(){
            
            localStorage.setItem('scrollpos', window.scrollY);
            var scrollpos = localStorage.getItem('scrollpos');
            console.log('ho settato io', scrollpos);
        };

        window.onbeforeunload = function(e) {
                var scrollpos = localStorage.getItem('scrollpos');
                elem.style.top = scrollpos;
            localStorage.setItem('scrollpos', window.scrollY);
            console.log('elem',elem);
        };
