import router from './router.js'
import Navbar from './components/Navbar.js'

router.beforeEach((to, from, next) => {
  if (to.name !== 'Login' && !localStorage.getItem('auth-token') ? true : false)
    next({ name: 'Login' })
  else next()
})

new Vue({
  el: '#app',
  template: `<div>
  <Navbar />
  <router-view class="m-3"/></div>`,
  router,
  components: {
    Navbar,
  },
})
