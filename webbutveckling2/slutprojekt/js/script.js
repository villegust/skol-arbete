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

// datum skript
// document.write(new Date().getFullYear())
document.getElementById("carr").innerText= `Copyright ${new Date().getFullYear()} © All Rights Reserved`

