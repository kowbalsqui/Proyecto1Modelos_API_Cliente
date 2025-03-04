function consultaCorsApi(token) {
    console.log("Ejecutando petición CORS con token:", token);
    
    fetch("http://127.0.0.1:8092/api/v1/usuarios/me/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log("Datos recibidos:", data);
        // Actualiza el contenido del contenedor en la página
        let resultadoDiv = document.getElementById("resultadoUser");
        resultadoDiv.innerHTML = `
            <h3>Datos del Usuario</h3>
            <p><strong>ID:</strong> ${data.id}</p>
            <p><strong>Nombre:</strong> ${data.nombre}</p>
            <p><strong>Email:</strong> ${data.email}</p>
            <p><strong>Fecha de Registro:</strong> ${data.fecha_Registro ? data.fecha_Registro : "No asignada"}</p>
            <p><strong>Puntuación:</strong> ${data.puntuacion}</p>
            <p><strong>Activo:</strong> ${data.es_activo}</p>
        `;
    })
    .catch(error => {
        console.error("Error en la petición:", error);
        document.getElementById("resultadoUser").innerHTML = `<p class="text-danger">Error: ${error}</p>`;
    });
}
