$(document).ready(function() {

	$('#Generate').on('click', function(event) {
		event.preventDefault();
        let getMms = $('#message').val();
        if (getMms != '') {
            $.ajax({
                data : {
                    message_ : getMms
                },
                type : 'POST',
                url : '/generate_HF_MD4',
                success: function(html) {
                    //alert(html.status);
                    // $("#message").html(html.result);
                    $('#textHash').val(html.result);
                }
        
            });
            
        }else {
            alert("Por favor ingrese un texto");
        }
		
	
    });

});