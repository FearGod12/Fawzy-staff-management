<div class="first">
    <img src="images/logo.png" alt="logo">
</div>
<nav>
    <ul>
        <li><a href="./script/main.php?page=__home" id="dashboard">Dashboard</a></li>
        <li><a href="./script/main.php?page=__newstaff" id="add-employee-link">Add Employee</a></li>
        <li><a href="#" id="delete-employee-link">Delete Employee</a></li>
        <li><a href="#" id="search-employee-link">Search Employee</a></li>
        <li><a href="#" id="edit-employee-link">Edit Employee</a></li>
        <li><a href="./script/main.php?page=__employeelist" id="view-employee-list-link">View Employee List</a></li>
        <form>
            <input type="text" id="searchInput" placeholder="Search for an employee...">
            <button type="button" id="searchButton" onclick="search()">Search</button>
        </form>
        <div id="employeeList"></div>
    </ul>
</nav>