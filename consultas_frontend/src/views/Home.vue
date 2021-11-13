<template>
  <div class="home">
    <h1>Tu Buscador Latino</h1>
    <div class="buttons">
      <button
        type="button"
        class="btn btn-lg btn-primary"
        @click="$router.push('parteI')"
      >
        Parte I
      </button>
      <button
        type="button"
        class="btn btn-lg btn-primary"
        @click="$router.push('parteII')"
      >
        Parte II
      </button>
    </div>
  </div>
</template>

<script>
export default {};
</script>
<style>
h1 {
  padding: 30px;
  color: black;
  font-size: 45px;
}
.home {
  text-align: center;
}
.buttons {
  position: absolute;
  top: 30%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
}
.btn {
  border-radius: 6px;
  width: 230px;
  height: 80px;
  font-size: 35px;
  margin: 10px;
}

.button-Home:hover {
  background-color: #fef5ed;
}
.btn-primary {
  background-color: #adc2a9 !important;
}
</style>