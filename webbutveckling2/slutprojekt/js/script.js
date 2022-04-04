const slideMenu = document.querySelector(".slideMenu")
const navMenu = document.querySelector(".nav-menu")

slideMenu.addEventListener("click", () => {
    slideMenu.classList.toggle("click");
    navMenu.classList.toggle("active");
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
    slideMenu.classList.remove("click");
    navMenu.classList.remove("active");
}))

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

// datum skript
document.write(new Date().getFullYear())

