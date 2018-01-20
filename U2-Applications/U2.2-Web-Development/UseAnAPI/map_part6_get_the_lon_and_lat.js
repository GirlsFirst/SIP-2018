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

function panToCountry() {
	var countryName = document.getElementById("country-name").value;
	var lon = 0;
	var lat = 0;
	
	var query = "https://restcountries.eu/rest/v2/name/"+countryName+"?fullText=true"

	query = query.replace(/ /g, "%20")
	// alert(query);

	var countryRequest = new XMLHttpRequest();
	countryRequest.open('GET', query, false);

	countryRequest.send();
	
	//alert("Ready State " + countryRequest.readyState);
	//alert("Status " + countryRequest.status);
	//alert("Response" + countryRequest.responseText);

	// Step 1: First we should only pan if the information was correct:
	if(countryRequest.readyState != 4 || countryRequest.status != 200 || countryRequest.responseText === "") {
	 	alert("Request had an error!");
	 	return;
	}

	// Step 2: Let's copy this output into a text file and
	// see where the lattitude and longitude live
	// We need to convert this to JSON using the JSON.parse
	// function in order to use the data.
	//alert(countryRequest.responseText);
	var countryInformation = JSON.parse(countryRequest.responseText);
	
	// Step 3: We have to figure out where the information is based
	// on the JSON we got back. This can be very tricky sometimes.
	// For instance, this JSON returns an ARRAY of information.
	// Inside the FIRST array element, we have our latlng variable.
	// This variable has the information we need!
	lat = countryInformation[0].latlng[0];
	lon = countryInformation[0].latlng[1];
	
	window.console.log(countryName + ": lon " + lon + " & lat " + lat);

	var location = ol.proj.fromLonLat([lon, lat]);

	view.animate({
		center: location, // Location
		duration: 2000  // Two seconds
	});
}

window.onload = init;
