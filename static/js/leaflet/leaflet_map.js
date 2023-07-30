var dataurl = '{% url "planner:gis_data" %}';

window.addEventListener("map:init", function (event) {
  var map = event.detail.map;
  // Download GeoJSON data with Ajax
  fetch(dataurl)
    .then(function(resp) {
      return resp.json();
    })
    .then(function(data) {
      L.geoJson(data, {
        onEachFeature: function onEachFeature(feature, layer) {
          layer.bindPopup(feature.properties.name);
      }}).addTo(map);
    });
});