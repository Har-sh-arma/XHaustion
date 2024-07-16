
//navbar highlight
let s = window.location.href.split("/")
let a = document.querySelectorAll(".nav > div > a")
flag = false
a.forEach(el=>{
    if (el.innerText === s[s.length-2].toUpperCase()) {
        el.classList.add("current_nav")
        flag = true
    }
})

if (!flag) {
    a[0].classList.add("current_nav")
}



const getSystemState = async() => {
    let res = await fetch(`${window.location.origin}/api/system_state/` , {origin: window.location.origin})
    let data = await res.json()
    return JSON.parse(data)
}

const getConfig = async() => {
    let res = await fetch(`${window.location.origin}/api/config/`)
    let data = await res.json()
    return data
}

const setConfig = async(config) => {
    let res = await fetch(`${window.location.origin}/api/config/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(config),
    })

    return
}


const setSystemState = async(sys_state) => {
    let res = await fetch(`${window.location.origin}/api/system_state/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(sys_state),
    })
    return
}
document.addEventListener('contextmenu', event => {
    event.preventDefault();
});
//document.addEventListener("keydown", e => {
//    if(e.key == "F11") e.preventDefault();
//});
//// document.onkeydown = function (e) {
////     return false;
//// }
// Prevent context menu
document.addEventListener('contextmenu', event => {
    event.preventDefault();
});

// Function to disable zooming
const disableZoom = () => {
    // Prevent pinch-to-zoom and zoom-in/out on touch devices
    document.addEventListener('touchstart', event => {
        if (event.touches.length > 1) {
            event.preventDefault();
        }
    }, { passive: false });

    document.addEventListener('touchmove', event => {
        if (event.scale !== 1) {
            event.preventDefault();
        }
    }, { passive: false });

    document.addEventListener('gesturestart', event => {
        event.preventDefault();
    }, { passive: false });

    document.addEventListener('gesturechange', event => {
        event.preventDefault();
    }, { passive: false });

    document.addEventListener('gestureend', event => {
        event.preventDefault();
    }, { passive: false });

    // Disable double-tap to zoom
    let lastTouchEnd = 0;
    document.addEventListener('touchend', event => {
        let now = (new Date()).getTime();
        if (now - lastTouchEnd <= 300) {
            event.preventDefault();
        }
        lastTouchEnd = now;
    }, { passive: false });

    // Prevent zooming using touchpad gestures on laptops
    document.addEventListener('wheel', event => {
        if (event.ctrlKey) {
            event.preventDefault();
        }
    }, { passive: false });
};

// Execute the function to disable zooming
disableZoom();


