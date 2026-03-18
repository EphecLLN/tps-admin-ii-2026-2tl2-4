$TTL 86400
@   IN  SOA ns.l2-4.ephec-ti.be. admin.l2-4.ephec-ti.be. (
            2026031108 ; Serial (on l'augmente encore)
            3600       ; Refresh
            1800       ; Retry
            604800     ; Expire
            86400 )    ; Minimum TTL

@   IN  NS  ns.l2-4.ephec-ti.be.

@   IN  A   91.134.138.162
ns  IN  A   91.134.138.162
www IN  A   91.134.138.162
blog IN CNAME www

mail    IN    A    91.134.138.162

@       IN      MX  10  mail.l2-4.ephec-ti.be.
