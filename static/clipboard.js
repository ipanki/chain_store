function copyToClipBoard(text) {
    var tmp = document.createElement("input");
    tmp.style = "position: absolute; left: -1000px; top: -1000px";
    tmp.value = text;
    document.body.appendChild(tmp);
    tmp.select();
    document.execCommand("copy");
    document.body.removeChild(tmp);
}
