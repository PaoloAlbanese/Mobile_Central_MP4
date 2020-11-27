window.addEventListener("scroll", SetScrollY);
        // setting the scroll position as local storage variable. it will be read py the 'PreserveScroll' script to preserve scroll position upon load
        function SetScrollY(){
            
            localStorage.setItem('scrollpos', window.scrollY);
            
            
        };

        window.onbeforeunload = function(e) {
            
                
            localStorage.setItem('scrollpos', window.scrollY);
            
        };
