function initMap() {

  var lat=$("#studio-lat").val();
  var lng=$("#studio-lng").val();

  var location = {lat: Number(lat), lng: Number(lng)};

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 18,
    center: location
  });
  var marker = new google.maps.Marker({
    position: location,
    map: map
  });
}
