var data3=[
    {
      State: 'Ohio',
      High: 11689442,
      Low: 11594163
    },
    {
      State: 'Washington',
      High: 7535591,
      Low: 7061530
    },
    {
      State: 'Virginia',
      High: 8517685,
      Low: 8326289
    },
    {
      State: 'California',
      High: 39557045,
      Low: 38802500
    },
    {
      State: 'Texas',
      High: 28701845,
      Low: 26956958
    },
    {
      State: 'Pennsylvania',
      High: 12807060,
      Low: 12787209
    },
    {
      State: 'Florida',
      High: 21299325,
      Low: 19893297
    },
    {
      State: 'Georgia',
      High: 10519475,
      Low: 10097343
    },
    {
      State: 'North Carolina',
      High: 10383620,
      Low: 9943964
    },
    {
      State: 'New York',
      High: 19542209,
      Low: 19746227
    },
    {
      State: 'Illinois',
      High: 12741080,
      Low: 12880580
    },
    {
      State: 'New Jersey',
      High: 8908520,
      Low: 8938175
    },
    {
      State: 'Michigan',
      High: 9995915,
      Low: 9909877
    }
  ];
  Highcharts.chart('plot1', {

    chart: {
        type: 'dumbbell',
        inverted: true
    },

    legend: {
        enabled: false
    },

    subtitle: {
        text: '1960 vs 2018'
    },

    title: {
        text: 'Change in Life Expectancy'
    },

    tooltip: {
        shared: true
    },

    xAxis: {
        type: 'category'
    },

    yAxis: {
        title: {
            text: 'Life Expectancy (years)'
        }
    },

    series: [{
        name: 'Life expectancy change',
        data: data3
    }]

});