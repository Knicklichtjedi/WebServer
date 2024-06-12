<script setup>

import Plotly from 'plotly.js/dist/plotly';
import {onMounted, ref} from 'vue';

const baseURL = `${import.meta.env.VITE_API_BASE_URL}`

async function getData() {
  /**
   * Request data from the server using the /data endpoint
   * @type {null}
   */
  let dataResponse = null;
  let response = null;

  try {
    response = await fetch(`${baseURL}/data`);
  } catch (e) {
    console.log(e);
  }

  if (response !== null) {
    try {
      dataResponse = await response.json();
    } catch (e) {
      console.log(e);
    }
  } else {
    console.log("Response failed, cannot decode to JSON!")
  }

  return dataResponse;
}

async function drawGraph(dataResponse) {
  /**
   * Draw the graph based on data given, design is markers and scatter plot
   * @type {[{mode: string, x, y, type: string}]}
   */

  const data = [{
    x: dataResponse.a,
    y: dataResponse.b,
    mode: 'markers',
    type: 'scatter'
  }];

  const plotElement = Plotly.newPlot('plot', data);

  return plotElement;
}

async function getGraph() {
  /**
   * Request data from the server and generate a graph
   * @type {null}
   */
  const graphData = await getData();
  const plotElement = await drawGraph(graphData);
}

// Display empty plot to avoid page movement
onMounted(() => {
  Plotly.newPlot('plot');
});

</script>

<template>

  <title>This is the demo for JCB</title>

  <div id="plot"></div>

  <BCard>
    <BCardText>
      Displaying the loaded data, which was requested from the Web Server.
    </BCardText>
    <BButton variant="outline-primary" @click="getGraph">Load Data</BButton>
  </BCard>

</template>
