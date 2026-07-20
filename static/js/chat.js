const suggestions = document.querySelectorAll(".suggestion");

const input = document.getElementById("question");

suggestions.forEach(button => {

    button.addEventListener("click", () => {

        input.value = button.innerText;

        input.focus();

    });

});