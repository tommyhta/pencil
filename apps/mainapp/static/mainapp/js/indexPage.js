$(document).ready(function(){
    var scrollThis = $('.scroll');
    scrollThis.click(function(e){
        e.preventDefault();
        $('body,html').animate({
            scrollTop : $(this.hash).offset().top-75
        }, 1000)
    })
    // These are the animations/paralax effect when user scrolls
    $(window).scroll(function(){
        var wScroll=$(this).scrollTop();
        // console.log(wScroll)
        if(wScroll < 300){  
            $('#pencil_main').css({
                'transform' : 'rotate('+wScroll/2 +'deg)'
            });
        };

        if(wScroll > $('.models').offset().top-700){
            $('.faaade').addClass('comeoutt');
        }; 
        
        if(wScroll > $('#capabilities').offset().top-650){
            $('.fadeCap').addClass('comeout')
        }
        
        // Nav bar effect depends on the location of the page
        scrollThis.each(function(){
            var scrollThis = $('.scroll');
            var offset = $(this.hash).offset().top-200
            if(offset <= wScroll){
                $(this).parent().addClass('active');
                $(this).parent().siblings().removeClass('active');
            };
        });
    });
    
    // These effect will happen as the page finished loading
    $('.faade').each(function(){
        $('.faade').addClass('comeout');
    });
    $('.fadeF').addClass('comeoutt')
});