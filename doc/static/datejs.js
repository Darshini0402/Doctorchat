function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
    }
    document.getElementById("defaultOpen").click(); 
    function contact()
    {
        alert("Feel free to call or message anytime:\nDarshini:+919840336198\nDikshita:+918130263296\nShubhangi: +917479577601\nSreelakshmi: +971566428580");
    }
    var today = new Date().toISOString().split('T')[0];
    document.getElementsByName("somedate")[0].setAttribute('min', today);
