//Får knappen
var mybutton = document.getElementById("myBtn");

// när användaren har scrollat ner 20px, så dycker knappen upp.
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

//När man trycker på en knapp så scrollar den upp till toppen
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}