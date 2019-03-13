$(document).ready(function(){
    $(window).scroll(function () {
        if ($(this).scrollTop() > 0) {
            $('.main_container #scroller').fadeIn();
        } else {
            $('.main_container #scroller').fadeOut();
        }
    });
    $('.main_container #scroller').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 400);
        return false;
    });
});
