<style scoped>
    a {
        text-decoration: none;
        color: rgba(0, 0, 0, 0.87);
    }
</style>

<template>
  <v-toolbar app>
    <v-toolbar-side-icon @click="moveToHome"></v-toolbar-side-icon>
    <v-toolbar-title>이맥의 개발 히스토리</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat><router-link to="/post">Post</router-link></v-btn>
      <v-btn flat><router-link to="/portfolio">Portfolio</router-link></v-btn>
      <v-btn flat><router-link to="/login">Sign in</router-link></v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
// import VueRouter from 'vue-router'

export default {
	name: 'NavBar',
	props: {
	},
	data() {
		return {
			//
		}
    },
    methods: {
        scrollToTop: function() {
            window.scrollTo(0,0);
        },
        moveToHome: function() {
            this.$router.push("/");
            this.scrollToTop();
        }
    }
}
</script>

