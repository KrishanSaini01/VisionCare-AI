const input = document.getElementById("image");

const preview = document.getElementById("preview");

input.addEventListener("change", function(){

    const file = this.files[0];

    if(file){

        preview.src = URL.createObjectURL(file);

        preview.style.display = "block";

    }

});