function initMap() {

  var lat=document.getElementById("studio-lat");
  var lng=document.getElementById("studio-lng");

  var location = {lat: Number(lat.innerHTML), lng: Number(lng.innerHTML)};
  lat.style.display="none";
  lng.style.display="none";

  console.log(location);
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 18,
    center: location
  });
  var marker = new google.maps.Marker({
    position: location,
    map: map
  });
}
