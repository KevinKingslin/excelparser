// DataTable
window.addEventListener("DOMContentLoaded", (event) => {
    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector("#sidebarToggle");
    if (sidebarToggle) {
        sidebarToggle.addEventListener("click", (event) => {
            event.preventDefault();
            document.body.classList.toggle("sb-sidenav-toggled");
            localStorage.setItem(
                "sb|sidebar-toggle",
                document.body.classList.contains("sb-sidenav-toggled")
            );
        });
    }
});

// Keep DataTable as global variable
var table;

$(document).ready(function product() {
    // Initialise DataTable
    table = $('#datatablesSimple').DataTable({
       "ajax": {
          "processing": true,
          "url": "getProducts",
          "dataSrc": "",
          "data": "",
        },
        "columns": [
                { "data": "ID"},
                { "data": "name"},
                { "data": "lowest_price"},
                { "data": {variations: "variations", variantCount: "variantCount"}, "render": function(data, type, row, meta){
                    // Create nested table
                    table_string = "<table class='table'><thead><th>Variation</th><th>Stock</th></thead><tbody>"
                        $.each(data.variations, function(i){
                            table_string += "<tr><td>" + data.variations[i]['variant'] + "</td><td>" + data.variations[i]['stock'] + '</td></tr>'
                        })
                    table_string += "</tbody></table>"
                    return table_string
                }},
                { "data": "last_updated"},
            ],
    });
});

// function getProducts(){
//     data = fetch("/getProducts", {
//         method: "GET",
//     });

//     console.log(data)
// }

// Function to add new products
async function addProducts() {
    event.preventDefault();
    input = document.getElementById("excel_file");
    const formData = new FormData();

    // Check for empty file
    if(input.value == ""){
        alert("No file uploaded")
        return
    }

    file = input.files[0];

    // Send request
    formData.append("excel_file", input.files[0]);

    // Send Excel file to backend and wait for response
    response = await fetch("/addProducts", {
        method: "POST",
        body: formData,
    });
    response = await response.json()

    // Checkfor error response
    if(response["error"]){
        alert(response["error"])
        return
    }

    // Clear existing DataTable
    table.clear().draw();
    table.destroy();

    // Initialise new DataTable
    table = $('#datatablesSimple').DataTable({
        "ajax": {
           "processing": true,
           "url": "getProducts",
           "dataSrc": "",
           "data": "",
         },
         "columns": [
                 { "data": "ID"},
                 { "data": "name"},
                 { "data": "lowest_price"},
                 { "data": {variations: "variations", variantCount: "variantCount"}, "render": function(data, type, row, meta){
                     table_string = "<table><thead><th>Variation</th><th>Stock</th></thead><tbody>"
                         $.each(data.variations, function(i){
                             table_string += "<tr><td>" + data.variations[i]['variant'] + "</td><td>" + data.variations[i]['stock'] + '</td></tr>'
                         })
                     table_string += "</tbody></table>"
                     return table_string
                 }},
                 { "data": "last_updated"},
             ],
     }); 

    input.value = "" // Clear file data
    $('#productModal').modal('hide')
}
