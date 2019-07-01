<template>
  <v-app>
    <v-content>
			<NavBar/>
      <router-view/>
			<Footer/>
    </v-content>
  </v-app>
</template>

<script>
import store from './store'
import NavBar from './components/NavBar'
import Footer from './components/Footer'

export default {
	name: 'App',
	components: {
		NavBar,
		Footer,
	},
	store,
	data() {
		return {
			//
		}
	}
}
</script>
