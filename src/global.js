
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
    let res = await fetch("api/system_state/")
    let data = await res.json()
    return JSON.parse(data)
}

const getConfig = async() => {
    let res = await fetch("api/config/")
    let data = await res.json()
    return data
}



