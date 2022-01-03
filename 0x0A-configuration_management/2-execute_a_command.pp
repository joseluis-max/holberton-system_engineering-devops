# Killing a process
exec {  'pkill killmenow':
  command => 'pkill --signal SIGTERM killmenow',
  path    => ['/usr/bin/'],
}

