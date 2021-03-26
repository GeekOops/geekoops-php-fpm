[![Test deployment](https://github.com/GeekOops/geekoops-php-fpm/actions/workflows/CI.yml/badge.svg)](https://github.com/GeekOops/geekoops-php-fpm/actions/workflows/CI.yml)

# geekoops-php-fpm

Configurable ansible role for setting up `php-fpm` for a webserver (e.g. [nginx](https://github.com/GeekOops/geekoops-nginx)). It is intended to use as basis for many PHP projects like [Mediawiki](https://www.mediawiki.org/), [Nextcloud](https://nextcloud.com) or [Lychee](https://lycheeorg.github.io/).

Compatible with

- openSUSE Leap 15.2

Due to the very different php configuration on Debian/Ubuntu I'm not planning to port this role to other systems.

## Role Variables

| Value | Description | Default |
|-------|-------------|---------|
| `configure_php_ini` | Configrue the `php.ini` file | `true` |
| `configure_php_fpm` | Configure php-fpm configuration files  | `true` |
| `enable_php_fpm` | Enable `php-fpm` service | `true` |
| `apcu_enable` | Enable the [APCu](https://www.php.net/manual/en/book.apcu.php) cache | `false` |
| `apcu_shm_size` | APCu cache size | `32M` |
| `php_memlimit` | PHP memory limit | `128M` |
| `php_uploads` | Enable PHP uploads | `On` |
| `php_maxuploadsize` | Max upload size | `256M` |
| `php_maxuploads` | Max uploads in a request | `20` |


## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: jellyfish
      roles:
         - { role: geekoops-php-fpm }

A bit more extended example for our `cuddlefish` server:

    - hosts: jellyfish
      roles:
         - role: geekoops-php-fpm
            vars:
              apcu_enable: true
              apcu_shm_size: 32M
              php_memlimit: 256M
              php_maxuploadsize: 64M
         

## License

MIT

## Author Information

phoenix

Have a lot of fun!

# Development

## Add githooks

This repository ships pre-commit git hooks that will check the yaml syntax. To configure them do

    git config --local core.hooksPath .githooks/