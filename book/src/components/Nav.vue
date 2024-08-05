<template>
    <nav class="navbar is-link" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
        <div class="navbar-brand">
            <a class="navbar-item is-size-4" href="/">RateMyReads</a>
        </div>

        <div id="navbar-menu" class="navbar-menu">
            <div class="navbar-start">
                <a href='/' class="navbar-item">Домашняя</a>
                <a href='/about' class="navbar-item">О нас</a>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <a href="/sign-up" class="button is-primary"><strong>Регистрация</strong></a>
                        <a href="/log-in" class="button is-light">Войти</a>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>