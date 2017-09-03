$("#search_by_fullname").on('keyup', function(){
  console.log("HEEEI");
  var matcher = new RegExp($(this).val(), 'gi');
  $('.mua-listing').show().not(function(){
      return matcher.test($(this).find('#first-info').text())
  }).hide();
});
