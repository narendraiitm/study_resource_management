import StudentHome from './StudentHome.js'
import InstructorHome from './InstructorHome.js'
import AdminHome from './AdminHome.js'
import StudyResource from './StudyResource.js'

export default {
  template: `<div>
  <StudentHome v-if="userRole=='stud'"/>
  <AdminHome v-if="userRole=='admin'" />
  <InstructorHome v-if="userRole=='inst'" />
  <StudyResource v-for="(resource, index) in resources" :key='index' :resource = "resource" />
  </div>`,

  data() {
    return {
      userRole: localStorage.getItem('role'),
      authToken: localStorage.getItem('auth-token'),
      resources: [],
    }
  },

  components: {
    StudentHome,
    InstructorHome,
    AdminHome,
    StudyResource,
  },
  async mounted() {
    const res = await fetch('/api/study_material', {
      headers: {
        'Authentication-Token': this.authToken,
      },
    })
    const data = await res.json()
    if (res.ok) {
      this.resources = data
    } else {
      alert(data.message)
    }
  },
}
