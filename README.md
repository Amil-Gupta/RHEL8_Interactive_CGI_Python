# RHEL8_Interactive_CGI_Python
Upload the menu.py file into the cgi-bin directory of your apache httpd server(or the respective directory of another server-hosting software)
Give sudo privileges to "apache" with NOPASSWD
Works best if Docker is installed on the system
To access this code via browser, use the format "http://< server's public I.P. >/cgi-bin/menu.py?ord=<sentence separated by '+' signs >&val=< see the program for details>&name=< see the program for details >"
