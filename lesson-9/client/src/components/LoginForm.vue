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
      e.preventDefault();
      this.formError = null;
      const response = await fetch( "/api/v1/auth/token/", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.user),
      })
      console.log(response)

      if (response.status !== 200) {
        this.formError = 'Unable to login'
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
      }
    }
  }
}
</script>

<template>
  <form @submit="onUserLogin">
    Email: <input name="email" v-model="user.email"/>
    Password: <input type="password" name="password" v-model="user.password"/>

    {{ formError }}

    <input type="submit">
  </form>
</template>

<style scoped>
</style>
