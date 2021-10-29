let autocomplete;
function initAutocomplete() {
  autocomplete = new google.maps.places.Autocomplete(
    document.getElementById("autocomplete"),
    {
      types: ["establishment"],
      componentRestrictions: { country: ["US"] },
      fields: ["address_components", "geometry"],
    }
  );

  autocomplete.addListener("place_changed", onPlaceChanged);
}
function onPlaceChanged() {
  var place = autocomplete.getPlace();

  if (!place.geometry) {
    // User did not select a prediction; reset the input field
    document.getElementById("autocomplete").placeholder = "Enter a place";
  } else {
    // Display details about the valid place
    console.log(place);
    for (var i = 0; i < place.address_components.length; i++) {
      for (var j = 0; j < place.address_components[i].types.length; j++) {
        if (place.address_components[i].types[j] == "street_number") {
          var num = place.address_components[i].long_name;
          var addy = place.address_components[i + 1].long_name;
          document.getElementById("address").value = num + " " + addy;
          document.getElementById("address").innerText = num + " " + addy;
        }
        if (place.address_components[i].types[j] == "route") {
        }
        if (place.address_components[i].types[j] == "locality") {
          document.getElementById("city").value =
            place.address_components[i].long_name;
          document.getElementById("city").innerText =
            place.address_components[i].long_name;
        }
        if (
          place.address_components[i].types[j] == "administrative_area_level_1"
        ) {
          document.getElementById("state").value =
            place.address_components[i].short_name;
          document.getElementById("state").innerText =
            place.address_components[i].short_name;
        }
        if (place.address_components[i].types[j] == "country") {
          document.getElementById("country").value =
            place.address_components[i].long_name;
          document.getElementById("country").innerText =
            place.address_components[i].long_name;
        }

        if (place.address_components[i].types[j] == "postal_code") {
          document.getElementById("zip_code").value =
            place.address_components[i].long_name;
          document.getElementById("zip_code").innerText =
            place.address_components[i].long_name;
        }
      }
    }

    document.getElementById("latitude").value = place.geometry.location.lat();
    document.getElementById("longitude").value = place.geometry.location.lng();
  }
}
