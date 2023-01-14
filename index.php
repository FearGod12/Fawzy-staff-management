<?php
    // inclusions
    include_once('./_header.php'); # import header
    include_once('./_nav.php'); # import navbar

    // PAGE CONTENTS SHOULD BE LOADED BELOW
    load_page($_SESSION['page']); # import page content
    // Remove the comment from the line above when needed.
    
    include_once('./_footer.php'); # import footer
?>