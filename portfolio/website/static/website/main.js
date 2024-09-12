window.onresize = function() {
    if(window.innerWidth < 880){
        let menu = document.getElementById("flexibleNav");
        let butt = document.getElementById("bNav");
        butt.classList.remove("hidden");
        menu.classList.add("collapse", "navbar-collapse");
    }
    else{
        let menu = document.getElementById("flexibleNav");
        let butt = document.getElementById("bNav");
        butt.classList.add("hidden");
        menu.classList.remove("collapse", "navbar-collapse");
    }
};

function foo() {
    document.getElementById("contact").parentElement.classList.toggle("highlighted");
};
    
function meineFunktion() {
    foo();
    setTimeout(foo, 800)
};

/* window.onscroll = function() {
    let trig = document.getElementById("#carouselBar");
    let pic = document.getElementById('#b-img');
    if (trig.scrollIntoView){
        let menu = document.getElementById("#menuHeader");
        menu.setAttribute("background-color", "black !important");
    }
    if(pic.scrollIntoView){
        let menu = document.getElementById("#menuHeader");
        menu.setAttribute("background-color", "white !important");
    }
} */
