$TTL 86400
@   IN  SOA ns.l2-4.ephec-ti.be. admin.l2-4.ephec-ti.be. (
            2026033106 ; Serial
            3600       ; Refresh
            1800       ; Retry
            604800     ; Expire
            86400 )    ; Minimum TTL

@   IN  NS  ns.l2-4.ephec-ti.be.

@   IN  A   91.134.138.162
ns  IN  A   91.134.138.162
blog IN CNAME www
mail IN  A   91.134.138.162


www  IN  A     91.134.138.162    ; IP Manager 1
www  IN  A     91.134.137.17     ; IP Manager 2



@   IN  MX  10 mail.l2-4.ephec-ti.be.

@   IN  TXT "v=spf1 mx -all"

_dmarc IN TXT "v=DMARC1; p=none; rua=mailto:admin@l2-4.ephec-ti.be"

mail._domainkey IN TXT ( "v=DKIM1; h=sha256; k=rsa; "
          "p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArSRVrcohRpKTCOjOzZ/eu/+9A3/t9YXDxuCE4Ljs3TFy/mFvmk5T99GqAX+dF2OtT+/xSzVpr/GKLgse2ONKnCqjxLqDH9nWyG89gQ5ptIZjkmHnFvROIZN810/+F6PDMJ72HqSe2iiDoPw3EISHVm986iWWpPnNLJ40lF1+mn/gP4ixQw6mas1oiEFd1wI1WUL08K8qPkFjGd"
          "dsQrOZk0kCwD9e0qdGUhbcmea6n5R8VIcWmYfNIGUgzAqsGddoWsYQcZ/9u/V7CtOlLOAsLCzeP2PkVJbAcCmlLRRYvR/KDLnsL/o9r+ykNoxv9o3taZoG2nOuaulg6WxV32NhtwIDAQAB" )
