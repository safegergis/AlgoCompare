<template>
  <div>
    <BarChart :chartData="chartData" :options="options" />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { BarChart } from 'vue-chart-3'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

const props = defineProps<{
  data: number[]
}>()

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
  }
}

const chartData = computed(() => ({
  labels: ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort', 'Linear Search'],
  datasets: [
    {
      data: props.data,
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(255, 159, 64, 0.2)'
      ],
      borderColor: [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1
    }
  ]
}))
</script>
