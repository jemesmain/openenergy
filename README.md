# openenergy project

Un projet pour effectuer du suivi énergétique ouvert dans les bâtiments.
## Architecture

## Installation

### Capteur - les données sont recueillies
#### Adeunis
#### Lopy

### Gateway - les grandes oreilles sont à l'écoute

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

** Initialisation du dépot logiciel de Chirpstack**
Chirpstack met a disposition un dépot qui est compatible avec les paquets apt d'Ubuntu. Tout d'abord il faut s'assurer que les paquets nécessaire à l'obtention des paquets soient bien installés.
```
sudo apt install apt-transport-https dirmngr

Set up the key for this new repository:

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1CE2AFD36DBCCA00

Add the repository to the repository list by creating a new file:

sudo echo "deb https://artifacts.chirpstack.io/packages/3.x/deb stable main" | sudo tee /etc/apt/sources.list.d/chirpstack.list

Update the apt package cache:

sudo apt update
```
** Installation du ChirpStack Gateway Bridge**

Note: If you intend to run the ChirpStack Gateway Bridge only on gateway(s) themselves, you can skip this step.

Install the package using apt:

sudo apt install chirpstack-gateway-bridge
The configuration file is located at /etc/chirpstack-gateway-bridge/chirpstack-gateway-bridge.toml. The default configuration is sufficient for this guide.

Start the ChirpStack Gateway Bridge service:

# start chirpstack-gateway-bridge
sudo systemctl start chirpstack-gateway-bridge

# start chirpstack-gateway-bridge on boot
sudo systemctl enable chirpstack-gateway-bridge
##### Chirpstack bridge
##### Chirpstack server
##### Chirpstack application server
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

