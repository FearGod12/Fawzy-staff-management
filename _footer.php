<footer>
  <div class="container">
    <div class="row">
      <div class="col-md-4">
        <h4>Fawzy Hotel</h4>
        <p>Block vii, plot 1,2,3 Adewumi Layout Off Akinyemi Way, <br> Ring Road, Ibadan, Nigeria</p>
      </div>
      <div class="col-md-4">
        <h4>Contact Us</h4>
        <p>Email: info@fawzyhotel.com</p>
        <p>Phone: +234 810 547 9934</p>
      </div>
      <div class="col-md-4">
        <h4>Follow Us</h4>
        <a href="https://www.facebook.com/fawzyhotel/">Facebook</a>
        <a href="https://www.instagram.com/fawzyhotel/">Instagram</a>
        <a href="https://twitter.com/fawzyhotel">Twitter</a>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <p>Copyright © 2023 Fawzy Hotel. All rights reserved.</p>
      </div>
    </div>
  </div>
</footer>

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