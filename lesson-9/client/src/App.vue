<script setup>
import { RouterLink, RouterView } from 'vue-router'
import UserBadge from "./components/UserBadge.vue";

</script>

<script >

import router from "./router";

export default {
  name: "App",
  data () {
    return {
      search: '',
    }
  },
  methods: {
    onMovieSearch() {
      router.push({name: 'movies-search', params: {search: this.search}})
      this.search = ''
    }
  }
}
</script>

<template>
  <div>
    <div class="row">
  <header>
    <nav class="navbar navbar-expand-lg bg-light text-font">
      <div class="container-fluid">
        <!-- Collapsible wrapper -->
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <a href="/movies/" style="color: black; text-decoration: none; font-size: 24px"> Ithillel IMDB </a>
        </div>
        <!-- Search form -->
        <div class="navbar-collapse" style="align-items: center">
          <form class="input-group w-auto d-flex">
            <input
                class="form-control"
                placeholder="Search"
                type="text"
                v-model="search"
            />

            <button
                class="btn btn-outline-secondary"
                type="submit"
                data-mdb-ripple-color="dark"
                @click="onMovieSearch"
            >
              Submit
            </button>
          </form>
        </div>

        <UserBadge />

      </div>
    </nav>
  </header>
    </div>
  </div>

  <RouterView />
</template>

<style scoped>
.text-font {
  font-family: Comic Sans MS, sans-serif;
}
</style>

