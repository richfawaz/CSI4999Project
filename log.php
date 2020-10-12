<!DOCTYPE html>

<html>
  <head>
    <style>
      .header {
        height: 80px;
        background-color: black;
        border-top: 2px solid gold;
		color: gold;
      }
	  
	  .nav {
	  height: 30px;
	  font-size: 25px;
	  font-family: "Courier New", Courier, monospace;
	  background-color: gold;
	  }

      .search {
		padding-top: 10px;
		border-bottom: 2px solid gold;
        height: 30px;
        background-color: black;
		color: gold;
		
      }

      .body {
        border-top: 2px solid black;
        height: 3000px;
        background-color: #A9E3F0;
		padding: 15px;
      }
	  
	  .intro {
	 width: 850px;
	  }

      .footer {
        height: 100px;
        border-top: 2px solid gold;
        background-color: black;
        color: white;
      }
	  
	  .contact {
	  color: white;
	  float: left;
	  padding: 3px;
	 width: 250px;
	  }
	  
	  .copyright {
	display: block;
	margin: auto;
    width: 250px;
	  }
	  
	  .follow {
	  width: 250px;
	  color: white;
	  float: right;
	  padding: 3px;
	  }
	  
    </style>
  </head>
  <body>

    <!-- This is the div for the header -->
    <div class=header>
      <center>
        <h1>
          Weather Pi
        </h1>
      </center>
    </div>
	<div class=nav>
	<center>
	<a href="http://localhost/main.html" style="text-decoration: none; font-weight: bold; color: black;">Home |</a>
	
	<a href="http://localhost/about.html" style="text-decoration: none; font-weight: bold; color: black;">About |</a>
	<a href="http://localhost/productpost.html" style="text-decoration: none; font-weight: bold; color: black;">Log |</a>
	<a href="http://localhost/loginsignup.html" style="text-decoration: none; font-weight: bold; color: black;">Logout</a>
	</center>
	</div>

    <!-- This is the div for the search bar -->
      <div class=search>
        <center>
            <form action="http://localhost/pullproduct.php" method="post">
            Search for entries: 
            <input type="text" name="search" value="">
            <input type="submit" value="Search">
          </form>
        </center>
      </div>  
	  
	   <!-- This is the div for the body -->
	   <div class=body> 
	   
	   	 <?php

//This config file ls for connecting to the database
//include ("connect.php");
$user = "root";
$password = "";
$host = "localhost";
$dbname = "weather pi";


$con = mysqli_connect($host, $user, $password, $dbname);
// Check connection
if (!$con) {
  die("Connection failed: " . mysqli_connect_error());
}

$sql= "SELECT * FROM dht22";
$result = $con->query($sql);
//$image = "SELECT image FROM products";
//$results= $con->query($sql);


if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
		echo "<center>"; //<img src='uploads/".$row["image"]."' width=200><br>";
        echo "" . $row["id"]. "    " . $row["timestamp"]. "    " . $row["temperature"]. "*F    " . $row["humidity"] . "% <br><br>";
		echo "</center>";
    }
} else {
    echo "0 results";
}

$sql= "SELECT * FROM images";
$result = $con->query($sql);
//echo "" . $row["image"]. "- $" . $row["timestamp"]. " <br> " . $row[""]. " <br><br>";

$con->close();


?>
     </div> 
	 
    <!-- This is the div for the footer -->
    <div class=footer>
	
	<div class=contact>
	<br>
	<u>change</u><br>
	change<br> 
	change
	</div>
	<center>
	<div class=copyright>
	<center>
	change
</center>
</div>
</center>
      <div class=follow>
        <center>
          <u>Follow us on social media!</u> <br>
        <a href="https://www.facebook.com">
<img border="0" alt="Facebook" src="https://cdn.clipart.email/5b89a96f154a8105d767153819cc222b_facebook-logos-png-images-free-download_2000-2000.png" width="50" height="50">
</a>
<a href="https://www.twitter.com">
<img border="0" alt="Twitter" src="https://cdn.clipart.email/fcf0df581fb3270b21dc370803b034ad_logo-twitter-circle-png-transparent-image-47449-free-icons-and-_2267-2267.png" width="50" height="50">
</a>
</center>
      </div>
	  
    </div>
  </body>
</html>
<!DOCTYPE html>
