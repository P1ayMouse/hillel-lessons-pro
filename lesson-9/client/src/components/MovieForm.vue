<script>
import router from "../router"
import StarRating from 'vue-star-rating'
export default {
  name: 'MovieForm',
  data () {
    return {
      dataLoaded: false,
      formError: false,
      fullMovie: {},
      movie: {},
      persons: {},
      rating: {},
    }
  },
  async mounted () {
    this.dataLoaded = false
    const urlMovies = `/api/v1/movies/movies/${this.$route.params.id}/`
    const urlPersonMovie = `/api/v1/movies/personmovies/?limit=100&search=${this.$route.params.id}`
    const urlRating = `/api/v1/movies/ratings/?search=${this.$route.params.id}`
    const urlTopThree = `/api/v1/movies/movies/?limit=3&ordering=-rating__average_rating`

    Promise.all([
        fetch (urlMovies).then(response => response.json()),
        fetch(urlPersonMovie).then(response => response.json()),
        fetch(urlRating).then(response => response.json()),
        fetch(urlTopThree).then(response => response.json()),
      ]).then(data => {
          this.movie = data[0]
          this.persons = data[1].results
          this.rating = data[2][0]
          this.topThree = data[3].results

          console.log(this.movie, this.persons, this.rating, this.topThree)

          this.dataLoaded = true
        })
        .catch(error => {
          console.error(error)
        })
  },
  methods: {
    onPersonPush(person) {
      router.push({name: 'person', params: {id: person.person_id.id}})
    },
  },
  components: {
    StarRating
  }
};
</script>

<template>
  <div v-if="!dataLoaded">
    <div class="text-center m-5">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
  <div class="text-font m-4" v-if="dataLoaded">
    <div class="d-flex align-items">
      <div>
        <img src="./icons/none_image.png" class="card-img-top m-3" style="width:300px;">
        <div class="d-flex align-items-center justify-content-center">
          <star-rating :max-rating="10" :star-size="25" :show-rating="false" :rating="rating.average_rating" :increment="0.01" :read-only="true"/>
        </div>
        <p style="text-align: center; font-size: 14px;" class="mt-2" v-if="rating">based on {{ rating.num_votes }} rates</p>
      </div>
      <div class="m-4">
        <h4>{{ movie.name }}</h4>
        <span v-if="movie.year" class="card-text" style="font-size: 12px;">{{ movie.year.substring(0, 4) }}</span>
        <span v-if="movie.year && movie.directors.length !== 0">, </span>
        <span v-for="(director, index) in movie.directors" style="font-size: 12px;" class="card-text">{{director}}{{index === movie.directors.length - 1 ? '' : ', '}}</span>
        <div class="mt-3">
          <span class="badge rounded-pill text-bg-secondary m-1" v-if="movie.genres" v-for="(genre, index) in movie.genres"> {{ genre }} </span>
        </div>
      </div>
    </div>
    <div style="width: 70%;">
      <table class="table table-striped" v-if="persons.length > 0">
        <thead>
        <tr>
          <th style="width: 45%"> Name </th>
          <th style="width: 5%"> Age </th>
          <th style="width: 30%"> Job </th>
          <th> Roles </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(person, index) in persons" @click="onPersonPush(person)">
          <td style="width: 45%">{{ person.person_id.name }}</td>
          <td style="width: 5%">{{ person.person_id.birth_year ? person.person_id.birth_year.slice(0, 4) : '' }}</td>
          <td style="width: 30%">{{ person.category }}</td>
          <td><span v-for="(character, index) in person.characters">{{ character }}<span v-if="index !== (person.characters.length - 1)">; </span></span></td>
        </tr>
        </tbody>
      </table>
    </div>
    <div class="rating-card">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Top rated Like This</h5>
          <div class="card-group row row-cols-1 g-3">
            <div v-for="(movie, index) in topThree">
              <div class="card h-10">
                <div class="card-body">
                  <img src="./icons/none_image.png" class="card-img-top mb-2" style="width: 200px;" :alt="movie.name">
                  <div class="ms-2">
                    <p class="card-title mb-0" style="font-weight: bold; font-size: 18px;">{{ movie.name }}</p>
                    <div class="card-text mt-1" style="font-size: 12px">
                      <span v-if="movie.year" class="">{{ movie.year.substring(0, 4) }}</span>
                      <span v-if="movie.year && movie.directors.length !== 0">, </span>
                      <span v-for="(director, index) in movie.directors">{{director}}{{index === movie.directors.length - 1 ? '' : ', '}}</span>
                    </div>
                  </div>
                  <div>
                    <span class="badge rounded-pill text-bg-secondary mt-2 m-1" v-for="(genre, index) in movie.genres"> {{ genre }} </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.text-font {
  text-decoration: none;
  font-family: Comic Sans MS, sans-serif;
}
.rating-card {
  display: flex;
  align-items: center;
  position: absolute;
  top: auto;
  right: 0;
  bottom: 0;
  margin-right: 1rem;
  width: 270px;
}
</style>