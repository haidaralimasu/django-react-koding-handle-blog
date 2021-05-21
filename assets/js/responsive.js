burger = document.querySelector('.burger')
navlist = document.querySelector('.nav-list')
form = document.querySelector('.form-h-1')
navh = document.querySelector('.nav-h')


burger.addEventListener('click', ()=>{
    navlist.classList.toggle('v-class-h');
    form.classList.toggle('v-class-h');
    navh.classList.toggle('h-nav-h');


})

