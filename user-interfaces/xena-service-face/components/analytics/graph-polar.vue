<template>
  <v-card
    class = '
      mx-auto
      text-center
    '
    outlined
    tile
  >
    <v-btn
      block
      text
      tile
      small
      disabled
      color = 'rgba(189, 147, 249, 1)'
    >
      {{ title }}
    </v-btn>

    <v-divider></v-divider>

    <canvas
      :id = '`pie-chart-${targetPlatform}`'
    ></canvas>
  </v-card>
</template>

<script lang = 'ts'>
import Vue from 'vue'

import { Chart } from 'chart.js'

export default Vue.extend({
  data: () => ({
    platforms: {
      linux: 40,
      windows: 5,
      macos: 30,
    } as any,
    chart: null,
  }),
  props: {
    targetPlatform: {
      required: false,
      type: String,
    },
    title: {
      required: true,
      type: String,
    }
  },
  methods: {
    chartInit () {
      if (this.chart)
        return
      this.chart = new Chart(document.getElementById(`pie-chart-${this.targetPlatform}`), {
        type: 'polarArea',
        data: {
          labels: Object.keys(this.platforms),
          datasets: [
            { 
              data: Object.keys(this.platforms).map(p => this.platforms[p]),
              label: "Clients",
              borderColor: '#6272a4',
              hoverBorderColor: '#bd93f9',
              borderWidth: 0.9,
              fill: true,
            },
          ]
        },
        options: {
          title: {
            display: false,
            text: this.title
          },
          scale: {
            display: false
          },
          scales: {
            xAxes: [{
              ticks: {
                display: false
              },
              gridLines: {
                display: false
              }
            }],
            yAxes: [{
              ticks: {
                display: false
              },
              gridLines: {
                display: false
              }
            }]
          },
          legend: {
            display: true
          },
          tooltips: {
            enabled: true
          },
        }
      })
    },
  },
  
  mounted () {
    this.chartInit()
  }
})
</script>

<style lang = 'css' scoped>
</style>