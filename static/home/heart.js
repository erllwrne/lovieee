(function(){
  const container = document.getElementById('hearts-container');
  if(!container) return;

  const hearts = ['❤','💖','💕','💘','💓'];

  function rand(min, max){ return Math.random() * (max - min) + min; }

  function spawnHeart(){
    const span = document.createElement('span');
    span.className = 'heart';
    span.innerText = hearts[Math.floor(Math.random()*hearts.length)];
    span.style.left = (rand(2, 92)) + '%';
    span.style.fontSize = (rand(14, 48)) + 'px';
    span.style.opacity = rand(0.7, 1).toString();
    span.style.top = (window.innerHeight + 20) + 'px';
    container.appendChild(span);
    setTimeout(()=> {
      span.style.transform = `translateY(-${window.innerHeight + 300}px)`;
      span.style.opacity = '0';
    }, 20);
    setTimeout(()=> {
      if(span.parentNode) span.parentNode.removeChild(span);
    }, 7000);
  }

  setInterval(spawnHeart, 700);
  for(let i=0;i<6;i++){ setTimeout(spawnHeart, 200*i); }
})();
