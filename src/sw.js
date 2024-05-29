//Write a service worker with caching 

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches
            .open('my-site-cache-v1')
            .then((cache) => cache.addAll(["modeCustom/index.html", "modeCustom/style.css", "modeCustom/script.js", "index.html", "style.css", "script.js"]))
    );
})

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches
            .match(event.request)
            .then((response) => response || fetch(event.request))
    );
})