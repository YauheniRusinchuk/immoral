$(function() {

    var video = document.querySelector("#videoElement");
    $('#stop').hide();


    $('#start').click((e)=>{
        e.preventDefault();
        start();
        $("#start").hide()
        $('#stop').show();
    })

    $('#stop').click((e)=>{
        e.preventDefault();
        stopVideo();
        $("#stop").hide();
        $("#start").show();
    })


    function start() {
        if (navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({audio: true, video: { width: 600, height: 375}})
            .then(function(stream) {
                video.srcObject = stream;
            })
            .catch(function(error) {
                console.log("Something went wrong!");
            });
        }
    }

    function stopVideo() {
      let stream = video.srcObject;
      let tracks = stream.getTracks();

      tracks.forEach(function(track) {
        track.stop();
      });

      video.srcObject = null;
    }


})
