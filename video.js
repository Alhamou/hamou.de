/* Click-to-play YouTube. The page shows a local poster; nothing is loaded from
   YouTube (Google) until the visitor presses play. Without JavaScript the link
   simply opens the video on YouTube. */
(function () {
  function play(link) {
    var id = link.getAttribute('data-yt');
    if (!id || !/^[\w-]{6,20}$/.test(id)) return false;
    var lang = (document.documentElement.lang || 'en').slice(0, 2);
    var frame = document.createElement('iframe');
    frame.src = 'https://www.youtube-nocookie.com/embed/' + id +
      '?autoplay=1&rel=0&playsinline=1&hl=' + encodeURIComponent(lang);
    frame.title = link.getAttribute('data-title') || 'YouTube';
    frame.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    frame.allowFullscreen = true;
    frame.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    var box = document.createElement('div');
    box.className = link.className + ' on';
    box.appendChild(frame);
    link.parentNode.replaceChild(box, link);
    frame.focus();
    return true;
  }

  document.addEventListener('click', function (e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var link = e.target.closest ? e.target.closest('a[data-yt]') : null;
    if (link && play(link)) e.preventDefault();
  });
})();
