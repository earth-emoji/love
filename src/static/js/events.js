var send_data = {}

$(document).ready(function () {
    
    // reset all parameters on page load
    resetFilters();
    // bring all the data without any filters
    getAPIData();

    // on selecting the country option
    $('#visibility').on('change', function () {

        // update the selected country
        if(this.value == "all")
            send_data['visibility'] = "";
        else
            send_data['visibility'] = this.value;

        // get api data of updated filters
        getAPIData();
    });

    // on filtering the variety input
    $('#day').on('change', function () {
        // get the api data of updated variety
        if(this.value == "all")
            send_data['day'] = "";
        else
            send_data['day'] = this.value;
        getAPIData();
    });

    // sort the data according to price/points
    $('#sort_by').on('change', function () {
        send_data['sort_by'] = this.value;
        getAPIData();
    });

    // display the results after reseting the filters
    $("#display_all").click(function(){
        resetFilters();
        getAPIData();
    })
})


/**
    Function that resets all the filters   
**/
function resetFilters() {
    $("#visibility").val("all");
    $("#day").val("all");
    $("#sort_by").val("none");

    send_data['visibility'] = '';
    send_data['day'] = '';
    send_data["sort_by"] = '',
    send_data['format'] = 'json';
}

/**.
    Utility function to showcase the api data 
    we got from backend to the table content
**/
function putTableData(result) {
    // creating table row for each result and
    // pushing to the html cntent of table body of listing table
    let row;
    if(result["results"].length > 0){
        $("#no_results").hide();
        $("#list_data").show();
        $("#listing").html("");  
        $.each(result["results"], function (a, b) {
            row = "<tr> <td>" + b.name + "</td>" +
                "<td>" + b.location + "</td>" +
                "<td>" + b.visibility + "</td>" +
                "<td>" + formatServerDateTime(b.start_time)+ "</td>" +
                "<td>" + formatServerDateTime(b.end_time)+ "</td></tr>"
            $("#listing").append(row);
        });
    }
    else{
        // if no result found for the given filter, then display no result
        $("#no_results h5").html("No results found");
        $("#list_data").hide();
        $("#no_results").show();
    }
    // setting previous and next page url for the given result
    let prev_url = result["previous"];
    let next_url = result["next"];
    // disabling-enabling button depending on existence of next/prev page. 
    if (prev_url === null) {
        $("#previous").addClass("disabled");
        $("#previous").prop('disabled', true);
    } else {
        $("#previous").removeClass("disabled");
        $("#previous").prop('disabled', false);
    }
    if (next_url === null) {
        $("#next").addClass("disabled");
        $("#next").prop('disabled', true);
    } else {
        $("#next").removeClass("disabled");
        $("#next").prop('disabled', false);
    }
    // setting the url
    $("#previous").data("url", result["previous"]);
    $("#next").data("url", result["next"]);
    // displaying result count
    $("#result-count span").html(result["count"]);
}

function formatServerDateTime(datetime) {

    date = new Date(datetime);

    var formatter = new Intl.DateTimeFormat('en-us', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        hour12: true,
        timeZone: 'UTC'
      });
      
    return formatter.format(date);

}

function getAPIData() {
    let url = $('#list_data').data("url");

    $.ajax({
        method: 'GET',
        url: url,
        data: send_data,
        beforeSend: function(){
            $("#no_results h5").html("Loading data...");
        },
        success: function (result) {
            putTableData(result);
        },
        error: function (response) {
            $("#no_results h5").html("Something went wrong");
            $("#list_data").hide();
        }
    });
}

$("#next").click(function () {
    let url = $(this).data("url");
    if (!url)
        $(this).prop('all', true);

    $(this).prop('all', false);
    $.ajax({
        method: 'GET',
        url: url,
        success: function (result) {
            putTableData(result);
        },
        error: function(response){
            console.log(response)
        }
    });
})

$("#previous").click(function () {
    let url = $(this).data("url");
    if (!url)
        $(this).prop('all', true);

    $(this).prop('all', false);
    $.ajax({
        method: 'GET',
        url: url,
        success: function (result) {
            putTableData(result);
        },
        error: function(response){
            console.log(response)
        }
    });
})
