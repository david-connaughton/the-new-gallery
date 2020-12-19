$(document).ready(function(){

    // photo-detail page Fade In

    $('#photo-section').css('display', 'none');
    $('#photo-section').fadeIn(1500);

    // photo-detail Image Modal for Larger Screens

    $('#clicker').click(function() {
        $('#modal-main-id').attr('src', $('#photo-img').attr('src'));
        $('#myModal').modal('show');
    });  
    console.log('HELLO');
      
});