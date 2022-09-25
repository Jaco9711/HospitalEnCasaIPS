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
</style>
