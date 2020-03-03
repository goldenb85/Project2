var stateData = "data/dumbell_logic.js";

Highcharts.chart('container', {

    chart: {
        type: 'dumbbell',
        inverted: true
    },

    legend: {
        enabled: false
    },

    subtitle: {
        text: '2014 vs 2018'
    },

    title: {
        text: 'Change in State Population'
    },

    tooltip: {
        shared: true
    },

    xAxis: {
        type: 'category'
    },

    yAxis: {
        title: {
            text: 'State Population Change'
        }
    },

    series: [{
        name: 'State Population Change',
        data: stateData
    }]

});