

// $(document).ready(function(){
//     alert("asasa");
// });

$(document).ready(function(){
    $('#enviarID').attr('disabled', true);
});



var materiales = "";
$("#mate1ID").click(function(){

    $('#enviarID').attr('disabled', false);

    var sel = $("#mate1ID :selected");
    var val = sel.val();
    var text = sel.text();


    $("#mate2ID").append('<option value="' + val + '">' + text + '</option>');

    materiales = materiales + val + ",";
    $("#ocultoID").text(materiales);
    
    $(sel).remove();



});


$("#mate2ID").click(function(){

    var cant = document.getElementById("mate2ID").length;

    if (cant > 1){
        $('#enviarID').attr('disabled', false);
    }else{
        $('#enviarID').attr('disabled', true);
    }

    var sel = $("#mate2ID :selected");
    var val = sel.val();
    var text = sel.text();



    $("#mate1ID").append('<option value="' + val + '">' + text + '</option>');

    materiales = materiales.replace(val + ',', '');
    $("#ocultoID").text(materiales);
    
    $(sel).remove();



});
