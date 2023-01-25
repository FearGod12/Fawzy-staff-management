<div class="footer">
    <div class="container">
        <div class="row">
            <div class="col">
                <p>Copyright © Fawzy Hotel and Event Planners 2023LTD.</p>
            </div>
            <div class="col">
                <p>Contact Us: Block vii, plot 1,2,3 Adewumi layout, off Akinyemi Way, Ring Road, Ibadan. <br> Email: Fawzyhotel@gmail.com <br>Tel. 08105479934</p>
            </div>
            <div class="col">
                <p>Terms and Conditions</p>
            </div>
        </div>
    </div>
</div>
    <script src="script.js"></script>
  </body>
</html>
<script>
    const addEmployeeLink = document.getElementById("add-employee-link");
    const deleteEmployeeLink = document.getElementById("delete-employee-link");
    const searchEmployeeLink = document.getElementById("search-employee-link");
    const editEmployeeLink = document.getElementById("edit-employee-link");
    const viewEmployeeListLink = document.getElementById("view-employee-list-link");
    const content = document.getElementById("content");

    addEmployeeLink.addEventListener("click", function() {
        content.innerHTML = "Add Employee Form Goes Here";
    });

    deleteEmployeeLink.addEventListener("click", function() {
        content.innerHTML = "Delete Employee Form Goes Here";
    });

    searchEmployeeLink.addEventListener("click", function() {
        content.innerHTML = "Search Employee Form Goes Here";
    });

    editEmployeeLink.addEventListener("click", function() {
        content.innerHTML = "Edit Employee Form Goes Here";
    });

    viewEmployeeListLink.addEventListener("click", function() {
        content.innerHTML = "Employee List Goes Here";
});

const employeeList = [
  { name: "John Smith", title: "Manager" },
  { name: "Jane Doe", title: "Developer" },
  // ...
];

function search() {
  const searchInput = document.getElementById("searchInput");
  const searchTerm = searchInput.value;
  const employeeListDiv = document.getElementById("employeeList");
  let employeeListHTML = "";
  
  for (const employee of employeeList) {
    if (employee.name.includes(searchTerm)) {
      employeeListHTML += `<div>${employee.name} - ${employee.title}</div>`;
    }
  }
  
  employeeListDiv.innerHTML = employeeListHTML;
}

</script>