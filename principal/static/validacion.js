


$(document).ready(function(){
    $('#signupForm').validate({
       rules: {
          rut: {
             required: true,
             minlength: 9
          },
          nombrep: {
             required: true,
             minlength: 5
          },
          comments: {
             required: true
          },
          password: {
             required: true,
             minlength: 5
          },
          email: {
             required: true,
             email: true
          },
          edad: {
            required: true,
            minlength: 1
         },
         comments: {
            required: true
         },
          agree: "required"
       },
       messages: {  
          rut: {
             required: "Por favor ingresa tu rut",
             minlength: "ingresa un rut valido"
          },         
          nombrep: {
             required: "Por favor ingresa tu nombre completo",
             minlength: "Tu nombre debe ser de no menos de 5 caracteres"
          },
          comments: "Por favor ingresa un comentario",
          password: {
             required: "Por favor ingresa una contraseña",
             minlength: "Tu contraseña debe ser de no menos de 5 caracteres de longitud"
          },
          edad: {
            required: "Por favor ingresa tu edad",
            minlength: "Tu edad debe ser de no menos de 1 caracter"
         },
          email: "Por favor ingresa un correo válido"
       }
       
    });
 });

 