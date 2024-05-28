//Write a service worker with caching 

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches
            .open('my-site-cache-v1')
            .then((cache) => cache.addAll(['/', 'index.html', 'modeCustom/index.html']))
    );
})

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches
            .match(event.request)
            .then((response) => response || fetch(event.request))
    );
})