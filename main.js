(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

  // stagger indexes (cascade delay per child)
  Array.prototype.forEach.call(document.querySelectorAll('.stagger'), function (box) {
    Array.prototype.forEach.call(box.children, function (child, i) {
      child.style.transitionDelay = (i * 80) + 'ms';
    });
  });

  // scroll progress (RTL: fills from the right)
  var bar = document.querySelector('.progress b');
  if (bar) {
    var tick = function () {
      var root = document.documentElement;
      var max = root.scrollHeight - root.clientHeight;
      bar.style.transform = 'scaleX(' + (max > 0 ? root.scrollTop / max : 0) + ')';
    };
    var raf = false;
    window.addEventListener('scroll', function () {
      if (!raf) {
        raf = true;
        requestAnimationFrame(function () { raf = false; tick(); });
      }
    }, { passive: true });
    tick();
  }
})();

(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var supported = 'IntersectionObserver' in window;
  var els = document.querySelectorAll('.reveal, .stagger');
  function showAll(list) { Array.prototype.forEach.call(list, function (el) { el.classList.add('in'); }); }

  if (!supported || reduce.matches) { showAll(els); return; }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        io.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });

  Array.prototype.forEach.call(els, function (el) { io.observe(el); });
  setTimeout(function () { showAll(document.querySelectorAll('.reveal:not(.in), .stagger:not(.in)')); }, 6000);
})();
