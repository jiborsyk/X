function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
  	  if (this.readyState===4 && this.status ===200) {
	      callback(this.response);
	    }
    }
    request.open("GET", path);
    request.send();
}

/* The callback function
   The response is a dictionary with the following keys/values:
          'div' - the name of the <div> element in the HTML file
                  where the resulting graph will be displayed
         'data' - the data for the graph, in the format that the
                  Plot.ly newPlot function expects
       'layout' - the layout information for the graph, in the
                  format that the Plot.ly newPlot function expects

  This function extracts the values associated with these keys
  and passes them as arguments in a call to the newPlot function.
*/
function pietime(button){

    function makePie(response) {
        let d = JSON.parse(response);
        console.log(d)
        let val = []
        let lab = []
        for (i in d[button]){
            lab.push(i);
            val.push(d[button][i])
            }

        var layout = {
            title:{text:button,font:{size:40}},
            height: 600,
            width: 1000,
            margin: {
                l: 5,
                r: 5,
                b: 10,
                t: 100,
                pad: 4
            }};
        data = [{values:val,labels:lab,type:'pie'}]
        Plotly.newPlot('pie', data, layout)
        }
    ajaxGetRequest("/speciessort", makePie)
}


function getMap(){
    var data = [{type: 'densitymapbox', lon: [-74, -73, -74], lat: [43, 44, 45], z: [7, 5, 2]}];

    var layout = {width: 1000, height: 600, mapbox: {style: 'stamen-terrain'}};

    Plotly.newPlot('map', data, layout)
}

function extMap(){
    function makeMap(response){
    let dat = JSON.parse(response)

    let long = []
    let lati = []
    let zed = []
    for (county in dat){
        long.push(dat[county]['lon'])
        lati.push(dat[county]['lat'])
        zed.push(dat[county]['Near Extinction'])
    }
    var data = [{type:'densitymapbox',lon:long, lat:lati,z:zed}]
    var layout = {width: 1000, height: 700, mapbox: {style: 'stamen-terrain'}};
    Plotly.newPlot('map', data, layout);}
    ajaxGetRequest("/species_location",makeMap)
}
function endMap(){
    function makeMap(response){
    let dat = JSON.parse(response)

    let long = []
    let lati = []
    let zed = []
    for (county in dat){
        long.push(dat[county]['lon'])
        lati.push(dat[county]['lat'])
        zed.push(dat[county]['Critically Endangered'])
    }
    var data = [{type:'densitymapbox',lon:long, lat:lati,z:zed}]
    var layout = {width: 1000, height: 700, mapbox: {style: 'stamen-terrain'}};
    Plotly.newPlot('map', data, layout);}
    ajaxGetRequest("/species_location",makeMap)
}

function vulMap(){
    function makeMap(response){
    let dat = JSON.parse(response)

    let long = []
    let lati = []
    let zed = []
    for (county in dat){
        long.push(dat[county]['lon'])
        lati.push(dat[county]['lat'])
        zed.push(dat[county]['Vulnerable'])
    }
    var data = [{type:'densitymapbox',lon:long, lat:lati,z:zed}]
    var layout = {width: 1000, height: 700, mapbox: {style: 'stamen-terrain'},center:{lon:-73,lat:42}};
    Plotly.newPlot('map', data, layout);}}


function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState===4&&this.status ===200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}

function renderSearch(response){
    let searches = JSON.parse(response)
    let element = document.getElementById('boat')
    element.innerHTML = searches
}


function requestSearch(){
    ajaxGetRequest('/getsearch', renderSearch)
}



function searchCounty(){
    let searchElement = document.getElementById('search')
    let search = searchElement.value
    searchElement.value = ""
    let toSend = (search);
    console.log(toSend)
    ajaxPostRequest('/search',toSend,requestSearch);}
