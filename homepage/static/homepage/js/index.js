
function resizeHeaderOnScroll() {

  var distanceY = window.pageYOffset || document.documentElement.scrollTop,
  shrinkOn = 100;
  headerEl = document.getElementById('top_image_container');
  checklist = document.getElementById('checklist');
  //checklist.style.height = '500px';

  if (distanceY > shrinkOn) {

    checklist.style.height = '500px';
    //headerEl.style.height = '200px';

  } else  {
    //headerEl.classList.remove("shrink");
    //headerEl.style.height = "100%";
      checkWidth();

      console.log($(window).width());
      //$('#top_image_container').animate({height:'100%'});


  }

}

function checkWidth() {

    if($(window).width() > 900) {
          checklist.style.height = '250px';
    } else {

      checklist.style.height = '500px';
    }
}


window.addEventListener('scroll', resizeHeaderOnScroll);

window.onload = function() {

    checkWidth();

};