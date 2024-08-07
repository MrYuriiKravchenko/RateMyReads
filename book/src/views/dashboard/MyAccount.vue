<template>
  <div class="about">
    <div class="hero is-link">
      <div class="hero-body has-text-centered">
        <h1 class="title">Мой аккаунт</h1>
      </div>
    </div>

    <section class="section">
      <button @click="logout()" class="button is-danger">Выйти</button>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    methods: {
        logout() {
            console.log('logout')

            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}
</script>