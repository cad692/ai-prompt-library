(function () {
  "use strict";

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.left = "-9999px";
      document.body.appendChild(ta);
      ta.select();
      try {
        var ok = document.execCommand("copy");
        document.body.removeChild(ta);
        ok ? resolve() : reject(new Error("copy failed"));
      } catch (err) {
        document.body.removeChild(ta);
        reject(err);
      }
    });
  }

  function showToast(msg) {
    var t = document.getElementById("toast");
    if (!t) return;
    t.textContent = msg;
    t.classList.add("show");
    setTimeout(function () {
      t.classList.remove("show");
    }, 1600);
  }

  var btn = document.getElementById("copy-prompt-btn");
  var src = document.getElementById("prompt-source");
  var box = document.getElementById("prompt-text");

  if (!btn || !src) return;

  btn.addEventListener("click", function () {
    var text = src.textContent;
    copyText(text)
      .then(function () {
        showToast("Prompt copied");
      })
      .catch(function () {
        if (box) {
          var range = document.createRange();
          range.selectNodeContents(box);
          var sel = window.getSelection();
          sel.removeAllRanges();
          sel.addRange(range);
        }
        showToast("Select-all ready — press Ctrl+C / Cmd+C");
      });
  });
})();
