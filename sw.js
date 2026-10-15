const CACHE_NAME = 'japanese-handbook-v4';
const ASSETS = [
  './',
  './index.html',
  './日语随身宝.html',
  './动词变形特训.html',
  './manifest.json',
  './练习题库/index.html',
  './练习题库/01_动词变形特训.html',
  './练习题库/02_形容词变形特训.html',
  './练习题库/03_助词辨析特训.html',
  './练习题库/04_句型造句特训.html',
  './练习题库/05_常用口语特训.html'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(ASSETS);
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;
      return fetch(event.request).then(response => {
        if (!response || response.status !== 200 || response.type !== 'basic') {
          return response;
        }
        const responseToCache = response.clone();
        caches.open(CACHE_NAME).then(cache => {
          cache.put(event.request, responseToCache);
        });
        return response;
      }).catch(() => {
        return caches.match('./index.html');
      });
    })
  );
});
