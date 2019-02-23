$(function(){

    $('.form_registation').on('submit',(e)=>{
        e.preventDefault();
        console.log("CLICK REGISTATION FORM")

        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: {
                login : $('.registration_login_form').val(),
                password : $('.registration_password_form').val(),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function() {
                console.log('EEEE YRA ...');
            },
        })
    })
})
