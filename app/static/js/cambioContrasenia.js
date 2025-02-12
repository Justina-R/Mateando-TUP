document.addEventListener("DOMContentLoaded", () => {
    const formulario = document.getElementById("change-password-form");
    formulario.addEventListener("submit", validaContrasenia);
});

const validaContrasenia = async (e) => {
    e.preventDefault();

    const currentPassword = document.getElementById("currentPassword").value;
    const newPassword = document.getElementById("newPassword").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    if(verficaContrasenia(newPassword, confirmPassword)) {
        const passwordValida = await verificaContraseniaOriginal(currentPassword);
        if (passwordValida) {
            Swal.fire({
                icon: "success",
                title: "¡Listo!",
                text: "Contraseña Modificada con Éxito.",
                confirmButtonText: "Ok",
            }).then((result) => {
                if (result.isConfirmed) {
                    e.target.submit();
                }
            });
        }
    }
};

const verficaContrasenia = (newPassword, confirmPassword) => {
    if (newPassword == confirmPassword) {
        ocultarError("Password");
        return true;
    } else {
        mensajeError("Password", "Ingresa la misma contraseña en ambos campos.");
        return false;
    }
};

const verificaContraseniaOriginal = async (newPassword) => {
    try {
        console.log(newPassword);
        const response = await fetch('/verifyPassword', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ newPassword })
        });

        const data = await response.json();
        // retorna 'true' si ya existe
        if(data.contraseniaCorrecta){
            ocultarError("Password");
            return data.contraseniaCorrecta;
        }else {
            mensajeError("Password", "La contraseña actual es incorrecta.");
            return data.contraseniaCorrecta;
        }
    } catch (error) {
        console.error('Error al verificar la contraseña: ', error);
        return false;
    }
}



/* Mensaje de error: */
function mensajeError(id, msj) {
    const elemento = document.getElementById(`error${id}`);

    elemento.textContent = msj;
}

function ocultarError(id) {
    const elemento = document.getElementById(`error${id}`);
    elemento.textContent = "";
}