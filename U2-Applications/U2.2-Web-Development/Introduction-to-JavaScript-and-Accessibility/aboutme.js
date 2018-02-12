/* add <script src="aboutme.js"></script> to <head> of PortfolioPt1.html */
alert("Welcome to my page!");
imgID = 1;

function bigImg(x) {
    x.style.height = "400px";
    x.style.width = "400px";
}

function normalImg(x) {
    x.style.height = "70px";
    x.style.width = "70px";
}

function showHideSection(section){
  var x = document.getElementById(section);
  if (x.style.display === "none") {
    x.style.display = "block";
    document.getElementById("show/hide").innerHTML = "Hide Bio"
  } else {
    x.style.display = "none";
    document.getElementById("show/hide").innerHTML = "Show Bio"
  }
}

function nextImg(){
  img = document.getElementById("projects");
	if (imgID == 1) {
    img.innerHTML = '<h1>Recent Projects:</h1><h2>Robot Project</h2><p>I made a robot dance! Check out the screenshot below!</p><img id="scratch-project" src="https://upload.wikimedia.org/wikipedia/it/7/75/Boe-bot.jpg" alt="Screen shot of my robot">';
    imgID = 2;
	} else {
    img.innerHTML = '<h1>Recent Projects:</h1><h2>Side Scroller</h2><p>Last week, I build a cool side scroller project in Scratch. To build it, I learned about storyboarding, graphic design and using the concepts of functions, loops, conditionals, and variables. Check out the screenshot below!</p><img id="scratch-project" src="side-scrolling-screenshot.png" alt="Screen shot of Side Scroller Spaceship">';
		imgID = 1;
	}
}
