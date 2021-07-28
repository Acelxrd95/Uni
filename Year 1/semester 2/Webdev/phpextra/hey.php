<!DOCTYPE html>
<html>

<body>

    <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
        Name1: <input type="text" name="fname">
        <br>
        Name2: <input type="text" name="lname">
        <br>
        <input type="submit">
    </form>

    <?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // collect value of input field
    $name = htmlspecialchars($_REQUEST['fname']);
    $namel = htmlspecialchars($_REQUEST['lname']);
    if (empty($name)) {
        echo "Name is empty";
    } else {
        echo $name;
        echo "<br>";
        echo $namel;

    }

}
?>

</body>

</html>