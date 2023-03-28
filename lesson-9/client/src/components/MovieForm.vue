<script>
import router from "../router";

export default {
  name: 'MovieForm',
  props: ['id'],
  data () {
    return {
      dataLoaded: false,
      fullMovie: {},
      movie: {},
      persons: {}
    }
  },
  async mounted () {
    this.dataLoaded = false
    const urlMovies = `/api/v1/movies/movies/${this.$route.params.id}/`;
    const urlPersonMovie = `/api/v1/movies/personmovies/?search=${this.$route.params.id}`;

    Promise.all([
        fetch (urlMovies). then (response => response. json()),
        fetch(urlPersonMovie). then( response => response. json())
      ]).then(data => {
          this.movie = data[0]

          this.persons = data[1].results

          console.log(this.movie, this.persons)
          this.dataLoaded = true
        })
        .catch(error => {
          console.error(error)
        })
  },
  methods: {
    onPersonPush(person) {
      router.push({name: 'person', params: {id: person.person_id.id}})
    }
  }
};
</script>

<template>
  <div v-if="!dataLoaded">
    <div class="text-center">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
  <div class="text-font m-4" v-if="dataLoaded">
    <div class="d-flex align-items">
      <img src="./icons/none_image.png" class="card-img-top m-3 " style="width:300px;">
      <div class="m-4">
        <h4> {{ movie.name }} </h4>
        <span style="font-size: 12px;" v-if="movie.year !== null"> {{ movie.year.substring(0, 4) }} </span>
        <span style="font-size: 12px;" v-else> No year </span>
        <span v-for="(person, index) in persons">
          <span style="font-size: 12px;" v-if="person.category === 'director'">, {{ person.person_id.name }}</span>
        </span>
        <div class="mt-3">
          <span class="badge rounded-pill text-bg-secondary m-1" v-if="movie.genres !== []" v-for="(genre, index) in movie.genres"> {{ genre }} </span>
        </div>
      </div>
    </div>
    <div style="width: 70%;">
      <table class="table table-striped" v-if="persons.length > 0">
        <thead>
        <tr>
          <th style="width: 45%"> Name </th>
          <th style="width: 5%"> Age </th>
          <th style="width: 35%"> Job </th>
          <th> Roles </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(person, index) in persons" @click="onPersonPush(person)">
          <td style="width: 45%">{{ person.person_id.name }}</td>
          <td style="width: 5%">{{ person.person_id.birth_year ? person.person_id.birth_year.slice(0, 4) : '' }}</td>
          <td style="width: 35%">{{ person.category }}</td>
          <td><span v-for="(character, index) in person.characters">{{ character }}<span v-if="index !== (person.characters.length - 1)">; </span></span></td>
        </tr>
        </tbody>
      </table>
<!--      <div class="d-flex align-items" style="margin-top: 40px;">-->
<!--        <label class="form-label">Name:</label>-->
<!--        <input name="name" class="form-control" placeholder="Input your name"/>-->
<!--        <label class="form-label">Email:</label>-->
<!--        <input name="email" class="form-control" placeholder="Input your email"/>-->
<!--      </div>-->
    </div>
  </div>
</template>

<style scoped>
.text-font {
  text-decoration: none;
  font-family: Comic Sans MS, sans-serif;
}
</style>