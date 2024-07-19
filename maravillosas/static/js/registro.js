function validateForm() {
    // Obtener los valores de los campos
    var nombre = document.getElementById("Nombre completo").value.trim();
    var usuario = document.getElementById("Nombre de usuario").value.trim();
    var email = document.getElementById("correo electronico").value.trim();
    var numero = document.getElementById("numero de telefono").value.trim();
    var contraseña = document.getElementById("contraseña").value.trim();

    // Validar que los campos no estén vacíos
    if (nombre === ""|| usuario === "" || email === "" ||numero === ""|| contraseña === "") {
        alert("Por favor, complete todos los campos.");
        return;
    }

    // Validar el formato del correo electrónico utilizando una expresión regular
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Por favor, ingrese un correo electrónico válido.");
        return;
    }

    // Redirigir a home.html
    window.location.href = "inicio.html";
    alert("Cuenta creada exitosamente.")
}
