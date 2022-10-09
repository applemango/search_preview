const elements = document.querySelectorAll("#rso .MjjYud > div.g.Ww4FFb.vt6azd.tF2Cxc, .MjjYud .g .BYM4Nd .eKjLze .g, .CCcQAA .g > div > div, .hlcw0c > .MjjYud .g > div:not(.kvH3mc) > div:not(.Z26q7c)")
elements.forEach(function(element, i){
    let url;
    try {
        url = element.childNodes[0].childNodes[0].childNodes[0].childNodes[0].href
    } catch (e) {
        if( e instanceof TypeError) {
            url = element.childNodes[1].childNodes[0].childNodes[0].childNodes[0].href
        }
    }
    const e = `
    <a href="${url}" style="width:111px;display:flex;/*align-items: center*/;justify-content: center;">
        <img loading="lazy" align="left" src="http://127.0.0.1:4200/get/?url=${url}" style="width:111px;height:82px">
    </a>`
    element.style.display = "flex"
    element.innerHTML = e + element.innerHTML
})