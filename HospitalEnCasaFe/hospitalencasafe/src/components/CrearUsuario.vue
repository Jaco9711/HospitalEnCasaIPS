<template>
    <h1>Crear Usuario</h1>
    <div class="RegistroUsuario">
        <div class="container_RegistroUsuario">
        <form>
            <label>
                Username:
            </label>
            <input type="text" placeholder="Username">
            <br>
            <label>
                Password:
            </label>
            <input type="Password">  
            <br>     
            <label>
                Nombres:
            </label>
            <input type="text" placeholder="Nombres">                 
            <br>               
            <label>
                Apellidos:
            </label>
            <input type="text" placeholder="Apellidos">            
            <br>   
            <label>
                Telefono:
            </label>
            <input type="text" placeholder="Telefono">            
            <br>               
            <label>
                Genero:
            </label>
            <select id="u_genero">
                <option>Masculino</option>
                <option>Femenino</option>
            </select>     
            <br>
            <button>Registrar</button>    
        </form>
    </div>
</div>
</template>
<style>
    .RegistroUsuario{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .container_RegistroUsuario{
        border: 3px solid #283747;
        border-radius: 10px;
        width: 25%;
        height: 85%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .RegistroUsuario h2{
        color: #283747;
    }
    
    .RegistroUsuario form{
        width: 70%;
    }
    
    .RegistroUsuario input{
    height: 40px;
    width: 100%;
    box-sizing: border-box;
    padding: 10px 20px;
    margin: 5px0;
    border: 1px solid #283747;
    }
    
    .RegistroUsuario button{
    width: 100%;
    height: 40px;
    color: #E5E7E9;
    background: #283747;
    border: 1px solid #E5E7E9;
    border-radius: 5px;
    padding: 10px 25px;
    margin: 5px0 25px0;
    }
    
    .RegistroUsuario button:hover{
    color: #E5E7E9;
    background: crimson;
    border: 1px solid #283747;
    }
    </style>