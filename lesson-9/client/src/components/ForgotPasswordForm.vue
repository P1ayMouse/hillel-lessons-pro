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
  <div v-if="formError" className="alert alert-danger" role="alert">
    {{ formError }}
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
</template>

<style scoped>

</style>