var optionsLineTheta = {
  chart: {
    height: 350,
    type: 'line',
    stacked: true,
    animations: {
      enabled: true,
      easing: 'linear',
      dynamicAnimation: {
        speed: 1000
      }
    },
    dropShadow: {
      enabled: true,
      opacity: 0.3,
      blur: 5,
      left: -7,
      top: 22
    },
    toolbar: {
      show: false
    },
    zoom: {
      enabled: false
    }
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    curve: 'straight',
    width: 5,
  },
  grid: {
    padding: {
      left: 0,
      right: 0
    }
  },
  markers: {
    size: 0,
    hover: {
      size: 0
    }
  },
  series: [],
  noData: {
	text: 'Loading...'
  },
  xaxis: {
    type: 'datetime'//,
    //range: 2700000
  },
  title: {
    text: 'Theta',
    align: 'left',
    style: {
      fontSize: '12px'
    }
  },
  subtitle: {
    text: '20',
    floating: true,
    align: 'right',
    offsetY: 0,
    style: {
      fontSize: '22px'
    }
  },
  legend: {
    show: true,
    floating: true,
    horizontalAlign: 'left',
    onItemClick: {
      toggleDataSeries: false
    },
    position: 'top',
    offsetY: -28,
    offsetX: 60
  },
}

var linechart_theta = new ApexCharts(
  document.querySelector("#linechart_theta"),
  optionsLineTheta
);
linechart_theta.render()

window.setInterval(function() {
$.getJSON('http://localhost:5000/eeg/raw_theta', function(response) {
	linechart_theta.updateSeries([{
	  name: 'Theta',
	  data: response
	}])
});
}, 500);