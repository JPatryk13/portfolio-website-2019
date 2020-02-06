/* Make navbar dark when scrolled down */

// Get html's body
var body = document.getElementsByTagName("body")[0];

// When the user scrolls the page, execute makeItSolid
body.onscroll = function() {makeItSolid()};

// Get the navbar
var navbar = document.getElementById("Navbar");

// Add transition style to the navbar
// navbar.classList.add("t-03");

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function makeItSolid() {
    if (window.pageYOffset > 0) {
        navbar.style.backgroundColor = "rgba(51, 51, 51, 1)";
    } else {
        navbar.style.backgroundColor = "rgba(51, 51, 51, 0)";
	}
}