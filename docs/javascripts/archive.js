/* Library filtering + document page tools. document$ is Material's
   page-load observable, so this also works with instant navigation. */
document$.subscribe(function () {
  initLibrary();
  initDocument();
});

function initLibrary() {
  var root = document.querySelector(".xa-library");
  if (!root) return;

  var input = root.querySelector("[data-xa-filter]");
  var sort = root.querySelector("[data-xa-sort]");
  var grid = root.querySelector("[data-xa-grid]");
  var count = root.querySelector("[data-xa-count]");
  var empty = root.querySelector("[data-xa-empty]");
  var cards = Array.prototype.slice.call(grid.querySelectorAll(".xa-card"));
  var state = { cat: "", tags: [] };

  function apply() {
    var words = input.value.toLowerCase().split(/\s+/).filter(Boolean);
    var shown = 0;
    cards.forEach(function (card) {
      var tags = card.dataset.tags ? card.dataset.tags.split("|") : [];
      var ok = (!state.cat || card.dataset.cat === state.cat) &&
        state.tags.every(function (t) { return tags.indexOf(t) !== -1; }) &&
        words.every(function (w) { return card.dataset.text.indexOf(w) !== -1; });
      card.hidden = !ok;
      if (ok) shown++;
    });
    count.textContent = "Showing " + shown + " of " + cards.length;
    empty.hidden = shown !== 0;
  }

  function reorder() {
    var key = sort.value;
    cards.sort(function (a, b) {
      return key === "title"
        ? a.dataset.title.localeCompare(b.dataset.title)
        : b.dataset.updated.localeCompare(a.dataset.updated);
    }).forEach(function (card) { grid.appendChild(card); });
  }

  root.querySelectorAll(".xa-chip").forEach(function (chip) {
    chip.addEventListener("click", function () {
      state.cat = chip.dataset.cat;
      root.querySelectorAll(".xa-chip").forEach(function (c) { c.classList.toggle("is-on", c === chip); });
      apply();
    });
  });
  root.querySelectorAll(".xa-tag").forEach(function (chip) {
    chip.addEventListener("click", function () {
      var t = chip.dataset.tag, i = state.tags.indexOf(t);
      if (i === -1) state.tags.push(t); else state.tags.splice(i, 1);
      chip.classList.toggle("is-on", i === -1);
      apply();
    });
  });
  input.addEventListener("input", apply);
  sort.addEventListener("change", function () { reorder(); apply(); });
  apply();
}

function initDocument() {
  var select = document.querySelector("[data-xa-jump]");
  if (!select) return;
  document.querySelectorAll(".xg-doc section.page").forEach(function (page) {
    var no = page.querySelector(".pageno");
    var title = page.querySelector(".ptitle");
    var label = title ? title.textContent.trim() : page.querySelector(".cover-title") ? "Cover & Index" : "";
    select.add(new Option((no ? no.textContent.trim() : page.id) + (label ? " — " + label : ""), page.id));
  });
  select.addEventListener("change", function () {
    if (!select.value) return;
    location.hash = select.value;
    select.value = "";
  });
}

/* Buttons with [data-xa-search] open the site-wide full-text search. */
document.addEventListener("click", function (e) {
  var btn = e.target.closest("[data-xa-search]");
  if (!btn) return;
  var toggle = document.getElementById("__search");
  var field = document.querySelector("[data-md-component=search-query]");
  if (!toggle || !field) return;
  toggle.checked = true;
  toggle.dispatchEvent(new Event("change"));
  if (btn.dataset.xaSearch) {
    field.value = btn.dataset.xaSearch;
    field.dispatchEvent(new Event("input", { bubbles: true }));
  }
  setTimeout(function () { field.focus(); }, 50);
});
