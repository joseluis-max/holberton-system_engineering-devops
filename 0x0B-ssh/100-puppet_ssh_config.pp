# configuration ssh config file
$str = "Host *
  ForwardAgent yes
  ForwardX11 yes
  IdentityFile ~/.ssh/school
"
file {'/etc/ssh/ssh_config':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  content => $str,
  mode    => '0755',
}

