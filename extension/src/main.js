const elements = document.querySelectorAll("#rso .MjjYud > div.g.Ww4FFb.vt6azd.tF2Cxc")
elements.forEach(function(element, i){
    const url = element.childNodes[0].childNodes[0].childNodes[0].childNodes[0].href
    const e = `
    <a href="${url}" style="width:111px;height:82px">
        <img loading="lazy" align="left" src="http://127.0.0.1:4200/get/?url=${url}" style="width:111px;height:82px">
    </a>`
    element.style.display = "flex"
    element.innerHTML = e + element.innerHTML
})