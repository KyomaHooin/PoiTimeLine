<?php

$data = array_filter(scandir(getcwd()), function ($var) { return preg_match('/^(?!\.).*(?<!\.php)$/', $var); } );

?>

<!doctype html>
<html lang="en">
	<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>Spinning is life</title>
	<link href="../bootstrap.min.css" rel="stylesheet">
	</head>

	<body class="bg-dark">
	<main class"container">

	<!-- HEADER --!>
	<header class="p-3 text-bg-dark">
	<div class="container">
	<div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
	<a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
	<svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap"><use xlink:href="#bootstrap"/></svg>
	</a>

	<ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
	<li><a href="/" class="nav-link px-2 text-secondary">Home</a></li>
	<li><a href="#" class="nav-link px-2 text-white">Archive</a></li>
	<li><a href="#" class="nav-link px-2 text-white">Artist</a></li>
	<li><a href="#" class="nav-link px-2 text-white">Library</a></li>
	<li><a href="#" class="nav-link px-2 text-white">FAQs</a></li>
	<li><a href="#" class="nav-link px-2 text-white">About</a></li>
	</ul>

	<form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search">
	<input type="search" class="form-control form-control-dark text-bg-dark" placeholder="Search..." aria-label="Search">
	</form>

	<div class="text-end">
	<button type="button" class="btn btn-warning">Login</button>
	</div>
	</div>
	</div>
	</header>
	<!-- ARCHIVE --!>
	<div class="row m-2 justify-content-center">
	<div class="col col-md-8">
	<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4 my-md-2">

	<?php

	foreach($data as $dn) {

	echo '<div class="col d-flex align-items-start position-relative align-items-center">';
	echo '<a class="stretched-link" href="/archive/' . $dn . '">';
	echo '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="white" class="bi bi-folder-fill flex-shrink-0 me-2" viewBox="0 0 16 16"><path d="M9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.825a2 2 0 0 1-1.991-1.819l-.637-7a1.99 1.99 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3zm-8.322.12C1.72 3.042 1.95 3 2.19 3h5.396l-.707-.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981l.006.139z"/></svg>';
	echo '</a><div class="text-light"><h3 class="fw-bold fs-4 mb-0">' . $dn . '</h3></div>';
	echo '</div>';

	}

	?>

	</div>
	</div>
	</div>

	</main>
	<script src="../bootstrap.min.js"></script>
	</body>
</html>

