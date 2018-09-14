function query_render(url) {
    $.ajax({
        method: "GET",
        url: url,
        data: { }
    }).done(function (html) {
        $('#render_content').html(html);
    });
}
function gethijos(dato) {
    if(dato.value=="0"){
        $('#hijo').hide();
    }else{
        $('#hijo').show();
    }
}
function getchange(dato) {
    if(dato.value=="Soltero")
    {
        $('#conyuge').hide();
    }else
    {
        $('#conyuge').show();
    }
}
function getvalue(json, name) {
    if(~name.indexOf("empleado_")){
        if(name.indexOf("empleado_foto"))
            return json[name.replace("empleado_", "")];
        if(~name.indexOf("empleado_estado_civil")){
            getchange(json[name.replace("empleado_", "")]);
            gethijos(json[name.replace("empleado_", "")]);
            return json[name.replace("empleado_", "")];
        }
    }else
    if(~name.indexOf("conyuge_")){
        if(json['conyuge'].length>0){
            if(name.replace("conyuge_", "") in json['conyuge'][0]){
                return json['conyuge'][0][name.replace("conyuge_", "")];
            }else{
                return json['conyuge'][0]['persona'][name.replace("conyuge_", "")];
            }
        }
    }else
    if(~name.indexOf("padre_")){
        if(json['padres'].length>0){
            return json['padres'][0][name.replace("padre_", "")];
        }
    }else
    if(~name.indexOf("madre_")){
        if(json['padres'].length>0){
            return json['padres'][1][name.replace("madre_", "")];
        }
    }else
    {
        return json['persona'][name];
    }
}
function geturl(ele){
    if(~ele.indexOf("postgrado_")){
        return "/personal_baja_postgrado";
    }else
    if(~ele.indexOf("otroestudio_")){
        return "/personal_baja_otroestudio";
    }else
    if(~ele.indexOf("thijos_")){
        return "/personal_baja_hijo";
    }else
    if(~ele.indexOf("tcapacitacion_")){
        return "/personal_baja_capacitacion";
    }else
    if(~ele.indexOf("tbecas_")){
        return "/personal_baja_beca"
    }else
    if(~ele.indexOf("tidiomas_")){
        return "/personal_baja_idioma"
    }else
    if(~ele.indexOf("texperiencia_")){
        return "/personal_baja_experiencia"
    }
}
function addrow(ele) {
    if(ele=="postgrado"){
        postgrado++;
        $('#'+ele+' tbody').append("<tr>"+
                "<input name='"+ele+"_id"+String(postgrado)+"' type='hidden' class='form-control' value='' />"+
                "<td><input name='"+ele+"_detalle"+String(postgrado)+"' type='text' class='form-control' placeholder='Detalle' /></td>"+
                "<td><input name='"+ele+"_anho"+String(postgrado)+"' type='number' oninput='if(this.value.length > 4){this.value = this.value.slice(0,4);}' class='form-control dig' maxlength='4' min='1900' max='2100' placeholder='a&#241;o' /></td>"+
                "<td><button type='button' onclick='eliminar(this,null,postgrado)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td>"+
                "</tr>");
    }else
    if(ele=="otroestudio"){
        otroestudio++;
        $('#'+ele+' tbody').append("<tr>"+
                  "<input name='"+ele+"_id"+String(otroestudio)+"' type='hidden' class='form-control' value='' />"+
                "<td><input name='"+ele+"_detalle"+String(otroestudio)+"' type='text' class='form-control' placeholder='Detalle' /></td>"+
                "<td><input name='"+ele+"_anho"+String(otroestudio)+"' type='number' oninput='if(this.value.length > 4){this.value = this.value.slice(0,4);}' class='form-control dig' maxlength='4' min='1900' max='2100' placeholder='a&#241;o' /></td>"+
                "<td><button type='button' onclick='eliminar(this,null,otroestudio)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td>"+
                "</tr>");
    }else
    if(ele=="thijos"){
        thijos++;
        $('#'+ele+' tbody').append("<tr>"+
                        "<input name='"+ele+"_id"+String(thijos)+"' type='hidden' class='form-control' value='' />"+
                "<td><input name='"+ele+"_nombres"+String(thijos)+"' type='text' class='form-control' placeholder='Nombres y Apellidos' /></td>"+
                "<td><input name='"+ele+"_direccion"+String(thijos)+"' type='text' class='form-control' placeholder='Direccion' /></td>"+
                "<td><input name='"+ele+"_telefono"+String(thijos)+"' type='tel' class='form-control dig' placeholder='Telefono' /></td>"+
                "<td><input name='"+ele+"_fecha_nac"+String(thijos)+"' type='text' class='form-control datepicker' placeholder='Fecha de Nacimiento' /></td>"+
                "<td><button type='button' onclick='eliminar(this,null,thijos)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td></tr>");
        ($("input[name='"+ele+"_fecha_nac"+String(thijos)+"']")).bootstrapMaterialDatePicker({ format: 'DD/MM/YYYY',
        clearButton: false,
        weekStart: 1,
        lang:'es',
        time: false }).on('change',function () {
                    $(this).parent().addClass('focused');
                });
    }else
    if(ele=="tcapacitacion"){
        tcapacitacion++;
        $('#'+ele+' tbody').append("<tr>"+
                        "<input name='"+ele+"_id"+String(tcapacitacion)+"' type='hidden' class='form-control' value='' />"+
                "<td><input name='"+ele+"_documento"+String(tcapacitacion)+"' type='text' class='form-control' placeholder='Documentos' /></td>"+
                "<td><input name='"+ele+"_motivo"+String(tcapacitacion)+"' type='text' class='form-control' placeholder='Naturaleza' /></td>"+
                "<td><input name='"+ele+"_fecha_ini"+String(tcapacitacion)+"' type='text' class='form-control datepicker' placeholder='Fecha inicio' /></td>"+
                "<td><input name='"+ele+"_fecha_fin"+String(tcapacitacion)+"' type='text' class='form-control datepicker' placeholder='Fecha Finalizacion' /></td>"+
                "<td><button type='button' onclick='eliminar(this,null,tcapacitacion)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float edit'><i class='material-icons'>close</i></button></td>"+
                "</tr>");
        $("input[name='"+ele+"_fecha_fin"+String(tcapacitacion)+"']").bootstrapMaterialDatePicker({ format: 'DD/MM/YYYY',
        clearButton: false,
        weekStart: 1,
        lang:'es',
        time: false }).on('change',function () {
                    $(this).parent().addClass('focused');
                });
        $("input[name='"+ele+"_fecha_ini"+String(tcapacitacion)+"']").bootstrapMaterialDatePicker({ format: 'DD/MM/YYYY',
        clearButton: false,
        weekStart: 1,
        lang:'es',
        time: false }).on('change', function(e, date) {
            $(this).parent().addClass('focused');
            $("input[name='"+ele+"_fecha_fin"+String(tcapacitacion)+"']").bootstrapMaterialDatePicker('setMinDate', date);
        });
    }else
    if(ele=="tbecas"){
        tbecas++;
        $('#'+ele+' tbody').append("<tr>"+
                        "<input name='"+ele+"_id"+String(tbecas)+"' type='hidden' class='form-control' value='' />"+
                "<td><input name='"+ele+"_memo"+String(tbecas)+"' type='text' class='form-control' placeholder='Memo o Resolucion' /></td>"+
                "<td><input name='"+ele+"_nombre"+String(tbecas)+"' type='text' class='form-control' placeholder='Nombre del Evento' /></td>"+
                "<td><input name='"+ele+"_naturaleza"+String(tbecas)+"' type='text' class='form-control' placeholder='Naturaleza' /></td>"+
                "<td><input name='"+ele+"_fecha_ini"+String(tbecas)+"' type='text' class='form-control datepicker' placeholder='Fecha inicio' /></td>"+
                "<td><input name='"+ele+"_fecha_fin"+String(tbecas)+"' type='text' class='form-control datepicker' placeholder='Fecha Finalizacion' /></td>"+
                "<td><button type='button' onclick='eliminar(this,null,tbecas)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td>"+
                "</tr>");
        $("input[name='"+ele+"_fecha_fin"+String(tbecas)+"']").bootstrapMaterialDatePicker({ format: 'DD/MM/YYYY',
        clearButton: false,
        weekStart: 1,
        lang:'es',
        time: false }).on('change',function () {
                    $(this).parent().addClass('focused');
                });
        $("input[name='"+ele+"_fecha_ini"+String(tbecas)+"']").bootstrapMaterialDatePicker({ format: 'DD/MM/YYYY',
        clearButton: false,
        weekStart: 1,
        lang:'es',
        time: false }).on('change', function(e, date) {
             $(this).parent().addClass('focused');
            $("input[name='"+ele+"_fecha_fin"+String(tbecas)+"']").bootstrapMaterialDatePicker('setMinDate', date);
        });
    }else
    if(ele=="tidiomas"){
        tidiomas++;
        $('#'+ele+' tbody').append("<tr>"+
                        "<input name='"+ele+"_id"+String(tidiomas)+"' type='hidden' class='form-control' value='' />"+
                "<td><input name='"+ele+"_idioma"+String(tidiomas)+"' type='text' class='form-control' placeholder='Idioma' /></td>"+
                "<td><input id='"+ele+"_habla"+String(tidiomas)+"' name='"+ele+"_habla"+String(tidiomas)+"' type='checkbox' class='form-control' /><label for='"+ele+"_habla"+String(tidiomas)+"'></label></td>"+
                "<td><input id='"+ele+"_lee"+String(tidiomas)+"' name='"+ele+"_lee"+String(tidiomas)+"' type='checkbox' class='form-control' /><label for='"+ele+"_lee"+String(tidiomas)+"'></label></td>"+
                "<td><input id='"+ele+"_escribe"+String(tidiomas)+"' name='"+ele+"_escribe"+String(tidiomas)+"' type='checkbox' class='form-control'/><label for='"+ele+"_escribe"+String(tidiomas)+"'></label></td>"+
                "<td><input id='"+ele+"_aprendio"+String(tidiomas)+"' name='"+ele+"_aprendio"+String(tidiomas)+"' type='checkbox' class='form-control' /><label for='"+ele+"_aprendio"+String(tidiomas)+"'></label></td>"+
                "<td><button type='button' onclick='eliminar(this,null,tidiomas)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td>"+
                "</tr>");
    }else
    if(ele=="texperiencia"){
        texperiencia++;
        $('#'+ele+' tbody').append("<tr>"+
                        "<input name='"+ele+"_id"+String(texperiencia)+"' type='hidden' class='form-control' value='' />"+
                "<td><input name='"+ele+"_experiencia"+String(texperiencia)+"' type='text' class='form-control' placeholder='Experincia' /></td>"+
                "<td><input name='"+ele+"_entidad"+String(texperiencia)+"' type='text' class='form-control' placeholder='Entidad' /></td>"+
                "<td><input name='"+ele+"_anho"+String(texperiencia)+"' type='number' oninput='if(this.value.length > 4){this.value = this.value.slice(0,4);}' class='form-control dig' value='1900' maxlength='4' min='1900' max='2100' placeholder='A&#241;o' /></td>"+
                "<td><button type='button' onclick='eliminar(this,null,texperiencia)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td>"+
                "</tr>");
    }
    $('#'+ele+' tbody .dig').each(function () {
        $(this).rules('add', 'digits');
    });
}
function eliminar(ele,id,cont) {
    if(cont!=null){
        cont--;
    }
    if(id!=null){
        swal({
            title: "Baja",
            text: "Desea Eliminar?",
            type: "warning",
            showCancelButton: false,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Confirmar",
            closeOnConfirm: true
            },function () {
            objeto = JSON.stringify({
                'id' : id.value
            })
            ajax_call(geturl(id.name), {object: objeto}, null, function () {
                ele.closest('tr').remove();
            })

        });

    }else{

        ele.closest('tr').remove();
    }
}
function filedata() {
    $(".file").each(function () {
        $(this).fileinput('refresh',{
        allowedFileExtensions: ['jpg', 'png'],
        maxFileSize: 2000,
        maxFilesNum: 1,
        showUpload: false,
        layoutTemplates: {
                            main1: '{preview}\n' +
                                '<div class="kv-upload-progress hide"></div>\n' +
                                '<div class="input-group {class}">\n' +
                                '   {caption}\n' +
                                '   <div class="input-group-btn">\n' +
                                '       {remove}\n' +
                                '       {cancel}\n' +
                                '       {browse}\n' +
                                '   </div>\n' +
                                '</div>',
                            main2: '{preview}\n<div class="kv-upload-progress hide"></div>\n{remove}\n{cancel}\n{browse}\n',
                            preview: '<div class="file-preview {class}">\n' +
                                '    {close}\n' +
                                '    <div class="{dropClass}">\n' +
                                '    <div class="file-preview-thumbnails">\n' +
                                '    </div>\n' +
                                '    <div class="clearfix"></div>' +
                                '    <div class="file-preview-status text-center text-success"></div>\n' +
                                '    <div class="kv-fileinput-error"></div>\n' +
                                '    </div>\n' +
                                '</div>',
                            icon: '<span class="glyphicon glyphicon-file kv-caption-icon"></span>',
                            caption: '<div tabindex="-1" class="form-control file-caption {class}">\n' +
                                '   <div class="file-caption-name"></div>\n' +
                                '</div>',
                            btnDefault: '<button type="{type}" tabindex="500" title="{title}" class="{css}"{status}>{icon}{label}</button>',
                            btnLink: '<a href="{href}" tabindex="500" title="{title}" class="{css}"{status}>{icon}{label}</a>',
                            btnBrowse: '<div tabindex="500" class="{css}"{status}>{icon}{label}</div>',
                            progress: '<div class="progress">\n' +
                                '    <div class="progress-bar progress-bar-success progress-bar-striped text-center" role="progressbar" aria-valuenow="{percent}" aria-valuemin="0" aria-valuemax="100" style="width:{percent}%;">\n' +
                                '        {percent}%\n' +
                                '     </div>\n' +
                                '</div>',
                            footer: '<div class="file-thumbnail-footer">\n' +
                                '    <div class="file-caption-name" style="width:{width}">{caption}</div>\n' +
                                '    {progress} {actions}\n' +
                                '</div>',
                            actions: '<div class="file-actions">\n' +
                                '    <div class="file-footer-buttons">\n' +
                                '        {delete} {other}' +
                                '    </div>\n' +
                                '    {drag}\n' +
                                '    <div class="file-upload-indicator" title="{indicatorTitle}">{indicator}</div>\n' +
                                '    <div class="clearfix"></div>\n' +
                                '</div>',
                            actionDelete: '<button type="button" class="kv-file-remove {removeClass}" title="{removeTitle}"{dataUrl}{dataKey}>{removeIcon}</button>\n',
                            actionDrag: '<span class="file-drag-handle {dragClass}" title="{dragTitle}">{dragIcon}</span>'
                        }
    })
    });
    $('.datepicker').bootstrapMaterialDatePicker({
        format: 'DD/MM/YYYY',
        clearButton: false,
        weekStart: 1,
        lang :'es',
        maxDate:new Date(),
        time: false
    }).on('change',function () {
        $(this).parent().addClass('focused');
    });
}
function datepicker(ele){
    ele.bootstrapMaterialDatePicker({
        format: 'DD/MM/YYYY',
        clearButton: false,
        weekStart: 1,
        lang:'es',
        maxDate:new Date(),
        time: false
    }).on('change',function () {
        $(this).parent().addClass('focused');
    });
}
function isEmptyObject( obj ) {
    for ( var name in obj ) {
        return false;
    }
    return true;
    }
