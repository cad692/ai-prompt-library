(function () {
  "use strict";

  var DATA = [];
  var ORDER = [];
  var currentId = null;
  var promptCache = Object.create(null);
  var lastFocus = null;

  var els = {
    list: document.getElementById("prompt-list"),
    search: document.getElementById("search"),
    cat: document.getElementById("filter-category"),
    diff: document.getElementById("filter-difficulty"),
    count: document.getElementById("result-count"),
    empty: document.getElementById("empty-state"),
    backdrop: document.getElementById("sheet-backdrop"),
    sheet: document.getElementById("preview-sheet"),
    title: document.getElementById("sheet-title"),
    usage: document.getElementById("sheet-usage"),
    preview: document.getElementById("sheet-preview"),
    meta: document.getElementById("sheet-meta"),
    openFull: document.getElementById("btn-open-full"),
    copy: document.getElementById("btn-copy"),
    github: document.getElementById("btn-github"),
    prev: document.getElementById("btn-prev"),
    next: document.getElementById("btn-next"),
    close: document.getElementById("btn-close-sheet"),
    toast: document.getElementById("toast"),
  };

  var CAT_NAMES = window.PROMPT_CAT_NAMES || {};
  var BASE = (window.BASE_URL || "").replace(/\/$/, "");
  var REPO = (window.GITHUB_REPO_URL || "").replace(/\/$/, "");

  function badgeClass(d) {
    return "badge badge-" + String(d || "").toLowerCase();
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function getById(id) {
    for (var i = 0; i < DATA.length; i++) {
      if (DATA[i].id === id) return DATA[i];
    }
    return null;
  }

  function filtered() {
    var q = (els.search.value || "").trim().toLowerCase();
    var cat = els.cat.value;
    var diff = els.diff.value;
    return DATA.filter(function (p) {
      if (cat && p.category !== cat) return false;
      if (diff && p.difficulty !== diff) return false;
      if (!q) return true;
      var hay = [p.title, p.usage, p.preview]
        .concat(p.tags || [])
        .join(" ")
        .toLowerCase();
      return hay.indexOf(q) !== -1;
    });
  }

  function groupByCategory(items) {
    var order = [];
    var map = Object.create(null);
    items.forEach(function (p) {
      if (!map[p.category]) {
        map[p.category] = [];
        order.push(p.category);
      }
      map[p.category].push(p);
    });
    return { order: order, map: map };
  }

  function render() {
    var items = filtered();
    ORDER = items.map(function (p) {
      return p.id;
    });
    els.count.textContent = items.length + " prompt" + (items.length === 1 ? "" : "s");
    els.empty.hidden = items.length > 0;
    els.list.innerHTML = "";

    var grouped = groupByCategory(items);
    grouped.order.forEach(function (cat) {
      var block = document.createElement("section");
      block.className = "cat-block";
      block.setAttribute("aria-label", CAT_NAMES[cat] || cat);

      var bar = document.createElement("div");
      bar.className = "cat-bar";
      bar.setAttribute("data-cat", cat);
      var list = grouped.map[cat];
      bar.innerHTML =
        "<span>" +
        escapeHtml(CAT_NAMES[cat] || cat) +
        '</span><span class="muted">' +
        escapeHtml(list[0].id) +
        " to " +
        escapeHtml(list[list.length - 1].id) +
        "</span>";
      block.appendChild(bar);

      list.forEach(function (p) {
        var row = document.createElement("button");
        row.type = "button";
        row.className = "prompt-row";
        row.dataset.id = p.id;
        row.setAttribute("aria-label", "Open preview for " + p.title);
        row.innerHTML =
          '<div><div><span class="row-id">' +
          escapeHtml(p.id) +
          '</span><span class="row-title">' +
          escapeHtml(p.title) +
          '</span></div><p class="row-usage">' +
          escapeHtml(p.usage) +
          '</p></div><div class="row-side"><span class="' +
          badgeClass(p.difficulty) +
          '">' +
          escapeHtml(p.difficulty) +
          '</span><span class="open-btn" aria-hidden="true">Open ↗</span></div>';
        row.addEventListener("click", function () {
          openSheet(p.id, row);
        });
        block.appendChild(row);
      });
      els.list.appendChild(block);
    });
  }

  function setUrl(id, push) {
    var url = new URL(window.location.href);
    if (id) url.searchParams.set("p", id);
    else url.searchParams.delete("p");
    var method = push ? "pushState" : "replaceState";
    history[method]({ promptId: id || null }, "", url.pathname + url.search + url.hash);
  }

  function focusables() {
    return els.sheet.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
  }

  function trapFocus(e) {
    if (!els.sheet.classList.contains("open") || e.key !== "Tab") return;
    var nodes = Array.prototype.slice.call(focusables());
    if (!nodes.length) return;
    var first = nodes[0];
    var last = nodes[nodes.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }

  function fillSheet(p) {
    currentId = p.id;
    els.meta.innerHTML =
      '<span class="pill">' +
      escapeHtml(p.id) +
      '</span><span class="pill pill-cat">' +
      escapeHtml(CAT_NAMES[p.category] || p.category) +
      '</span><span class="' +
      badgeClass(p.difficulty) +
      '">' +
      escapeHtml(p.difficulty) +
      "</span>";
    els.title.textContent = p.title;
    els.usage.textContent = p.usage;
    els.preview.textContent = p.preview;
    els.openFull.href = BASE + "/prompts/" + p.id + "-" + p.slug + ".html";
    els.github.href = REPO + "/blob/main/prompts-md/" + p.id + "-" + p.slug + ".md";

    var idx = ORDER.indexOf(p.id);
    els.prev.disabled = idx <= 0;
    els.next.disabled = idx < 0 || idx >= ORDER.length - 1;
  }

  function openSheet(id, focusEl) {
    var p = getById(id);
    if (!p) return;
    lastFocus = focusEl || document.activeElement;
    fillSheet(p);
    els.backdrop.classList.add("open");
    els.sheet.classList.add("open");
    els.sheet.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    setUrl(id, true);
    window.setTimeout(function () {
      els.close.focus();
    }, 30);
  }

  function closeSheet(fromPopstate) {
    els.backdrop.classList.remove("open");
    els.sheet.classList.remove("open");
    els.sheet.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    currentId = null;
    if (!fromPopstate) setUrl(null, true);
    if (lastFocus && typeof lastFocus.focus === "function") lastFocus.focus();
  }

  function showToast(msg) {
    els.toast.textContent = msg;
    els.toast.classList.add("show");
    window.setTimeout(function () {
      els.toast.classList.remove("show");
    }, 1800);
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

  function fetchPrompt(p) {
    if (promptCache[p.id]) return Promise.resolve(promptCache[p.id]);
    var url = "prompts-md/" + p.id + "-" + p.slug + ".md";
    return fetch(url)
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.text();
      })
      .then(function (md) {
        var match = md.match(/## Prompt\s*\r?\n+```text\r?\n([\s\S]*?)\r?\n```/);
        if (!match) match = md.match(/```text\r?\n([\s\S]*?)\r?\n```/);
        if (!match) throw new Error("prompt block missing");
        promptCache[p.id] = match[1].replace(/\r\n/g, "\n").trim();
        return promptCache[p.id];
      });
  }

  function onCopy() {
    var p = getById(currentId);
    if (!p) return;
    els.copy.disabled = true;
    els.copy.textContent = "Loading…";
    fetchPrompt(p)
      .then(function (text) {
        return copyText(text).then(function () {
          showToast("Prompt copied");
        });
      })
      .catch(function () {
        showToast("Could not load prompt. Open full page or use offline ZIP.");
        // Fallback: open full page
      })
      .finally(function () {
        els.copy.disabled = false;
        els.copy.textContent = "Copy prompt";
      });
  }

  function move(delta) {
    var idx = ORDER.indexOf(currentId);
    if (idx < 0) return;
    var next = ORDER[idx + delta];
    if (!next) return;
    fillSheet(getById(next));
    setUrl(next, true);
  }

  function bind() {
    els.search.addEventListener("input", render);
    els.cat.addEventListener("change", render);
    els.diff.addEventListener("change", render);
    els.close.addEventListener("click", function () {
      closeSheet(false);
    });
    els.backdrop.addEventListener("click", function () {
      closeSheet(false);
    });
    els.copy.addEventListener("click", onCopy);
    els.prev.addEventListener("click", function () {
      move(-1);
    });
    els.next.addEventListener("click", function () {
      move(1);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && els.sheet.classList.contains("open")) {
        e.preventDefault();
        closeSheet(false);
      }
      trapFocus(e);
    });
    window.addEventListener("popstate", function (e) {
      var id = (e.state && e.state.promptId) || new URL(window.location.href).searchParams.get("p");
      if (id) openSheet(id, lastFocus);
      else if (els.sheet.classList.contains("open")) closeSheet(true);
    });
  }

  function bootFromQuery() {
    var id = new URL(window.location.href).searchParams.get("p");
    if (id && getById(id)) {
      // Don't push again
      var p = getById(id);
      lastFocus = document.body;
      fillSheet(p);
      els.backdrop.classList.add("open");
      els.sheet.classList.add("open");
      els.sheet.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
      history.replaceState({ promptId: id }, "", window.location.pathname + "?p=" + encodeURIComponent(id));
    }
  }

  fetch("assets/prompts-index.json")
    .then(function (r) {
      if (!r.ok) throw new Error("index missing");
      return r.json();
    })
    .then(function (json) {
      DATA = json;
      bind();
      render();
      bootFromQuery();
    })
    .catch(function () {
      els.count.textContent = "Could not load prompt index.";
      els.empty.hidden = false;
      els.empty.textContent =
        "Search index failed to load. Use the static list below or the offline ZIP.";
    });
})();
