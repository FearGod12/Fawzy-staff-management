<h1>Employee Data Collection</h1>
<form id="employee-form">
    Upload Passport :<input type="file" id="passport-upload" name="passport-upload" required>
    
    <label for="name">Full Name:</label>
    <input type="text" id="name" name="name" required>
    <br>
    <label for="name">Home Address:</label>
    <input type="text" id="addres" name="address" required>
    <br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" >
    <br>
    <label for="phone">Phone Number:</label>
    <input type="tel" id="phone" name="phone" required><br>
    Gender:
    <select name="gender" id="">
        <option value="male">Male</option>
        <option value="female">Female</option>
    </select>
    <br><br>
    <label for="position">Position:</label>
    <input type="text" id="position" name="position" >
    <label for="dob">Date of Birth:</label>
    <input type="date" id="dob" name="dob" placeholder="mm/dd/yy">
    <br><br>
    Department: <select id="department" name="department" required>
        <option value="front desk">Reception</option>
        <option value="Restaurant">Restaurant</option>
        <option value="Kitchen">Kitchen</option>
        <option value="laundry">laundry</option>
        <option value="Housekeeping">Housekeeping</option>
        <option value="management">management</option>
    </select><br><br>
    <label for="salary">Salary:</label>
    <input type="number" id="salary" name="salary"><br><br>
    <label for="startdate">Start Date:</label>
    <input type="date" id="startdate" name="startdate" placeholder="mm/dd/yy">
    <p style="font-size: 30px;">
        <h2> Guarantor's Section </h2>
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="name">Home Address:</label>
        <input type="text" id="addres" name="address" required>
        <br>
        <label for="name">Business Name/Address:</label>
        <input type="text" id="B-addres" name="B-address" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" >
        <br>
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required><br>
        Gender:
        <select name="gender" id="">
            <option value="male">Male</option>
            <option value="female">Female</option>
        </select><br><br>
        Upload ID :<input type="file" id="ID-upload" name="ID-upload" required>
    
        <br>
        <input type="submit" value="Submit">
    
</form>

<script>
    let form = document.getElementById("passport-form");
    form.addEventListener("submit", function(e) {
    e.preventDefault();
    let file = document.getElementById("passport-upload").files[0];
    let formData = new FormData();
    formData.append("passport", file);

    let xhr = new XMLHttpRequest();
    xhr.open("POST", "upload.php", true);
    xhr.send(formData);
});




    const form1 = document.getElementById("employee-form");
    form.addEventListener("submit", (e) => {
    e.preventDefault();
    let file = document.getElementById("passport-upload").files[0];
    let formData = new FormData();
    formData.append("passport", file);
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const position = document.getElementById("position").value;
    const department = document.getElementById("department").value;
    
    // Send data to server or handle it in some other way here
    console.log("Name: ", name);
    console.log("Email: ", email);
    console.log("Phone: ", phone);
    console.log("Position: ", position);
    console.log("Department: ", department);
    });

</script>