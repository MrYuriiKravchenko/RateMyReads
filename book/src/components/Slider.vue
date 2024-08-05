<template>
    <div class="slider-container">
        <div class="slider" :style="{ transform: `translateX(-${currentSlide * 100}%)`}">
            <div class="slide" v-for="(slide, index) in slides" :key="index">
                <img :src="slide.image" :alt="slide.alt">
                <div class="carousel-caption d-none d-md-block">
                    <h5>{{ slide.caption }}</h5>
                </div>
            </div>
        </div>
        <button @click="prevSlide" class="slider-button prev-button">&lt;</button>
        <button @click="nextSlide" class="slider-button next-button">&gt;</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            currentSlide: 0,
            slides: [
                { image: '/images/slide1.jpeg', alt: 'Главная', caption: 'Добро пожаловать в RateMyReads!' },
                { image: '/images/slide2.jpeg', alt: 'Закладки', caption: 'Откройте для себя мир книг! Найдите новые захватывающие истории и делитесь впечатлениями с другими.' },
                { image: '/images/slide3.jpeg', alt: 'Рейтинг', caption: 'Оставляйте свои отзывы и выставляйте оценки.' },
            ]
        };
    },
    methods: {
        nextSlide() {
            this.currentSlide = (this.currentSlide + 1) % this.slides.length;
        },
        prevSlide() {
            this.currentSlide = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
        }
    }
};
</script>

<style scoped>
@import "~bulma/css/bulma.css";

.slider-container {
  position: relative;
  width: 95%; 
  height: 200px; 
  overflow: hidden;
  margin: auto; 
  border: 1px solid #ccc;
  border-radius: 15px;
}

.slider {
  display: flex;
  transition: transform 0.5s ease-in-out;
  height: 100%;
}

.slide {
  min-width: 100%;
  box-sizing: border-box;
  height: 100%;
  position: relative; 
}

.slide img {
  width: 100%;
  height: 100%; 
  object-fit: cover;
  display: block;
  border-radius: 15px; 
}

.carousel-caption {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  background: rgba(0, 0, 0, 0.5);
  padding: 5px;
  border-radius: 5px;
  text-align: center; 
}

.slider-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: 1em;
  cursor: pointer;
  z-index: 1;
}

.prev-button {
  left: 10px;
}

.next-button {
  right: 10px;
}
</style>
