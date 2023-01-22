<!DOCTYPE html>
<html>
  <head>
    <title>Employee Management</title>
    <link rel="stylesheet" type="text/css" href="css/home.css">
    <link rel="stylesheet" href="css/footer.css">
  </head>
  <body>
    <div class="first">
        <img src="images/logo.png" alt="logo">
    <h1 >Fawzy Staff Management Portal</h1>
    </div>
        <nav>
      <ul>
        <li><a href="newstaff.html" id="add-employee-link">Add Employee</a></li>
        <li><a href="#" id="delete-employee-link">Delete Employee</a></li>
        <li><a href="#" id="search-employee-link">Search Employee</a></li>
        <li><a href="#" id="edit-employee-link">Edit Employee</a></li>
        <li><a href="employeelist.html" id="view-employee-list-link">View Employee List</a></li>
        <form>
          <input type="text" id="searchInput" placeholder="Search for an employee...">
          <button type="button" id="searchButton" onclick="search()">Search</button>
        </form>
        <div id="employeeList"></div>
        
      </ul>
    </nav>
    <div id="banner">
      <img src="images/IMG_20230122_143408_664.jpg" alt="fawzy">
      </div>
  </div>
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