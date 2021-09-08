# Minimal Linux kernel requirement for NAT

If you are looking for only NAT i.e., you are only interested in Network Address
Translation and not about filtering/mangling, unlike most of the sites, I have
generated minimal kernel configuration file.

> @ -453,7 +453,66 @@  
> \# CONFIG\_IPV6 is not set  
> \# CONFIG\_NETWORK\_SECMARK is not set  
> \# CONFIG\_NETWORK\_PHY\_TIMESTAMPING is not set  
> \-# CONFIG\_NETFILTER is not set  
> +CONFIG\_NETFILTER=y  
> +  
> +CONFIG\_NETFILTER\_NETLINK=y  
> +CONFIG\_NETFILTER\_NETLINK\_LOG=y  
> +CONFIG\_NF\_CONNTRACK=y  
> +CONFIG\_NETFILTER\_XTABLES=y  
> +  
> +CONFIG\_NF\_DEFRAG\_IPV4=y  
> +CONFIG\_NF\_CONNTRACK\_IPV4=y  
> +CONFIG\_IP\_NF\_IPTABLES=y  
> +CONFIG\_NF\_NAT=y  
> +CONFIG\_NF\_NAT\_NEEDED=y  
> \# CONFIG\_IP\_DCCP is not set  
> \# CONFIG\_IP\_SCTP is not set  
> \# CONFIG\_RDS is not set  
>

---

Update on: 18/01/2012
