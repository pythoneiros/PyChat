<?php
  # Nome do arquivo da conversa
  $conversa = "historic-1.html";
?>
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>ChatServ 1.2</title>
  <meta http-equiv="refresh" content=1;url="view.php#fim">
  <style type="text/css">
  body { background: #f2f2f2; font-size: 17px; }
  header { margin: 21px 0; text-align: center; }
  section { background: #fff; width: 62%; margin-right: auto; margin-left: auto; padding: 21px; border: 1px solid #ccc; }
  section .aviso { color: #eee; font-size: 14px; background: #555; padding: 5px; }
  section p > span { margin-right: 10px; font-weight: bold; }
  footer { padding: 21px 0; color: #555; text-align: center; font-size: 13px; }
  .cor0 { color: #555; }
  .cor1 { color: #4A89DC; }
  .cor2 { color: #4B0082; }
  .cor3 { color: #D770AD; }
  .cor4 { color: #F6BB42; }
  .cor5 { color: #E9573F; }
  .cor6 { color: #C0392B; }
  .cor7 { color: #663300; }
  .cor8 { color: green; }
  </style>
</head>
<body>
  <header>
    <h2>ChatServer 1.2</h2>   
  </header>
  <section>
    <?php include $conversa; ?>
  </section>
  <footer id="fim">
    ChatServ 1.2 
  </footer>
</body>
</html>