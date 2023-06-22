<?php
    include_once("./_header.php"); # import header
    include_once("./_nav.php"); # import navigation

    # page content starts here
    load_page($_SESSION['page']); # import ``page`` if exist
    # page content ends here
    include_once("./_footer.php"); # import footer
?>