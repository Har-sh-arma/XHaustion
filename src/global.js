
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


let config = {
    "pwm_pins": [12, 32],
    "CS_PIN": 38,
    "SCK_PIN":40,
    "temperature_pins": [37, 35, 33, 31, 29],
    "exhaust_max_rpm": 5000,
    "intake_max_rpm": 3000,
    "has_intake": 1,
    "num_dampers": 4,
    "temperature_range": [
        40,
        70,
        100,
        150
    ],
    "passive_modes": {
        "default": {
            "fans": {
                "exhaust": 10,
                "intake": 5
            },
            "dampers": [
                25,
                25,
                25,
                25
            ]
        },
        "1": {
            "fans": {
                "exhaust": 40,
                "intake": 10
            },
            "dampers": [
                35,
                25,
                35,
                25
            ]
        },
        "2": {
            "fans": {
                "exhaust": 50,
                "intake": 10
            },
            "dampers": [
                35,
                35,
                35,
                35
            ]
        },
        "3": {
            "fans": {
                "exhaust": 70,
                "intake": 20
            },
            "dampers": [
                45,
                45,
                45,
                45
            ]
        }
    },
    "fan_power_scaling_for_hoods": [
        [
            40,
            60,
            80,
            100
        ],
        [
            30,
            50,
            70,
            90
        ],
        [
            20,
            40,
            50,
            80
        ],
        [
            10,
            30,
            50,
            70
        ]
    ],
    "damper_angles": [
        25,
        45,
        60,
        90
    ]
}

const getSystemState = async() => {
    // let res = await fetch(`${window.location.origin}/api/system_state/` , {origin: window.location.origin})
    // let data = await res.json()
    // return JSON.parse(data)


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
}


const setSystemState = async(sys_state) => {
    let res = await fetch(`${window.location.origin}/api/system_state/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(sys_state),
    })
}

document.addEventListener('contextmenu', event => {
    event.preventDefault();
});
document.addEventListener("keydown", e => {
    if(e.key == "F11") e.preventDefault();
});
// document.onkeydown = function (e) {
//     return false;
// }
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