(function ($) {
    $("#sidebarCollapse").click(function () {
        $("#sidebar").css({ marginLeft: '0px' });
        $("#overlay").show()
    });

    $("#overlay, #sidebar button.close-nav").click(function () {
        $("#sidebar").css({ marginLeft: '-250px' });
        $("#overlay").hide()
    });
})(jQuery)