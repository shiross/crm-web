validations ={//during, post, range of values
    'ci': [/^[0-9]{1,8}$/, /^[0-9]{6,8}$/, 'Solo se aceptan numeros entre 6 y 8 dígitos.'],
    'username': [/^[a-zA-Z0-9_]{1,50}$/,/^[a-zA-Z0-9_]{1,50}$/, 'Solo se acepta texto alfanumerico entre 1 y 50 caracteres.'],
    'password': [/^.{1,25}$/, /^.{8,25}$/, 'La contraseña debe tener 8 caracteres como mínimo y 25 como máximo.'],
    'int32': [/[0-9]+$/, /[0-9]+$/, 'Solo se acepta un número entero positivo.', [0, 2147483647]],
    'int32_signed': [/^-$|-?[0-9]+$/, /-?[0-9]+$/, 'Solo se acepta un número entero.', [-2147483648, 2147483647]],
    'float': [/-$|^-?[0-9]+$|^-?[0-9]+\.[0-9]*$/, /-?[0-9]+$|-?[0-9]+(.[0-9]+)?$/, 'Solo se acepta un número real o entero.', [-2147483648, 2147483647]],
    'text': [/^[a-zA-Z0-9 ñÑáéíóúÁÉÍÓÚ@.,()/]{0,200}$/,/^[a-zA-Z0-9 ñÑáéíóúÁÉÍÓÚ@.,()/]{0,200}$/, 'Solo se aceptan texto menor a 200 caracteres.'],
    'mail': [/^[a-zA-Z0-9_@.-]{1,100}$/, /^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+$/, 'Esto no es una dirección de correo válida'],
    'name': [/^[a-zA-Z ñÑáéíóúÁÉÍÓÚ]{1,50}$/,/^[a-zA-Z ñÑáéíóúÁÉÍÓÚ]{1,50}$/, 'Solo se acepta texto alfabetico entre 1 y 50 caracteres.'],
    'simple': [/^[a-zA-Z0-9 ñÑáéíóúÁÉÍÓÚ]{1,50}$/,/^[a-zA-Z0-9 ñÑáéíóúÁÉÍÓÚ]{1,50}$/, 'Solo se acepta texto alfanumerico entre 1 y 50 caracteres.']
}

function attach_validators() {
    for(j in validations){
        (function (j) {
            $('.'+j).unbind('keypress')
            $('.'+j).keypress(function (e) {
                if(e.charCode == 0) return true

                validator = validations[j]
                value = $(this).val() + String.fromCharCode(e.charCode)
                if(!validator[0].test(value)){
                    return false
                }
                if(validator.length > 3){
                    number = parseFloat(value)
                    if(!isNaN(value)){
                        return validator[3][0] <= number && number <= validator[3][1]
                    }
                }
                return true
            })
            $('.'+j).focusout(function (e) {
                field = $('#'+this.id)
                reg = validations[field.attr('data-regexp')]
                if (reg[1].test(field.val())){
                    $(this).parent().removeClass('error')
                    $(this).parent().next('label').text('')
                } else {
                    $(this).parent().addClass('error')
                    $(this).parent().next('label').text(reg[2])
                }
            })
            $('.'+j).attr('data-regexp', j)
            $('.'+j).parent().after('<label class="error"></label>')
        })(j)
    }
}

function validate_fields(ids) {
    for(i in ids){
        field = $('#' + ids[i])
        reg = validations[field.attr('data-regexp')]
        if(!reg[1].test(field.val())){
            return false
        }
    }
    return true
}

function clean_form() {
    $('div.focused').removeClass('focused')
    $('div.error').removeClass('error')
    $('label.error').text('')
}