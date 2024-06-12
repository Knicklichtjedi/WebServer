// main.js
import {createApp} from 'vue'
import App from "./App.vue";
import {createBootstrap} from 'bootstrap-vue-next'

// Add the necessary CSS
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'
import './style.css'

const app = createApp(App)
app.use(createBootstrap({components: true, directives: true}))
app.mount('#app')