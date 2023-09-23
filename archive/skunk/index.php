<?php

$data = array_filter(scandir(getcwd()), function ($var) { return preg_match('/.*\.json/', $var); } );
$name = array_map(function ($var) { return explode('.', $var)[0]; }, $data);

?>

<!doctype html>
<html lang="en">
	<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>Spinning is life</title>
	<link href="../../bootstrap.min.css" rel="stylesheet">
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
	<li><a href="/archive" class="nav-link px-2 text-white">Archive</a></li>
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
	<div class="col col-md-7">

<?php
	foreach($name as $fn) {

	$jsn = json_decode(file_get_contents($fn . '.json'), true);

	echo '<div class="card my-3 bg-dark border">';
	echo '<div class="card-body row g-3">';

	echo '<div class="col col-md-6 d-flex align-items-center">';
	echo '<img src="' . $fn . '.png' . '" class="mx-auto" alt="image">';
	echo '</div>';

	echo '<div class="col">';
	echo '<table class="table table-dark table-borderless table-sm m-0"><tbody>';
	echo '<tr><td class="align-middle text-end">';
	echo '<a href="' . $fn . '.tgz.enc' . '" class="link-warning link-underline-opacity-0"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#ffc107" class="bi bi-download" viewBox="0 0 16 16"><path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/><path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/></svg></a>';
	echo '</td><td>';
	echo '<h5 class="my-2">' . $jsn['name'] . '</h5>';
	echo '<tr><td class="text-end">Date:</td><td>' . $jsn['date'] . '</td></tr>';
	echo '<tr><td class="text-end">Size:</td><td>' . $jsn['size'] . ' Mb</td></tr>';
	echo '<tr><td class="text-end">Duration:</td><td>' . $jsn['duration'] . ' min</td></tr>';

	echo implode(', ', array_map(function ($var) {
		return '<tr><td class="text-end">Location:</td><td>' . $var . '</td></tr>';
	}, $jsn['location']));
	
	echo '<tr><td class="text-end">Artist:</td><td>';

	echo implode(', ', array_map(function ($var) {
		return '<a target="_blank" href="/artist/#' . $var . '" class="link-warning link-underline-opacity-0">' . $var . '</a>';
	}, $jsn['artist']));
	
	echo '</td></tr>';
	
	echo implode(', ', array_map(function ($var) {
		return '<tr><td class="text-end">Music:</td><td>' . $var . '</td></tr>';
	}, $jsn['music']));
	
	echo '</tbody></table>';
	echo '</div>';
	echo '</div>';

	if (!empty($jsn['meta'])) {
		echo '<div class="row mx-2 mb-2">';
		echo '<div class="col d-flex flex-wrap align-items-center text-light">';
		foreach ($jsn['meta'] as $meta) {
			echo '<div class="btn btn-outline-light m-1">'. $meta . '</div>';
		}
		echo '</div>';
		echo '</div>';
	}

	echo '</div>';
	}
?>

	</div>
	</div>

	</main>
	<script src="../../bootstrap.min.js"></script>
	</body>
</html>
