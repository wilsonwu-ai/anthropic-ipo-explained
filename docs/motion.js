// Starts each figure's CSS animation when it scrolls into view.
// Without JS (or with reduced motion) every chart shows its final state.
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var svgs = document.querySelectorAll('figure[data-visual] svg');
  if (reduce || !('IntersectionObserver' in window)) return;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.remove('play');
        void e.target.getBoundingClientRect();
        e.target.classList.add('play');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.35 });
  svgs.forEach(function (s) { io.observe(s); });
  // Click a chart to replay it.
  svgs.forEach(function (s) {
    s.style.cursor = 'pointer';
    s.addEventListener('click', function () {
      s.classList.remove('play');
      void s.getBoundingClientRect();
      s.classList.add('play');
    });
  });
})();
