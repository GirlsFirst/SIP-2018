var ourLoc;
var view;
var map;

function init() {
	// Initalize things here
	ourLoc = ol.proj.fromLonLat([41.043316, 28.862457]);

	view = new ol.View({
		center: ourLoc,
		zoom: 6
	});

	map = new ol.Map({
		target: 'map',
		layers: [
		  new ol.layer.Tile({
		    source: new ol.source.OSM()
		  })
		],
		// Note from the View Animation website:
		// Improve user experience by loading tiles while animating. Will make
		// animations stutter on mobile or slow devices.
		loadTilesWhileAnimating: true,
		view: view
	});
}

// Step 2: Let's make our button do something!
// We use "animate" on the view to animate it.
// To pan the view, we simply need to tell the view 
// where to go and how long to take to get there.
function panHome() {
	view.animate({
		center: ourLoc, // "Home" Location
		duration: 2000  // Two seconds
	});
}

// Final Step: Now ask the students how they might
// let someone move the map to a particular
// city or location. Would they have the
// user input longitude/lattitude, or is it
// easier for them to use a name of a city?
// To use the name of a city, we need
// another API!

window.onload = init;
