console.log('i am custom.js')

$('.reply_btn').click(function(){
  $(this).parent().parent().next('.replied-comments').fadeToggle()
});