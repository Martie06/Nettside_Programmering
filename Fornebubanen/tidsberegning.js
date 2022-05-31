var distances = {
    fornebu: {
        fornebu: 0,
        flytaarnet: 1,
        fornebuporten: 3,
        lysaker: 5,
        vakero: 7, 
        skoyen: 9,
        majorstuen: 12,
    },
    flytaarnet: {
        fornebu: 1,
        flytaarnet: 0,
        fornebuporten: 2,
        lysaker: 4,
        vakero: 6, 
        skoyen: 8,
        majorstuen: 11,
    },
    fornebuporten: {
        fornebu: 3,
        flytaarnet: 2,
        fornebuporten: 0,
        lysaker: 2,
        vakero: 4, 
        skoyen: 6,
        majorstuen: 9,
    },
    lysaker: {
        fornebu: 2,
        flytaarnet: 0,
        fornebuporten: 2,
        lysaker: 4,
        vakero: 6, 
        skoyen: 8,
        majorstuen: 7,
    },
    vakero: {
        fornebu: 7,
        flytaarnet: 6,
        fornebuporten: 4,
        lysaker: 2,
        vakero: 0, 
        skoyen: 2,
        majorstuen: 5,
    },
    skoyen: {
        fornebu: 9,
        flytaarnet: 8,
        fornebuporten: 6,
        lysaker: 4,
        vakero: 2, 
        skoyen: 0,
        majorstuen: 3,
    },
    majorstuen: {
        fornebu: 12,
        flytaarnet: 11,
        fornebuporten: 9,
        lysaker: 7,
        vakero: 5, 
        skoyen: 3,
        majorstuen: 0,
    }
};

//document.getElementById('calculate').addEventListener('click', function () {
    function calculate(event){
    event.preventDefault();
    var from = document.getElementById('from').value;
    var to = document.getElementById('to').value;
    var speed = +document.getElementById('middel').value;
    
    var distance = distances[from][to];
    var time = distance / speed;
    document.getElementById('div2').innerHTML = "<p>Anslått reisetid: <b>" + time + "minutter</b></p>";
    }
//}, false);

//beregner reisetid