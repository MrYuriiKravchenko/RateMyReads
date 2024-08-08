<template>
    <div class="courses">
        <div class="hero is-link">
            <div class="hero-body has-text-centered">
                <h1 class="title">Книги</h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-2">
                        <aside class="menu">
                            <p class="menu-label">Жанры</p>

                            <ul class="menu-list">
                                <li><a class="is-active">Все жанры</a></li>
                                <li><a>Фэнтези</a></li>
                                <li><a>Детектив</a></li>
                                <li><a>Боевик</a></li>
                                <li><a>Исторические</a></li>
                            </ul>
                        </aside>
                    </div>

                    <div class="column is-10">
                        <div class="columns is-multiline">
                            <div 
                                class="column is-3"
                                v-for="book in books"
                                v-bind:key="book.id"
                            >
                                <div class="card">
                                    <div class="card-image">
                                        <figure class="image is-2by3">
                                            <img src="https://bulma.io/assets/images/placeholders/1280x960.png" alt="Placeholder image">
                                        </figure>
                                    </div>

                                    <div class="card-content">
                                        <div class="media">
                                            <div class="media-content">
                                                <p class="is-size-5">{{ book.title }}</p>
                                            </div>
                                        </div>

                                            <div class="content">
                                                <p>{{ book.description }}</p>

                                                <router-link :to="{name: 'Book', params: {slug: book.slug}}">More</router-link>
                                        
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="column is-12">
                                <nav class="pagination">
                                    <a class="pagination-previous">Предыдущая</a>
                                    <a class="pagination-next">Следущая</a>

                                    <ul class="pagination-list">
                                        <li>
                                            <a class="pagination-link is-current">1</a>
                                        </li>
                                        <li>
                                            <a class="pagination-link">2</a>
                                        </li>
                                        <li>
                                            <a class="pagination-link">3</a>
                                        </li>
                                    </ul>
                                </nav>
                            </div>
                        </div>
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
        return {
            books: []
        }
    },
    mounted() {
        console.log('mounted')

        axios
            .get('/api/v1/books/')
            .then(response => {
                console.log(response.data)

                this.books = response.data.results
            })
    }
}
</script>