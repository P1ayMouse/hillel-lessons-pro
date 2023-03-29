<script>
export default {
  name: "RegisterForm",

  data () {
    return {
      user: {
      },
      formError: null
    }
  },
  methods: {
    async onUserRegister(e) {
      e.preventDefault();
      this.formError = null
      const response = await fetch( "/api/v1/auth/user-registration/", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.user),
      })
      console.log(response)

      const responseData = await response.json();

      if (response.status === 200) {
        this.$router.push("/login");
      }
      else {
        switch (response.status) {
          case 400:
            if (responseData.detail !== undefined)
            {
              this.formError = responseData.detail;
            }
            else if (responseData.email !== undefined)
            {
              this.formError = responseData.email[0];
            }
            else if (responseData.username !== undefined)
            {
              this.formError = responseData.username[0];
            }
            else
            {
              this.formError = "Unknown error";
            }
            break;
          default:
            this.formError = "Unknown error";
            break;
        }
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
      <form @submit="onUserRegister" class="col-2">
        <br>
        <div class="mb-4">
          <label class="form-label">e-mail:</label>
          <input type="email" name="email" class="form-control" v-model="user.email" placeholder="Input your email" required/>
        </div>
        <div class="mb-4">
          <label class="form-label">password:</label>
          <input type="password" name="password" class="form-control" v-model="user.password" placeholder="Input your password" required/>
        </div>
        <div class="mb-4">
          <label class="form-label">repeat password:</label>
          <input type="password" name="password2" class="form-control" v-model="user.password2" placeholder="Repeat password" required/>
        </div>
        <div class="mb-4">
          <label class="form-label">username:</label>
          <input name="username" class="form-control" v-model="user.username" placeholder="Input your username" required/>
        </div>
        <div class="d-flex justify-content-center ">
          <input type="submit" class="btn btn-outline-secondary" value="Register"
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
}
.alert-danger:first-letter {
  text-transform: uppercase;
}
.text-font {
  text-decoration: none;
  font-family: Comic Sans MS, sans-serif;
  color: black;
}
</style>