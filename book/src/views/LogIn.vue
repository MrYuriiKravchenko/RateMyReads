<template>
<div>
  <div class="signup">
    <div class="hero is-link">
      <div class="hero-body has-text-centered">
        <h1 class="title">Вход</h1>
      </div>
    </div>
  </div>

  <section class="section">
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <form v-on:submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                      <p
                          v-for="error in errors"
                          v-bind:key="error"
                      >
                          {{ error }}
                      </p>
                    </div>

                    <div class='field'>
                      <div class='control'>
                        <button class='button is-dark'>Вход</button>
                      </div>
                    </div>
                </form>

                <hr>

                или <router-link to="/sign-up">нажмите сюда</router-link> что бы зарегистрироваться!

            </div>
        </div>
    </div>
  </section>
</div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return{
      username: '',
      password: '',
      errors: []
    }
  },
  methods: {
    submitForm() {
      console.log('submitForm')

      axios.defaults.headers.common['Authorization'] = ''

      localStorage.removeItem('token')

      this.errors = []

      if (this.username === '') {
        this.errors.push('Имя пользователя отсутствует!')
      }
      if (this.password === '') {
        this.errors.push('Пароль отсутствует!')
      }

      if(!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password
        }

        axios
          .post('/api/v1/token/login/', formData)
          .then(response => {
            const token = response.data.auth_token

            this.$store.commit('setToken', token)

            axios.defaults.headers.common['Authorization'] = 'Token ' + token

            localStorage.setItem('token', token)

            this.$router.push('/dashboard/my-account/')
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }

              console.log(JSON.stringify(error.response.data))
            } else if (error.message) {
              this.errors.push('Что-то пошло не так. Пожалуйста, попробуйте еще раз')

              console.log(JSON.stringify(error))
            }
          })
      }
    }
  }
}
</script>
