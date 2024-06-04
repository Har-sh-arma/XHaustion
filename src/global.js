
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
