# configuration ssh config file
$str = "Include /etc/ssh/ssh_config.d/*.conf

Host *
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
