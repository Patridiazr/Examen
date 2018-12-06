var CACHE_NAME = 'papaApp';
var urlsToCache = [
  '/',
  './index.html',
  '/static/css/estilos.css',
  '/static/js/app.js',
  '/static/css/flexboxgrid.css',
  '/static/css/bootstrap.css', 
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Cache open!');
        return cache.addAll(urlsToCache);
      })
  );
});


self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
        .then(function(response) {
            // Cache hit - return response
            if (response) {
                return response;
            }
            return fetch(event.request);
        })
    );
});