<template>
  <div class="container-partI">
    <h1>Parte II</h1>
    <input type="text" v-model="querySearch" />
    <button
      type="button"
      class="btn2 btn-dark btn-sm btn-space"
      @click="createSearch"
    >
      Buscar
    </button>
    <table id="itemsData" class="table btn-space">
      <thead>
        <tr id="headTable">
          <th>Search</th>
          <th>firstSearch</th>
          <th>amount</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in data" :key="item">
          <td>{{ item.search }}</td>
          <td>{{ new Date(item.firstSearch * 1000) }}</td>
          <td>{{ item.amount }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import pdf from "vue-pdf";
export default {
  name: "ParteI",
  components: {
    pdf,
  },
  data() {
    return {
      querySearch: "",
      data: [],
    };
  },
  methods: {
    createSearch() {
      let word = this.querySearch.toLowerCase();
      axios
        .get("http://127.0.0.1:8000/querySearch/" + word + "/", {
          headers: {},
        })
        .then((res) => {
          let sizeData = Object.keys(res.data).length;
          if (sizeData > 0) {
            console.log("existe");
            return res;
          } else return false;
        })
        .then((response) => {
          if (response) {
            window.location.replace(
              "http://127.0.0.1:8000/querySearch/document/" + word + "/"
            );
          } else {
            alert("No existe esa busqueda");
          }
        });
    },
  },
  mounted() {
    var url = "http://127.0.0.1:8000/querySearch/";
    axios
      .get(url)
      .then((response) => {
        this.data = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style>
h1 {
  padding: 30px;
  color: black;
  font-size: 45px;
}
.container-partI {
  text-align: center;
}
table {
  border-collapse: collapse;
  width: 100%;
}
table,
th,
td {
  border: 1px solid black;
}

#itemsData tr:nth-child(even) {
  background-color: #f2f2f2;
}
#headTable {
  background-color: #99a799;
}
#itemsData tr:hover {
  background-color: #d3e4cd;
}
.btn-space {
  margin-top: 20px;
}
.btn-space {
  margin-left: 20px;
}
</style>
