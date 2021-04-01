/*
var tableHeader = document.getElementById("tableHeader");
originalYPosition = tableHeader.offsetTop;
originalXPosition = tableHeader.offsetLeft;

window.onscroll = function() {stickyHeader()};

function stickyHeader() {

    var yPos = tableHeader.offsetTop;
    var xPos = tableHeader.offsetLeft;

    var windowTop = window.pageYOffset;
    var windowLeft = window.pageXOffset;

    console.log("------");
    console.log(windowTop);
    console.log(windowLeft);
    console.log(yPos);
    console.log(xPos);
    console.log("------");

    if(window.pageYOffset >= yPos) {
        tableHeader.style.position = "absolute";
        tableHeader.style.top = String(windowTop) + "px";
        tableHeader.style.left = String(0 - windowLeft) + "px"

    } else {
        tableHeader.style.top = String(originalYPosition) + "px"
        tableHeader.style.left = String(originalXPosition) + "px"
    }
}
*/
