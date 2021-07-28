<?php

$modules = [
  ["dept" => "Ethical Hacking", "year" => 1, "sem" => "Second Semester", "module" => "Web Development and Databases"],
  ["dept" => "Ethical Hacking", "year" => 1, "sem" => "Second Semester", "module" => "Digital Forensics"],
  ["dept" => "Ethical Hacking", "year" => 1, "sem" => "First Semester", "module" => "Programming & Algorithims"],
  ["dept" => "Computer Science", "year" => 1, "sem" => "First Semester", "module" => "Software Design"],
]
// no code will be added here; it is only an HTML portion with dynamic PHP data injection

 ?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <style media="screen">
    *{
      font-family:sans-serif;

    }
    table {
      text-align: center;
      margin: 0 auto;
      margin-top: 100px
      }
      tbody td{
      padding: 15px;
      background-color: rgb(230, 254, 255)
      }

      thead td{
      padding: 15px;
      background-color: rgb(69, 69, 69);
      color:#fff;
      border: rgb(36, 149, 255)
      }
    </style>
  </head>
  <body>
    <h1 style="text-align:center">Modules Information</h1>

    <table>
      <thead>
        <tr>
          <td>Department</td>
          <td>Year</td>
          <td>Semester</td>
          <td>Module</td>
        </tr>
      </thead>
      <tbody>
        <!--  create a one row (1 tr tag) that has 4 data columns (4 td tags), the row should repeat using a php loop -->

      </tbody>
    </table>


  </body>
</html>
