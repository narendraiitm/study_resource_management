import Home from './components/Home.js'
import Login from './components/Login.js'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login', component: Login, name: 'Login' },
]

export default new VueRouter({
  routes,
})
