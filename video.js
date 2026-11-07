/* Click-to-play YouTube. The page shows a local poster; nothing is loaded
   from YouTube (Google) until the visitor presses play. Without JavaScript
   the link simply opens the video on YouTube.

   One click has to start the video. Chrome, Edge and Firefox on the desktop
   do that with a plain embed and ?autoplay=1. Safari and most mobile
   browsers do not carry the click into the new frame, so the visitor had to
   press play a second time. For them the click loads YouTube's player API,
   which starts the video once the player is ready. If the browser still
   refuses to play with sound, the video starts muted (YouTube shows its
   unmute button) instead of stopping on a second play button. */
(function () {
  var HOST = 'https://www.youtube-nocookie.com';
  var ALLOW = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
  var PLAYING = 1;
  var BUFFERING = 3;
  var needsApi = /Apple/.test(navigator.vendor || '') || /Mobi|Android/.test(navigator.userAgent || '');
  var api = null;

  function loadApi() {
    if (!api) {
      api = new Promise(function (resolve, reject) {
        if (window.YT && window.YT.Player) {
          resolve(window.YT);
          return;
        }
        var timer = setTimeout(function () { reject(new Error('YouTube API timeout')); }, 6000);
        var previous = window.onYouTubeIframeAPIReady;
        window.onYouTubeIframeAPIReady = function () {
          clearTimeout(timer);
          if (typeof previous === 'function') previous();
          resolve(window.YT);
        };
        var s = document.createElement('script');
        s.src = 'https://www.youtube.com/iframe_api';
        s.async = true;
        s.onerror = function () {
          clearTimeout(timer);
          reject(new Error('YouTube API blocked'));
        };
        document.head.appendChild(s);
      });
      api.catch(function () { api = null; });
    }
    return api;
  }

  function plainFrame(id, lang, title) {
    var frame = document.createElement('iframe');
    frame.src = HOST + '/embed/' + id + '?autoplay=1&rel=0&playsinline=1&hl=' + encodeURIComponent(lang);
    frame.title = title;
    frame.allow = ALLOW;
    frame.allowFullscreen = true;
    frame.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    return frame;
  }

  function apiPlayer(YT, slot, opts) {
    var played = false;
    var muted = false;
    function startMuted(p) {
      if (played || muted) return;
      muted = true;
      p.mute();
      p.playVideo();
    }
    new YT.Player(slot, {
      host: HOST,
      videoId: opts.id,
      width: '100%',
      height: '100%',
      playerVars: { autoplay: 1, playsinline: 1, rel: 0, hl: opts.lang },
      events: {
        onReady: function (e) {
          var p = e.target;
          var frame = p.getIframe();
          frame.title = opts.title;
          opts.done();
          if (opts.focus && document.activeElement === document.body) frame.focus();
          if (p.getPlayerState() === PLAYING) {
            played = true;
            return;
          }
          p.playVideo();
          // Not every browser reports a blocked start, so check again.
          setTimeout(function () {
            var s = p.getPlayerState();
            if (s !== PLAYING && s !== BUFFERING) startMuted(p);
          }, 3000);
        },
        onStateChange: function (e) {
          if (e.data === PLAYING) played = true;
        },
        onAutoplayBlocked: function (e) {
          startMuted(e.target);
        }
      }
    });
  }

  function play(link) {
    var id = link.getAttribute('data-yt');
    if (!id || !/^[\w-]{6,20}$/.test(id)) return false;
    var opts = {
      id: id,
      lang: (document.documentElement.lang || 'en').slice(0, 2),
      title: link.getAttribute('data-title') || 'YouTube',
      focus: document.activeElement === link
    };

    // The poster stays, with a spinner, until the player has loaded.
    var box = document.createElement('div');
    box.className = link.className + ' on loading';
    var poster = link.querySelector('img');
    if (poster) {
      poster = poster.cloneNode(true);
      poster.removeAttribute('loading');
      poster.removeAttribute('fetchpriority');
      box.appendChild(poster);
    }
    var slot = document.createElement('div');
    slot.className = 'ytSlot';
    box.appendChild(slot);
    link.parentNode.replaceChild(box, link);
    opts.done = function () { box.classList.remove('loading'); };
    setTimeout(opts.done, 10000);

    function plain() {
      if (slot.parentNode !== box) return;
      var frame = plainFrame(id, opts.lang, opts.title);
      frame.addEventListener('load', opts.done);
      box.replaceChild(frame, slot);
      if (opts.focus) frame.focus();
    }

    if (!needsApi) {
      plain();
    } else {
      // If the API cannot load (offline, blocked by an extension), fall back
      // to the plain embed.
      loadApi().then(function (YT) { apiPlayer(YT, slot, opts); }).catch(plain);
    }
    return true;
  }

  document.addEventListener('click', function (e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var link = e.target.closest ? e.target.closest('a[data-yt]') : null;
    if (link && play(link)) e.preventDefault();
  });
})();
