# configuration ssh config file
$str = "Host *
        ForwardAgent yes
        ForwardX11 yes
        IdentityFile ~/.ssh/holberton
"
file {'ssh config':
  path    => '/etc/ssh/ssh_config',
  content => $str,
}
