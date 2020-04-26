## le serveur http sur le port 80
server {
      ##listen      1.2.3.4:80 default; ## could not bind to 1.2.3.4
      ##listen      80 default; ## default is duplicated with default server /etc/nginx/site-available/default _> remove default
      listen      80;
      ##server_name example.com www.example.com;
      server_name my_server.securise.com..com www.my_server.securise.com..com;
      ## Redirige le HTTP vers le HTTPS ##
      return 301 https://$server_name$request_uri;
}

## Le serveur https sur le port 1446 pour node-red. N'oubliez pas vote config SSL###
server {
      #access_log  logs/my_server.com/ssl_access.log main;
      #access_log  logs/my_server.com/ssl_access.log;
      #access_log  /var/log/nginx/my_server.com.ssl_access.log;
      #error_log   logs/my_server.com/ssl_error.log;
      #error_log    /var/log/nginx/my_server.com.error.log debug;
      index       index.html;
      root        /usr/local/nginx/html;
      
      ## Début de la config SSL ##
      ##listen      1.2.3.4:1446 ssl;
      listen      1446 ssl;
      #server_name example.com www.example.com;
      server_name my_server.securise.com..com www.my_server.com;
      fastcgi_param HTTPS on;

     ## Redirection de l url avec www vers une url sans www
      if ($host = 'www.my_server.com' ) {
         rewrite  ^/(.*)$  https://my_server.com/$1  permanent;
      }

    ### config SSL - A vous de jouer ###
     ##ssl_certificate      ssl/example.com/example.com_combined.crt;
     ##ssl_certificate_key  ssl/example.com/example.com.key_without_password;
     ssl_certificate /home/pi/openssl/cert/my_server.crt;
     ssl_certificate_key  /home/pi/openssl/cert/my_server.key.pem;
     ssl_protocols        SSLv3 TLSv1 TLSv1.1 TLSv1.2;
     ssl_ciphers RC4:HIGH:!aNULL:!MD5;
     ssl_prefer_server_ciphers on;
     keepalive_timeout    70;
     ssl_session_cache    shared:SSL:10m;
     ssl_session_timeout  10m;

    ## PROXY
      location / {
        add_header           Front-End-Https    on;
        add_header  Cache-Control "public, must-revalidate";
        add_header Strict-Transport-Security "max-age=2592000; includeSubdomains";
        #proxy_pass  http://exampleproxy;
        proxy_pass http://localhost:1880; 

        # 3 next line to prevent node-red connection lost
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
       
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503;
        proxy_set_header        Host            $host;
        proxy_set_header        X-Real-IP       $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
      }
}

## Le serveur https sur le port 1447 pour chirpstack. N'oubliez pas vote config SSL###
server {
      #access_log  logs/my_server.com/ssl_access.log main;
      #access_log  logs/my_server.com/ssl_access.log;
      #access_log  /var/log/nginx/my_server.com.ssl_access.log;
      #error_log   logs/my_server.com/ssl_error.log;
      #error_log    /var/log/nginx/my_server.com.error.log debug;
      index       index.html;
      root        /usr/local/nginx/html;
      
      ## Début de la config SSL ##
      ##listen      1.2.3.4:446 ssl;
      listen      1447 ssl;
      #server_name example.com www.example.com;
      server_name machine.my_server.com www.machine.my_server.com;
      fastcgi_param HTTPS on;

     ## Redirection de l url avec www vers une url sans www
      if ($host = 'www.my_server.com' ) {
         rewrite  ^/(.*)$  https://my_server.com/$1  permanent;
      }

    ### config SSL - A vous de jouer ###
     ##ssl_certificate      ssl/example.com/example.com_combined.crt;
     ##ssl_certificate_key  ssl/example.com/example.com.key_without_password;
     ssl_certificate /home/pi/openssl/cert/my_server.crt;
     ssl_certificate_key  /home/pi/openssl/cert/my_server.pem;
     ssl_protocols        SSLv3 TLSv1 TLSv1.1 TLSv1.2;
     ssl_ciphers RC4:HIGH:!aNULL:!MD5;
     ssl_prefer_server_ciphers on;
     keepalive_timeout    70;
     ssl_session_cache    shared:SSL:10m;
     ssl_session_timeout  10m;

    ## PROXY
      location / {
        add_header           Front-End-Https    on;
        add_header  Cache-Control "public, must-revalidate";
        add_header Strict-Transport-Security "max-age=2592000; includeSubdomains";
        #proxy_pass  http://exampleproxy;
        proxy_pass http://localhost:8080; 

        # 3 next line to prevent node-red connection lost
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
       
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503;
        proxy_set_header        Host            $host;
        proxy_set_header        X-Real-IP       $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
      }
}


## Le serveur https sur le port 1448 pour chirpstack. N'oubliez pas vote config SSL###
server {
      #access_log  logs/my_server.securise.com..com/ssl_access.log main;
      #access_log  logs/my_server.securise.com..com/ssl_access.log;
      #access_log  /var/log/nginx/my_server.com.ssl_access.log;
      #error_log   logs/machine.my_server.com/ssl_error.log;
      #error_log    /var/log/nginx/machine.my_server.com.error.log debug;
      index       index.html;
      root        /usr/local/nginx/html;
      
      ## Début de la config SSL ##
      ##listen      1.2.3.4:446 ssl;
      listen      1448 ssl;
      #server_name example.com www.example.com;
      server_name machine.my_server.com www.machine.my_server.com;
      fastcgi_param HTTPS on;

     ## Redirection de l url avec www vers une url sans www
      if ($host = 'www.machine.my_server.com' ) {
         rewrite  ^/(.*)$  https://machine.my_server.com/$1  permanent;
      }

    ### config SSL - A vous de jouer ###
     ##ssl_certificate      ssl/example.com/example.com_combined.crt;
     ##ssl_certificate_key  ssl/example.com/example.com.key_without_password;
     ssl_certificate /home/pi/openssl/cert/my_server.crt;
     ssl_certificate_key  /home/pi/openssl/cert/my_server.key.pem;
     ssl_protocols        SSLv3 TLSv1 TLSv1.1 TLSv1.2;
     ssl_ciphers RC4:HIGH:!aNULL:!MD5;
     ssl_prefer_server_ciphers on;
     keepalive_timeout    70;
     ssl_session_cache    shared:SSL:10m;
     ssl_session_timeout  10m;

    ## PROXY
      location / {
        add_header           Front-End-Https    on;
        add_header  Cache-Control "public, must-revalidate";
        add_header Strict-Transport-Security "max-age=2592000; includeSubdomains";
        #proxy_pass  http://exampleproxy;
        proxy_pass http://localhost:8085; 

        # 3 next line to prevent node-red connection lost
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
       
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503;
        proxy_set_header        Host            $host;
        proxy_set_header        X-Real-IP       $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
      }
}


