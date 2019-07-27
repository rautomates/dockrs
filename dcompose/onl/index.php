<html>
	<head> 
		<title> Demo </title>
	</head>

	<body>
		<h1> Demo App Compose </h1>
		<ul>
			<?php 
				$json = file_get_contents('http://cms-tools');
				$obj = json_decode($json);
				$products = $obj->products;
				foreach  ($products as $product) {
					echo "<li> $product </li>";
				}

			?>
		</ul>
	</body>
</html>

