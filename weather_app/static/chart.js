document.addEventListener('DOMContentLoaded', function() {
    const fetchButton = document.getElementById("fetchButton");
    const loadingContainer = document.getElementById("loadingContainer");
        fetchButton.addEventListener("click", function(event) {
            event.preventDefault();

            const city1 = document.getElementById("city1").value;
            const city2 = document.getElementById("city2").value;
            loadingContainer.classList.remove("d-none");
            if (city1 != "" && city2 != ""){
                console.log(city1);
                console.log(city2);
                fetch("/fetch_2_weeks_data", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        city1: city1,
                        city2: city2
                    })
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    var dates = data.date_range;
                    var cityAData = data.city1_data;
                    var cityBData = data.city2_data;
                
                
                    Highcharts.chart('chart-container', {
                        chart: {
                            type: 'spline'
                        },
                        title: {
                            text: 'Weather Comparison'
                        },
                        xAxis: {
                            categories: dates,
                            title: {
                                text: 'Date'
                            }
                        },
                        yAxis: {
                            title: {
                                text: 'Temperature (°C)'
                            }
                        },
                        series: [{
                            name: data.city1_name,
                            data: cityAData
                        }, {
                            name: data.city2_name,
                            data: cityBData
                        }]
                    });
                    loadingContainer.classList.add("d-none");



                })
                .catch(error => {
                    console.error("Error fetching data: ", error);
                    loadingContainer.classList.add("d-none");
                });
            }
        });
});