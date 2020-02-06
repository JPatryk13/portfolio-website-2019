/* Open */
function openNav() {
    document.getElementById("myNav").style.height = "100%";
}

/* Close */
function closeNav() {
    document.getElementById("myNav").style.height = "0%";
}

$(window).resize(function() {
    const vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    if (vw > 768) {
        closeNav();
    }
});