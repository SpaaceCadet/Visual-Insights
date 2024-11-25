$("#mobile").click(function() {
    $('.sideBar').addClass("showMenu");
    $('.sideBar').removeClass("widthChange");
    $('.backdrop').addClass('showBackdrop')
});
$(".cross-icon").click(function() {
    $('.sideBar').removeClass("showMenu");
    $('.backdrop').removeClass('showBackdrop')
});
$(".backdrop").click(function() {
    $('.sideBar').removeClass("showMenu");
    $('.backdrop').removeClass('showBackdrop')
});
$("#desktop").click(function() {
    $('li label').toggleClass("hideMenuList");
    $('.sideBar').toggleClass("widthChange");
});
$('li').click(function() {
    $('li').removeClass();
    $(this).addClass('selected');
    $('.sideBar').removeClass("showMenu");
});