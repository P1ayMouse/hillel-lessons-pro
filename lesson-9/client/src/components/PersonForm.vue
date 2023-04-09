<script>
export default {
  name: 'PersonForm',
  data () {
    return {
      personLoaded: false,
      person: {}
    }
  },
  async mounted () {
    this.personLoaded = false
    const urlPersonMovie = `/api/v1/movies/persons/?search=${this.$route.params.id}`;

    Promise.all([
      fetch(urlPersonMovie). then( response => response. json())
    ]).then(data => {

      this.person = data[0].results[0]

      console.log(this.person)
      this.personLoaded = true
    })
        .catch(error => {
          console.error(error)
        })
  }
};
</script>

<template>
  <div v-if="!personLoaded">
    <div class="text-center">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>

  <div class="text-font m-4" v-if="personLoaded">
    <div class="d-flex align-items">
      <img src="./icons/none_image.png" class="card-img-top m-3 " style="width:300px;">
      <div class="m-4">
        <h4> {{ person.name }} </h4>
        <span style="font-size: 12px;" v-if="person.birth_year"> {{ person.birth_year ? person.birth_year.slice(0, 4) : '' }}  </span>
        <span style="font-size: 12px;" v-if="person.death_year && person.birth_year"> - {{ person.death_year.slice(0, 4) }} </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.text-font {
  text-decoration: none;
  font-family: Comic Sans MS, sans-serif;
}
table {
  width: 70%;
}
</style>