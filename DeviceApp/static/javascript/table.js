function searchBox() {

    var filterSelect = document.getElementById("filterSelect");

    var filterNum = filterSelect.value;

    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("dataTable");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[filterNum];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().includes(filter) && txtValue.toUpperCase().indexOf(filter) == 0 || filter === "") {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }
