<script >

export default {
  name: "MoviesListForm",
  data () {
    return {
      moviesLoaded: false,
      currentUrl: '/api/v1/movies/movies/',
      count: 0,
      page: 0,
      limit: 18,
      movies: [],
      search: ''
    }
  },
  async mounted() {
    this.page = 1;
    await this.loadMovies('/api/v1/movies/movies/');
  },
  methods: {
    async loadMovies(url) {
      this.moviesLoaded = false

      const response_movies = await fetch(`/api/v1/movies/movies/?limit=${this.limit}&offset=${(this.page-1) * this.limit}&search=${this.search}`, {
        headers: {
          'Content-Type': 'application/json'
        }
      })

      if (response_movies.status === 200) {
        const response_movies_Data = await response_movies.json()
        this.movies = response_movies_Data.results
        this.count = response_movies_Data.count
      }

      this.moviesLoaded = true
    }
  },
  computed: {
    totalPages() {
      return Math.ceil(this.count / this.limit);
    }
  },

}
</script>

<template>
  <br>
<!--  <div v-if="!moviesLoaded">-->
<!--    <div class="text-center">-->
<!--      <div class="spinner-border" role="status">-->
<!--        <span class="visually-hidden">Loading...</span>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
  <div>
    <div class="row row-cols-1 row-cols-md-6 g-4 mx-1">
      <div v-for="(movie, index) in movies">
        <div class="card">
          <router-link :to="{name: 'movie', params: {id: movie.id}}" style="text-decoration: none; color: black">
          <div class="card-body text-font" style="line-height: 0.5;">
            <img src="./icons/none_image.png" class="card-img-top mb-2" :alt="`${ movie.name }`">
            <h5 class="card-title" style="font-weight: bold; font-size: 18px;">{{ movie.name }}</h5>
            <h6 v-if="movie.year !== null" class="card-text" style="font-size: 12px;"> {{ movie.year.substring(0, 4) }}, </h6>
            <p v-else class="card-text" style="font-size: 12px;"> None year </p>
            <div class="">
              <span class="badge rounded-pill text-bg-secondary m-1" v-if="movie.genres !== []" v-for="(genre, index) in movie.genres"> {{ genre }} </span>
            </div>
          </div>
          </router-link>
        </div>
      </div>
    </div>

    <br><br>
    <nav aria-label="Page navigation">
      <div class="d-flex justify-content-center">
        <ul class="pagination">
          <li class="page-item" :class="{disabled: page === 1}">
            <a class="page-link" href="#" aria-label="Previous" @click="page--; loadMovies()">
              <span aria-hidden="true"> &laquo; </span>
            </a>
          </li>
          <li v-for="pageNum in totalPages" class="page-item" :class="{active: page === pageNum}">
            <a class="page-link" href="#" @click="page = pageNum; loadMovies()" v-if="pageNum === 1 || pageNum === totalPages || (pageNum >= page - 1 && pageNum <= page + 1)">{{ pageNum }}</a>
            <span class="page-link" v-else-if="pageNum === page - 2 || pageNum === page + 2">...</span>
          </li>
          <li class="page-item" :class="{disabled: page === totalPages}">
            <a class="page-link" href="#" aria-label="Next" @click="page++; loadMovies()">
              <span aria-hidden="true"> &raquo; </span>
            </a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<style scoped>
.text-font {
  text-decoration: none;
  font-family: Comic Sans MS, sans-serif;
}
</style>

