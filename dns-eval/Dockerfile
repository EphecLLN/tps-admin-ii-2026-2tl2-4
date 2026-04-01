FROM internetsystemsconsortium/bind9:9.18
COPY conf/named.conf /etc/bind/named.conf
COPY zones/db.l2-4.ephec-ti.be /etc/bind/db.l2-4.ephec-ti.be
RUN chmod 755 /etc/bind \
    && chmod 644 /etc/bind/named.conf /etc/bind/db.l2-4.ephec-ti.be
ENTRYPOINT ["/usr/sbin/named"]
CMD ["-g", "-c", "/etc/bind/named.conf"]


