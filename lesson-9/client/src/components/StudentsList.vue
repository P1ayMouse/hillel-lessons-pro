<script >
export default {
  name: "StudentList",
  async mounted() {
    await this.loadStudents('/api/v1/lms/students/')
  },
  data () {
    return {
      studentsLoaded: false,
      search: '',
      currentUrl: '/api/v1/lms/students/',
      count: 0,
      page: 0,
      limit: 15,
      students: []
    }
  },
  methods: {
    async loadStudents(url) {
      this.studentsLoaded = false
      const token = localStorage.getItem('lesson-9-access')

      const response = await fetch(`/api/v1/lms/students/?limit=${this.limit}&offset=${this.page * this.limit}&search=${this.search}`, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      })

      if (response.status === 200) {
        const responseData = await response.json()
        this.students = responseData.results
        this.count = responseData.count
      }
      this.studentsLoaded = true
    }
  }
}
</script>

<template>
  Search: <input v-model="search" @change="loadStudents()"/>
  <div v-if="!studentsLoaded">
    <div class="text-center">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
  <table v-else class="table">
    <thead>
    <tr>
      <th> Name </th>
      <th> Birth Date </th>
      <th> Groups Count </th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="(student, index) in students">
      <td>{{ student.name }}</td>
      <td>{{ student.birth_date }}</td>
      <td>{{ student.groups_count }}</td>
    </tr>
    </tbody>

    <a href="#" @click="page--; loadStudents()" v-if="page !== 0" >&lt;&lt;&lt;prev</a>
    Showing page {{ page + 1 }} from {{ Math.floor(count/limit) + 1 }}
    <a  @click="page++; loadStudents()" v-if="count / limit > page + 1" href="#">next &gt;&gt;&gt;</a>


  </table>
</template>

<style scoped>
</style>
