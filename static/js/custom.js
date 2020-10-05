console.log('i am custom.js')

$('.reply_btn').click(function(){
  $(this).parent().parent().next('.replied-comments').fadeToggle()
});

// $('#follow').click(function(e){
//   e.preventDefault();
//   let href = this.href
//   $.ajax({
//     url:href,
//     success:function(response){
//             if(response['following']){
//                  $('#follow').html('Unfollow')
//             } else{
//                 $('#follow').html('follow')
//             }     

   
//     }
//   });
// });