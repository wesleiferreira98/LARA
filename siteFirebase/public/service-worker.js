self.addEventListener('install', e => {
    e.waitUntil(
      caches.open('your-cache-name').then(cache => {
        return cache.addAll([
          '/',
          '/index.html',
          // etc
        ]);
      })
    );
  });
  
  self.addEventListener('fetch', event => {
    event.respondWith(
      caches.match(event.request).then(response => {
        return response || fetch(event.request);
      })
    );
  });
  