<script setup>

    function saveMovie(){
        let movieForm = document.querySelector("form")
        let formData = new formData(movieForm)

        fetch("/api/v1/movies", {
            method: 'POST',
            body: formData
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // display a success message ///////////////////////////////////
            console.log(data);
        })
        .catch(function (error) {
            console.log(error);
        });
    }

</script>

<template>

    <form @submit.prevent="saveMovie">
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
    </form>

</template>

<style>

</style>