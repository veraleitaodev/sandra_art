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

    // to activate bootstrap 5 tooltips - code sourced on bootstrap documentation -
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))

    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    console.log(tooltipList);

    // remove item from the bag and reload on click
    $('.remove-item').click(function(e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id');
        var url = `/bag/remove/${itemId}/`;
        var data = {'csrfmiddlewaretoken': csrfToken};

        $.post(url, data)
         .done(function() {
             location.reload();
         });
});
