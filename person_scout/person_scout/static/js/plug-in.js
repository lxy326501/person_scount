// JavaScript Document

//aside
	$(function(){
		$(".nav-show ul").show();
		// nav收缩展开
		$('.nav-item>a').on('click', function () {
			$('.nav-item').children('ul').slideUp(200);
			if ($(this).next().css('display') == "none") {
				//展开
				$('.nav-item').children('ul').slideUp(200);
				$(this).next('ul').slideDown(200);
				$(this).parent('li').addClass('nav-show').siblings('li').removeClass('nav-show');
			} else {
				//收缩
				$(this).next('ul').slideUp(200);
				$('.nav-item.nav-show').removeClass('nav-show');
			}
		});
	});

//admin-hover效果
	$(".nav-admin-box").mouseenter(function(){
		$(".hover-admin").stop().slideDown(200)
	})
	$(".nav-admin-box").mouseleave(function(){
		$(".hover-admin").stop().slideUp(200)
	})

