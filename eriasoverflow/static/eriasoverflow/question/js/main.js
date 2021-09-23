/* NAV HIDDEN */
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

/* MENU SHOW */
if(navToggle){
    navToggle.addEventListener('click', () =>[
        navMenu.classList.add('show-menu')
    ])
}

/* MENU HIDE */
if(navClose){
    navClose.addEventListener('click', () =>{
        navMenu.classList.remove('show-menu')
    })
}

/* AUTO RESIZE INPUT */
const textarea = document.querySelector('textarea');

textarea.addEventListener("keyup", e =>{
    let scHeight = e.target.scrollHeight;
    textarea.style.height = `${scHeight}px`;
});