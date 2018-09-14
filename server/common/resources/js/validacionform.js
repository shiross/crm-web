/**
 * Created by Dev-1 on 05/01/2017.
 */
$(function() {
    $('#personal').validate({
            highlight: function (input) {
                $(input).parents('.form-line').addClass('error');
            },
            unhighlight: function (input) {
                $(input).parents('.form-line').removeClass('error');
            },
            errorPlacement: function (error, element) {
                $(element).parents('.form-group').append(error);
            },
        });
});
// $('#personal #d_personal .personal input').each(function () {
//         $(this).rules('add', 'required');
//     });
/*$('#personal #d_personal .personal select').each(function () {
        $(this).rules('add', 'required');
    });
$('#personal #d_personal .administrador select').each(function () {
        $(this).rules('add', 'required');
    });*/

$('#personal .dig').each(function () {
        $(this).rules('add','digits');
    });
$('#personal .email').each(function () {
    $(this).rules('add','email');
})
$('#personal').on('submit', function (e) {
        if($('#personal').valid()) {
            var data = new FormData($(this)[0]);
            var d = getFormData('#personal');
            data.append('objecto', d);
            $.ajax({
                url: "/personal_insert",
                type: "post",
                data: data,
                contentType: false,
                processData: false,
                cache: false,
            }).done(function (response) {
                response = JSON.parse(response)
                if (response.success) {
                    swal({
                        title: "Operacion Correcta...",
                        text: response.message,
                        type: "success",
                        showCancelButton: false,
                        confirmButtonColor: "#DD6B55",
                        confirmButtonText: "Confirmar",
                        closeOnConfirm: true
                    }).then(function () {
                        query_render('/personal');
                    });
                } else {
                    swal("Operacion Fallida", response.message, "error");
                }
            });
        }
        e.preventDefault();
    });
