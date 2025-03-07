# Description #

data2label is a tool that uses the check**mk** Multisite and REST APIs to set host labels based on information from the monitoring system (e.g. HW/SW-inventory).

data2label queries a Multisite view (which has to contain at least a column with host names) and sets labels by using a mapping from a configuration file.

# Prequisites #

data2label needs the [checkmkapi](https://github.com/HeinleinSupport/check_mk_extensions/tree/cmk2.0/check_mk_api) Python module.

# Usage #

    data2label.py --help
	usage: data2label.py [-h] -s URL -u USERNAME -p PASSWORD -c CONFIG [-d]
    
    optional arguments:
	  -h, --help            show this help message and exit
	  -s URL, --url URL     URL to Check_MK site
      -u USERNAME, --username USERNAME
                            name of the automation user
      -p PASSWORD, --password PASSWORD
                            secret of the automation user
      -c CONFIG, --config CONFIG
                            Path to config file
      -d, --dump            Dump unique values from the view

The config file contains a Python data structure (a dictionary) with four or five keys: view_name, labelmap, label_prefix, label_value and optional args. The labelmap is a dictionary where the keys are the columns from the view and the values are again dictionaries where the keys are regular expressions that should match the content from the view's column and the value is a list of label names.

Example:

    {
        'view_name': 'inv_hosts_cpu',
        'labelmap': {
            'inv_software_os_name': {
                'centos'                       : [u'redhat', u'linux'],
                'debian'                       : [u'debian', u'linux'],
                'suse'                         : [u'suse', u'linux'],
                'ubuntu'                       : [u''ubuntu', u'linux'],
                'xenserver'                    : [u'redhat', u'linux'],
                'Microsoft Windows 7'          : [u'win7', u'windows'],
                'Microsoft Windows Server 2008': [u'win2008', u'windows'],
                'Microsoft Windows Server 2012': [u'win2012', u'windows'],
                'Microsoft Windows Server 2016': [u'win2016', u'windows'],
            },
        }
        'label_prefix': {
            'inv_software_os_name': u'opsys/',
        },
        'label_value': {
            'inv_software_os_name': u'yes',
        },
    }
    
This would set the host labels 'opsys/redhat:yes' and 'opsys/linux:yes' on any Host that matches 'centos' in the Operating System column of the 'CPU Related Inventory of all Hosts' view.

An additional key 'args' may exist in the configuration dictionary which defines view parameters. E.g.:
    
    {
        'view_name': 'invswpac_search',
        'args': {
            'filled_in': 'filter',
            'invswpac_name': '^(apache2|chrony|cups|docker\.io|docker|docker-ce|docker-engine|dovecot.*|mailman|memcached|nginx|ntp|postgresql-[0-9.]+|postgresql-server|postfix)$',
        },
        'labelmap': {
            'invswpac_name': {
                'apache2': [u'apache', u'webserver'],
                'chrony': [u'chrony'],
                'cups': [u'cups'],
                'docker': [u'docker'],
                'dovecot': [u'dovecot'],
                'dovecot.*-imapd': [u'dovecot-imapd'],
                'dovecot.*-pop3d': [u'dovecot-pop3d'],
                'mailman': [u'mailman'],
                'memcached': [u'memcached'],
                'nginx': [u'nginx', u'webserver'],
                'ntp': [u'ntp'],
                'postfix': [u'postfix', u'mta'],
                'postgresql': [u'postgresql'],
            },
        },
        'label_prefix': {
            'invswpac_name': u'software/',
        },
        'label_value': {
            'invswpac_name': u'installed',
        },
    }

The command line switch '-d' dumps all unique values from the view for easier configuration.
