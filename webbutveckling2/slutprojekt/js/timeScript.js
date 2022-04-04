//tids script till reviews
const current = new Date();

const time = current.toLocaleTimeString("en-US", {
  hour: "2-digit",
  minute: "2-digit",
  hour12: false
});

document.getElementById("tid1").innerText += time
document.getElementById("tid2").innerText += time
document.getElementById("tid3").innerText += time
document.getElementById("tid4").innerText += time