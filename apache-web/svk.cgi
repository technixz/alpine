#!/bin/bash 
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Bash as CGI"
echo "</title></head><body style="background-color:black;">"

echo "<h3><tt style=\"text-align:left; color:orange\">"
echo "<center> <tt style=\"text-align:left; color:#00ffff\"> --- System information for host $(hostname -s) --- </tt> </center>" 
echo ""
echo "</tt></h3>"

echo "<h3><tt style=\"text-align:left; color:blue\">"
echo "Memory Info :"
echo "</tt></h3>"
echo "<pre> $(free -m) </pre>"

echo "<h3><tt style=\"text-align:left; color:red\">"
echo "Disk Info : "
echo "</tt></h3>"
echo "<pre> $(df -h|grep -vw 'tmpfs') </pre>"

echo "<h3><tt style=\"text-align:left; color:green\">"
echo "Server IP Address :"
echo "</tt></h3>"
echo "<pre> $(ifconfig) </pre>"

echo "<h3><tt style=\"text-align:left; color:black\">"
echo "<center>######</center>"
echo "<center>###### <tt style=\"text-align:left; color:#2e86c1\"> $(date) </tt> ###### </center>"
echo "<center>######</center>"
echo "</tt></h3>"
echo "</body></html>"

