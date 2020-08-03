#killing a process
exec{'killing_process':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => pkill killmenow,
  provider => 'shell'
}