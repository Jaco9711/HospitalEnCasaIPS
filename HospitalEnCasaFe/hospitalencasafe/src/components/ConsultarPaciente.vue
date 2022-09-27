<template>
    <br>
    <div>
        <center><h1>Consula de pacientes</h1></center>
        <br>
    </div>
    <div class="ConsultaPaciente">
        <div class="container_ConsultaPaciente">
            <form id="processConsultaPaciente">
                <br>
                <label id="p_id">Ingrese el ID del paciente:
                <input type="number" placeholder="ID del paciente" required>
                </label>
                <br>
                <br>
                <button>Buscar</button> 
            </form>
        <br>
        </div>
    </div>
    <br>
    <br>
    <div class="Paciente">
        <div>
        <br>
            <table>
                <tr>
                    <td>Username:</td>
                    <td>angietramirezc</td>
                </tr>
                <tr>
                    <td>Médico asignado:</td>
                    <td>15</td>
                </tr>
                <tr>
                    <td>Fecha de nacimiento:</td>
                    <td>22 de mayo de 1994</td>
                </tr>
                <tr>
                    <td>Ciudad de residencia:</td>
                    <td>Chía</td>
                </tr>
                <tr>
                    <td>Dirección:</td>
                    <td>Vereda Fonquetá sector Las Piscinas</td>
                </tr>
                <tr>
                    <td>Coordenadas:</td>
                    <td>Latiud: 4.85
                        <br>
                        Logitud: -74.05
                    </td>
                </tr>
            </table>
        <br>
        </div>
    </div>
</template>

<script>
  export default({
    data : function(){
    },

    methods : {
    },

    created : function(){
    }
  })
</script>

<style>
.ConsultaPaciente{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container_ConsultaPaciente{
    border: 3px solid #283747;
    border-radius: 10px;
    width: 25%;
    height: 85%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.ConsultaPaciente h2{
    color: #283747;
}

.ConsultaPaciente form{
    width: 70%;
}

.ConsultaPaciente input{
height: 40px;
width: 100%;
box-sizing: border-box;
padding: 10px 20px;
margin: 5px0;
border: 1px solid #283747;
}

.ConsultaPaciente button{
    width: 100%;
    height: 40px;
    color: #E5E7E9;
    background: #36a9cb;
    border: 1px solid #E5E7E9;
    border-radius: 5px;
    padding: 10px 25px;
    margin: 5px0 25px0;
}

.ConsultaPaciente button:hover{
    color: #E5E7E9;
    background: #ffab42;
    border: 1px solid #283747;
}
.Paciente{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.Paciente table {
    table-layout: auto;
    width: 100%;
    border-collapse: separate;
    border-radius: 10px;
    text-align: left;
    border:1px solid black;
    background-color: white;
}
.Paciente td{
    padding:5px;
    border-left: solid 1px black;
    border-bottom:solid 1px black;
}
</style>