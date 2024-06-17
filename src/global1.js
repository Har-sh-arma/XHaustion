
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


let conf1 = {"exhaust_pressure_range": [500, 1000, 1500, 2000], "fan_power_scaling_exhaust_pressure": [0, 25, 50, 75], "pressure_address": "0x48", "pressure_A0": "0x40", "pressure_offset": 60, "pressure_scaling": 12.5, "pwm_pins": [12, 32], "CS_PIN": 38, "SCK_PIN": 40, "temperature_pins": [37, 35, 33, 31, 29], "exhaust_max_rpm": 5000, "intake_max_rpm": 3000, "has_intake": 1, "num_dampers": 4, "damper_step": 5, "fan_step": 4, "temperature_range": [35, 71, 122, 188], "passive_modes": {"1": {"fans": {"exhaust": 100, "intake": 100}, "dampers": [18, 18, 18, 18]}, "2": {"fans": {"exhaust": 100, "intake": 50}, "dampers": [18, 18, 18, 18]}, "3": {"fans": {"exhaust": 75, "intake": 25}, "dampers": [18, 18, 18, 18]}, "default": {"fans": {"exhaust": 75, "intake": 75}, "dampers": [18, 18, 18, 18]}}, "fan_power_scaling_for_hoods": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "damper_angles": [25, 45, 60, 90]}

let sys_st1 = {
    "exhaust": 30,
    "intake": 20,
    "air_flow": 0,
    "temperatures": [
        0,
        0,
        0,
        0
    ],
    "dampers": [
        0,
        0,
        0,
        0
    ],
    "mode": "passive",
    "passive_mode": "default",
    "override": {"fans":{"exhaust": 0, "intake": 0}, "dampers": [0, 0, 0, 0]}
}

const getSystemState = async() => {
    // let res = await fetch(`${window.location.origin}/api/system_state/` , {origin: window.location.origin})
    // let data = await res.json()
    // return JSON.parse(data)
    return sys_st1
}

const getConfig = async() => {
    // let res = await fetch(`${window.location.origin}/api/config/`)
    // let data = await res.json()
    // return data
    return conf1
}

const setConfig = async(config) => {
    // let res = await fetch(`${window.location.origin}/api/config/`, {
    //     method: "POST",
    //     headers: {
    //         "Content-Type": "application/json",
    //     },
    //     body: JSON.stringify(config),
    // })

    // remove the below in prod
    conf1 = config
    return
}


const setSystemState = async(sys_state) => {
    // let res = await fetch(`${window.location.origin}/api/system_state/`, {
    //     method: "POST",
    //     headers: {
    //         "Content-Type": "application/json",
    //     },
    //     body: JSON.stringify(sys_state),
    // })
    sys_st1 = sys_state
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


