const cards = document.querySelectorAll(".card");

cards.forEach(card=>{
    card.addEventListener("mouseenter",()=>{
        card.style.transform="scale(1.1)";
        card.style.transition="0.3s";
    });

    card.addEventListener("mouseleave",()=>{
        card.style.transform="scale(1)";
    });
});

window.addEventListener("scroll",()=>{
    document.querySelectorAll("section").forEach(sec=>{
        let top = window.scrollY;
        if(top > sec.offsetTop - 500){
            sec.style.opacity = "1";
            sec.style.transform = "translateY(0)";
        }
    });
});