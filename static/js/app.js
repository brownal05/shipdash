

function init (){
var selector = d3.select("#selDataset");

    d3.json("/charterers").then((chrtrNames) => {
    chrtrNames.forEach((chrtr) => {
        selector
        .append("option")
        .text(chrtr)
        .property("value", chrtr);
    });
    const firstChrtr = chrtrNames[0];
 
    buildMetadata(firstChrtr);

});

};

function optionChanged(newChrtr) {
    buildMetadata(newChrtr);
    };



init();

function buildMetadata(chrtr) {

 
    d3.json("/fixtures/" + chrtr).then(function(response){
      console.log(response);
      selection = d3.select("#chrtr-stats")
      console.log(selection)
      selection.html("");
      var table = selection.append("table")
      .append("tbody")
  
      Object.entries(response).forEach(([key, value]) => {
        var row = table.append("tr")
        row.append("td").text(key, ": ");
        row.append("td").text(value)
        
      });
      
    }); 
  
  }