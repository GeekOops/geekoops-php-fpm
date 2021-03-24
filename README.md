# geekoops-php-fpm

Configurable ansible role for setting up `php-fpm` for a webserver (e.g. [nginx](https://github.com/GeekOops/geekoops-nginx)). Works with

- openSUSE Leap 15.2

## TODOs

I just started :-)


## Role Variables



## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: geekoops-php-fpm }

## License

BSD

## Author Information

phoenix

Have a lot of fun!

# Development

## Add githooks

This repository ships pre-commit git hooks that will check the yaml syntax. To configure them do

    git config --local core.hooksPath .githooks/