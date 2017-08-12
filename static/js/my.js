/**
 * Created by admin on 2017/5/20.
 */
$(document).ready(function(){

    $(".avatar a:first").mouseenter(function(){
        $(".avatar span:first").slideUp(1000)
    });

    $(".avatar a:first").mouseleave(function(){
        $(".avatar span:first").slideDown(1000)
    });

    //barcode in
    $("#gb2big5").mouseenter(function () {
        $(".app-footer-guide").fadeTo(100,1);
    });

    //barcode out
    $("#gb2big5").mouseleave(function () {
        $(".app-footer-guide").fadeTo(100,0);
    });
    
    //turn head
    $(".scroll-h").click(function () {
        $("html, body").animate({
          scrollTop: $($(this)).offset().bottom + "px"
        }, {
          duration: 500,
          easing: "swing"
        });
        return false;
    });

    //turn foot
    $(".scroll-b").click(function () {
        $("html, body").animate({
          scrollTop: $($(this)).offset().top + "px"
        }, {
          duration: 500,
          easing: "swing"
        });
        return false;
    });

    /**
     * 页面随滚
     */
    // $(function() {
    // var $sidebar   = $("aside"),
    //     $window    = $(window),
    //     offset     = $sidebar.offset(),
    //     topPadding = 15;
    //
    // $window.scroll(function() {
    //     if ($window.scrollTop() > offset.top) {
    //         $sidebar.stop().animate({
    //             marginTop: $window.scrollTop() - offset.top + topPadding
    //         });
    //     } else {
    //         $sidebar.stop().animate({
    //             marginTop: 0
    //         });
    //     }
    // });

});

});


function switchbutton(obj) {
    if (obj.paused) {
        obj.play();
    } else {
        obj.pause();
    }
};




