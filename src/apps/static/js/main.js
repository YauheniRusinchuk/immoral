$(function(){

    $('.btn_add_new').click((e)=>{
        e.preventDefault();
        $('.plusnew_container').slideToggle('fast');
    })

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
                $('.seccess_form').slideDown('fast', ()=>{
                    setTimeout(()=>{
                        $('.seccess_form').slideUp('fast', ()=>{
                            window.location.href = window.location.origin + "/login"
                        });
                    }, 2000)
                })
            },

            error: function(error) {
               $('.error_form').slideDown('fast', ()=>{
                   setTimeout(()=>{
                       $('.error_form').slideUp('fast');
                   }, 2000)
               })
            }
        })
    })
})
