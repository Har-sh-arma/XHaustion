
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


let conf1 = {"pwm_pins": [12, 32], "CS_PIN": 38, "SCK_PIN": 40, "temperature_pins": [37, 35, 33, 31, 29], "exhaust_max_rpm": 5000, "intake_max_rpm": 3000, "has_intake": 1, "num_dampers": 4, "damper_step": 5, "fan_step": 4, "temperature_range": [10, 36, 77, 128], "passive_modes": {"1": {"fans": {"exhaust": 40, "intake": 10}, "dampers": [35, 25, 35, 25]}, "2": {"fans": {"exhaust": 50, "intake": 10}, "dampers": [35, 35, 35, 35]}, "3": {"fans": {"exhaust": 70, "intake": 20}, "dampers": [45, 45, 45, 45]}, "default": {"fans": {"exhaust": 10, "intake": 5}, "dampers": [25, 25, 25, 25]}}, "fan_power_scaling_for_hoods": [[10, 29, 70, 73], [30, 50, 70, 90], [20, 40, 50, 80], [10, 30, 50, 70]], "damper_angles": [25, 45, 60, 90]}


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
document.addEventListener("gesturestart", function (e) {
	e.preventDefault();
    document.body.style.zoom = 0.99;
});

document.addEventListener("gesturechange", function (e) {
	e.preventDefault();

  document.body.style.zoom = 0.99;
});
document.addEventListener("gestureend", function (e) {
	  e.preventDefault();
    document.body.style.zoom = 1;
}); 