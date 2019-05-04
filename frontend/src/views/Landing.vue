<template>
	<el-container>
		<el-header>
			<h1>Sere mě to</h1>
			{{ user.login }}
		</el-header>

		<el-main>
			<el-autocomplete
				class="inline-input"
				v-model="searchInput"
				:fetch-suggestions="querySearch"
				placeholder="What city sere you?"
				:trigger-on-focus="false"
				@select="selectCity"
				@keyup.enter="selectCity"
			></el-autocomplete>
		</el-main>

		<el-footer>HackPrague 2019, created 28. 4. 2019</el-footer>
	</el-container>
</template>

<script>
export default {
	name: 'home',
	components: {},
	props: {
		city: {
			type: String,
			required: false
		}
	},
	data() {
		return {
			cities: [],
			searchInput: ''
		}
	},
	created() {
		this.$store.dispatch('fetchUser', 1)
	},
	computed: {
		user() {
			return this.$store.getters['getUser']
		}
	},
	methods: {
		querySearch(queryString, cb) {
			var vals = this.cities
			var results = queryString
				? vals.filter(this.createFilter(queryString))
				: vals
			// call callback function to return suggestions
			cb(results)
		},
		createFilter(queryString) {
			return v => {
				return v.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
			}
		},
		loadAll() {
			return [{ value: 'Brno', id: '1' }, { value: 'Praha', id: '2' }]
		},
		selectCity(e) {
			this.$store.dispatch('selectCity', { cityId: e.id, cityName: e.value })
			this.$router.push({
				name: 'home',
				params: { city: e.value.toLowerCase() }
			})
		}
	},
	mounted() {
		this.cities = this.loadAll()
	}
}
</script>
