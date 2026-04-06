# Burp Suite Certificate (HTTPS case)

Must manually add PortSwigger CA certificate to our browser's list of trusted CAs (certificate authorities)

1. Download CA cert: activate Burp Proxy and go to http://burp/cert/
2. Save `cacert.der`, then go to FireFox `about:preferences` and go to `certificates` -> `View Certificates`
3. Import `cacert.der`
4. Trust PortSwigger CA to identify websites

Done