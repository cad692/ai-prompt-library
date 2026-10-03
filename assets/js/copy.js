(function () {
  "use strict";

  var src = document.getElementById("prompt-source");
  var formRoot = document.getElementById("fill-form");
  var preview = document.getElementById("prompt-text");
  var copyBtn = document.getElementById("copy-prompt-btn");
  var resetBtn = document.getElementById("reset-fill-btn");
  var statusEl = document.getElementById("fill-status");

  if (!src || !formRoot || !preview || !copyBtn) return;

  var template = src.textContent;
  var placeholders = uniquePlaceholders(template);

  function uniquePlaceholders(text) {
    var re = /\[([A-Z][A-Z0-9_]*)\]/g;
    var seen = Object.create(null);
    var list = [];
    var m;
    while ((m = re.exec(text))) {
      if (!seen[m[1]]) {
        seen[m[1]] = true;
        list.push(m[1]);
      }
    }
    return list;
  }

  function labelFor(key) {
    return key
      .toLowerCase()
      .split("_")
      .map(function (w) {
        return w.charAt(0).toUpperCase() + w.slice(1);
      })
      .join(" ");
  }

  function questionFor(key) {
    var map = {
      DECISION: "What decision are you trying to make?",
      OPTIONS: "What options are you comparing? (list them)",
      DEADLINE: "What is your deadline?",
      STAKEHOLDERS: "Who is affected by this decision?",
      VALUES_OR_PRIORITIES: "What matters most to you in this choice?",
      TIME_MONEY_LOCATION_OR_FAMILY_CONSTRAINTS: "What practical limits do you have (time, money, location, family)?",
      TOPIC: "What topic should this cover?",
      AUDIENCE: "Who is the audience?",
      PURPOSE: "What is the purpose?",
      TONE: "What tone do you want?",
      CITY_OR_SETTING: "What city or setting should we use?",
    };
    if (map[key]) return map[key];
    return "What should we use for " + labelFor(key) + "?";
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function highlightFilled(text) {
    // Keep remaining placeholders highlighted; filled text is plain
    return escapeHtml(text).replace(/(\[[A-Z][A-Z0-9_]*\])/g, '<span class="ph">$1</span>');
  }

  function getValues() {
    var values = Object.create(null);
    placeholders.forEach(function (key) {
      var input = document.getElementById("field-" + key);
      values[key] = input ? String(input.value || "").trim() : "";
    });
    return values;
  }

  function filledPrompt() {
    var values = getValues();
    return template.replace(/\[([A-Z][A-Z0-9_]*)\]/g, function (full, key) {
      return values[key] ? values[key] : full;
    });
  }

  function missingCount() {
    var values = getValues();
    var n = 0;
    placeholders.forEach(function (key) {
      if (!values[key]) n += 1;
    });
    return n;
  }

  function updatePreview() {
    var text = filledPrompt();
    preview.innerHTML = highlightFilled(text);
    var miss = missingCount();
    if (!placeholders.length) {
      statusEl.textContent = "No fill-in fields in this prompt. You can copy it as-is.";
    } else if (miss === 0) {
      statusEl.textContent = "All details filled. Preview is ready — tap Copy.";
    } else {
      statusEl.textContent =
        miss + " detail" + (miss === 1 ? "" : "s") + " still empty. Fill them above, or copy with brackets left in.";
    }
  }

  function buildForm() {
    formRoot.innerHTML = "";
    if (!placeholders.length) {
      formRoot.innerHTML = '<p class="muted">This prompt has no [PLACEHOLDERS] to customize.</p>';
      updatePreview();
      return;
    }

    var intro = document.createElement("p");
    intro.className = "muted";
    intro.textContent =
      "Answer only the questions below. Your answers replace the square-bracket fields automatically.";
    formRoot.appendChild(intro);

    placeholders.forEach(function (key, i) {
      var wrap = document.createElement("div");
      wrap.className = "fill-field";

      var label = document.createElement("label");
      label.setAttribute("for", "field-" + key);
      label.innerHTML =
        '<span class="fill-q">' +
        escapeHtml(String(i + 1) + ". " + questionFor(key)) +
        '</span><span class="fill-key">[' +
        escapeHtml(key) +
        "]</span>";

      var input =
        key.length > 24 ||
        /OPTIONS|CONSTRAINTS|PRIORITIES|CONTEXT|DESCRIPTION|NOTES|TASKS|DETAILS/.test(key)
          ? document.createElement("textarea")
          : document.createElement("input");
      if (input.tagName === "INPUT") input.type = "text";
      input.id = "field-" + key;
      input.name = key;
      input.autocomplete = "off";
      input.placeholder = "Type your answer for [" + key + "]";
      if (input.tagName === "TEXTAREA") input.rows = 3;

      input.addEventListener("input", updatePreview);

      wrap.appendChild(label);
      wrap.appendChild(input);
      formRoot.appendChild(wrap);
    });

    updatePreview();
  }

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
    }, 1800);
  }

  copyBtn.addEventListener("click", function () {
    var text = filledPrompt();
    copyText(text)
      .then(function () {
        showToast(missingCount() ? "Copied (some fields still empty)" : "Filled prompt copied");
      })
      .catch(function () {
        var range = document.createRange();
        range.selectNodeContents(preview);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        showToast("Select-all ready — press Ctrl+C / Cmd+C");
      });
  });

  if (resetBtn) {
    resetBtn.addEventListener("click", function () {
      placeholders.forEach(function (key) {
        var input = document.getElementById("field-" + key);
        if (input) input.value = "";
      });
      updatePreview();
      showToast("Cleared answers");
    });
  }

  buildForm();
})();
