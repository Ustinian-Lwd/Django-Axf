
$(function () {
    // 隐藏滚动条
    $('.home').width(innerWidth)



    //轮播图
    var swiper = new Swiper('#topSwiper', {
      slidesPerView: 1,
      spaceBetween: 30,
      autoplay: 2500,
      loop: true,
      pagination: '.swiper-pagination',
    });


    //每日必购
    var mustbuySwiper = new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        spaceBetween: 10,
        loop: true
    })

})