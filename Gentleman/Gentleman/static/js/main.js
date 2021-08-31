window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    header.classList.toggle('sticky', window.scrollY > 0);
});



var times = document.querySelector('.times');
var bars = document.querySelector('.bars');


bars.addEventListener('click', function(){
    document.querySelector('.navlist').style.display = 'block';
    document.querySelector('.bars').style.display = 'none';
    document.querySelector('.times').style.display = 'block';
});



times.addEventListener('click', function(){
    document.querySelector('.navlist').style.display = 'none';
    document.querySelector('.bars').style.display = 'block';
    document.querySelector('.times').style.display = 'none';
});