function first(obj) {
for (var a in obj) return a;
}
function getarray(dic) {
    var array =[];
    while(!isEmptyObject(dic)){
        var elec ={};
        x = first(dic);
        x=x.substr(x.length - 1);
        for( var ele in dic){
            if(~ele.indexOf(x)){
                elec[ele.replace(x,"")] = dic[ele];
                delete dic[ele];
            }
        }
        array.push(elec);
    }
    return array;
}
function cargar_eventos() {
    $('#newpost').click(function(){
        addrow('postgrado')
    })
    $('#newotro').click(function(){
        addrow('otroestudio')
    })
    $('#newhijo').click(function(){
        addrow('thijos')
    })
    $('#newcap').click(function(){
        addrow('tcapacitacion')
    })
    $('#newexp').click(function(){
        addrow('texperiencia')
    })
    $('#newidio').click(function(){
        addrow('tidiomas')
    })
    $('#newbeca').click(function(){
        addrow('tbecas')
    })
}
function verificardata(dt){
    for(key in dt){
        if(dt[key]!=null){
            return true
        }
    }
    return false
}
function verificardatap(dt){
    for(key in dt){
        if(dt[key]!=null){
            if(key.indexOf('tipo') && (dt[key]!='0' || dt[key]!='1')){
                return true
            }
        }
    }
    return false
}
function verificararray(dt){
    if(dt.length>0){
        return true
    }
    return false
}
function getFormData(dom_query){
    var out ={};
    var persona = {};
    var hijos ={};
    var capacitacion ={};
    var postgrado ={};
    var otroestudio ={};
    var experiencia ={};
    var empleado = {};
    var idioma = {};
    var beca = {};
    var conyuge = {};
    var padre = {};
    var madre = {};
    var s_data = $(dom_query).serializeArray();
    for(var i = 0; i<s_data.length; i++){
        var record = s_data[i];
        if(record.value===""){
            record.value=null;
        }
        if(~record.name.indexOf("empleado_"))
            empleado[record.name.replace("empleado_", "")] = record.value;
        else if(~record.name.indexOf("conyuge_"))
                conyuge[record.name.replace("conyuge_", "")] = record.value;
        else if(~record.name.indexOf("padre_"))
                padre[record.name.replace("padre_", "")] = record.value;
        else if(~record.name.indexOf("madre_"))
                madre[record.name.replace("madre_", "")] = record.value;
        else if(~record.name.indexOf("postgrado_"))
                postgrado[record.name.replace("postgrado_", "")] = record.value;
        else if(~record.name.indexOf("otroestudio_"))
                otroestudio[record.name.replace("otroestudio_", "")] = record.value;
        else if(~record.name.indexOf("thijos_"))
                hijos[record.name.replace("thijos_", "")] = record.value;
        else if(~record.name.indexOf("tcapacitacion_"))
                capacitacion[record.name.replace("tcapacitacion_", "")] = record.value;
        else if(~record.name.indexOf("tbecas_"))
                beca[record.name.replace("tbecas_", "")] = record.value;
        else if(~record.name.indexOf("tidiomas_"))
                idioma[record.name.replace("tidiomas_", "")] = record.value;
        else if(~record.name.indexOf("texperiencia_"))
                experiencia[record.name.replace("texperiencia_", "")] = record.value;
        else
            persona[record.name] = record.value;
    }

    out['empleado'] = empleado;
    if(verificardata(conyuge)){
        out['conyuge'] = conyuge;
    }

    if(verificardatap(padre))
    {
        out['padre'] = padre;
    }
    if(verificardatap(madre))
    {
        out['madre'] = madre;
    }
    postg=getarray(postgrado)
    if(verificararray(postg)){
        out['postgrado'] = postg;
    }
    otro=getarray(otroestudio)
    if(verificararray(otro)){
        out['otroestudio'] = otro;
    }
    hijo=getarray(hijos)
    if(verificararray(hijo)){
        out['hijos'] = hijo;
    }
    cap=getarray(capacitacion)
    if(verificararray(cap)){
        out['capacitacion'] = cap;
    }
    bec=getarray(beca)
    if(verificararray(bec)){
        out['becas'] = bec;
    }
    idio=getarray(idioma)
    if(verificararray(idio)){
        out['idioma'] = idio;
    }
    exp=getarray(experiencia)
    if(verificararray(exp)){
        out['experiencia'] = exp;
    }
    out['persona'] = persona;
    return JSON.stringify(out);
}
function updateeventos(json,callback) {

    //var json = JSON.parse(str.replace(/&quot;/g,'"'));
    $('#personal-update').find('input').val(function (index, value) {
        if(getvalue(json,this.name)!=""){
            if(~this.name.indexOf("padre_tipo")){
                return value
            }
            if(~this.name.indexOf("madre_tipo")){
                return value
            }
            //$('input[name='+this.name+']').parent().addClass('focused');
        }
        return getvalue(json,this.name);
    })
    $('#personal-update').find('select').val(function (index, value) {
        /*if(getvalue(json,this.name)!=''){
            $('select[name='+this.name+']').parent().addClass('focused');
        }*/
        return getvalue(json,this.name);
    }).selectpicker('refresh');
    if(json['foto']!="")
        $('#show_img').attr('src',json['foto']);
    $('#personal-update').append("<input id='empleado_id' name='empleado_id' type='hidden' class='form-control' value='"+json['id']+"' />");
    $('#personal-update').append("<input name='id' type='hidden' class='form-control' value='"+json['persona']['id']+"' />");
    if(json['conyuge'].length>0){
        $('#personal-update').append("<input name='conyuge_id' type='hidden' class='form-control' value='"+json['conyuge'][0]['id']+"' />");
        $('#personal-update').append("<input name='conyuge_persona_id' type='hidden' class='form-control' value='"+json['conyuge'][0]['persona']['id']+"' />");
    }
    for(var i = json['padres'].length-1; i>=0; i--){
        if(json['padres'][i]['tipo']=="0"){
            $('#personal-update').append("<input name='padre_id' type='hidden' class='form-control' value='"+json['padres'][i]['id']+"' />");
        }else{
            $('#personal-update').append("<input name='madre_id' type='hidden' class='form-control' value='"+json['padres'][i]['id']+"' />");
        }
    }
    postgrado = json['postgrados'].length-1;
    otroestudio = json['otrosestudios'].length-1;
    thijos = json['hijos'].length-1;
    tcapacitacion = json['capacitacion'].length-1;
    tbecas = json['becas'].length-1;
    tidiomas = json['idioma'].length-1;
    texperiencia = json['experiencia'].length-1;
    for(var i = json['postgrados'].length-1; i>=0; i--){
        $('#postgrado tbody').append("<tr>"+
                            "<input name='postgrado_id"+String(i)+"' type='hidden' class='form-control' value='"+json['postgrados'][i]['id']+"' />"+
                            "<td><input name='postgrado_detalle"+String(i)+"' type='text' class='form-control' placeholder='Detalle'  value='"+json['postgrados'][i]['detalle']+"' /></td>"+
                            "<td><input name='postgrado_anho"+String(i)+"' type='number' oninput='if(this.value.length > 4){this.value = this.value.slice(0,4);}' class='form-control dig' maxlength='4' min='1900' max='2100' placeholder='a&#241;o'  value='"+json['postgrados'][i]['anho']+"'/></td>"+
                            "<td><button type='button' onclick='eliminar(this,postgrado_id"+String(i)+",postgrado)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td>"+
                            "</tr>");
    }
    $('#postgrado tbody .dig').each(function () {
        $(this).rules('add', 'digits');
    });
    for(var i = json['otrosestudios'].length-1; i>=0; i--){
        $('#otroestudio tbody').append("<tr>"+
                            "<input name='otroestudio_id"+String(i)+"' type='hidden' class='form-control' value='"+json['otrosestudios'][i]['id']+"' />"+
                            "<td><input name='otroestudio_detalle"+String(i)+"' type='text' class='form-control' placeholder='Detalle'  value='"+json['otrosestudios'][i]['detalle']+"' /></td>"+
                            "<td><input name='otroestudio_anho"+String(i)+"' type='number' oninput='if(this.value.length > 4){this.value = this.value.slice(0,4);}' class='form-control dig' maxlength='4' min='1900' max='2100' placeholder='a&#241;o'  value='"+json['otrosestudios'][i]['anho']+"'/></td>"+
                            "<td><button type='button' onclick='eliminar(this,otroestudio_id"+String(i)+",otroestudio)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td>"+
                            "</tr>");
    }
    $('#postgrado tbody .dig').each(function () {
        $(this).rules('add', 'digits');
    });
    for(var i = json['hijos'].length-1; i>=0; i--){
        $('#thijos tbody').append("<tr>"+
                            "<input name='thijos_id"+String(i)+"' type='hidden' class='form-control' value='"+json['hijos'][i]['id']+"' />"+
                            "<td><input name='thijos_nombres"+String(i)+"' type='text' class='form-control' placeholder='Nombres y Apellidos' value='"+json['hijos'][i]['nombres']+"' /></td>"+
                    "<td><input name='thijos_direccion"+String(i)+"' type='text' class='form-control' placeholder='Direccion' value='"+json['hijos'][i]['direccion']+"' /></td>"+
                    "<td><input name='thijos_telefono"+String(i)+"' type='text' class='form-control dig' placeholder='Direccion' value='"+json['hijos'][i]['telefono']+"' /></td>"+
                    "<td><input name='thijos_fecha_nac"+String(i)+"' type='text' class='form-control datepicker' placeholder='Fecha de Nacimiento' value='"+json['hijos'][i]['fecha_nac']+"'/></td>"+
                        "<td><button type='button' onclick='eliminar(this,thijos_id"+String(i)+",thijos)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td></tr>"+
                            "</tr>");
                    ($("input[name='thijos_fecha_nac"+String(i)+"']")).bootstrapMaterialDatePicker({ format: 'DD/MM/YYYY',
                        clearButton: false,
                        weekStart: 1,
                        lang:'es',
                        time: false }).on('change',function () {
                                    $(this).parent().addClass('focused');
                                });
    }
    $('#postgrado tbody .dig').each(function () {
        $(this).rules('add', 'digits');
    });
    for(var i = json['capacitacion'].length-1; i>=0; i--){
        $('#tcapacitacion tbody').append("<tr>"+
                            "<input name='tcapacitacion_id"+String(i)+"' type='hidden' class='form-control' value='"+json['capacitacion'][i]['id']+"' />"+
                            "<td><input name='tcapacitacion_documento"+String(i)+"' type='text' class='form-control' placeholder='Documentos' value='"+json['capacitacion'][i]['documento']+"'/></td>"+
                            "<td><input name='tcapacitacion_motivo"+String(i)+"' type='text' class='form-control' placeholder='Naturaleza' value='"+json['capacitacion'][i]['motivo']+"'/></td>"+
                            "<td><input name='tcapacitacion_fecha_ini"+String(i)+"' type='text' class='form-control datepicker' placeholder='Fecha inicio' value='"+json['capacitacion'][i]['fecha_ini']+"'/></td>"+
                            "<td><input name='tcapacitacion_fecha_fin"+String(i)+"' type='text' class='form-control datepicker' placeholder='Fecha Finalizacion' value='"+json['capacitacion'][i]['fecha_fin']+"'/></td>"+
                            "<td><button type='button' onclick='eliminar(this,tcapacitacion_id"+String(i)+",tcapacitacion)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float edit'><i class='material-icons'>close</i></button></td>"+
                            "</tr>");
    }
    for(var i = json['becas'].length-1; i>=0; i--){
        $('#tbecas tbody').append("<tr>"+
                            "<input name='tbecas_id"+String(i)+"' type='hidden' class='form-control' value='"+json['becas'][i]['id']+"' />"+
                            "<td><input name='tbecas_memo"+String(i)+"' type='text' class='form-control' placeholder='Memo o Resolucion' value='"+json['becas'][i]['memo']+"'/></td>"+
                            "<td><input name='tbecas_nombre"+String(i)+"' type='text' class='form-control' placeholder='Nombre del Evento' value='"+json['becas'][i]['nombre']+"'/></td>"+
                            "<td><input name='tbecas_naturaleza"+String(i)+"' type='text' class='form-control' placeholder='Naturaleza' value='"+json['becas'][i]['naturaleza']+"'/></td>"+
                            "<td><input name='tbecas_fecha_ini"+String(i)+"' type='text' class='form-control datepicker' placeholder='Fecha inicio' value='"+json['becas'][i]['fecha_ini']+"'/></td>"+
                            "<td><input name='tbecas_fecha_fin"+String(i)+"' type='text' class='form-control datepicker' placeholder='Fecha Finalizacion' value='"+json['becas'][i]['fecha_fin']+"'/></td>"+
                            "<td><button type='button' onclick='eliminar(this,tbecas_id"+String(i)+",tbecas)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td>"+
                            "</tr>");
    }
    for(var i = json['idioma'].length-1; i>=0; i--){
        $('#tidiomas tbody').append("<tr>"+
                    "<input name='tidiomas_id"+String(i)+"' type='hidden' class='form-control' value='"+json['idioma'][i]['id']+"' />"+
                    "<td><input name='tidiomas_idioma"+String(i)+"' type='text' class='form-control' placeholder='Idioma' value='"+json['idioma'][i]['idioma']+"' /></td>"+
                    "<td><input id='tidiomas_habla"+String(i)+"' name='tidiomas_habla"+String(i)+"' type='checkbox' class='module chk-col-deep-purple' "+getchecked(json['idioma'][i]['habla'])+"><label for='tidiomas_habla"+String(i)+"'></label></td>"+
                    "<td><input id='tidiomas_lee"+String(i)+"' name='tidiomas_lee"+String(i)+"' type='checkbox' class='module chk-col-deep-purple' "+getchecked(json['idioma'][i]['lee'])+"><label for='tidiomas_lee"+String(i)+"'></label></td>"+
                    "<td><input id='tidiomas_escribe"+String(i)+"' name='tidiomas_escribe"+String(i)+"' type='checkbox' class='module chk-col-deep-purple' "+getchecked(json['idioma'][i]['escribe'])+"><label for='tidiomas_escribe"+String(i)+"'></label></td>"+
                    "<td><input id='tidiomas_aprendio"+String(i)+"' name='tidiomas_aprendio"+String(i)+"' type='checkbox' class='module chk-col-deep-purple' "+getchecked(json['idioma'][i]['aprendio'])+"><label for='tidiomas_aprendio"+String(i)+"'></label></td>"+
                    "<td><button type='button' onclick='eliminar(this,tidiomas_id"+String(i)+",tidiomas)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td>"+
                    "</tr>");
    }
    for(var i = json['experiencia'].length-1; i>=0; i--){
        $('#texperiencia tbody').append("<tr>"+
                            "<input name='texperiencia_id"+String(i)+"' type='hidden' class='form-control' value='"+json['experiencia'][i]['id']+"' />"+
                            "<td><input name='texperiencia_experiencia"+String(i)+"' type='text' class='form-control' placeholder='Experincia' value='"+json['experiencia'][i]['experiencia']+"'/></td>"+
                            "<td><input name='texperiencia_entidad"+String(i)+"' type='text' class='form-control' placeholder='Entidad' value='"+json['experiencia'][i]['entidad']+"' /></td>"+
                            "<td><input name='texperiencia_anho"+String(i)+"' type='number' oninput='if(this.value.length > 4){this.value = this.value.slice(0,4);}' class='form-control' maxlength='4' min='1900' value='1900' max='2100' placeholder='A&#241;o' value='"+json['experiencia'][i]['anho']+"' /></td>"+
                            "<td><button type='button' onclick='eliminar(this,texperiencia_id"+String(i)+",texperiencia)' class='btn bg-green bg-indigo btn-circle waves-effect waves-circle waves-float delete'><i class='material-icons'>close</i></button></td>"+
                            "</tr>");
    }
    callback()
}
function actionsformpersonal(){
    $('#empleado_da_pais').on('change',function () {
        $('#empleado_da_departamento option').filter(function () {
            return this.value!=''
        }).remove()
        $('#empleado_da_departamento').selectpicker('refresh')
        $('#empleado_da_cuidad option').filter(function () {
            return this.value!=''
        }).remove()
        $('#empleado_da_cuidad').selectpicker('refresh')
        $('#empleado_da_sucursal option').filter(function () {
            return this.value!=''
        }).remove()
        $('#empleado_da_sucursal').selectpicker('refresh')
        objeto = JSON.stringify({
            'pais_id':$(this).val()
            })
        ajax_callselect('/get_departamento',{object:objeto},$('#empleado_da_departamento'),null)
    })

    $('#empleado_da_departamento').on('change',function () {
        $('#empleado_da_cuidad option').filter(function () {
            return this.value!=''
        }).remove()
        $('#empleado_da_sucursal option').filter(function () {
            return this.value!=''
        }).remove()
        $('#empleado_da_sucursal').selectpicker('refresh')
        objeto = JSON.stringify({
            'departamento_id':$(this).val()
            })
        ajax_callselect('/get_ciudad',{object:objeto},$('#empleado_da_cuidad'),null)
    })

    $('#empleado_da_cuidad').on('change',function () {
        $('#empleado_da_sucursal option').filter(function () {
            return this.value!=''
        }).remove()
        objeto = JSON.stringify({
            'ciudad_id':$(this).val()
            })
        ajax_callselect('/get_sucursal',{object:objeto},$('#empleado_da_sucursal'),null)
    })

    /*$('#empleado_da_cargo').on('change',function () {
        $('#sueldo').val($('option:selected',this).attr('tag'))
        if($('option:selected',this).val()=='')
        $('#sueldo').parents('.form-line').removeClass('focused');
        else
        $('#sueldo').parents('.form-line').addClass('focused');
    })*/
}
function getchecked(ve) {
    if(ve){
        return "checked"
    }
    return ""
}
postgrado = 0;
otroestudio = 0;
thijos = 0;
tcapacitacion = 0;
tbecas = 0;
tidiomas = 0;
texperiencia = 0;
