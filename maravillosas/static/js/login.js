function validateLoginForm() {
    // Obtener los valores de los campos
    var usuario = document.getElementById("Nombre de usuario").value.trim();
    var contraseña = document.getElementById("Contraseña").value.trim();

    // Validar que los campos no estén vacíos
    if (usuario === "" || contraseña === "") {
        alert("Por favor, complete todos los campos.");
        return;
    }

    // Redireccionar a home.html
    window.location.href = "inicio.html";
    
}

