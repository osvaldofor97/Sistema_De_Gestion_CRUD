document.addEventListener("DOMContentLoaded", init);
const URL_API = 'http://localhost:3000/api/'
let customers = []

function init(){
  search()
}

function agregar(){
  clean();
  abrirFormulario();
}

function abrirFormulario(){
  let htmlModal = document.getElementById("modal");
  htmlModal.setAttribute("class","Modale opened")
}

function cerrarModal(){
  let htmlModal = document.getElementById("modal");
  htmlModal.setAttribute("class","Modale closed")
}

async function search(){
  let url = URL_API + 'customers'
  let response = await fetch(url, {
      "method": 'GET',
      "headers":{
        "Content-Type": 'application/json'
      }
    })
  
  //console.log(response)

  customers = await response.json();
  //console.log(customers)
  let html = ''
  for(datos of customers){

    let row = `<tr>
      <td>${datos.id}</td>
      <td>${datos.firstname}</td>
      <td>${datos.lastname}</td>
      <td>${datos.email}</td>
      <td>${datos.phone}</td>
      <td>
        <a href="#" onclick="edit(${datos.id})" class="btnEditar">Editar</a>
        <a href="#" onclick="remove(${datos.id})" class="btnEliminar">Eliminar</a>
      </td>
    </tr>`
    html = html + row;
  }
    document.querySelector('#customers > tbody').outerHTML = html
}

function edit(id){
  abrirFormulario()
  let customer = customers.find(x => x.id == id)
  document.getElementById('txtId').value = datos.id
  document.getElementById('txtFirstname').value = datos.firstname
  document.getElementById('txtLastname').value = datos.lastname
  document.getElementById('txtPhone').value = datos.phone
  document.getElementById('txtEmail').value = datos.email
}


async function remove(id){
  respuesta = confirm('¿Esta seguro de eliminarlo?');
  if(respuesta){
    let url = URL_API + 'customers/' + id
    let response = await fetch(url, {
      "method": 'DELETE',
      "headers":{
        "Content-Type": 'application/json'
      }
    });

    location.reload();
  }else{
    alert('Operacion cancelada')
  }
}

function clean(){

  document.getElementById('txtId').value = ''
  document.getElementById('txtFirstname').value = ''
  document.getElementById('txtLastname').value = ''
  document.getElementById('txtPhone').value = ''
  document.getElementById('txtEmail').value = ''
  
}

async function save(){
    
    let data = {
      "firstname": document.getElementById('txtFirstname').value,
      "lastname": document.getElementById('txtLastname').value,
      "email": document.getElementById('txtEmail').value,
      "phone": document.getElementById('txtPhone').value
    }

    let id =  document.getElementById('txtId').value
    if(id != ''){
      data.id = id
    }

    let url = URL_API + 'customers'
    let response = await fetch(url, {
      "method": 'POST',
      "body": JSON.stringify(data),
      "headers":{
        "Content-Type": 'application/json'
      }
    });

    location.reload();
}