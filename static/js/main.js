$(document).ready(function () {
    
    // back to the top button is hidden in default position and shows when the user scrolls down
    
    $(window).scroll(function() {
       console.log("page scrolling!");
     $('.back-top-btn').show();
    });

    // when the user clicks on the back to top button, the page returns to the top and the button disappears
    $('.back-top-link').click(function () {
        console.log("button was clicked!"); 
         
        window.scrollTo(0,0);
        $('.back-top-btn').hide();
    });
});
