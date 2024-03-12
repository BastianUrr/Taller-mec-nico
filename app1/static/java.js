

$(document).ready(function(){
    
    $("#regID").attr("disabled", true);

});

function funcionDePrueba(){
    alert("Función de prueba...");
}

var valNom = false, valApe = false, valCon = false, valCor = false;

function activarODesactivarBoton(){
    if (valNom && valApe && valCon && valCor)
        $("#regID").attr("disabled", false);
    else
        $("#regID").attr("disabled", true);  
}

$("#corID").keyup(function(){

    var text = $("#corID").val();
    var largo = text.length;
    // alert(text + " - " + largo);
    if (largo >= 3){
        valCor = true;   
    }else{
        valCor = false;  
    }

    activarODesactivarBoton();

})

$("#conID").keyup(function(){

    var text = $("#conID").val();
    var largo = text.length;
    // alert(text + " - " + largo);
    if (largo >= 3){
        valCon = true;   
    }else{
        valCon = false;  
    }

    activarODesactivarBoton();

})

$("#apeID").keyup(function(){

    var text = $("#apeID").val();
    var largo = text.length;
    // alert(text + " - " + largo);
    if (largo >= 3 && largo < 15){
        valApe = true;   
    }else{
        valApe = false;  
    }

    activarODesactivarBoton();

})

$("#nomID").keyup(function(){

    var text = $("#nomID").val();
    var largo = text.length;
    // alert(text + " - " + largo);
    if (largo >= 3 && largo < 15){
        valNom = true;   
    }else{
        valNom = false;  
    }

    activarODesactivarBoton();

})
