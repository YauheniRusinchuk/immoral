$(function(){
    $('.btn_login').click((e)=> {
        e.preventDefault();
        $('.login_container_show').slideDown('fast');
    })

    $('.img_login_delete').click((e)=> {
        e.preventDefault();
        $('.login_container_show').slideUp('fast');
    })


})
