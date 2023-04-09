import { createRouter, createWebHistory } from "vue-router"
import LoginView from "../views/LoginView.vue"
import RegisterView from "../views/RegisterView.vue"
import ForgotPasswordView from "../views/ForgotPasswordView.vue"
import MoviesListView from "../views/MoviesListView.vue"
import ProfileView from "../views/ProfileView.vue"
import MovieView from "../views/MovieView.vue"
import PersonView from "../views/PersonView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: "/movies/",
    },
    {
      path: "/login/",
      name: "login",
      component: LoginView,
    },
    {
      path: "/register/",
      name: "register",
      component: RegisterView,
    },
    {
      path: "/password-forgot/",
      name: "password-forgot",
      component: ForgotPasswordView,
    },
    {
      path: "/movies/:search",
      name: "movies-search",
      component: MoviesListView,
      props: true,
    },
    {
      path: "/movies/",
      name: "movies",
      component: MoviesListView,
    },
    {
      path: "/profile/",
      name: "profile",
      component: ProfileView,
    },
    {
      path: "/movies/movie/:id",
      name: "movie",
      component: MovieView,
      props: true,
    },
    {
      path: "/person/:id",
      name: "person",
      component: PersonView,
      props: true,
    },
  ],
})

export default router
