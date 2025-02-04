<template>
    <h1>{{ greeting }}</h1>
    <p>Welcome to your Vue 3 application!</p>
</template>

<script setup>
import { ref } from 'vue'

const greeting = ref('Hello, Vue 3!')
</script>

<style scoped>
</style>