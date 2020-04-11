# openenergy project

Un projet pour effectuer du suivi énergétique ouvert dans les bâtiments.
## Architecture
**illustration**
## Installation

### Capteur - les données sont recueillies
#### Adeunis
#### Lopy

### Gateway - les grandes oreilles sont à l'écoute
#### Rakwireless RAK7246 LPWAN Developer Gateway - RAK7246 - EU868
#### Lopy Nano Gateway

### Serveur - on stock et on affiche
#### Chirpstack - on gère les élément de notre réseau
##### Chirpstack quickstart
[Chirpstack quickstart guide](https://www.chirpstack.io/guides/debian-ubuntu/ "Chirpstack quick guide in English")

**Installation de programmes complémentaires**
Les trois programmes suivants doivent être installé pour le bon fonctionnement
- Mosquitto: un programme qui implémente le protocole MQTT qui fonctionne sur des messages en publication / subscription.
- Redis: pour le stockage de données transitoire
- PostgreSQL: une base de données

```
sudo apt install mosquitto mosquitto-clients redis-server redis-tools postgresql
``` 
**Initialisation de la base PostgreSQL et des utilisateurs**

Deux utilisateurs avec mots de passe ainsi que deux utilisateurs avec mot de passe, chirpstack_as et chirpstack_ns sont créés. Ils seront repris dans plusieurs des configurations de la gateway, du server et de l'application server.
```
sudo -u postgres psql

Inside this prompt, execute the following queries to set up the databases that are used by the ChirpStack stack components. It is recommended to change the usernames and passwords. Just remember to use these other values when updating the chirpstack-network-server.toml and chirpstack-application-server.toml configuration files. Since these two applications both use the same table to track database upgrades, they must have separate databases.

-- set up the users and the passwords
-- (note that it is important to use single quotes and a semicolon at the end!)

create role chirpstack_as with login password 'dbpassword';
create role chirpstack_ns with login password 'dbpassword';

-- create the database for the servers

create database chirpstack_as with owner chirpstack_as;
create database chirpstack_ns with owner chirpstack_ns;

-- change to the ChirpStack Application Server database

\c chirpstack_as

-- enable the pq_trgm and hstore extensions
-- (this is needed to facilitate the search feature)

create extension pg_trgm;

-- (this is needed to store additional k/v meta-data)

create extension hstore;

-- exit psql

\q
```

**Initialisation du dépot logiciel de Chirpstack**

Chirpstack met a disposition un dépot qui est compatible avec les paquets apt d'Ubuntu. Tout d'abord il faut s'assurer que les paquets nécessaires à l'obtention des paquets soient bien installés.
```
sudo apt install apt-transport-https dirmngr

Set up the key for this new repository:

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1CE2AFD36DBCCA00

Add the repository to the repository list by creating a new file:

sudo echo "deb https://artifacts.chirpstack.io/packages/3.x/deb stable main" | sudo tee /etc/apt/sources.list.d/chirpstack.list

Update the apt package cache:

sudo apt update
```
**Installation du ChirpStack Gateway Bridge**

L'installation du Chispstack Gateway Bridge présente deux modes:
- mode "sécurisé": ou le Gateway bridge est installé sur chacune des Gateway mais pour cela il faut avoir acces aux "paramétrages avancées" de la Gateway. Ce mode va être de plus en plus généralisé attendu que Chirspstack est en train de développer un Gateway OS.
- mode "non-securisé": le Gateway bridge est installé sur le server. C'est le mode à préférer si vous ne voulez pas ou ne pouvez pas modifier le contenu de vos gateways.

*Installation du paquet*
```
sudo apt install chirpstack-gateway-bridge
```

Le fichier de configuration est situé /etc/chirpstack-gateway-bridge/chirpstack-gateway-bridge.toml. Le ficher de configuration par défaut est sufisant pour cette installation.

Pour la configuration détaillée voir la partie chirpstack gateway bridge ci-dessous.

Il y a deux manières de démarrer les service de ce bridge:
- Manuellement:

```sudo systemctl start chirpstack-gateway-bridge```
- au démarrage:
```sudo systemctl enable chirpstack-gateway-bridge```

**Installation du ChirpStack Network Server**
Installation des paquet en utilisant apt apt:

sudo apt install chirpstack-network-server

Le fichier de configuration est situé /etc/chirpstack-network-server/chirpstack-network-server.toml et doit être configuré pour correspondre avec les bases de données, les utilisateur et les mots de passe PostgreSQL. Il doit aussi correspondre aux réglage des fréquence d'émission. Pour l'Europe c'est le EU868 et pour les USA US915. Pour plus d'option voir avec la partie ChirpStack Network Server configuration

Après la modification du fichier de configuration, vous devez redémarrer Chirpstack Network Server et valider qu'il n'y a pas d'erreur.

Il y a deux manières de démarrer les service de ce server:
- Manuellement:
```sudo systemctl start chirpstack-network-server```
- au démarrage
```sudo systemctl enable chirpstack-network-server```

Afin de visualiser les log du network server.
```sudo journalctl -f -n 100 -u chirpstack-network-server```

Pour la configuration détaillée voir la partie chirpstack server ci-dessous.

**Installation de  ChirpStack Application Server**
Installation des paquets en utilisant apt:

```sudo apt install chirpstack-application-server```

le chemin du fichiers de configuration est le suivant /etc/chirpstack-application-server/chirpstack-application-server.toml et doit être mis à jour pour correspondre à la configuration de la base de données PostgreSQL.

Pour la configuration détaillée voir la partie chirpstack application server ci-dessous.

Note: il faut impérativement remplacé le paramètre jwt_secret avec une chaine de sécurité! Voupouvez utiliser la commande suivante openssl rand -base64 32 pour générer une chaine de sécurité secret.

Le ChirpStack Application Server service peut être démarré de deux manières:

- manuellement:
```sudo systemctl start chirpstack-application-server```

- au démarrage:
```sudo systemctl enable chirpstack-application-server```

Afin de voir si il n'y a pas d'erreur vous pouvez visualiser le log de ChirpStack Application Server avec la commande suivante:

```sudo journalctl -f -n 100 -u chirpstack-application-server```


##### Chirpstack bridge
Selon la typologie de votre gateway, deux mode sont disponible pour transmettre les messages:

- Semtech UDP Packet Forwarder c'est le cas qui correspond à la gateway RakWireless
- Basic Station Packet Forwarder
Les instruction détaillées de l'installation sont présente à l'adresse suivante: https://www.chirpstack.io/gateway-bridge/install/debian/

**DETAIL de la CONFIGURATION**
Le détail est présent à l'adresse suivante: https://www.chirpstack.io/gateway-bridge/install/config/
Le fichier de configuration finalisé sur github est ici: Settings/Chirpstack/chirpstack-gateway-bridge/chirpstack-gateway-bridge.toml

Il spécifie:
- que le type choisi est udp paquet forwarder
- qu'il écoute sur le port 1700. Un port mapping pouvant être effectué sur la box de votre FAI c'est vers ce port ou le port correspondant au port mapping qui doit etre spécifié dans les réglages de la gateway.
- que le protocole MQTT est actif sur le port 1883.

**TROUBLESHOOTING**

https://www.chirpstack.io/guides/troubleshooting/gateway/
Il s'agit de verifier que l'on recoive bien des informations de la gateway

Tout d'abord il faut s'assurer que le Semtech Packet Forwarder de la gateway recoive bien des données du capteur. Ainsi on utilise la commande TCP dump pour suivre les messages échangés. Le port doit correspondre à celui de la configuration de ChirpStack Gateway Bridge.
- Lorsqque ChirpStack Gateway Bridge tourne sur la gateway l'instruction suivante vérifiera cela: 
```sudo tcpdump -AUq -i lo port 1700```
- Lorsque ChirpStack Gateway Bridge est installé sur une machine / serveur différents dans ce cas c'est l'intruction suivante:

```sudo tcpdump -AUq port 1700```

On doit constater une réponse équivalente à ci-dessous pour valider le bon fonctionement
```11:42:00.114726 IP localhost.34268 > localhost.1700: UDP, length 12 E..(..@.@."................'.....UZ.....
11:42:00.130292 IP localhost.1700 > localhost.34268: UDP, length 4E.. ..@.@.".....................
```

Si l'instruction TCP dump ne permet pas de constater de message alors il vous faut vérifier la configuration de la gateway local_conf.json à l'aide du manuel technique de votre gateway. Le fichier de configuration devrait contenir les lignes similaires suivantes.
```
{
    "gateway_conf": {
        ...
        "serv_port_down": 1700,
        "serv_port_up": 1700,
        "server_address": "localhost",
        ...
    }
}
```

Ensuite on peut s'assurer que le chirpstack-gateway-bridge recoivent des données.
- journalctl -f -n 100 -u chirpstack-gateway-bridge
- tail -f -n 100 /var/log/chirpstack-gateway-bridge/chirpstack-gateway-bridge.log

On devrait ainsi avoir ce type de contenu à l'écran
```INFO[0013] mqtt: subscribing to topic qos=0 topic=gateway/7276ff002e062c18/command/#

INFO[0267] mqtt: publishing message qos=0 topic=gateway/7276ff002e062c18/event/up
```

Si le contenu de l'écran n'est pas de ce type il faut
- revérifier la configuration de la gateway
- vérifier que le service du ChirpStack Gateway Bridge est en fonctionnement. Pour vérifier on utilise la commande suivante:

```ps aux |grep chirpstack-gateway-bridge
```
Le résultat devrait ressembler à cela:

```root      6403  0.0  0.2  12944  1088 pts/0    S+   12:53   0:00 grep --color=auto chirpstack-gateway-bridge
gateway+ 23060  0.1  2.1 214260 10664 ?        Ssl  Aug30  47:55 /usr/bin/chirpstack-gateway-bridge
```
- Vérifier ChirpStack Gateway Bridge configuration pour s'assurer des réglages machine:port dans le fichier de configuration chirpstack-gateway-bridge.toml.

- Vérifier que ChirpStack Gateway Bridge publie des données sur le broker MQTT. On effectue cela en souscrivant "au fil" concernant les gateway: gateway/# MQTT. on effectue cela avec l'instruction mosquitto_sub:

```mosquitto_sub -v -t "gateway/#"```
Si vous ne voyer aucun message lorsque le capteur envoie des données, il faut alors s'assurer que  ChirpStack Gateway Bridge est autorisé de publier des données sur le sujet MQTT et que le client  mosquitto_sub client est autorisé de souscrire à ce sujet MQTT Ce problème apparait habituellement lorsque vous avec configuré le MQTT Broker afin que les client doivent s'authentifier lors de la connexion.
##### Chirpstack server
Configuration file
Par défaut chirpstack-network-server va regarder dans l'ordre les chemins suivant si l'instruction en comporte pas explicitement la spécification suivante --config:

- chirpstack-network-server.toml (current working directory)
- $HOME/.config/chirpstack-network-server/chirpstack-network-server.toml
- /etc/chirpstack-network-server/chirpstack-network-server.toml

Le fichier de configuration est présent dans la partie settings

Dans le fichier de configuration le minimum a vérifier est le chemin vers la base de données postgres
```# * verify-full - Always SSL (verify that the certification presented by the server was signed by a trusted CA and the server host name matches the one in the certificate)
dsn="postgres://localhost/chirpstack_ns?sslmode=disable"
```

Le détail de toute les options est présent à l'adresse suivante https://www.chirpstack.io/network-server/install/config/


##### Chirpstack application server
Configuration file
Par défaut chirpstack-application-server va regarder dans l'ordre les chemins suivant si l'instruction en comporte pas explicitement la spécification suivante --config:
- chirpstack-application-server.toml (current working directory)
- $HOME/.config/chirpstack-application-server/chirpstack-application-server.toml
- /etc/chirpstack-application-server/chirpstack-application-server.toml

Le fichier de configuration est présent dans la partie settings

Dans le fichier de configuration le minimum a vérifier est le chemin vers la base de données postgres
```# * verify-full - Always SSL (verify that the certification presented by the server was signed by a trusted CA and the server host name matches the one in the certificate)
dsn="postgres://localhost/chirpstack_as?sslmode=disable"
```
Le uuid de l'application serveur ne doit pas être modifié à priori:
```
# Random UUID defining the id of the application-server installation (used by
# ChirpStack Network Server as routing-profile id).
# For now it is recommended to not change this id.
id="6d5db27e-4ce2-4b2b-b5d7-91f069397978"
```
Le protocol mqtt écoute par défaut sur 1883
```# MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
  server="tcp://localhost:1883"
  ```
Ceci peut rentrer en conflit avec un mqtt comme mosquito qui serait déja démarré sur votre machine ou avec celui qui est démarré par thingsboard. Les fichiers de configurations ou tout est installé sur le meme serveur contiennent des valeurs compatibles. (Cf technical data port list si dessous) Les mêmes conflit de port sont valable pour le port qui va etre utilisé sur votre explorateur web.

Le port de l'explorateur web est le 8080 par défaut
```
# This is the API and web-interface exposed to the end-user.
  [application_server.external_api]
  # ip:port to bind the (user facing) http server to (web-interface and REST / gRPC api)
  bind="0.0.0.0:8080"
  ```
Il ne faut pas oublier de remplir la partie JWT secret (cf chirpstack quickstart)
```# JWT secret used for api authentication / authorization
  # You could generate this by executing 'openssl rand -base64 32' for example
  jwt_secret=""
  ```
Commme les différentes partie du serveur sont sur la même machine je ne me suis pas occupé de sécuriser la communication interne comme spécifié. La partie Nginx s'occupe de cela.

Le détail de toute les options est présent à l'adresse suivante https://www.chirpstack.io/application-server/install/config/
#### Thingsboard - on gère les tableaux de bord et les alertes

La procédure d'installation et de configuration est présente à l'adresse suivante https://thingsboard.io/docs/user-guide/install/rpi/ ou dans la partie web_content
Elle se compose des étapes suivantes
 
- 1. Installation de composents tiers Java 8 (OpenJDK)
- 2. Installation des services ThingsBoard
- 3. Configuration de la base de données ThingsBoard
    - 3.1 Installation PostgreSQL 
    - 3.2 Configuration ThingsBoard
- 4. Limitation de la mémoire pour les machine de petite capacité (1GB of RAM)
- 5. Script d'installation
- 6. Démarrage des services ThingsBoard
- 7. Réglages complémentaires
- Troubleshooting

Ce guide décrit l'installation de ThingsBoard sur un Raspberry Pi 3 doté du système d'exploitation Raspbian Buster.

** 1. Installation de composents tiers Java 8 (OpenJDK)**

Le service ThingsBoard tourne sur Java 8. Suivre ces instruction pour installer OpenJDK 8:
```
sudo apt update
sudo apt install openjdk-8-jdk
```
Merci de ne pas oulbié de spécifier dans la configuration que le système d'exploitation doit utiliser par défaut OpenJDK 8. En utilisant la commande suivante vous pouvez spécifier cela:
```
sudo update-alternatives --config java
```
Vous pouvez verifier l'installation avec la commande:
```
java -version
```
Le résultat attendu est le suivant:
```
openjdk version "1.8.0_xxx"
OpenJDK Runtime Environment (...)
OpenJDK 64-Bit Server VM (build ...)
```
** 2. Installation des services ThingsBoard**
Télécharger les paquets d'installation
```
wget https://github.com/thingsboard/thingsboard/releases/download/v2.4.3/thingsboard-2.4.3.deb
```

Installation du service ThingsBoard.
```
sudo dpkg -i thingsboard-2.4.3.deb
```
3. Configuration de la base de données ThingsBoard
     
    
L''équipe ThingsBoard recommande d'utiliser PostgreSQL pour le développement et des environnements de production avec une charge raisonable de  (< 5000 msg/sec).

**- Installation PostgreSQL**
Les instructions ci-dessous vous permettent l'installation de PostgreSQL.
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo service postgresql start
```
Une fois PostgreSQL installé il vous faut créer un nouvel utilisateur / password pour l'utilisateur principal. Les instructions ci-desssous vous permettent d'effectuer cela.
```
sudo su - postgres
psql
\password
\q
```
Appuyer sur “Ctrl+D” pour retourner sur la console de l'utisateur principal afin de créer la base de données  thingsboard DB:
```
psql -U postgres -d postgres -h 127.0.0.1 -W
CREATE DATABASE thingsboard;
\q
```
    **  - Configuration ThingsBoard**

Editer le fichier de configuration ThingsBoard
```
sudo nano /etc/thingsboard/conf/thingsboard.conf
```
Ajouter les lignes suivantes au fichier. Ne pas oublier de remplacer  “PUT_YOUR_POSTGRESQL_PASSWORD_HERE” avec le nom et mot de passe utilisateur choisi.
```
# DB Configuration 
export DATABASE_ENTITIES_TYPE=sql
export DATABASE_TS_TYPE=sql
export SPRING_JPA_DATABASE_PLATFORM=org.hibernate.dialect.PostgreSQLDialect
export SPRING_DRIVER_CLASS_NAME=org.postgresql.Driver
export SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/thingsboard
export SPRING_DATASOURCE_USERNAME=postgres
export SPRING_DATASOURCE_PASSWORD=PUT_YOUR_POSTGRESQL_PASSWORD_HERE
```
**- 4. Limitation de la mémoire pour les machine de petite capacité (1GB of RAM)**
Editer le fichier de configuration ThingsBoard
```
sudo nano /etc/thingsboard/conf/thingsboard.conf
```
Ajouter les lignes suivantes au fichier.
```
# Update ThingsBoard memory usage and restrict it to 256MB in /etc/thingsboard/conf/thingsboard.conf
export JAVA_OPTS="$JAVA_OPTS -Xms256M -Xmx256M"
```
**5. Script d'installation**
Une fois le service ThingsBoard installée et la configuration de la base de données renseignée, il faut executer le script suivant.:
```
# --loadDemo option will load demo data: users, devices, assets, rules, widgets.
sudo /usr/share/thingsboard/bin/install/install.sh --loadDemo

```
** - 6. Démarrage des services ThingsBoard**

Exécuter la commande suivante pour  démarrer ThingsBoard:
```
sudo service thingsboard start
```
Une fois démarré tapé l'adresse suivant sur votre explorateur web:
```
http://localhost:8080/

```
Les logins suivants sont ceux disponnible par défaut si vous avez spécifié –loadDemo pendant le script d'installation:

*Systen Administrator: sysadmin@thingsboard.org / sysadmin*

*Tenant Administrator: tenant@thingsboard.org / tenant*

*Customer User: customer@thingsboard.org / customer*

Vous pouvez toujours changer les mots de passe dans les logins utilisateurs

Merci de bien attendre environ 240 secondes pour que l'interface démarre en particulier pour les machines lentes avec 1-2 CPUs ou 1-2 GB RAM.

** - 7. Réglages complémentaires**

Le fichier de configuration utilisé est présent dans la partie settings.
Du fait que thingsboard est installé sur la même machine que Chirpstack leur port de l'explorateur web sont en conflit sur le 8080
Il vous faut de la meme manière que le fichier de configuration éditer le fichier Thingsboard.yml et le modifier comme indiqué sur le port 8085:
```
# Server bind port
  port: "${HTTP_BIND_PORT:8085}"
```
Le protocole MQTT est aussi en conflit pour des raisons identiques sur le port 8880. Pour Thingsboard vous pouvez le configurer sur le port 8883
```
mqtt:
    # Enable/disable mqtt transport protocol.
    enabled: "${MQTT_ENABLED:true}"
    bind_address: "${MQTT_BIND_ADDRESS:0.0.0.0}"
    bind_port: "${MQTT_BIND_PORT:8883}"
```

**- Troubleshooting**

Si le service Thingsboard ne démarre pas malgré les modifications ci-dessus il vousu faut analyser les éléments plus précisement à l'aide des instructions suivantes:
Les logs de ThingsBoard logs sont enregistré dans le répertoire suivant:
```
/var/log/thingsboard

```
Vous pouvez toujours utiliser la commande suivante pour vérifier les erreur du coté "backend":
```
cat /var/log/thingsboard/thingsboard.log | grep ERROR
```



#### Node-red - pour aider au décryptage des message

    PRE DECODAGE DU PAYLOAD PAR TTN OU CHIRPSTACK CONVERSION EN STRING...

## Securisation
### Certificat
### HTTPS avec Nginx

## Alternatives
### The thing network
### Grafana

## Technical data
### port list

