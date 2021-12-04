$(document).ready(function() {

	$('#Generate').on('click', function(event) {
		event.preventDefault();
        let getMms = $('#message').val();
        let getKey = $('#key_value').val();
        let getSelAl = $('#select_algorithm').val();

        if (getMms != '' && getKey != '' && getSelAl != '0') {
            $.ajax({
                data : {
                    message_ : getMms,
                    key_ : getKey,
                    agl_ : getSelAl
                },
                type : 'POST',
                url : '/generate_HF_HMAC',
                success: function(html) {
                    //alert(html.status);
                    // $("#message").html(html.result);
                    $('#textHash').val(html.result);
                }
        
            });
            
        }else if(getMms == '') {
            alert("Por favor ingrese un texto");
        }else if(getKey == '') {
            alert("Por favor ingrese una clave");
        }else if(getSelAl == '0') {
            alert("Por favor seleccione un algoritmo");
        }
		
	
    });

});