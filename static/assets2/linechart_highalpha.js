var optionsLineHighAlpha = {
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
    text: 'HighAlpha',
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

var linechart_highalpha = new ApexCharts(
  document.querySelector("#linechart_highalpha"),
  optionsLineHighAlpha
);
linechart_highalpha.render()

window.setInterval(function() {
$.getJSON('http://localhost:5000/eeg/raw_highalpha', function(response) {
	linechart_highalpha.updateSeries([{
	  name: 'HighAlpha',
	  data: response
	}])
});
}, 500);