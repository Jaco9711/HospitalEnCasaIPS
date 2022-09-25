<template>
    <h1>Crear Usuario</h1>
    <div>
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
</template>