/* Article pages: the footer language picker opens this page in another
   language and remembers the choice for the home page. */
(function () {
  var sel = document.getElementById('langSelect');
  if (!sel || !sel.hasAttribute('data-nav')) return;
  sel.addEventListener('change', function () {
    var opt = sel.options[sel.selectedIndex];
    try { localStorage.setItem('hamou-lang', opt.getAttribute('lang')); } catch (e) {}
    location.href = sel.value;
  });
})();
