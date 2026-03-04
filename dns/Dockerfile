FROM internetsystemsconsortium/bind9:9.18
ADD conf/named.conf /etc/bind/named.conf
ADD zones/db.l2-4.ephec-ti.be /etc/bind/db.l2-4.ephec-ti.be
RUN chown -R bind:bind /etc/bind/
