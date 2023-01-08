<template>
  <v-app>
    <div style="display: flex">
      <v-row
      >
        <v-col>
          <v-file-input
            label="Upload file"
            accept="text/csv"
            show-size
            counter
            filled
            v-model="selectedFile"
          ></v-file-input>
        </v-col>
        <v-col>
          <v-container>
            <v-btn class="button-toolbar submit" @click="importTokens()" :loading=btnApplyLoading>
              <v-icon style="color: #0066A2"> mdi-cloud-upload</v-icon>
            </v-btn>
          </v-container>
        </v-col>
        <v-col/>
        <v-col/>
      </v-row>
    </div>
    <div class="footer">
      <snack-bar :snackbar="snackbar"></snack-bar>
    </div>
  </v-app>
</template>

<script>
import userMixin from "@/mixins/user-mixins";
import CONSTANTS from "@/constants/constants";

export default {
  name: "ManageAssignRevoke",
  mixins: [userMixin],
  watch: {
    selectedGame() {
      if (!this.selectedGame || this.selectedGame === 'All') {
        this.packagesAutoComplete = []
        this.isPackagesEmpty = true
      } else {
        this.isPackagesEmpty = false
        this.packagesAutoComplete = this.games[this.selectedGame]['packages'].map(el => el)
      }
    }
  },
  data() {
    return {
      options: null,
      btnApplyLoading: false,
      selectedFile : null,
      snackbar: {
        snackbar: false,
        text: '',
        timeout: 1500,
        color: 'success'
      },
    }
  },
  mounted() {
    this.init();
  },
  methods: {
    async init() {
      await this.getGamesAndPackages()
    },
    async getGamesAndPackages() {
      const res = await this.$axios.get('/all-games-packages/')
      this.games = res.data.games
      this.gamesAutoComplete = []
      Object.keys(this.games).forEach((ind, _) => {
        this.gamesAutoComplete.push({'value': ind, 'text': this.games[ind]['game_name']})
      })
    },

    async importTokens() {

      if (!this.selectedFile) {
        this.snackbar = {
          text : 'Select CSV file',
          color : 'red accent-2',
          snackbar :  true
        }
        return
      }

      let formData = new FormData();
      formData.append("importedFile", this.selectedFile);
      try {
        this.btnApplyLoading = true
        const res = await this.$axios.post('export-import/', formData)
        this.snackbar.text = res.data.msg
        this.snackbar.color = 'success'
        this.snackbar.snackbar = true
        this.selectedFile = null
      } catch (e) {
        console.log(e.response)
        this.snackbar.text = e.response['status'] === 401 ? 'Session expired, login again!' : `Request failed ${e.response.data.msg}`
        this.snackbar.color = 'red accent-2'
        this.snackbar.snackbar = true
      } finally {
        this.btnApplyLoading = false
      }
    }
  }
}
</script>

<style scoped>

</style>
