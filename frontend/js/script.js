server_url = "http://127.0.0.1:5000/process_image";

function sendFile(type){
    $('#input_handle').click();
    $('#type').val(type);
    console.log(type);
}

$('document').ready(function(){
    $('#input_handle').change(function(){
        var data = new FormData($('#form')[0]);
        $.ajax({
            url: server_url,
            data: data,
            cache: false,
            contentType: false,
            processData: false,
            method: 'POST',
            type: 'POST',
            success: function (data) {
                //$('#output').show();

                var reader = new FileReader();
                reader.onload = function (e) {
                    $('#input_image').attr('src', e.target.result);
                }
                reader.readAsDataURL($('#input_handle')[0].files[0]);
                
                $('#output_image').attr("src", 'http://127.0.0.1:5000/static/outputs/' + data);
            }
        });
    });
      // Or with jQuery
    
      $('.dropdown-trigger').dropdown();

});