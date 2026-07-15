<?php

session_start();

$id = uniqid();

$FILE_PATH = '/var/www/data/upload/';

$UPLOAD = null;

if (!isset($_SESSION['message'])) { $_SESSION['message'] = null; }

if (isset($_FILES['file'])) {
	if ($_FILES['file']['error'] == 0) {
		# replace slash, space, dot and single quote
		$UPLOAD = preg_replace("/\/| |\.|'/", '_', $_FILES['file']['name']);
		# protect FS
		move_uploaded_file($_FILES['file']['tmp_name'], $FILE_PATH . $UPLOAD . '_' . $id);
		$_SESSION['message'] = 1;
	}

	#PRG
	header('Location: /upload/');
	exit();
}

?>

<!doctype html>
<html lang="cs">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>PK's upload</title>
	<link href="custom.css" rel="stylesheet">
</head>

<body class="bg-light">

<div class="container-md">

<main>

<div class="row py-4 justify-content-center">
<div class="col-md-8">

<?php

if ($_SESSION['message'] == 1) {
	echo '<div class="alert alert-warning alert-dismissible fade show" role="alert">' . 'Done! Thank you..' . '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
	$_SESSION['message'] = null;
}

?>

<div class="text-center"><h2>PK's upload</h2></div>
<br/>
<div class="text-center"><h5>[ please upload anything up to 3GB in total ]</h5></div>
<br/>

<form method="post" action="." enctype="multipart/form-data">

<div class="form-group">
	<input type="file" class="form-control" id="any" name="file">
</div>

<div class="d-grid col-4 mx-auto my-4">
	<button type="submit" class="btn btn-danger">Odeslat</button>
</div>

</form>

<hr/>

</div>
</div>

</main>

<footer class="text-small text-center"><p>&copy; 2026 PTL project</p></footer>

</div>

</body>

</html>

