#killing a process
exec {'killing_process':
  command  => 'pkill killmenow'
}