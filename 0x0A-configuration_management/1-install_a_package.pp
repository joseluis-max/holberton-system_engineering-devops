# Installing a package
package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gen',
  source => 'https://rubygems.org/',
}
