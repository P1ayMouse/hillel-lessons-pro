<script >

export default {
  name: "LoginForm",

  data () {
    return {
      user: {
      },
      formError: null
    }
  },
  methods: {
    async onUserLogin(e) {
      e.preventDefault()
      this.formError = null
      const response = await fetch( "/api/v1/auth/token/", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.user),
      })
      console.log(response)

      if (response.status !== 200) {
        try {
          this.formError = (await response.json()).detail
        }
        catch {
          this.formError = 'Unknown error'
        }
      }
      else {
        const response_data = await response.json()
        localStorage.setItem('lesson-9-access', response_data.access)
        localStorage.setItem('lesson-9-refresh', response_data.refresh)
        this.$router.push('/profile')
      }
    }
  }
}
</script>

<template>
  <div class="text-font">
    <div class="error-container d-flex justify-content-center m-4">
      <div v-if="formError" class="alert alert-danger" role="alert" style="color: #a41515;">
        {{ formError }}
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <form @submit="onUserLogin" class="col-2">
        <br>
        <div class="mb-4">
          <label class="form-label">e-mail:</label>
          <input name="email" class="form-control" v-model="user.email" placeholder="Input your email" required />
        </div>
        <div class="mb-4">
          <label class="form-label">password:</label>
          <input type="password" name="password" class="form-control" v-model="user.password" placeholder="Input your password" required />
        </div>
        <div class="d-flex justify-content-center">
          <input type="submit" class="btn btn-outline-secondary" value="Log In"
                 style="--bs-btn-padding-x: .80rem; --bs-btn-padding-y: .10rem;">
        </div>
        <div class="mt-5 d-flex justify-content-between">
            <RouterLink to="/password-forgot/" class="float-start"> forgot password? </RouterLink>
            <RouterLink to="/register/" class="float-end"> register </RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.alert-danger {
  font-size: 1em;
  padding: 0.5em;
  display: inline-block;
  text-transform: capitalize;
}
.text-font {
  text-decoration: none;
  font-family: Comic Sans MS, sans-serif;
  color: black;
}
</style>
