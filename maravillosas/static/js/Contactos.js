document.addEventListener("DOMContentLoaded", function () {
    // Esperar a que el DOM esté completamente cargado

    // Obtener el formulario de contacto por su ID
    var contactForm = document.getElementById("contactForm");

    // Agregar un evento de escucha para el envío del formulario
    contactForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevenir el envío del formulario

        // Obtener los valores de los campos del formulario
        var nombre = document.getElementById("Nombre y Apellido").value.trim();
        var email = document.getElementById("Correo Electrónico").value.trim();
        var asunto = document.getElementById("Asunto").value.trim();
        var mensaje = document.getElementById("Escribe tu mensaje").value.trim();

        // Validar que los campos no estén vacíos
        if (nombre === "" || email === "" || asunto === "" || mensaje === "") {
            alert("Por favor, complete todos los campos.");
            return false; // Detener el envío del formulario
        }

        // Validar el formato del correo electrónico utilizando una expresión regular
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert("Por favor, ingrese un correo electrónico válido.");
            return false; // Detener el envío del formulario
        }

        // Si todas las validaciones pasan, el formulario se enviará
        alert("Mensaje enviado correctamente.");
        // Aquí podrías enviar el formulario utilizando AJAX o cualquier otra técnica

        // Redireccionar a home.html después de enviar el formulario
        window.location.href = "home.html";
    });
});