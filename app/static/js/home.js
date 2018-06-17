//SEARCH for Occupation FUNCTION Starts
function searchMovie() {
    $("#searchResult").html("");

    
    var searchInput = document.getElementById("searchInputField"); 

    //Place given for the Search for Occupations
    var searchUrl = "";

    var resultUrl = searchUrl + searchInput.value;


    $.getJSON( resultUrl, function( data ) {
     
        var items = [];

        $.each( data, function( index, value ) {
            items.push("<li>" 
                + "<a href='results.html?skills=" + val.id + "'>" 
                + "<img src= '" + value.imageUrl + "' >"
                + "<span class='spanText'>" + value.title + "</span>"
                + "</a>"
                + "</li>");
                });

                $( "<ul>", { "class": "my-new-list", html: items.join( "" )})
            .appendTo($("#searchResult"));
        });
}
//SEARCH FUNCTION ends



$(document).ready(function () {
//Creating div for different events
    for(var i = 0; i < 20; i++) {
        var meetingContainer = $("<div>")
        .attr("class", "meetingClassContainer")
        .appendTo("#entireBodyDivId");
    }

    $(".meetingClassContainer").on("click", function () {
        window.location.href = "results.html?meetUp=" + this.id; 
    });
            }

    //WOULD LIKE TO CREATE A CAROUSEL LATER
        );