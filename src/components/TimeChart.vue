<template>
  <div>
    <BarChart :chartData="chartData" :options="options" @click="handleClick" />
    <button
      @click="showAllBars"
      class="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
    >
      Show All
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { BarChart } from 'vue-chart-3'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

const props = defineProps<{
  data: number[]
}>()

const hiddenBars = ref<boolean[]>(new Array(5).fill(false))

const options = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false
    }
  },
  scales: {
    y: {
      display: true,
      title: {
        display: true,
        text: 'Time (ms)'
      }
    },
    x: {
      display: true,
      title: {
        display: true,
        text: 'Sorting Algorithms'
      }
    }
  },
  onClick: (event: any, elements: any) => {
    if (elements.length > 0) {
      const index = elements[0].index
      hiddenBars.value[index] = !hiddenBars.value[index]
    }
  }
}

const chartData = computed(() => ({
  labels: ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort', 'Linear Search'],
  datasets: [
    {
      data: props.data.map((value, index) => (hiddenBars.value[index] ? null : value)),
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(75, 192, 192, 0.2)'
      ],
      borderColor: [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(75, 192, 192, 1)'
      ],
      borderWidth: 1
    }
  ]
}))

const handleClick = (event: any, elements: any) => {
  if (elements.length > 0) {
    const index = elements[0].index
    hiddenBars.value[index] = !hiddenBars.value[index]
  }
}

const showAllBars = () => {
  hiddenBars.value = new Array(5).fill(false)
}
</script>
