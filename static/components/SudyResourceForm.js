export default {
  template: `<div>
  <input type="text" placeholder="topic" v-model="resource.topic"/>
  <input type="text" placeholder="description" v-model="resource.description" />
  <input type="text" placeholder="Resource Link" v-model="resource.resource_link" />
  <button @click="createResource"> Create Resource</button>
  </div>`,

  data() {
    return {
      resource: {
        topic: null,
        description: null,
        resource_link: null,
      },
      token: localStorage.getItem('auth-token'),
    }
  },

  methods: {
    async createResource() {
      const res = await fetch('/api/study_material', {
        method: 'POST',
        headers: {
          'Authentication-Token': this.token,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.resource),
      })

      const data = await res.json()
      if (res.ok) {
        alert(data.message)
      }
    },
  },
}
