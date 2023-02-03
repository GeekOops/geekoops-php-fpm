[![Test deployment](https://github.com/GeekOops/geekoops-php-fpm/actions/workflows/CI.yml/badge.svg)](https://github.com/GeekOops/geekoops-php-fpm/actions/workflows/CI.yml)

# geekoops-php-fpm

Configurable ansible role for setting up `php-fpm` for a webserver (e.g. [nginx](https://github.com/GeekOops/geekoops-nginx)). It is intended to use as basis for many PHP projects like [Mediawiki](https://www.mediawiki.org/), [Nextcloud](https://nextcloud.com) or [Lychee](https://lycheeorg.github.io/).

Compatible with

- openSUSE Leap 15.3
- openSUSE Leap 15.4

Due to the very different php configuration on Debian/Ubuntu I'm not planning to port this role to other systems.

## Role Variables

| Value | Description | Default |
|-------|-------------|---------|
| `configure_php_ini` | Configrue the `php.ini` file | `true` |
| `configure_php_fpm` | Configure php-fpm configuration files  | `true` |
| `configure_apparmor` | Configure apparmor configuration files  | `false` |
| `enable_php_fpm` | Enable `php-fpm` service | `true` |
| `apcu_enable` | Enable the [APCu](https://www.php.net/manual/en/book.apcu.php) cache | `false` |
| `apcu_shm_size` | APCu cache size | `32M` |
| `php_memlimit` | PHP memory limit | `128M` |
| `php_uploads` | Enable PHP uploads | `On` |
| `php_maxuploadsize` | Max upload size | `256M` |
| `php_maxuploads` | Max uploads in a request | `20` |
| `php_socket` | Socket for php to listen on | `/run/php-fpm/php-fpm.sock` |
| `php_allowed_clients` | List of addresses (IPv4/IPv6) allowed to connect if `php_socket` is a network address | |
| `php_niceness` | Set the nice priority for the pool processes | not set |
| `php_pm` | Process manager (static, dynamic, ondemand) | dynamic |
| `php_max_children` | Maximum number of child processes | 10 |
| `php_start_servers` | Number of child processes created at startup | 2 |
| `php_min_spare_servers` | Minimum desired number of idle server processes when pm is set to dynamic | 2 |
| `php_max_spare_servers` | Maximum desired number of idle server processes when pm is set to dynamic | 2 |
| `php_process_idle_timeout` | Number of seconds after which an idle process will be killed | 10s |
| `php_max_requests` | If set, the number of requests each child is allowed to execute before being terminated |  |
| `php_chroot` | If set, chroot to this directory as start. If set, you might also need to set `php_chdir = /` |  |
| `php_limit_extensions` | Limit the extension that php-fpm will be parsing | `.php .php3 .php4 .php5 .php7` |
| `php_env_PATH` | Set the `PATH` variable for php-fpm | `/usr/local/bin:/usr/bin:/bin` |
| `php_env_tmp` | Set the tmp directory for php-fpm | `/tmp` |
| `php_open_basedir` | If set, this limits all file operations to the defined directory and below |  |
| `php_disable_functions` | Allows you to disable certain function |  |
| `php_disable_classes` | Allows you to disable certain function |  |
| `php_realpath_cache_size` | If set, determines the size of the realpath cache to be used |  |
| `php_realpath_cache_ttl` If set, sets the duration in seconds to cache realpath information | |
| `php_expose` | Expose that PHP is installed on the server | true |
| `php_max_execution_time` | Maximum execution time for each script in seconds | 0 |
| `php_max_input_time` | Maximum amount of time in seconds each script may spend parsing request data | 60 |
| `php_post_max_size`| Maximum size of POST data that PHP will accept | 8M |
| `php_log_level` | The log level for the `php-fpm` log. Possible Values: alert, error, warning, notice, debug | error |
| `php_max_processes` | Global php-fpm process maximum | 128 |
| `php_events_mechanism` | Specify the event mechanism FPM will use (select, poll, epoll, kqueue, `/dev/poll` or port) | epoll |


## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: jellyfish
      roles:
         - { role: geekoops-php-fpm }

A bit more extended example for our `cuddlefish` server:

    - hosts: cuddlefish
      roles:
         - role: geekoops-php-fpm
            vars:
              apcu_enable: true
              apcu_shm_size: 32M
              php_memlimit: 256M
              php_maxuploadsize: 64M
         

## License

MIT


# Troubleshooting

For your convenience we list some known configuration issues when integrating this role with other roles or with certain systems and how you can resolve them.

## unix socket: Permission denied

Typical symptoms of this issues are error in your `nginx` log file like the following:

    connect() to unix:/run/php-fpm/php-fpm.sock failed (13: Permission denied) while connecting to upstream, client: 192.168.122.1, server: jellyfish, request: "GET /phpinfo.php HTTP/1.1", upstream: "fastcgi://unix:/run/php-fpm/php-fpm.sock:", host: "leap15-4"

This typically means, that your `nginx` webserver has no access to the `php-fpm` socket located in `/run/php-fpm/php-fpm.sock`.

**Solution**

* Ensure that your webserver (e.g. `nginx`) has access to the unix socket. Typically adding `nginx` to the `www` group resolves this issue.

## phpinfo.php returns "Access denied."

A typical request looks like the following:

    $ curl http://leap15-4/phpinfo.php
    Access denied.

In most cases this is an AppArmor or SELinux issue.

First try to set the `php-fpm` AppArmor profile to complain and check if this resolves the issue:

    # aa-complain /etc/apparmor.d/php-fpm

If so, you can use the `yast apparmor` module of YaST to modify the `php-fpm` module to allow access to your php files. Then you can set AppArmor back to enforce.
