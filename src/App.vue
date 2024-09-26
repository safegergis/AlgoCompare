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
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import TimeChart from '@/components/TimeChart.vue'

const unsortedArray = ref('')
const sortedArrayBubble = ref('')
const sortedArrayMerge = ref('')
const sortedArrayQuick = ref('')
const sortedArrayRadix = ref('')

const timeTaken = ref<number[]>([])

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
  if (response) {
    sortedArrayBubble.value = response.bubble_sort.sorted_array.join(', ')
    sortedArrayMerge.value = response.merge_sort.sorted_array.join(', ')
    sortedArrayQuick.value = response.quick_sort.sorted_array.join(', ')
    sortedArrayRadix.value = response.radix_sort.sorted_array.join(', ')

    timeTaken.value = [
      response.bubble_sort.time_taken,
      response.merge_sort.time_taken,
      response.quick_sort.time_taken,
      response.radix_sort.time_taken
    ]
  }
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

const clearArray = () => {
  unsortedArray.value = ''
  sortedArrayBubble.value = ''
  sortedArrayMerge.value = ''
  sortedArrayQuick.value = ''
  sortedArrayRadix.value = ''
  timeTaken.value = []
}
</script>

<template>
  <div class="bg-gray-300 flex flex-col items-center justify-center h-screen">
    <div class="container mx-auto p-4">
      <Card>
        <CardHeader>
          <CardTitle>Array Sorting Visualizer</CardTitle>
        </CardHeader>
        <CardContent>
          <form @submit.prevent="handleSubmit" class="space-y-4">
            <Textarea
              v-model="unsortedArray"
              placeholder="Enter your unsorted array (comma-separated numbers)"
              class="w-full"
            />
            <Button type="submit">Sort Array</Button>
          </form>
          <div class="flex justify-between mt-2">
            <Button @click="openDialog">Generate Random Array</Button>
            <Button @click="clearArray" variant="destructive">Clear</Button>
          </div>
        </CardContent>
      </Card>

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

      <Card class="mt-8 p-4">
        <h2 class="text-xl font-semibold mb-2">Sorting Time Comparison</h2>
        <div class="">
          <TimeChart :data="timeTaken" />
        </div>
      </Card>

      <Card class="mt-8">
        <CardHeader>
          <CardTitle>Bubble Sort</CardTitle>
        </CardHeader>
        <CardContent>
          <p v-if="timeTaken.length > 0" class="bg-gray-100 p-4 rounded">
            Time taken by Bubble Sort: {{ timeTaken[0] }} ms
          </p>
          <p v-else class="bg-gray-100 p-4 rounded">No time taken yet</p>
          <p v-if="sortedArrayBubble" class="text-sm text-gray-500 p-4 rounded">
            Result: {{ sortedArrayBubble }}
          </p>
          <p v-else class="text-sm text-gray-500 p-4 rounded">Array not sorted yet</p>
        </CardContent>
      </Card>

      <Card class="mt-4">
        <CardHeader>
          <CardTitle>Merge Sort</CardTitle>
        </CardHeader>
        <CardContent>
          <p v-if="timeTaken.length > 0" class="bg-gray-100 p-4 rounded">
            Time taken by Merge Sort: {{ timeTaken[1] }} ms
          </p>
          <p v-else class="bg-gray-100 p-4 rounded">No time taken yet</p>
          <p v-if="sortedArrayMerge" class="text-sm text-gray-500 p-4 rounded">
            Result: {{ sortedArrayMerge }}
          </p>
          <p v-else class="text-sm text-gray-500 p-4 rounded">Array not sorted yet</p>
        </CardContent>
      </Card>

      <Card class="mt-4">
        <CardHeader>
          <CardTitle>Quick Sort</CardTitle>
        </CardHeader>
        <CardContent>
          <p v-if="timeTaken.length > 0" class="bg-gray-100 p-4 rounded">
            Time taken by Quick Sort: {{ timeTaken[2] }} ms
          </p>
          <p v-else class="bg-gray-100 p-4 rounded">No time taken yet</p>
          <p v-if="sortedArrayQuick" class="text-sm text-gray-500 p-4 rounded">
            Result: {{ sortedArrayQuick }}
          </p>
          <p v-else class="text-sm text-gray-500 p-4 rounded">Array not sorted yet</p>
        </CardContent>
      </Card>

      <Card class="mt-4">
        <CardHeader>
          <CardTitle>Radix Sort</CardTitle>
        </CardHeader>
        <CardContent>
          <p v-if="timeTaken.length > 0" class="bg-gray-100 p-4 rounded">
            Time taken by Radix Sort: {{ timeTaken[3] }} ms
          </p>
          <p v-else class="bg-gray-100 p-4 rounded">No time taken yet</p>
          <p v-if="sortedArrayRadix" class="text-sm text-gray-500 p-4 rounded">
            Result: {{ sortedArrayRadix }}
          </p>
          <p v-else class="text-sm text-gray-500 p-4 rounded">Array not sorted yet</p>
        </CardContent>
      </Card>
    </div>
  </div>
</template>

<style scoped>
/* You can add any additional scoped styles here if needed */
</style>
