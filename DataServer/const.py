META = [{
        'lookup': 'city',
        'tag': 'city',
        'path': ['names','en'],
        },{
        'lookup': 'continent',
        'tag': 'continent',
        'path': ['names','en'],
        },{
        'lookup': 'continent_code',
        'tag': 'continent',
        'path': ['code'],
        },{
        'lookup': 'country',
        'tag': 'country',
        'path': ['names','en'],
        },{
        'lookup': 'iso_code',
        'tag': 'country',
        'path': ['iso_code'],
        },{
        'lookup': 'latitude',
        'tag': 'location',
        'path': ['latitude'],
        },{
        'lookup': 'longitude',
        'tag': 'location',
        'path': ['longitude'],
        },{
        'lookup': 'metro_code',
        'tag': 'location',
        'path': ['metro_code'],
        },{
        'lookup': 'postal_code',
        'tag': 'postal',
        'path': ['code'],
        }]

PORTMAP_OLD = {
     0:"DoS",        # Denial of Service
    1:"ICMP",        # ICMP
    20:"FTP",        # FTP Data
    21:"FTP",        # FTP Control
    22:"SSH",        # SSH
    23:"TELNET",     # Telnet
    25:"EMAIL",      # SMTP
    43:"WHOIS",      # Whois
    53:"DNS",        # DNS
    80:"HTTP",       # HTTP
    88:"AUTH",       # Kerberos
    109:"EMAIL",     # POP v2
    110:"EMAIL",     # POP v3
    115:"FTP",       # SFTP
    118:"SQL",       # SQL
    143:"EMAIL",     # IMAP
    156:"SQL",       # SQL
    161:"SNMP",      # SNMP
    220:"EMAIL",     # IMAP v3
    389:"AUTH",      # LDAP
    443:"HTTPS",     # HTTPS
    445:"SMB",       # SMB
    636:"AUTH",      # LDAP of SSL/TLS
    1433:"SQL",      # MySQL Server
    1434:"SQL",      # MySQL Monitor
    3306:"SQL",      # MySQL
    3389:"RDP",      # RDP
    5900:"RDP",      # VNC:0
    5901:"RDP",      # VNC:1
    5902:"RDP",      # VNC:2
    5903:"RDP",      # VNC:3
    8080:"HTTP",     # HTTP Alternative
}

PORTMAP = {
    33:"3HD",
    29:"MONO29", 
    32:"THAIRATH",
    3:"TPBS",
    23:"WORKPOINT",
    34:"AMARIN",
    31:"GMMONE",
    27:"CH8",
    22:"NATION",
    1:"TV5",
    30:"MCOT",
    35:"CH7",
    2:"NBT",
    36:"PPTV",
    16:"TNN24",
    18:"NEWTV",
    24:"TRUE4U",
    25:"GMM25",
}
