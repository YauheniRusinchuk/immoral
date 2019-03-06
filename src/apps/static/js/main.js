$(function(){


    $(".rslides").responsiveSlides();



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

    let loc = window.location;
    let wsStart = 'ws://';
    if(loc.protocol == 'https:') {
        wsStart = 'wss://';
    }

    let endPoint = wsStart + loc.host

    let socket = new WebSocket(endPoint)

    socket.onmessage = function(e) {
        console.log('messages', e)
        $('.update_btn_new').slideDown('slow');
    }

    socket.onopen = function(e) {
        console.log('open', e)
    }









})
