// Initialize and add the map
// function initMap(lat, lng) {
function initMap() {
  // The location of Uluru
  const uluru = { lat: 38.344, lng: -120.036 };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: uluru,
    // center: {lat: parseFloat(lat), lng: parseFloat(lng)}
  });
  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}
