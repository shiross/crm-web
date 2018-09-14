function showMessage(mensaje,tipo,icono){
    $.notify({
        //icon: 'glyphicon glyphicon-' + icono,
        icon: 'glyphicon glyphicon-ok',
        message: mensaje
    },{
        //element: 'body',
        //position: "fixed",
        type: tipo,
        allow_dismiss: false,
        //newest_on_top: false,
        //showProgressbar: false,
        placement: {
            from: "bottom",
            align: "center"
        },
        //offset: 20,
        //spacing: 10,
        //z_index: 1031,
        delay: 1000,
        timer: 1000,
        mouse_over: null,
        animate: {
            enter: 'animated fadeInDown',
            exit: 'animated fadeOutUp'
        },
        template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
                    '<span data-notify="message">{2}</span>' +
                    //'<span class="glyphicon glyphicon-"'+icon+'"></span>' +
                    '<span class="glyphicon glyphicon-'+icono+'"></span>' +
                '</div>'
    });
 }


$('.partial_render').click(function (e) {
        e.preventDefault();
        url = $(this).attr('href')
        if(url !='#'){
            $.ajax({
                method: "GET",
                url: $(this).attr('href'),
                data: {}
            }).done(function (html) {
                if(html.indexOf("<html>") >= 0){
                    document.open()
                    document.write(html)
                    document.close()
                } else {
                    $('#render_content').html(html)
                }
            });
        }
    })

function responsive() {
    width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
    $('#right-options').html($('#left-option').html())
    if (width < 768) {
        $('#search-button').show()
        $('#right-bar').hide()
        $('#right-options').hide()
        $('#left-options').show()
    } else {
        $('#search-button').hide()
        $('#right-bar').show()
        $('#right-options').show()
        $('#left-options').hide()
    }
}

$(window).bind("load resize", function() {
    responsive();
});

function quit_search() {
    aux1 = $(".search-group");
    aux1.removeAttr('id')
    aux1.hide()
}

function show_search() {
    aux1 = $(".search-group")
    $(aux1[0]).attr('id', 'search-button')
    $(aux1[1]).attr('id', 'right-bar')
    $(aux1[0]).css('display', 'inline-block')
    //aux1.removeAttr('style')
    responsive()
}

quit_search()