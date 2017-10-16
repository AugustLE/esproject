var hasScrolled = false;

function scrollDown() {

    var scroll_offset = document.getElementById("scroll_offset").value;
    var id = document.getElementById("scroll_point").value;
    console.log(scroll_offset);

    if(!hasScrolled) {

        $('body,html').animate({
        scrollTop: $('#'+id).offset().top - scroll_offset
        }, 2000);
    }
}

window.onload = function() {

    setTimeout(scrollDown, 500);

    //scrollDown();
};

function animateFrontIcon() {

    //$("#myelm").stop().animate({height : "300px"}, 500);
}


window.onscroll = function() {

    hasScrolled = true;

};