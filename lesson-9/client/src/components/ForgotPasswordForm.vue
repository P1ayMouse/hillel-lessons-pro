<script>
export default {
  name: "ForgotPasswordForm",

  data() {
    return {
      user: {},
      formError: null
    }
  },
  methods: {
    async onUserForgotPassword(e) {
      e.preventDefault();
      this.formError = null;
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
    <div className="d-flex justify-content-center">
      <form @submit="onUserForgotPassword" class="col-2">
        <br>
        <div className="mb-4">
          <label className="form-label">e-mail:</label>
          <input type="email" name="email" className="form-control" v-model="user.email" placeholder="Input your email"/>
        </div>
        <div className="d-flex justify-content-center ">
          <input type="submit" className="btn btn-outline-secondary" value="Send password reset"
                 style="--bs-btn-padding-x: .80rem; --bs-btn-padding-y: .10rem;">
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