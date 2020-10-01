#Replace phpp by php
exec{ 'Deleting a p':
      path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
      command => 'sed -i "s/phpp/php/1" /var/www/html/wp-settings.php',
}