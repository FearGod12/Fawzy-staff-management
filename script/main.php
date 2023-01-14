<?php
    // This script will handle all HTTP requests
    session_start(); # start a user session

    if(!(isset($_SESSION['page']))) # load default page
    {
        $_SESSION['page'] = '__home';
    }
    else if (isset($_REQUEST['page'])) # else if page is defined in the url (GET or POST)
    {
        $_SESSION['page'] = $_REQUEST['page'];
        reload();
    }

    function load_page($page) # import ``page`` if exist
    {
            include_once($page.".php");
    }

    function reload()
    {
        header('location: ../');
    }
?>