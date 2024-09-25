<script setup lang="ts">
import { ref } from 'vue'
import { Textarea } from '@/components/ui/textarea'
import { Button } from '@/components/ui/button'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle
} from '@/components/ui/dialog'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { ofetch } from 'ofetch'

const unsortedArray = ref('')
const sortedArray = ref('')

const handleSubmit = async () => {
  const array = { array: unsortedArray.value.split(',').map(Number) }
  console.log(array)
  const response = await ofetch('http://127.0.0.1:5000/sort', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(array)
  })
  console.log(response)
  console.log(response.bubble_sort.sorted_array)
  sortedArray.value = response.quick_sort.sorted_array
}

const isDialogOpen = ref(false)
const arrayLength = ref<number>(10)
const lowerBound = ref<number>(0)
const upperBound = ref<number>(100)

const openDialog = () => {
  isDialogOpen.value = true
}

const generateRandomArray = () => {
  const array = Array.from(
    { length: arrayLength.value },
    () => Math.floor(Math.random() * (upperBound.value - lowerBound.value + 1)) + lowerBound.value
  )
  unsortedArray.value = array.join(', ')
  isDialogOpen.value = false
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
      <div class="mt-4">
        <Button @click="openDialog">Generate Random Array</Button>
      </div>

      <Dialog v-model:open="isDialogOpen">
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Generate Random Array</DialogTitle>
            <DialogDescription> Set the parameters for your random array. </DialogDescription>
          </DialogHeader>
          <div class="grid gap-4 py-4">
            <div class="grid grid-cols-4 items-center gap-4">
              <Label for="arrayLength" class="text-right">Array Length</Label>
              <Input id="arrayLength" v-model="arrayLength" type="number" class="col-span-3" />
            </div>
            <div class="grid grid-cols-4 items-center gap-4">
              <Label for="lowerBound" class="text-right">Lower Bound</Label>
              <Input id="lowerBound" v-model="lowerBound" type="number" class="col-span-3" />
            </div>
            <div class="grid grid-cols-4 items-center gap-4">
              <Label for="upperBound" class="text-right">Upper Bound</Label>
              <Input id="upperBound" v-model="upperBound" type="number" class="col-span-3" />
            </div>
          </div>
          <DialogFooter>
            <Button @click="generateRandomArray">Generate</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>

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
