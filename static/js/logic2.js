// load the data
// will need to change path when pushed
var stateData = "../static/data/combined_df.geojson";
console.log(stateData);

//myMap object
// Define a map object


// Create the tile layer that will be the background of our map
var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
});
var satellite = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox.satellite',
  accessToken: API_KEY
});

var outdoors = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox.outdoors',
  accessToken: API_KEY
});
var baseLayers = {
  "Lightmap": lightmap,
  "Satellite": satellite,
 
  "Outdoors": outdoors
    
};
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5,
  layers:[outdoors]
});
L.control.layers(baseLayers).addTo(myMap);
function chooseColor(quantile) {
  if (quantile === "4th") {
    return 'red'
} else if (quantile === "3rd") {
    return 'orange'
} else if (quantile === "2nd") {
    return 'yellow'
} else if (quantile === "1st") {
    return 'green'
} else {}
    return 'black'

  // switch (quantile) {
  // case "4th":
  //   return "red";
  // case "3rd":
  //   return "orange";
  // case "2nd":
  //   return "yellow";
  // case "1st":
  //   return "green";
  // default:
  //   return "black";
  // }
}
console.log(stateData)
// Grabbing our GeoJSON data..
d3.json(stateData).then( function(data) {
  console.log(data)
  // Creating a geoJSON layer with the retrieved data
  L.geoJson(data, {
    // Style each feature (in this case a neighborhood)
    style: function(feature) {
      return {
        color: "white",
        // Call the chooseColor function to decide which color to color our neighborhood (color based on borough)
        fillColor: chooseColor(feature.properties.quantile),
        fillOpacity: 0.5,
        weight: 1.5
      };
    },
    // Called on each feature
    onEachFeature: function(feature, layer) {
      // Set mouse events to change map styling
      layer.on({
        // When a user's mouse touches a map feature, the mouseover event calls this function, that feature's opacity changes to 90% so that it stands out
        mouseover: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.9,
            passive: true
          });
        },
        // When the cursor no longer hovers over a map feature - when the mouseout event occurs - the feature's opacity reverts back to 50%
        mouseout: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.5,
            passive: true
          });
        },
        // When a feature (neighborhood) is clicked, it is enlarged to fit the screen
        click: function(event) {
          map.fitBounds(event.target.getBounds());
        }
      });
      // Giving each feature a pop-up with information pertinent to it
      layer.bindPopup("<h1>" + feature.properties.State + "</h1> <hr> <h2>" + feature.properties.borough + "</h2>");

    }
  }).addTo(myMap);

});
function add_legend(){
var legend = L.control({ position: 'bottomright' });

legend.onAdd = function(map) {
    var div = L.DomUtil.create("div", "legend");
    div.innerHTML += "<h4>Quantile</h4>";
    div.innerHTML += '<i style="background: green"></i><span>1st Quantile</span><br>';
    div.innerHTML += '<i style="background: yellow"></i><span>2nd Quantile</span><br>';
    div.innerHTML += '<i style="background: orange"></i><span>3rd Quantile</span><br>';
    div.innerHTML += '<i style="background: red"></i><span>4th Quantile</span><br>';

  
    return div;
  };

legend.addTo(myMap);
}
add_legend();