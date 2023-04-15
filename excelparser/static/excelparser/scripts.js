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

    const datatablesSimple = document.getElementById("datatablesSimple");
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }
});

function addProducts() {
    event.preventDefault();
    input = document.getElementById("excel_file");
    const formData = new FormData();

    file = input.files[0];

    filetype = file.name.split(".").pop();
    console.log(filetype);
    if (filetype !== "xlsx") {
        if (filetype !== "xls") {
            alert("Invalid file type");
            return;
        }
    }

    filesize = Math.round(file.size / 1000000);
    if (filesize > 2) {
        alert("File size greater than 2Mb");
        return;
    }

    formData.append("excel_file", input.files[0]);

    fetch("/addProducts", {
        method: "POST",
        body: formData,
    });

    setTimeout(function(){
        window.location.reload();
     }, 1000);
}
