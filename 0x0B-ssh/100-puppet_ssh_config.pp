# configuration ssh config file
$str = "Include /etc/ssh/ssh_config.d/*.conf

Host *
        ForwardAgent yes
        ForwardX11 yes
        IdentityFile ~/.ssh/holberton
"
file {'ssh config':
  path    => '/etc/ssh/ssh_config',
  content => $str,
  mode    => '0755',
}
