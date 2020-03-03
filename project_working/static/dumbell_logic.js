var stateData = data

console.log(stateData)






var data = [{
    "name": "Ohio",
    "high": 11689442,
    "low": 11594163
}, {
    "name": "Washington",
    "high": 7535591,
    "low": 7061530
}, {
    "name": "Virginia",
    "high": 8517685,
    "low": 8326289
}, {
    "name": "California",
    "high": 39557045,
    "low": 38802500
}, {
    "name": "Texas",
    "high": 28701845,
    "low": 26956958
}, {
    "name": "Pennsylvania",
    "high": 12807060,
    "low": 12787209
}, {
    "name": "Florida",
    "high": 21299325,
    "low": 19893297
}, {
    "name": "Georgia",
    "high": 10519475,
    "low": 10097343
}, {
    "name": "North Carolina",
    "high": 10383620,
    "low": 9943964
}, {
    "name": "New York",
    "high": 19542209,
    "low": 19746227
}, {
    "name": "Illinois",
    "high": 12741080,
    "low": 12880580
}, {
    "name": "New Jersey",
    "high": 8908520,
    "low": 8938175
}, {
    "name": "Michigan",
    "high": 9995915,
    "low": 9909877
}]







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
            text: 'State Population'
        }
    },

    series: [{
        name: 'State Population',
        data: data
    }]

});


// end new stuff 