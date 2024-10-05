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

const target = ref<number>(0)

const found = ref<number[]>([])

const timeTaken = ref<number[]>([])

const handleSubmit = async () => {
  const body = { array: unsortedArray.value.split(',').map(Number), target: target.value }
  const response = await ofetch('http://127.0.0.1:5000/sort', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  })
  if (response) {
    sortedArrayBubble.value = response.bubble_sort.sorted_array.join(', ')
    sortedArrayMerge.value = response.merge_sort.sorted_array.join(', ')
    sortedArrayQuick.value = response.quick_sort.sorted_array.join(', ')
    sortedArrayRadix.value = response.radix_sort.sorted_array.join(', ')
    found.value = response.linear_search.found.join(', ')
    timeTaken.value = [
      response.bubble_sort.time_taken,
      response.merge_sort.time_taken,
      response.quick_sort.time_taken,
      response.radix_sort.time_taken,
      response.linear_search.time_taken
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
  <div class="bg-gray-300 flex flex-col items-center justify-center min-h-screen sm:p-4">
    <div class="container mx-auto">
      <Card class="mb-4">
        <CardHeader>
          <CardTitle class="text-xl sm:text-2xl">Array Sorting Visualizer</CardTitle>
        </CardHeader>
        <CardContent>
          <form @submit.prevent="handleSubmit" class="space-y-4">
            <p class="text-sm">Enter the array to be sorted</p>
            <Textarea
              v-model="unsortedArray"
              placeholder="Enter your unsorted array (comma-separated numbers)"
              class="w-full"
              rows="3"
            />
            <p class="text-sm">Enter the target number for linear search</p>
            <Input v-model="target" placeholder="Enter the target number" class="w-full" />
            <Button type="submit" class="w-full sm:w-auto">Sort Array</Button>
          </form>
          <div
            class="flex flex-col sm:flex-row justify-between mt-4 space-y-2 sm:space-y-0 sm:space-x-2"
          >
            <Button @click="openDialog" class="w-full sm:w-auto">Generate Random Array</Button>
            <Button @click="clearArray" variant="destructive" class="w-full sm:w-auto"
              >Clear</Button
            >
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
            <Button @click="generateRandomArray" class="w-full">Generate</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>

      <Card class="mb-4">
        <CardHeader>
          <CardTitle class="text-lg sm:text-xl">Sorting Time Comparison</CardTitle>
        </CardHeader>
        <CardContent>
          <TimeChart :data="timeTaken" />
        </CardContent>
      </Card>

      <Card class="mb-4">
        <CardHeader>
          <CardTitle class="text-lg">Bubble Sort</CardTitle>
        </CardHeader>
        <CardContent>
          <p v-if="timeTaken.length > 0" class="bg-gray-100 p-2 rounded text-sm">
            Time taken: {{ timeTaken[0] }} ms
          </p>
          <p v-else class="bg-gray-100 p-2 rounded text-sm">No time taken yet</p>
          <p v-if="sortedArrayBubble" class="text-xs text-gray-500 mt-2 break-words">
            Result: {{ sortedArrayBubble }}
          </p>
          <p v-else class="text-xs text-gray-500 mt-2">Array not sorted yet</p>
        </CardContent>
      </Card>

      <Card class="mb-4">
        <CardHeader>
          <CardTitle class="text-lg">Merge Sort</CardTitle>
        </CardHeader>
        <CardContent>
          <p v-if="timeTaken.length > 0" class="bg-gray-100 p-2 rounded text-sm">
            Time taken: {{ timeTaken[1] }} ms
          </p>
          <p v-else class="bg-gray-100 p-2 rounded text-sm">No time taken yet</p>
          <p v-if="sortedArrayMerge" class="text-xs text-gray-500 mt-2 break-words">
            Result: {{ sortedArrayMerge }}
          </p>
          <p v-else class="text-xs text-gray-500 mt-2">Array not sorted yet</p>
        </CardContent>
      </Card>

      <Card class="mb-4">
        <CardHeader>
          <CardTitle class="text-lg">Quick Sort</CardTitle>
        </CardHeader>
        <CardContent>
          <p v-if="timeTaken.length > 0" class="bg-gray-100 p-2 rounded text-sm">
            Time taken: {{ timeTaken[2] }} ms
          </p>
          <p v-else class="bg-gray-100 p-2 rounded text-sm">No time taken yet</p>
          <p v-if="sortedArrayQuick" class="text-xs text-gray-500 mt-2 break-words">
            Result: {{ sortedArrayQuick }}
          </p>
          <p v-else class="text-xs text-gray-500 mt-2">Array not sorted yet</p>
        </CardContent>
      </Card>

      <Card class="mb-4">
        <CardHeader>
          <CardTitle class="text-lg">Radix Sort</CardTitle>
        </CardHeader>
        <CardContent>
          <p v-if="timeTaken.length > 0" class="bg-gray-100 p-2 rounded text-sm">
            Time taken: {{ timeTaken[3] }} ms
          </p>
          <p v-else class="bg-gray-100 p-2 rounded text-sm">No time taken yet</p>
          <p v-if="sortedArrayRadix" class="text-xs text-gray-500 mt-2 break-words">
            Result: {{ sortedArrayRadix }}
          </p>
          <p v-else class="text-xs text-gray-500 mt-2">Array not sorted yet</p>
        </CardContent>
      </Card>

      <Card class="mb-4">
        <CardHeader>
          <CardTitle class="text-lg">Linear Search</CardTitle>
        </CardHeader>
        <CardContent>
          <p v-if="timeTaken.length > 0" class="bg-gray-100 p-2 rounded text-sm">
            Time taken: {{ timeTaken[4] }} ms
          </p>
          <p v-else class="bg-gray-100 p-2 rounded text-sm">No time taken yet</p>
          <p v-if="found.length > 0" class="text-xs text-gray-500 mt-2 break-words">
            Target found at indices: {{ found }} <br />
          </p>

          <p v-else class="text-xs text-gray-500 mt-2">Target not found</p>
        </CardContent>
      </Card>
    </div>
  </div>
</template>

<style scoped>
/* You can add any additional scoped styles here if needed */
</style>
