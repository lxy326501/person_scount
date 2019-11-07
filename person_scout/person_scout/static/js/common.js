
$(function(){
    // nav收缩展开
    $('.nav-item>a').on('click',function(){
        if (!$('.nav').hasClass('nav-mini')) {
            if ($(this).next().css('display') == "none") {
                //展开未展开
                $('.nav-item').children('ul').slideUp(300);
                $(this).next('ul').slideDown(300);
                $(this).parent('li').addClass('nav-show').siblings('li').removeClass('nav-show');
            }else{
                //收缩已展开
                $(this).next('ul').slideUp(300);
                $('.nav-item.,nav-show').removeClass('nav-show');
            }
        }
    });
});

// admin展开收缩
$(".nav-box").mouseenter(function(){
	$(this).children(".nav-hide").stop().slideDown(300);
});
$(".nav-box").mouseleave(function(){
	$(this).children(".nav-hide").stop().slideUp(300);
})