
// CHART

const DATA_COUNT = 7;
const NUMBER_CFG = {count: DATA_COUNT, min: -100, max: 100};
const labels = ['a','b','c','d'];

ctx = document.getElementById('chart');

myChart = new Chart(ctx, {
	type: 'bar',
	data: {
  labels: labels,
  datasets: [
    {
      label: 'Fully Rounded',
      data: [10,20,30,40,50,60,70,80],
      borderColor: '#ea4c46',
      backgroundColor: '#f8f9fa',
      borderWidth: 2,
      borderRadius: Number.MAX_VALUE,
      borderSkipped: false,
    },
  ]
},		
});

// MAP

BASECOORDS = [49.817492,15.472962];

var map = L.map('map').setView(BASECOORDS, 6);

//L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
//}).addTo(map);

L.tileLayer('https://maps.omniscale.net/v2/{id}/style.grayscale/{z}/{x}/{y}.png', {
	id: 'mapsosc-b667cf5a',
	attribution: 'Map data &copy; <a href="https://maps.omniscale.com/">Omniscale</a>',
}).addTo(map);

var marker =  L.marker([49.817492,15.472962]).addTo(map);

//marker.bindPopup('<b>Prague</b>').openPopup();

