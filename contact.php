<?php 

$field_name = $_POST['cf_name'];
$field_email = $_POST['cf_email'];
$field_message = $_POST['cf_message'];

// your email

$mail_to = 'mikenicholls88@gmail.com';

// Subject 

$subject = 'New message from FU-MALARIA site' . $field_name;

//Constructing the body of the message

$body_message = 'From: '.$field_name."\n";
$body_message .= 'E-mail: '.$field_email."\n";
$body_message .= 'Message: '.$field_message;

//Constructing the headers of the message

$headers = "From: $cf_email\r\n";
$headers .= "Reply-To: $cf_email\r\n";

// Defining mail() function and assigning it to a variable $mail_status, which is used below to check whether the mail has been sent or not

$mail_status = mail($mail_to, $subject, $body_message, $headers);

//If the mail() function executed successfully then do the code below

if ($mail_status) { ?>
    <script language="javascript" type="text/javascript">
        // Print a message
        alert('Thank you for the message. We will contact you shortly.');
        // Redirect to some page of the site. 
        window.location = 'index.html';
    </script>
<?php
}

// If the mail() function fails, then execute the following code

else { ?>

    <script language="javascript" type="text/javascript">
        // Print a message
        alert('Message failed. Please, send an email to mikenicholls88@gmail.com');
        // Redirect to some page of the site. 
        window.location = 'index.html';
    </script>

<?php } ?>

 ?>