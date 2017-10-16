
var hasScrolled = false;

function scrollDown() {

    if(!hasScrolled) {

        $('body,html').animate({
        scrollTop: $('#about_what').offset().top - 40
        }, 2000);
    }
}

window.onload = function() {
    setTimeout(scrollDown, 500);

    //scrollDown();
};

function animateFrontIcon() {

    $("#myelm").stop().animate({height : "300px"}, 500);
}


window.onscroll = function() {

    hasScrolled = true;

};