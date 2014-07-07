$('body').scrollspy({
    target: '.sidebar-top',
    offset: 40
});


$(document).ready(function() {
    $('.wrapper').dotdotdot({
        watch: "window",
        after: ".readmore",
    }); 
});

