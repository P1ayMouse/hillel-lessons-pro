<script>
export default {
  name: "ProfileForm",

  data() {
    return {
      user: {
      },
      userLoaded: false,
      formError: null,
    }
  },
  async mounted() {
    const token = localStorage.getItem('lesson-9-access')
    let user = null

    const response = await fetch('/api/v1/auth/user-info/', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    })

    if (response.status === 200) {
      user = await response.json()
    }
    else if (response.status === 403) {
      // try to renew token
      const newTokenResponse = await fetch('/api/v1/auth/refresh/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({'refresh': localStorage.getItem('lesson-9-refresh')})
          }
      )
    }
    else {
      user = {email: 'Error'}
    }

    this.user = user
    this.userLoaded = true
  },
  methods: {
    async onUserEditProfile(e) {
      e.preventDefault();
      this.formError = null;
    },
  }
}

</script>
<template>
  <div v-if="formError" className="alert alert-danger" role="alert">
    {{ formError }}
  </div>
  <div className="d-flex justify-content-center m-5" v-if="userLoaded">
    <form @submit="onUserEditProfile" class="col-2">
      <br>
      <div className="mb-4">
        <label className="form-label">e-mail:</label>
        <input type="email" name="email" className="form-control" v-model="user.email" readonly="readonly" placeholder="Input your first email"/>
      </div>
      <div className="mb-4">
        <label className="form-label">username:</label>
        <input name="username" className="form-control" v-model="user.username"
               placeholder="Input your first username"/>
      </div>
      <div className="mb-4">
        <label className="form-label">password:</label>
        <input type="password" name="password" className="form-control" v-model="user.password"
               placeholder="Input your password"/>
      </div>
      <div className="mb-4">
        <label className="form-label">repeat password:</label>
        <input type="password" name="password2" className="form-control" v-model="user.password2"
               placeholder="Repeat your password"/>
      </div>
      <div className="d-flex justify-content-center ">
        <input type="submit" class="btn btn-outline-secondary m-4" value="Update"
               style="--bs-btn-padding-x: .80rem; --bs-btn-padding-y: .10rem;">
      </div>
    </form>
  </div>
</template>

<style scoped>

</style>