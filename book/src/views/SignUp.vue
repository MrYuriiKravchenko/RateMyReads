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
                <form>
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" class="input">
                        </div>
                    </div>

                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" class="input">
                        </div>
                    </div>

                    <div class="field">
                        <label>Повторите пароль</label>
                        <div class="control">
                            <input type="password" class="input">
                        </div>
                    </div>

                    <div class='field'>
                      <div class='control'>
                        <button class='button is-dark'>Регистрация</button>
                      </div>
                    </div>
                </form>

                <hr>

                или <router-link to="/log-in">нажмите сюда</router-link> что бы войти!

            </div>
        </div>
    </div>
  </section>
</div>
</template>
