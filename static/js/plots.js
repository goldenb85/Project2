d3.json("http://127.0.0.1:5000/api/population/").then((data) => {
// d3.json("pop.json").then((data) => {  
        
        function filter2013(data){
          return data.id_year===2013;
        }
        function filter2014(data){
          return data.id_year===2014;
        }
        function filter2015(data){
          return data.id_year===2015;
        }
        function filter2016(data){
          return data.id_year===2016;
        }
        function filter2017(data){
          return data.id_year===2017;
        }
        function filter2018(data){
          return data.id_year===2018;
        }
        
        var year13_18,pop2013,pop2014,pop2015,pop2016, pop2017,pop2018,
        total2013,total2014,total2015,total2016,total2017,total2018,
        avg2013, avg2014, avg2015, avg2016, avg2017, avg2018 =[];
        var year13_18=["2013","2014","2015","2016","2017","2018"];
        
        var pop2013=data.filter(filter2013).map(popu => popu.population);
        var pop2014=data.filter(filter2014).map(popu => popu.population);
        var pop2015=data.filter(filter2015).map(popu => popu.population);
        var pop2016=data.filter(filter2016).map(popu => popu.population);
        var pop2017=data.filter(filter2017).map(popu => popu.population);
        var pop2018=data.filter(filter2018).map(popu => popu.population);
        var total2013=d3.sum(pop2013);
        var total2014=d3.sum(pop2014);
        var total2015=d3.sum(pop2015);
        var total2016=d3.sum(pop2016);
        var total2017=d3.sum(pop2017);
        var total2018=d3.sum(pop2018);
        var avg2013=d3.mean(pop2013);
        var avg2014=d3.mean(pop2014);
        var avg2015=d3.mean(pop2015);
        var avg2016=d3.mean(pop2016);
        var avg2017=d3.mean(pop2017);
        var avg2018=d3.mean(pop2018);
        var trace1={
          x: year13_18,
          y:[total2013,total2014,total2015,total2016,total2017,total2018],
          text: year13_18,
          name: "Total population",
          type: "bar",
          marker:{
            color:['#FFDC80','#FCAF45','#F77737','#F56040','#FD1D1D','#E1306C']
          }
        };
        var trace2={
          x:year13_18,
          y:[avg2013,avg2014,avg2015,avg2016,avg2017,avg2018],
          text: year13_18,
          name: "Population Average",
          type: "bar",
          marker:{
            color:['#6CFF33','#BFFF33','#FFEC33','#33FFC0','#33FFF4','#33D8FF']
          }
        }
        
        // Apply the group barmode to the layout
        var layout1 = {
          title: "Total Population from 2013 to 2018 for USA (52 states)",
          yaxis:{range:[310000000,335000000]}
        };
        var layout2 = {
          title: "Population Average from 2013 to 2018 for USA (52 states)",
          yaxis:{range:[6100000,6400000]}
        };
        // Render the plot to the div tag with id "plot"
        Plotly.newPlot("plot1", [trace1], layout1);
        Plotly.newPlot("plot2", [trace2], layout2);
    
        
      });
