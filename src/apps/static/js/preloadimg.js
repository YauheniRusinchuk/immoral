$(function(){

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                $('.settings_img').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }


    $('#file').change(function(){
       readURL(this);
    });




    var imagesPreview = function(input, placeToInsertImagePreview) {

        if (input.files) {
            var filesAmount = input.files.length;

            for (i = 0; i < filesAmount; i++) {
                var reader = new FileReader();

                reader.onload = function(event) {
                    $($.parseHTML('<img>')).attr('src', event.target.result).appendTo(placeToInsertImagePreview);
                }

                reader.readAsDataURL(input.files[i]);
            }
        }

    };

    $('#file').on('change', function() {
        imagesPreview(this, 'div.result_upload_img');
    });




})
