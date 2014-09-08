#!/bin/bash

#google test
net_test=`dig www.google.ca`

#dig dirac.cc.kek.jp
dig_info=`dig dirac.cc.kek.jp`

#resolve dirac.cc.kek.jp
ns_info=`nslookup dirac.cc.kek.jp`

#echo "$ns_info"

#return output on route
route_info=`route`

#echo "$route_info"

reslv_info=`cat /etc/resolv.conf`

#echo "$reslv_info"

ip_info=`ifconfig`

mail -c "info" "you@your.gmail.com" <<EOF
dig dirac.cc.kek.jp
$dig_info

nslookup dirac.cc.kek.jp
$ns_info

/bin/route
$route_info

cat /etc/resolv.conf
$reslv_info

ipconfig
$ip_info

google test
$net_test
EOF