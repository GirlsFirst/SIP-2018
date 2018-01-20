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

function panHome() {
	view.animate({
		center: ourLoc, // "Home" Location
		duration: 2000  // Two seconds
	});
}


// Step 2: Create the panToLocation function.
function panToLocation() {
	// Step 2: add the basic values we know we'll need
	var countryName = document.getElementById("country-name").value;
	var lon = 0.0;
	var lat = 0.0;

	// Step 3: Let's find our country's longitude and lattitude!
	// Ask the students to find the documentation where they can
	// search / query for a location's information!
	// Once you write this, pause and ask students what next?
	// How do we get information from this URL. Right now it's
	// just a url...
	var query = "https://restcountries.eu/rest/v2/name/"+countryName;
	
	// Step 2: Add the conversion from longitude and lattitude 
	// that we used for our home location!
	var location = ol.proj.fromLonLat([lon, lat]);

	// Step 2: Add the animation that we used in panHome
	// and swap out what we pan to! Stop here and run the code.
	// When it errors, ask the students what they think happened.
	// Direct them to think about the 0, 0 of longitude and lattitude 
	view.animate({
		center: location, // Location
		duration: 2000  // Two seconds
	});
}

window.onload = init;
