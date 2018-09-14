function ajax_call(url, data, render, callback) {
    $.ajax({
        method: "POST",
        url: url,
        data: data,
        async: false
    }).done(function (response) {
        if (render != null){
            $(render).html(response)
        } else {
            dictionary = JSON.parse(response)
            if ("message" in dictionary && dictionary.message != ''){
                if (dictionary.success) {
                    showMessage(dictionary.message, "success", "ok")
                } else {
                    showMessage(dictionary.message, "danger", "remove")
                }
            }
        }
        if(callback != null){
            if(typeof dictionary === 'undefined')
                callback(response)
            else
                callback(dictionary)
        }
    })
}
function remove_empty_columns() {
    if(!$.trim($('#table_content > tr > td:last-child').html()).length){
        $('#table_content > tr > td:last-child, .actions_header').remove()
    }
}
function remove_empty_columns_retiro() {
    if(!$.trim($('#table_body_retiro > tr > td:last-child').html()).length){
        $('#table_body_retiro > tr > td:last-child, .actions_header').remove()
    }
}
function query(url) {
    data = {
        data: JSON.stringify({
            page_nr: page_nr,
            max_entries: max_entries,
            like_search: like_search,
            order_by: order_by,
            ascendant: ascendant
        })
    }
    ajax_call(url, data, '#table_content', function () { remove_empty_columns() })
}
function ajax_call_exe(url, data, render, callback) {
    $.ajax({
        method: "POST",
        url: url,
        data: data,
        async: false
    }).done(function (response) {
        if (render != null){
            $(render).html(response)
        } else {
            dictionary = JSON.parse(response)
            if ("message" in dictionary && dictionary.message != ''){
                if (dictionary.success) {
                    swal({
                    title: "Operacion Correcta...",
                    text: dictionary.message,
                    type: "success",
                    showCancelButton: false,
                    confirmButtonColor: "#DD6B55",
                    confirmButtonText: "Confirmar",
                    }).then(function () {
                        query_render('/personal');
                    });
                } else {
                    swal({
                    title: "Operacion Incorrecta...",
                    text: dictionary.message,
                    type: "error",
                    showCancelButton: false,
                    confirmButtonColor: "#DD6B55",
                    confirmButtonText: "Confirmar",
                    }).then(function () {
                        query_render('/personal');
                    });
                }
            }
        }
        if(callback != null){
            callback(response)

        }
    })
}
function query_render(url) {
            $.ajax({
                method: "GET",
                url: url,
                data: { }
            }).done(function (html) {
                $('#render_content').html(html);
            });

}
function verif_inputs() {
    $.each($('#form .form-line input'), function (index, value) {
        if(value.value.length > 0){
            $(value).parent().addClass('focused')
        }
    })
    $.each($('#form .form-line select'), function (index, value) {
        if(value.value.length > 0){
            $(value).parent().parent().addClass('focused')
        }
    })

}
function verif_inputs_update() {
    $.each($('.form-line input'), function (index, value) {
        if(value.value != ""){
            $(value).parent().addClass('focused')
        }
    })
    $.each($('.form-line select'), function (index, value) {

        if(value.value != ""){
            $(value).parent().parent().addClass('focused')
        }
    })

}
function clean_form() {
    $('div.focused').removeClass('focused')
    $('div.error').removeClass('error')
    $('label.error').text('')
}
function reload_form() {
    //On focusin event
    $('.datepicker').focusin(function () {
        var $this = $(this);
        if ($this.val() == '') { $this.parents('.form-line').removeClass('focused'); }
    });
    $('.selectpicker').focusin(function () {
        var $this = $(this);
        if ($this.val() == '') { $this.parents('.form-line').removeClass('focused'); }
    });
    $('.form-control').focus(function () {
        $(this).parents('.form-line').addClass('focused');
    }).focusout(function () {
        var $this = $(this);
        if ($this.parents('.form-group').hasClass('form-float')) {
            if ($this.val() == '') { $this.parents('.form-line').removeClass('focused'); }
        }
        else {
            $this.parents('.form-line').removeClass('focused');
        }
    });

    $('body').on('click', '.form-float .form-line .form-label', function () {
        $(this).parent().find('input').focus();
    });
}

function confirmation_message(title, callback) {
    swal({
            //title: "¿Está seguro de que desea cancelar la operacion?",
            title: "¿Está seguro de que desea cancelar la operacion?",
            text: "Al cerrar esta ventana, no se guardará ningún cambio realizado",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Aceptar",
            cancelButtonText: "Cancelar",
            closeOnConfirm: true,
            closeOnCancel: true
        }, function (isConfirm) {
            if (isConfirm) {
                $('#form').modal('hide')
                //callback()
            }
        })
}
function ajax_callselect2(url, data,select,callback) {
    $.ajax({
        method: "POST",
        url: url,
        data: data,
        async: false
    }).done(function (response) {
        dictionary = JSON.parse(response);
        var opcion ="";
        for(var i = 0; i<dictionary.response.length; i++){
            opcion=opcion+"<option value='"+dictionary.response[i].id+"'>"+dictionary.response[i].nombre+"</option>";
        }
        select.append(opcion).selectpicker('refresh')
        if(callback!=null){
            callback()
        }
    })
}
function efectos() {
    //Tooltip
    $('[data-toggle="tooltip"]').tooltip({
        container: 'body'
    });
    //On focus event
    $('.form-control').focus(function () {
        $(this).parent().addClass('focused');
    });
    //On focusin event
    $('.datepicker').focusin(function () {
        var $this = $(this);
        if ($this.parents('.form-group').hasClass('form-float')) {
            if ($this.val() == '') { $this.parents('.form-line').removeClass('focused'); }
        }
        else {
            if ($this.val() == '') { $this.parents('.form-line').removeClass('focused'); }
        }
    });
    //On focusout event
    $('.form-control').focusout(function () {
        var $this = $(this);
        if ($this.parents('.form-group').hasClass('form-float')) {
            if ($this.val() == '') { $this.parents('.form-line').removeClass('focused'); }
        }
        else {
            if ($this.val() == '') { $this.parents('.form-line').removeClass('focused'); }
        }
    });

    //On label click
    $('body').on('click', '.form-float .form-line .form-label', function () {
        $(this).parent().find('input').focus();
    });
}
function ajax_callselect(url, data,select,callback) {
    $.ajax({
        method: "POST",
        url: url,
        data: data,
        async: false
    }).done(function (response) {
        dictionary = JSON.parse(response);
        var opcion ="";
        for(var i = 0; i<dictionary.response.length; i++){
            opcion=opcion+"<option value='"+dictionary.response[i].id+"'>"+dictionary.response[i].nombre+"</option>";
        }
        select.append(opcion).selectpicker('refresh')
        if(callback!=null){
            if(typeof response === 'undefined')
                callback()
            else
                callback(response)
        }
    })



}