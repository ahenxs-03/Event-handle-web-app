document.querySelector("div.category").style.display = "None";
function filter() {
  let fill = document.querySelector("select.filter").value;
  if (fill == "category") {
    document.querySelector("div.event").style.display = "None";
    document.querySelector("div.category").style.display = "block";
  } else {
    document.querySelector("div.category").style.display = "None";
    document.querySelector("div.event").style.display = "block";
  }
}
