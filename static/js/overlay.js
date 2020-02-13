/* Open */
function openNav() {
    document.getElementById("Overlay").style.height = "100%";
}

/* Close */
function closeNav() {
    document.getElementById("Overlay").style.height = "0%";
}

/* Close when the window is resized */
$(window).resize(function() {
    const vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    if (vw > 768) {
        closeNav();
    }
});