<script setup>

    import { ref, onMounted } from "vue";

    let csrf_token = ref("")
    
    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
        })
    }

    onMounted(() => {
        getCsrfToken()
    })

    function saveMovie(){
        let movieForm = document.querySelector("#movieForm")
        let formData = new FormData(movieForm)

        fetch("/api/v1/movies", {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log(data);
        })
        .catch(function (error) {
            console.log(error);
        });
    }

</script>

<template>

    <form @submit.prevent="saveMovie" id="movieForm">
        <div class="form-group mb-3">
            <label for="title" class="form-label">Movie Title</label>
            <input type="text" name="title" class="formcontrol" />
        </div>

        <div class="form-group mb-3">
            <label for="description" class="form-label">Movie Description</label>
            <textarea name="description" class="formcontrol" ></textarea>
        </div>

        <div class="form-group mb-3">
            <label for="poster" class="form-label">Movie Poster</label>
            <input type="file" name="poster" class="formcontrol" accept=".jpg,.png" />
        </div>

        <input type="submit" value="Submit">
    </form>

</template>

<style>

</style>