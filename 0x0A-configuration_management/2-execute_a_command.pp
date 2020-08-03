#killing a process
exec {'killing_process':
  path    => '/usr/bin/',
  command => 'pkill killmenow',
}