$("#search_by_fullname").on('keyup', function(){
  var matcher = new RegExp($(this).val(), 'gi');
  $('.mua-listing').show().not(function(){
      return matcher.test($(this).find('#first-info').text())
  }).hide();
});

$('#search_by_rating').change(function(){
    var val = $(this).val();
    val_float = parseFloat(val) * 1.0;
    $('.mua-rating-span').each(function(){
      var rating_text = $(this).text().substring(0,3)
      if(rating_text >= val_float && rating_text < val_float+1.0) $(this).parent().parent().show();
      else if(val == 'any') $(this).parent().parent().show();
      else $(this).parent().parent().hide();
    });
});

$('#filter-btn').click(function(){

  $("#search_by_fullname").val("");
  $('#search_by_rating').val('any');
  $('.mua-listing').show();
});
