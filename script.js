let index = 0;

function changeImage() {
    const images = document.querySelectorAll('.image-slide');
    
    // Esconde todas as imagens
    images.forEach((image) => {
        image.style.display = 'none';
    });

    // Exibe a próxima imagem
    index++;
    if (index >= images.length) {
        index = 0; // Se chegou no final, começa novamente
    }

    images[index].style.display = 'block';  // Exibe a imagem atual
}

// Altera a imagem a cada 3 segundos
window.onload = function() {
    setInterval(changeImage, 3000);
};
