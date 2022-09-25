import { createRouter, createWebHashHistory } from 'vue-router'
import app from './App.vue'
import Test from './components/Test.vue'
import RegistroPersonalSalud from './components/RegistroPersonalSalud.vue'
import RegistroFamiliar from './components/RegistrarFamiliar.vue'
import ConsultarPaciente from './components/ConsultarPaciente.vue'
import RegistrarPaciente from './components/RegistrarPaciente.vue'
import CrearUsuario from './components/CrearUsuario.vue'


const routes = [
  {
    path: '/root',
    name: 'root',
    component: app
  },
  {
    path: '/test',
    name: 'test',
    component: Test
  },
  {
    path: '/rps',
    name: 'RegistroPersonalSalud',
    component: RegistroPersonalSalud
  },
  {
    path: '/rf',
    name: 'RegistroFamiliar',
    component: RegistroFamiliar
  },
  {
    path: '/consPaciente',
    name: 'consPaciente',
    component: ConsultarPaciente
  },
  {
    path: '/rp',
    name: 'RegistrarPaciente',
    component: RegistrarPaciente
  },
  {
    path: '/cu',
    name: 'CrearUsuario',
    component: CrearUsuario
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
