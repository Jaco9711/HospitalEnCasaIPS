<template>
  <nav>
    <router-link to="/cu">Crear Usuario</router-link>|
    <router-link to="/rps">Registrar PersonalSalud</router-link>|
    <router-link to="/rp">Registrar Paciente</router-link>|
    <router-link to="/rf">Registrar Familiar</router-link>|    
    <router-link to="/consPaciente">Consultar Paciente</router-link>    
  </nav>
  <router-view/>

</template>

<style>
body{
    background-color: #7e7e7e21;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
/*.container_RegistroPersonalSalud{
        border: 3px solid #283747;
        border-radius: 10px;
        width: 25%;
        height: 85%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 9px 7px 28px 12px rgba(0,0,0,0.42);
    }*/
</style>