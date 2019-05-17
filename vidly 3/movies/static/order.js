
function init(){
    console.log('order.js loaded');

    // hook event for add button
    $(".btnAdd").click(function(e){
        console.log('button clicked');
        console.log(e);
        let id = $(this).attr('movie-id');
        console.log(id);
    });
}

window.onload = init;