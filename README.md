


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
        <link rel = "stylesheet" type="text/css" href="styler.css">

    </head>
    <body>
        <?php
        include_once 'header.php';

        ?>


        <div class ="container">



            <form action="<?php echo $_SERVER['PHP_SELF'];
                  ?>" method="post" >

                <div class="landl">
                    <img src="login pic.png" width="330px" height="300px"/>
                    <div class="landlsec">
                        <h3> User Login </h3>

                        <table>
                            <tr><td>Username</td><td>Password</td>


                            <tr><td> <input type="text" name="Username" id="Username" value="" /></td><td><input type="password" name="Password" id="Password" value="" /></td><td><input type="submit" name="Login" id="Login" value="Login" /></td></tr>

                        </table>
                        <br>
                        <br>
                        <br>
<div class="info">
                <a href="index.php"> Home |</href>
                <a href ="healp.php"> Help |</href>
                    <a href="about.php" > About |</href>
                        <a href="signup.php"> Sign up |</href>
                            <a href ="Adminlogin.php"> Admin Login </href>

                                    </div>
                    </div>

                </div>

            </form>


            <?php
                if (isset ($_POST['Username'])){
                $db1=mysqli_connect('localhost','root','','laundary');
            $query1 = "select * from reguser";
        $result1 = mysqli_query($db1, $query1);
        while ($row = mysqli_fetch_array($result1)) {
           if (isset ($_POST['Username'])) {
           if ($_POST['Username']==$row['Username'] && $_POST['Password']==$row['Password'])
            header("location:udashboard.php");
           }
        }
                }

            ?>


                                                                                   
            </div>
                                    </body>
<?php
                                    include_once 'foter.php';
                                    ?>
                                    </html>
