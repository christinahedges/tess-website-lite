document.getElementById('imageSelector').addEventListener('change', function() {
    var selectedImage1 = document.getElementById('selectedImage1');
    var selectedImage2 = document.getElementById('selectedImage2');
    var selectedValue = this.value;

    if (selectedValue) {
        var images = selectedValue.split(',');
        selectedImage1.src = 'images/' + images[0];
        selectedImage2.src = 'images/' + images[1];
        selectedImage1.style.display = 'block';
        selectedImage2.style.display = 'block';
    } else {
        selectedImage1.style.display = 'none';
        selectedImage2.style.display = 'none';
    }
});