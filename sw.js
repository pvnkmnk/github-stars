// STAR//GUIDE service worker — offline cache for key assets
const CACHE = "starguide-v1";

// Pre-cache lightweight static assets on install
const PRE = [
  "/github-stars/site.webmanifest",
];

self.addEventListener("install", e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(PRE)).catch(() => {})
  );
  self.skipWaiting();
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", e => {
  const url = new URL(e.request.url);
  const { pathname } = url;

  // Cross-origin: Google Fonts — cache-first (must check before origin guard)
  if (url.hostname === "fonts.googleapis.com" || url.hostname === "fonts.gstatic.com") {
    e.respondWith(
      caches.open(CACHE).then(c =>
        c.match(e.request).then(r =>
          r ||
          fetch(e.request).then(resp => {
            c.put(e.request, resp.clone());
            return resp;
          })
        )
      )
    );
    return;
  }

  // Other cross-origin: don't cache
  if (url.origin !== self.location.origin) return;

  // Out of scope: don't cache
  if (!pathname.startsWith("/github-stars/")) return;

  // Pre-cached assets: cache-first (uses network as fallback when cache misses)
  if (PRE.includes(pathname)) {
    e.respondWith(
      caches.match(e.request).then(r => r || fetch(e.request))
    );
    return;
  }

  // index.html: stale-while-revalidate (serve cached, update in background)
  if (pathname === "/github-stars/") {
    e.respondWith(
      caches.open(CACHE).then(c =>
        c.match(e.request).then(cached => {
          const net = fetch(e.request).then(resp => {
            if (resp.ok) c.put(e.request, resp.clone());
            return resp;
          });
          return cached || net;
        })
      )
    );
    return;
  }

  // Data files (stars/*): network-first, cache fallback
  if (pathname.startsWith("/github-stars/stars/")) {
    e.respondWith(
      caches.open(CACHE).then(c =>
        c.match(e.request).then(cached =>
          fetch(e.request)
            .then(resp => {
              if (resp.ok) c.put(e.request, resp.clone());
              return resp;
            })
            .catch(() => cached || new Response("Offline — data unavailable", { status: 503 }))
        )
      )
    );
    return;
  }

  // Everything else (og-preview.png etc.): network-first, cache on success
  e.respondWith(
    caches.open(CACHE).then(c =>
      fetch(e.request)
        .then(resp => {
          if (resp.ok) c.put(e.request, resp.clone());
          return resp;
        })
        .catch(() => caches.match(e.request))
    )
  );
});
