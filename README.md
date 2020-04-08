# openenergy project

Un projet pour effectuer du suivi énergétique ouvert dans les bâtiments.
## Architecture

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
**DETAIL CONFIGURATION**
TROUBLESHOOTING
##### Chirpstack server
**DETAIL CONFIGURATION**
##### Chirpstack application server
**DETAIL CONFIGURATION**
#### Thingsboard - on gère les tableaux de bord et les alertes
#### Node-red - pour aider au décryptage des message

    

## Securisation
### Certificat
### HTTPS avec Nginx

## Alternatives
### The thing network
### Grafana

## Technical data
### port list

