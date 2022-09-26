<template>
    <h1>Registrar Familiar</h1>
    <div class="RegistroFamiliar">
        <div class="container_RegistroFamiliar">
        <form>
            <label>
                ID familiar:
            </label>
            <input type="number" placeholder="Ingrese el ID del familiar" required>
            <br>
            <label>
                Correo Electronico:
            </label>
            <input type="text" placeholder="Correo Electronico">
            <br>     
            <label>
                Parentesco:
            </label>
            <input type="text" placeholder="Parentesco">                 
            <br>               
            <label>
                ID del paciente:
            </label>
            <input type="number" placeholder="Ingrese el ID del paciente" required>         
            <br>   
            <label>
                Nombre de usuario del familiar:
            </label>
            <input type="text" placeholder="Username">            
            <br>                    
            <br>
            <button class="btn-reg">Registrar</button>    
        </form>
    </div>
</div>
</template>
<style>
    .RegistroFamiliar{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .container_RegistroFamiliar{
        border: 3px solid #283747;
        border-radius: 10px;
        width: 25%;
        height: 85%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .RegistroFamiliar h2{
        color: #283747;
    }
    
    .RegistroFamiliar form{
        width: 70%;
    }
    
    .RegistroFamiliar input{
    height: 40px;
    width: 100%;
    box-sizing: border-box;
    padding: 10px 20px;
    margin: 5px0;
    border: 1px solid #283747;
    }
    
    .RegistroFamiliar button{
        width: 100%;
    height: 40px;
    color: #E5E7E9;
    background: #36a9cb;
    border: 1px solid #E5E7E9;
    border-radius: 5px;
    padding: 10px 25px;
    margin: 5px0 25px0;
    }
    
    .RegistroFamiliar button:hover{
        color: #E5E7E9;
    background: #ffab42;
    border: 1px solid #283747;
    }

    .btn-reg{
        margin-top:10px;
        margin-bottom:5px;
    }
    .RegistroFamiliar input{
        margin-top:10px;
        margin-bottom:10px;
    }   
    .RegistroFamiliar form{
        margin-top:10px;
        margin-bottom:10px;
    }     
    </style>