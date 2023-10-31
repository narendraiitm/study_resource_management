import StudentHome from './StudentHome.js'
import InstructorHome from './InstructorHome.js'
import AdminHome from './AdminHome.js'

export default {
  template: `<div>
  <StudentHome v-if="userRole=='stud'"/>
  <AdminHome v-if="userRole=='admin'" />
  <InstructorHome v-if="userRole=='inst'" />
  </div>`,

  data() {
    return {
      userRole: localStorage.getItem('role'),
    }
  },

  components: {
    StudentHome,
    InstructorHome,
    AdminHome,
  },
}
