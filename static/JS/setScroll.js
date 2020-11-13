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
