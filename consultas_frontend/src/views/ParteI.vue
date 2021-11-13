<template>
  <div class="container-partI">
    <h1>Parte I</h1>
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
          <th>pageId</th>
          <th>Title</th>
          <th>Snippet</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in data" :key="item">
          <td>{{ item.pageid }}</td>
          <td>{{ item.title }}</td>
          <td>{{ item.snippet }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
export default {
  name: "ParteI",
  data() {
    return {
      querySearch: "",
      data: [],
      dataSearch: {
        search: "",
        amount: 0,
        firstSearch: 0,
        lastSearch: 0,
        numberResults: 0,
      },
    };
  },
  methods: {
    createSearch() {
      var url = "https://en.wikipedia.org/w/api.php";
      var params = {
        action: "query",
        list: "search",
        srsearch: this.querySearch,
        format: "json",
      };
      url = url + "?origin=*&srlimit=max";
      Object.keys(params).forEach(function (key) {
        url += "&" + key + "=" + params[key];
      });
      axios
        .get(url)
        .then((response) => {
          this.dataSearch.search = this.querySearch.toLowerCase();
          this.dataSearch.numberResults = response.data.query.search.length;
          this.dataSearch.lastSearch = moment().unix();
          axios
            .get(
              "http://127.0.0.1:8000/querySearch/" +
                this.querySearch.toLowerCase() +
                "/",
              {
                headers: {},
              }
            )
            .then((res) => {
              let sizeData = Object.keys(res.data).length;
              if (sizeData > 0) {
                console.log("existe");
                return res;
              } else return false;
            })
            .then((response) => {
              if (response) {
                this.dataSearch.firstSearch = response.data.firstSearch;
                this.dataSearch.amount = response.data.amount + 1;
                axios.put(
                  "http://127.0.0.1:8000/querySearch/",
                  this.dataSearch
                );
              } else {
                this.dataSearch.firstSearch = moment().unix();
                this.dataSearch.amount = 1;
                axios.post(
                  "http://127.0.0.1:8000/querySearch/",
                  this.dataSearch,
                  {
                    headers: {},
                  }
                );
              }
            });
          this.data = response.data.query.search;
        })
        .catch((error) => {
          console.log(error);
        });
    },
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
</style>
