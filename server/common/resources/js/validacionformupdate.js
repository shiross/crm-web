/**
 * Created by Dev-1 on 05/01/2017.
*/
$(function() {
    $('#personal-update').validate({
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
// $('#personal-update #d_personal .personal input').each(function () {
//         $(this).rules('add', 'required');
//     });
// $('#personal-update #d_personal .personal select').each(function () {
//         $(this).rules('add', 'required');
//     });
// $('#personal-update #d_personal .administrador select').each(function () {
//         $(this).rules('add', 'required');
//     });

$('#personal-update .dig').each(function () {
        $(this).rules('add','digits');
    });
$('#personal-update .email').each(function () {
    $(this).rules('add','email');
})
$('#personal-update').on('submit', function (e) {
    e.preventDefault();
    if($('#personal-update').valid()){
        var data = new FormData($(this)[0]);
        var d = getFormData('#personal-update');
        data.append('objecto', d);
        $.ajax({
            url: "/personal_update",
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
                }).then(function () {
                    query_render('/personal');
                });
            } else {
                swal("Operacion Fallida", response.message, "error");
            }
            })
    }
});

