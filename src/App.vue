<script setup lang="ts">
import { ref } from 'vue'
import { Textarea } from '@/components/ui/textarea'
import { Button } from '@/components/ui/button'

const unsortedArray = ref('')
const sortedArray = ref('')

const handleSubmit = () => {
  // Here you would implement the sorting logic and time measurement
  // For now, we'll just split the input and sort it as a placeholder
  const array = unsortedArray.value.split(',').map(Number)
  sortedArray.value = array.sort((a, b) => a - b).join(', ')
}
</script>

<template>
  <div class="bg-gray-300 flex flex-col items-center justify-center h-screen">
    <div class="container mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Array Sorting Visualizer</h1>

      <form @submit.prevent="handleSubmit" class="space-y-4">
        <Textarea
          v-model="unsortedArray"
          placeholder="Enter your unsorted array (comma-separated numbers)"
          class="w-full"
        />
        <Button type="submit">Sort Array</Button>
      </form>

      <div class="mt-8">
        <h2 class="text-xl font-semibold mb-2">Sorting Time Comparison</h2>
        <div class="bg-gray-200 h-64 flex items-center justify-center">
          <p class="text-gray-500">Chart placeholder</p>
        </div>
      </div>

      <div class="mt-8">
        <h2 class="text-xl font-semibold mb-2">Sorted Array</h2>
        <p class="bg-gray-100 p-4 rounded">{{ sortedArray || 'Sorted array will appear here' }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* You can add any additional scoped styles here if needed */
</style>
