// Банановый дождь: по клику на любой элемент с атрибутом data-banana-rain
(function () {
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function bananaSrc() {
    var logo = document.querySelector(".md-header__button.md-logo img");
    return logo ? logo.src : "";
  }

  function rain(count) {
    if (reduceMotion) return;
    var src = bananaSrc();
    var layer = document.querySelector(".banana-rain");
    if (!layer) {
      layer = document.createElement("div");
      layer.className = "banana-rain";
      document.body.appendChild(layer);
    }
    for (var i = 0; i < count; i++) {
      var img = document.createElement("img");
      img.src = src;
      img.alt = "";
      img.className = "banana-drop";
      img.style.left = Math.random() * 100 - 3 + "%";
      img.style.width = 1.4 + Math.random() * 2.2 + "rem";
      img.style.animationDuration = 1.8 + Math.random() * 1.8 + "s";
      img.style.animationDelay = Math.random() * 0.6 + "s";
      img.style.setProperty("--spin", (Math.random() > 0.5 ? 1 : -1) * (180 + Math.random() * 360) + "deg");
      img.addEventListener("animationend", function () { this.remove(); });
      layer.appendChild(img);
    }
  }

  document.addEventListener("click", function (event) {
    if (event.target.closest("[data-banana-rain]")) rain(36);
  });
})();
