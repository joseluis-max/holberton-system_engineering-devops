# configuration ssh config file
$str = "Include /etc/ssh/ssh_config.d/*.conf

Host *
        ForwardAgent yes
        ForwardX11 yes
        IdentityFile ~/.ssh/holberton
"
file {'/etc/ssh/ssh_config':
  ensure  => '/etc/ssh/ssh_config',
  content => $str,
  mode    => '0755',
}
