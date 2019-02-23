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
                $('.seccess_form').show('fast', ()=>{
                    setTimeout(()=>{
                        $('.seccess_form').hide('fast', ()=>{
                            window.location.href = window.location.origin + "/login"
                        });
                    }, 2000)
                })
            },
        })
    })
})
