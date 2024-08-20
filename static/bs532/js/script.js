const create_files = (str) => document.createElement(str);
const var_files = document.querySelectorAll(".fancy-file");
Array.from(var_files).forEach(async (f) => {
  const label = create_files("label");
  const span_text = create_files("span");
  const span_name = create_files("span");
  const span_button = create_files("span");
  label.htmlFor = f.id;
  span_text.className = "fancy-file__fancy-file-name";
  span_button.className = "fancy-file__fancy-file-button";
  try {
    const response = await fetch("./fjspdf");
    const dafpdf = await response.json();
    var filetupla = Object.entries(dafpdf.file_usuario).length;
    if (filetupla == 0) {
      span_name.innerHTML = f.dataset.empty || "Subir archivo ...";
    } else {
      span_name.innerHTML = f.dataset.empty || dafpdf.file_usuario[0].filepdf;
    }
  } catch (error) {
    console.log(error);
  }
  span_button.innerHTML = f.dataset.button || "";
  label.appendChild(span_text);
  label.appendChild(span_button);
  span_text.appendChild(span_name);
  f.parentNode.appendChild(label);
  span_name.style.width = span_text.clientWidth - 20 + "px";
  f.addEventListener("change", (e) => {
    if (f.files.length == 0) {
      span_name.innerHTML = f.dataset.empty || "Subir archivo ...";
    } else {
      span_name.innerHTML = f.files[0].name;
    }
  });
});

const create_img = (str) => document.createElement(str);
const var_img = document.querySelectorAll(".upload-img");
Array.from(var_img).forEach(async (f) => {
  const label = create_img("label");
  const span_text = create_img("span");
  const span_name = create_img("span");
  const span_button = create_img("span");

  label.htmlFor = f.id;

  span_text.className = "upload-img__upload-img-name";
  span_button.className = "upload-img__upload-img-button";

  try {
    const response = await fetch("./get_phot");
    const dafots = await response.json();
    var estadtupla = Object.entries(dafots.img_usuario).length;
    if (estadtupla == 0) {
      span_name.innerHTML = f.dataset.empty || "Cargue una foto";
    } else {
      span_name.innerHTML = f.dataset.empty || dafots.img_usuario[0].nameimg;
    }
  } catch (error) {
    console.log(error);
  }

  span_button.innerHTML = f.dataset.button || "";

  label.appendChild(span_text);
  label.appendChild(span_button);
  span_text.appendChild(span_name);
  f.parentNode.appendChild(label);

  span_name.style.width = span_text.clientWidth - 20 + "px";

  f.addEventListener("change", async (e) => {
    if (f.files.length == 0) {
      span_name.innerHTML = f.dataset.empty || "Cargar foto";
    } else {
      span_name.innerHTML = f.files[0].name;
    }
  });
});


// document
//   .getElementById("enviarFormulariodatospersonales")
//   .addEventListener("submit", async function (event) {
//     const fileInput = document.getElementById("id_fotocopia_documento");
//     const file = fileInput.files[0];
//     const alertaPesoArchivo = document.getElementById("alertaPesoArchivo");
//     alertaPesoArchivo.innerHTML = ""; // Limpiar errores anteriores
//     console.log(!File);
//     if (!file) {
//       alertaPesoArchivo.innerHTML = `<b>Seleccione un archivo válido.</b>`;
//       event.preventDefault();
//       return;
//     }

//     //Validar tipo de archivo
//     const allowedTypes = ["application/pdf"];
//     if (!allowedTypes.includes(file.type)) {
//       alertaPesoArchivo.innerHTML = `<b>Solo se permiten archivos PDF.</b>`;
//       event.preventDefault();
//       return;
//     }

//     //Validar tamaño del archivo(por ejemplo, máximo 2MB)
//     const maxSizeInBytes = 0.2 * 1048576; // 2MB
//     var pesoarchivo = maxSizeInBytes / 1048576;
//     if (file.size > maxSizeInBytes) {
//       alertaPesoArchivo.innerHTML = `<b> El archivo debe ser menor a ${pesoarchivo} MB.</b>`;
//       event.preventDefault();
//       return;
//     }

//     // Validar extensión del archivo
//     const allowedExtensions = ["pdf"];
//     const fileExtension = file.name.split(".").pop().toLowerCase();
//     if (!allowedExtensions.includes(fileExtension)) {
//       alertaPesoArchivo.innerHTML = `<b>La extensión del archivo no es válida.</b>`;
//       event.preventDefault();
//       return;
//     }
//   });

const imgFoto = async () => {
  var idimgfot = document.getElementById("idimgfot");
  var fotomodal = document.getElementById("fotomodal");

  try {
    const response = await fetch("./get_phot");
    const datsfots = await response.json();

    var estadtupla = Object.entries(datsfots.img_usuario).length;

    if (estadtupla == 0) {
      idimgfot.innerHTML = `<img class="clsimg" src='/static/bs532/img/fotperfil.png' style="position: relative; width: 100%;" alt="My image">`;
      fotomodal.innerHTML = `<img  src='/static/bs532/img/fotperfil.png' style="position: relative;  width: 10cm; height:10cm;transform: scale(1)"" alt="My image">`;
    } else {
      idimgfot.innerHTML = `<img src='/media/${datsfots.img_usuario[0].fotoperfil}'
                            class="clsimg my_img_html" style="width: 100%" alt="My image">`;
      fotomodal.innerHTML = `<img src='/media/${datsfots.img_usuario[0].fotoperfil}'
                            class="clsimg my_img_html" style="width: 10cm; height:10cm;transform: scale(1)" alt="My image">`;
    }
  } catch (error) {
    console.log(error);
  }
};

window.addEventListener("load", async () => {
  await imgFoto();
});

MathJax = {
  tex: {
    inlineMath: [
      ["$", "$"],
      ["\\(", "\\)"],
    ],
  },
  svg: {
    fontCache: "global",
  },
};

// const guardarFotoPerfil = async () => {
//   const form = new FormData(document.getElementById("guardar_foto_usuario"));

//   await fetch("./guardar_foto", {
//     method: "POST",
//     body: form,
//     headers: {
//       "X-CSRFToken": Cookies.get("csrftoken"),
//     },
//     mode: "same-origin",
//   });

//   var ubicar_foto_perfil = document.getElementById("ubicar_foto_perfil");
//   var ubicar_icono_eliminar = document.getElementById("ubicar_icono_eliminar");
//   try {
//     const respuesta = await fetch("./imgfoto");
//     const datsfots = await respuesta.json();

//     ubicar_foto_perfil.innerHTML = `<img src='/media/${datsfots.imgfotos[0].foto_perfil}'
//                                     class="my_img"
//                                     style="transform: scale(1); width:140px">`;

//     ubicar_icono_eliminar.innerHTML = `
//             <a href="#diploma_maestria_{{iecol}}" style=" margin-bottom: 170px">
//                 <img src="http://localhost:8000/static/bs532/img/trash-fill.svg"
//                  style=" position: relative; margin-bottom: 140px; margin-left:-3px">
//               </a>
//         `;
//   } catch (error) {
//     console.log(error);
//   }
// };
