<template>
<div>
  <div class="login">
    <div class="hero is-link">
      <div class="hero-body has-text-centered">
        <h1 class="title">Регистрация</h1>
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


                    <div class="field">
                        <label>Повторите пароль</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
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
                        <button class='button is-dark'>Регистрация</button>
                      </div>
                    </div>
                </form>


                <hr>

                или <router-link to="/log-in">нажмите сюда</router-link> чтобы войти!

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
      password2: '',
      errors: []
    }
  },
  methods: {
    submitForm() {
      console.log('submitForm')

      this.errors = []

      if (this.username === '') {
        this.errors.push('Имя пользователя отсутствует!')
      }
      if (this.password === '') {
        this.errors.push('Пароль отсутствует!')
      }
      if (this.password !== this.password2) {
        this.errors.push('Пароль не совпадает!')
      }

      if(!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password
        }

        axios
          .post('/api/v1/users/', formData)
          .then(response => {
              this.$router.push('/log-in')
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
