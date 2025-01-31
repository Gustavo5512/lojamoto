let index = 0;
const images = document.querySelectorAll('.image-slide');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');

// Exibir a primeira imagem ao carregar a página
images[index].classList.add('active');

function changeImage(direction) {
    images[index].classList.remove('active');
    
    index += direction;
    if (index < 0) {
        index = images.length - 1;
    } else if (index >= images.length) {
        index = 0;
    }

    images[index].classList.add('active');
}

// Eventos de clique para mudar as imagens
prevBtn.addEventListener('click', () => changeImage(-1));
nextBtn.addEventListener('click', () => changeImage(1));
