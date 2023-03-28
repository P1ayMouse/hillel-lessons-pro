import { createRouter, createWebHistory } from 'vue-router'
import LoginView from "../views/LoginView.vue";
import StudentView from "../views/StudentView.vue";
import RegisterView from "../views/RegisterView.vue";
import ForgotPasswordView from "../views/ForgotPasswordView.vue";
import MoviesListView from "../views/MoviesListView.vue";
import ProfileView from "../views/ProfileView.vue";
import MovieView from "../views/MovieView.vue";
import PersonView from "../views/PersonView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register/',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/password-forgot/',
      name: 'password-forgot',
      component: ForgotPasswordView
    },
    // {
    //   path: '/lms/list-students/',
    //   name: 'student',
    //   component: StudentView
    // },
    {
      path: '/movies/',
      name: 'movies',
      component: MoviesListView,
      props: true
    },
    {
      path: '/profile/',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/movies/:id',
      name: 'movie',
      component: MovieView,
      props: true
    },
    {
      path: '/person/:id',
      name: 'person',
      component: PersonView,
      props: true
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
