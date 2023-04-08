<script setup>

    import { ref, onMounted } from "vue";

    let movies = ref([])

    function fetchMovies(){
        fetch("/api/v1/movies")
        .then(response => {
            if(response.ok){return response.json()}
            else{return Promise.reject('Something was wrong with fetch request!')}
        })
        .then(data => {
            console.log(data);
            movies.value = data["movies"]
        })
        .catch(error => {
            console.log(error);
        })
    }

    onMounted(() => {
        fetchMovies()
    })

</script>

<template>

    
    <div class="mt-5 container">
        <h1>Movies</h1>
        
        <div class="movies">
            <div v-for="movie in movies" class="movie">
                <div class="imgBox">
                    <img :src="movie.poster" :alt="movie.title">
                </div>
                <div class="details">
                    <h2>{{ movie.title }}</h2>
                    <p>{{ movie.description }}</p>
                </div>
            </div>
        </div>
        
    </div>
    

</template>

<style>
    .movies{
        display: flex;
        flex-wrap: wrap;
    }
    .movie{
        max-width: 550px;
        height: 250px;
        width: 100%;
        overflow: hidden;

        display: grid;
        grid-template-columns: 1fr 2fr;

        margin: 20px;
        border-radius: 5px;
        box-shadow: 0 0 5px rgb(209, 209, 209);
    }
    .movie img{
        width: 100%;
        height: 250px;
        object-fit: contain;
    }
    .details{
        padding: 15px;
    }
</style>