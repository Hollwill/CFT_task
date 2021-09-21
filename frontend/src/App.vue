<template>
  <div id="app">
    <div v-if="!image">
      <h2>Select an image</h2>
      <input type="file"
             @change="onFileChange($event)">
    </div>
    <div v-else>
      <img :src="image" alt="image">
      <h2 v-show="blackOrWhitePixels">more {{ blackOrWhitePixels }} pixel </h2>
      <input v-model="color" class="hex-input" type="text" placeholder="enter hex code">
      <button @click="countPixelsOfColor()">Count</button>
      <br>
      <h3 v-if="countOfPixelsColor === 0 || countOfPixelsColor">{{ countOfPixelsColor }} pixels</h3>
      <h3 v-else></h3>
      <button id="remove-input" @click="removeImage()">Remove image</button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      image: false,
      blackOrWhitePixels: false,
      color: '',
      countOfPixelsColor: false
    }
  },
  watch: {
    image: function (val) {
      if (this.image) {
        this.blackOrWhiteMore()
      }
    }
  },
  methods: {
    onFileChange: function (e) {
      var files = e.target.files || e.dataTransfer.files
      if (!files.length) {
        return
      }
      this.createImage(files[0])
    },
    createImage: function (file) {
      var reader = new FileReader()

      reader.onload = (e) => {
        this.image = e.target.result
      }
      reader.readAsDataURL(file)
    },
    blackOrWhiteMore: function () {
      this.$axios.post('/black_or_white_more', {image: this.image})
        .then((resp) => {
          this.blackOrWhitePixels = resp.data
        })
    },
    countPixelsOfColor: function () {
      this.$axios.post('/count_pixels_of_color', {
        image: this.image,
        color: this.color
      })
        .then((resp) => {
          this.countOfPixelsColor = resp.data
        })
    },
    removeImage: function () {
      this.image = false
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

img {
  width: 30%;
  margin: auto;
  display: block;
  margin-bottom: 10px;
}

#remove-input {
  margin-top: 2em;
}
</style>
