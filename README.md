
- [1. Openenergy project](#1-openenergy-project)
  - [1.1. Architecture](#11-architecture)
  - [1.2. Implémentation serveur Debian: Echinix](#12-implémentation-serveur-debian-echinix)
    - [1.2.1. Installation de Gnome](#121-installation-de-gnome)
    - [1.2.2. Clients de connexion distante](#122-clients-de-connexion-distante)
  - [1.3. Implémentation sur Raspberry Pi 3b](#13-implémentation-sur-raspberry-pi-3b)
    - [1.3.1. SSH 2 factor authentification](#131-ssh-2-factor-authentification)
    - [1.3.2. RealVNC 2 factor authentification](#132-realvnc-2-factor-authentification)
    - [1.3.3. Filezilla 2 factor authentification](#133-filezilla-2-factor-authentification)
- [2. Capteur et gateway](#2-capteur-et-gateway)
  - [2.1. Gateway - les grandes oreilles sont à l'écoute](#21-gateway---les-grandes-oreilles-sont-à-lécoute)
    - [2.1.1. Gateway parametrage chirpstack](#211-gateway-parametrage-chirpstack)
    - [2.1.2. gateway parametrage TTN](#212-gateway-parametrage-ttn)
    - [2.1.3. Rakwireless RAK7246 LPWAN Developer Gateway - RAK7246 - EU868](#213-rakwireless-rak7246-lpwan-developer-gateway---rak7246---eu868)
    - [2.1.4. Lopy Nano Gateway](#214-lopy-nano-gateway)
  - [2.2. Capteur - les données sont recueillies](#22-capteur---les-données-sont-recueillies)
    - [2.2.1. Installation capteur ADEUNIS](#221-installation-capteur-adeunis)
    - [2.2.2. Installation capteur NKE Watteco FlashO](#222-installation-capteur-nke-watteco-flasho)
    - [2.2.3. Lopy as a device](#223-lopy-as-a-device)
  - [2.3. Codage Decodage Capteur: les Codec](#23-codage-decodage-capteur-les-codec)
    - [2.3.1. modification du decodage pour chirpstack -\> thingsboard](#231-modification-du-decodage-pour-chirpstack---thingsboard)
    - [2.3.2. Codage Decodage Capteur Codec ADEUNIS](#232-codage-decodage-capteur-codec-adeunis)
  - [2.4. Codage Decodage Capteur Codec NKE](#24-codage-decodage-capteur-codec-nke)
  - [2.5. Recuperation des données: le protocole MQTT](#25-recuperation-des-données-le-protocole-mqtt)
- [3. Serveur - on stock et on affiche](#3-serveur---on-stock-et-on-affiche)
  - [3.1. LoRaWAN Network Server (LNS)Chirpstack - on gère les élément de notre réseau](#31-lorawan-network-server-lnschirpstack---on-gère-les-élément-de-notre-réseau)
    - [3.1.1. Chirpstack quickstart](#311-chirpstack-quickstart)
    - [3.1.2. Chirpstack bridge](#312-chirpstack-bridge)
    - [3.1.3. Chirpstack Bridge TROUBLESHOOTING](#313-chirpstack-bridge-troubleshooting)
    - [3.1.4. Chirpstack server](#314-chirpstack-server)
    - [3.1.5. Chirpstack application server](#315-chirpstack-application-server)
  - [3.2. Thingsboard - on gère les tableaux de bord et les alertes](#32-thingsboard---on-gère-les-tableaux-de-bord-et-les-alertes)
    - [3.2.1. Intégration Thingsboard - Chirpstack](#321-intégration-thingsboard---chirpstack)
    - [3.2.2. Thingsboard TROUBLESHOOTING](#322-thingsboard-troubleshooting)
      - [3.2.2.1. ERROR o.s.w.s.s.s.DefaultHandshakeHandler - Handshake failed due to invalid Upgrade header: null](#3221-error-oswsssdefaulthandshakehandler---handshake-failed-due-to-invalid-upgrade-header-null)
      - [3.2.2.2. Error HikaryPool](#3222-error-hikarypool)
      - [3.2.2.3. Error lwM2MServiceImpl](#3223-error-lwm2mserviceimpl)
      - [3.2.2.4. Error jdbc connection / connection refused](#3224-error-jdbc-connection--connection-refused)
  - [3.3. Node-red - pour aider au décryptage des messages](#33-node-red---pour-aider-au-décryptage-des-messages)
    - [3.3.1. Installation](#331-installation)
    - [3.3.2. PRE DECODAGE DU PAYLOAD PAR TTN OU CHIRPSTACK CONVERSION EN STRING](#332-pre-decodage-du-payload-par-ttn-ou-chirpstack-conversion-en-string)
    - [3.3.3. Exemple de Flux / Flow nodered](#333-exemple-de-flux--flow-nodered)
  - [3.4. Securisation](#34-securisation)
    - [3.4.1. Sécurisation de Node-Red](#341-sécurisation-de-node-red)
    - [3.4.2. Sécurisation de Chirpstack](#342-sécurisation-de-chirpstack)
    - [3.4.3. Sécurisation de ThingsBoard](#343-sécurisation-de-thingsboard)
    - [3.4.4. Génération manuelle des Certificats pour le protocole https](#344-génération-manuelle-des-certificats-pour-le-protocole-https)
    - [3.4.5. HTTPS avec Nginx](#345-https-avec-nginx)
      - [3.4.5.1. Installation de Nginx](#3451-installation-de-nginx)
      - [3.4.5.2. Configurer Nginx pour utiliser une connexion SSL](#3452-configurer-nginx-pour-utiliser-une-connexion-ssl)
      - [3.4.5.3. Configuration du fichier hosts](#3453-configuration-du-fichier-hosts)
      - [3.4.5.4. Autre fichier de configuration de Nginx](#3454-autre-fichier-de-configuration-de-nginx)
    - [3.4.6. Nginx et démarrage des services](#346-nginx-et-démarrage-des-services)
    - [3.4.7. Oauth2-Proxy: Nginx et 2 facteur authentication](#347-oauth2-proxy-nginx-et-2-facteur-authentication)
    - [3.4.8. Oauth2-Proxy: service sur RaspberryPi](#348-oauth2-proxy-service-sur-raspberrypi)
    - [3.4.9. frontend: login](#349-frontend-login)
    - [3.4.10. frontend: Cartographie / Leaflet / Progressive web app](#3410-frontend-cartographie--leaflet--progressive-web-app)
      - [3.4.10.1. Debugage smartphone / android](#34101-debugage-smartphone--android)
      - [3.4.10.2. mongodb et cartographie](#34102-mongodb-et-cartographie)
- [4. Docker Architecture](#4-docker-architecture)
  - [4.1. install](#41-install)
  - [4.2. Change Docker’s root dir](#42-change-dockers-root-dir)
  - [4.3. Docker-compose](#43-docker-compose)
  - [4.4. Docker developement](#44-docker-developement)
    - [4.4.1. Nginx container](#441-nginx-container)
    - [4.4.2. Cerbot nginx container](#442-cerbot-nginx-container)
      - [4.4.2.1. certbot nginx container TROUBLESHOOTING](#4421-certbot-nginx-container-troubleshooting)
    - [4.4.3. Oauth2-proxy container](#443-oauth2-proxy-container)
    - [4.4.4. mongo / mongo-express container](#444-mongo--mongo-express-container)
    - [4.4.5. Nodejs container](#445-nodejs-container)
    - [4.4.6. Nodered Container](#446-nodered-container)
    - [4.4.7. Thingsboard container](#447-thingsboard-container)
      - [4.4.7.1. Thingsboard container TROUBLESHOOTING](#4471-thingsboard-container-troubleshooting)
        - [4.4.7.1.1. ERROR lwM2M](#44711-error-lwm2m)
    - [4.4.8. Grafana container](#448-grafana-container)
    - [4.4.9. Chirpstack container](#449-chirpstack-container)
    - [4.4.10. XTRMUS XTR container](#4410-xtrmus-xtr-container)
- [5. KUBERNETES](#5-kubernetes)
  - [5.1. Install Kubetcl](#51-install-kubetcl)
  - [5.2. install minikube](#52-install-minikube)
  - [5.3. install Helm option](#53-install-helm-option)
    - [5.3.1. From Apt (Debian/Ubuntu)](#531-from-apt-debianubuntu)
    - [5.3.2. from snap](#532-from-snap)
  - [5.4. install Kompose docker-compose vers kubenetes](#54-install-kompose-docker-compose-vers-kubenetes)
  - [5.5. Kubernetes course](#55-kubernetes-course)
  - [5.6. kubernetes cert-manager](#56-kubernetes-cert-manager)
  - [5.7. kubernetes chirpstack](#57-kubernetes-chirpstack)
  - [5.8. UDP tunnelling dans miniKube](#58-udp-tunnelling-dans-minikube)
- [6. various linux command](#6-various-linux-command)
- [7. Alternatives](#7-alternatives)
  - [7.1. The thing network](#71-the-thing-network)
  - [7.2. Grafana](#72-grafana)
- [8. Technical data](#8-technical-data)
  - [8.1. port list](#81-port-list)
  - [8.2. Graphique Path](#82-graphique-path)
  - [8.3. LGM Centrale solaire du lycée du Grésivaudan](#83-lgm-centrale-solaire-du-lycée-du-grésivaudan)
  - [8.4. INPG acepi polygone pulse atex](#84-inpg-acepi-polygone-pulse-atex)

# 1. Openenergy project



Un projet pour effectuer du suivi énergétique avec des logiciels ouverts dans le secteur du bâtiment.

## 1.1. Architecture
---

**Illustration:**
Se référer au diagramme suivant: openenergy_architecture.jpg
Le pdf présent à l'adresse suivante openenergy.bicyclopresto.fr peut être consulté.

## 1.2. Implémentation serveur Debian: Echinix 
---

Le serveur Echinix est déployé sur un OS Debian 12

  ### 1.2.1. Installation de Gnome
  ---

pour installer gnome
sudo apt install tasksel
sudo tasksel
sudo apt-get install task-gnome-desktop

pour demarrer gnome automatiquement
sudo update-alternatives --config x-session-manager


  ### 1.2.2. Clients de connexion distante
  ---
Le protocole ssh est utilisé pour une connexion terminale distante.
Le protocole sshfs permet de monter un répertoire distant dans l'arborescence locale.
sshfs user@hostname:/remote_directory /local_directory -o follow_symlinks
Le logiciel Remmina permet de ce connecter via le protocole RDP ie. remote desktop protocol.


## 1.3. Implémentation sur Raspberry Pi 3b
---
Pour les administrateur le Raspberry Pi peut être accédé via SSH et RealVNC

### 1.3.1. SSH 2 factor authentification
---
**source**: https://www.raspberrypi.org/blog/setting-up-two-factor-authentication-on-your-raspberry-pi/

Especially if you intend to make the server accessible from the Internet, you probably want to enable two-factor authentication (2FA) using Time-based One-Time Password (TOTP).

What is two-factor authentication?
Two-factor authentication is an extra layer of protection. As well as a password, “something you know,” you’ll need another piece of information to log in. This second factor will be based either on “something you have,” like a smart phone, or on “something you are,” like biometric information.

We’re going to go ahead and set up “something you have,” and use your smart phone as the second factor to protect your Raspberry Pi.

Updating the operating system
The first thing you should do is make sure your Raspberry Pi is up to date with the latest version of Raspbian. If you’re running a relatively recent version of the operating system you can do that from the command line:
```
$ sudo apt-get update
$ sudo apt-get full-upgrade
```
If you’re pulling your Raspberry Pi out of a drawer for the first time in a while, though, you might want to go as far as to install a new copy of Raspbian using the new Raspberry Pi Imager, so you know you’re working from a good image.

**Enabling Secure Shell:**
The Raspbian operating system has the SSH server disabled on boot. However, since we’re intending to run the board without a monitor or keyboard, we need to enable it if we want to be able to SSH into our Raspberry Pi.

The easiest way to enable SSH is from the desktop. Go to the Raspbian menu and select “Preferences > Raspberry Pi Configuration”. Next, select the “Interfaces” tab and click on the radio button to enable SSH, then hit “OK.”

You can also enable it from the command line using systemctl:
```
$ sudo systemctl enable ssh
$ sudo systemctl start ssh
```
Alternatively, you can enable SSH using raspi-config, or, if you’re installing the operating system for the first time, you can enable SSH as you burn your SD Card.

Enabling challenge-response
Next, we need to tell the SSH daemon to enable “challenge-response” passwords. Go ahead and open the SSH config file:

$ sudo nano /etc/ssh/sshd_config
Enable challenge response by changing ChallengeResponseAuthentication from the default no to yes.


Editing /etc/ssh/ssd_config.
```
# Change to yes to enable challenge-response passwords (beware issues with
# some PAM modules and threads)
ChallengeResponseAuthentication yes
```

Then restart the SSH daemon:
```
$ sudo systemctl restart ssh
```
It’s good idea to open up a terminal on your laptop and make sure you can still SSH into your Raspberry Pi at this point — although you won’t be prompted for a 2FA code quite yet. It’s sensible to check that everything still works at this stage.

**Installing two-factor authentication:**

The first thing you need to do is download an app to your phone that will generate the TOTP. One of the most commonly used is Google Authenticator. It’s available for Android, iOS, and Blackberry, and there is even an open source version of the app available on GitHub.


**Google Authenticator in the App Store:**

So go ahead and install Google Authenticator, or another 2FA app like Authy, on your phone. Afterwards, install the Google Authenticator PAM module on your Raspberry Pi:
```
$ sudo apt install libpam-google-authenticator
```
Now we have 2FA installed on both our phone, and our Raspberry Pi, we’re ready to get things configured.

Configuring two-factor authentication
You should now run Google Authenticator from the command line — without using sudo — on your Raspberry Pi in order to generate a QR code:
```
$ google-authenticator
```
Answer yes to time base authentication

Afterwards you’re probably going to have to resize the Terminal window so that the QR code is rendered correctly. Unfortunately, it’s just slightly wider than the standard 80 characters across.


The QR code generated by google-authenticator. Don’t worry, this isn’t the QR code for my key; I generated one just for this post that I didn’t use.

Don’t move forward quite yet! Before you do anything else you should copy the emergency codes and put them somewhere safe.

These codes will let you access your Raspberry Pi — and turn off 2FA — if you lose your phone. Without them, you won’t be able to SSH into your Raspberry Pi if you lose or break the device you’re using to authenticate.

Next, before we continue with Google Authenticator on the Raspberry Pi, open the Google Authenticator app on your phone and tap the plus sign (+) at the top right, then tap on “Scan barcode.”

Your phone will ask you whether you want to allow the app access to your camera; you should say “Yes.” The camera view will open. Position the barcode squarely in the green box on the screen.


Scanning the QR code with the Google Authenticator app.

As soon as your phone app recognises the QR code it will add your new account, and it will start generating TOTP codes automatically.


**The TOTP in Google Authenticator app.**

Your phone will generate a new one-time password every thirty seconds. However, this code isn’t going to be all that useful until we finish what we were doing on your Raspberry Pi. Switch back to your terminal window and answer “Y” when asked whether Google Authenticator should update your .google_authenticator file.

Then answer “Y” to disallow multiple uses of the same authentication token, “N” to increasing the time skew window, and “Y” to rate limiting in order to protect against brute-force attacks.

You’re done here. Now all we have to do is enable 2FA.

**Enabling two-factor authentication**
We’re going to use Linux Pluggable Authentication Modules (PAM), which provides dynamic authentication support for applications and services, to add 2FA to SSH on Raspberry Pi.

Now we need to configure PAM to add 2FA:
```
$ sudo nano /etc/pam.d/sshd
```

Add auth required pam_google_authenticator.so to the top of the file. You can do this either above or below the line that says @include common-auth.


Editing /etc/pam.d/sshd.
add #2FA line as follow below @include line of standard unix authentication
```
# PAM configuration for the Secure Shell service

# Standard Un*x authentication.
@include common-auth

# Disallow non-root logins when /etc/nologin exists.
account    required     pam_nologin.so
```
so it will look like this

```
# PAM configuration for the Secure Shell service

# Standard Unix authentication.

@include common-auth


auth required pam_google_authenticator.so

# Disallow non-root logins when /etc/nologin exists.

account    required     pam_nologin.so
```
As I prefer to be prompted for my verification code after entering my password, I’ve added this line after the @include line. If you want to be prompted for the code before entering your password you should add it before the @include line.

Now restart the SSH daemon:
```
$ sudo systemctl restart ssh
```
Next, open up a terminal window on your laptop and try and SSH into your Raspberry Pi.

Wrapping things up
If everything has gone to plan, when you SSH into the Raspberry Pi, you should be prompted for a TOTP after being prompted for your password.


**SSH’ing into my Raspberry Pi:**

You should go ahead and open Google Authenticator on your phone, and enter the six-digit code when prompted. Then you should be logged into your Raspberry Pi as normal.

You’ll now need your phone, and a TOTP, every time you ssh into, or scp to and from, your Raspberry Pi. But because of that, you’ve just given a huge boost to the security of your device.

Now you have the Google Authenticator app on your phone, you should probably start enabling 2FA for your important services and sites — like Google, Twitter, Amazon, and others — since most bigger sites, and many smaller ones, now support two-factor authentication.

### 1.3.2. RealVNC 2 factor authentification
---
**source:**  https://help.realvnc.com/hc/en-us/articles/360003110878-How-do-I-set-up-2-step-authentication-for-my-RealVNC-account#enabling-2-step-authentication-0-0

Enabling 2-step authentication
To set up 2-step authentication for your RealVNC account, sign into the portal at https://manage.realvnc.com and click Security.



Click the Enable 2-step verification button.

A QR code will be displayed which you can scan with your TOTP app (e.g. Google Authenticator or Authy etc).

Enter the code and backup real vnc code in case your brake your smartphone.

### 1.3.3. Filezilla 2 factor authentification
---

Pour utiliser le 2 factor authentification il faut dans le gestionnaire de site utiliser le réglage type d'authentification interactif.
Pour éviter de devoir retaper les codes pour chacun des fichiers il faut cocher la case limiter le nombre de connexions simultannées dans les paramètres de transfert.

# 2. Capteur et gateway

**Une copie locale de l'ensemble des pages internet référencées est présente dans le dossier web_content**

Nous avons tenté d'utiliser notre propre réseau Chirpstack. Pour des problème de nombre de gateway nous nous sommes rabattu sur le réseau the thing network TTN.

Le conseil général de l'isère CG 38 développe sont propre réseau.

## 2.1. Gateway - les grandes oreilles sont à l'écoute
---
Les gateways servent a récupérer les données des capteur et à les transmettre au Lora Network Server LNS

### 2.1.1. Gateway parametrage chirpstack
---
La gateway a a priori selon la documentation 8 channel a parametrer dans la gateway profil
0, 1, 2, 3, 4, 5, 6, 7, 8, 9

### 2.1.2. gateway parametrage TTN
---

see on TTN website



### 2.1.3. Rakwireless RAK7246 LPWAN Developer Gateway - RAK7246 - EU868
---

**ATTENTION AVANT LA MISE SOUS TENSION DE LA GATEWAY BIEN INSTALLER L ANTENNE LORA SINON IL Y A UN RISQUE D ENDOMAGEMENT**

** réglage en direct clavie souris écran
Alimenter le raspberry pi zero w du rak7246 avec le port usb d'un pc
connecter a l'aide d'un cable mini / USB femelle un clavier et une souris usb (la souris ne servira peut être pas à grand chose)
connecter avec un mini/hdmi un écran

login par défaut pi / raspberry attention clavier qwerty

CHANGEMENT DE CLAVIER
sudo raspi-config

choisir menu 4 localisation option 
/menu 1 change locale
choisir un fr_fr plutot qu'un en_gb la version iso ira parfaitement
/menu 2 change timezone
europe/paris
/menu 3 change keyboard layout
prendre le clavier détecté puis la configuration other puis french et encore french puis the default for AltGr puis no compose key
et voila clavier azerty

**Connexion SSH**

Par défaut la gateway est en Wi-Fi AP Mode ce qui signifie qu'un réseau wifi avec le SSID nomé "Rakwireless_XXXX" peut être trouvé sur la liste des réseau wifi de votre PC.

Le mot de passe est rakwireless et l'adresse par défaut est 192.168.230.1

On se connecte en SSH sur le port 22 à cette adresse avec un outil tel que putty ou openssh.

Une fois connecté le login par défaut est le suivant "pi" et le mot de passe "raspberry"

**Réglage wifi**

https://doc.rakwireless.com/rak7246g-lorawan-developer-gateway/accessing-the-internet

Le réglage de la gateway s'effectue à partir de la commande suivante:
```
sudo gateway-config
```
***Recuperer Gateway ID encore appelé Geteway EUI qui est la chaine de caractère présente dans le tire de la fenetre immédiatement après ID:**
deveui B827EBFFFE627CCF

-menu Set pi password - est utilisé pour changer le mot de passe de la Gateway.

-menu New SSID pour le client - permet de définir les paramètre de votre réseau Wi-Fi Network. fonctionne uniquement en Wi-Fi Client mode.
Enter SSID Livebox-DF06 tout en minuscule
passphrase code wifi

-menu Change Wi-Fi Country - utilisé pour correspondre aux standard Wi-Fi de votre pays.

On peut choisir de la regler en ip statique du coté de la livebox avec la mac adress
ifconfig -a
element ethet sur la partie wlan0

-**menu Enable Client Mode/Disable AP Mode permet de passer en mode wifi. Cette page contient la méthode pour revenir en arrière. Cette instruction est a affectuer en dernier lorque l'ensemble des réglages ont été effectué.**

**Réglage de la gateway**

https://doc.rakwireless.com/rak7246g-lorawan-developer-gateway/configuring-the-gateway

-Menu 2 Setup RAK Gateway LoRa® concentrator: Pour Chirpstack choisir server is other server puis EU868 pour la gamme de fréquence Européenne. Ensuite vous pouvez entrer une adresse ip ou le dns de votre serveur chirpstack.

** Connexion TTN ou Connexion Chirpstack**

La connexion TTN est détaillée ici

https://doc.rakwireless.com/rak7246g-lorawan-developer-gateway/connecting-to-the-things-network

La connexion Chirpstack est détaillée ici

https://doc.rakwireless.com/rak7246g-lorawan-developer-gateway/connect-the-gateway-with-chirpstack

Il faut désormais effectuer les réglages de la gateway dans les pages chirpstack application server. Se rendre sur l'inteface web du server (sur le port par défaut 8080) chirpstack. Le login par défaut est admin/admin
Se rendre dans la partie gateways puis create.
**Reprendre les réglage de mac adress de la gateway et les copier dans gateway ID. cf partie ci-dessus sur Gateway ID/Gateway EUI**
Lorsque tout fonctionne vous devriez apercevoir last seen few second ago.

**Lors de mon installation j'ai résolu le fait que last seen few second ago n'apparaissait pas avec my_server:8000 dans la partie network-servers**
En effet dans la documentation il est dit localhost:8000. Il faut lui préferer son nom dns sur le réseau.

raspberrypi.home:8000 meme réseau privé??? port??? /el001.is-a-green.com:8000 depuis l'extérieur?? port???? 
différence entre rakwireless sudo gateway-config sans le port et la configuration chirpstack avec le port dans la partie network server raspberrypi.home:8000

### 2.1.4. Lopy Nano Gateway
---

On peut utiliser un Lopy 4 pour se comporter comme une gateway monocanal afin de transmettre les messages des capteurs.

https://docs.pycom.io/tutorials/lora/lorawan-nano-gateway/

Dans les fichiers lopy nano de la partie setting vous avez un exemple de programmation:

- Le fichier config.py:
    -  défini une mac avec FFFE en sont centre pour le réseau TTN ou FFEE pour le réseau Chirpstack. Cette mac est l'identifiant de la gateway pour chacun des deux réseaux TTN ou Chirpstack (respectivement en FFEE ou en FFFE selon le réseau choisi)
    ```
    GATEWAY_ID = WIFI_MAC[:6] + "FFEE" + WIFI_MAC[6:12]
    ```
    deveui
      70B3D54995E573F7 lopy red?
      db2b4bbc2cf740a3 lopy green

    - myserver doit être remplacé par le DNS du réseau qui héberge votre serveur chirpstack.
- le fichier main.py:
    - gère la connexion au réseau lorawan
    - puis avec le module nanogateway.py capte et transmet les éléments recu par les capteur au serveur TTN ou Chirpstack.

## 2.2. Capteur - les données sont recueillies
---
Les capteurs sont dans la pluspart des cas installés directement sur les compteurs d'eau ou d'énergie.

rappel sur les différentes key: https://stackoverflow.com/questions/54096980/lorawan-deveui-appeui-and-appkey


### 2.2.1. Installation capteur ADEUNIS
---
La société Adeunis propose tout une série de capteur Lorawan avec une bibliothèque qui permet de décoder les messages dans de nombreux logiciel par un appel de la librairie de décodage.
A partir de The Thing Network (TTN) ou Chirpstack il faut préalablement décodé les message en hexa vers un format de chaine de caractère qui est nécessaire pour l'appel de la librairie de décodage

L'outil qui permet de décoder les messages est ici:
http://codec-adeunis.com/decoder

La librairie est accessible ici:

http://codec-adeunis.com/download


source: https://www.adeunis.com/device-management/configuration-des-capteurs/
app: https://play.google.com/store/apps/details?id=com.adeunis.IoTConfiguratorApp

NONFAIT A CAUSE CONNEXION SMARTPHONE USB: avec une cle torx ouvir le capteur et connecter ce dernier a votre smartphone  mini usb mini usb.

Pour activer sous chirpstack il faut le DevEUI et l'Appkey... puis attendre 12 heures... ;) La nuit porte conseil!!!!!!!!!!!!!!!!!!!!!!!!!!


### 2.2.2. Installation capteur NKE Watteco FlashO
---
pour l'installation physique
source: http://support.nke-watteco.com/flasho/
pour la configuration lora
source: https://support.nke-watteco.com/

Le capteur flashO est un CAPTEURLORAWAN DE CLASS A

scanner le qrcode sur mobile et le partager
LW:D0:70B3D5E75F600000:70B3D5E75E00F27A:01280017:P5070071006:S002E484C81:CFC83
JoinEUI: 70B3D5E75F600000
DevEUI: 70B3D5E75E00F27A

### 2.2.3. Lopy as a device
---

Le LoPy 4.0 est une carte de développement miniature dédiée aux objets connectés, basée sur le langage Python 3, de faible consommation et disposant de connectivité WiFi, Bluetooth (compatible BLE), LoRa et Sigfox.
Une solution pour programmer le Lopy 4 est d'utiliser le Pymakr Plugin for Atom et d'interagir avec le Lopy via le port Usb de la carte PyMakr.
Le plugin est désormais fiable et facile d'utilisation.
https://docs.pycom.io/pymakr/installation/atom/

Dans les fichiers lopy device de la partie setting vous avez un exemple de programmation:

- Le fichier config.py:
    -  défini une mac avec FFFE en sont centre pour le réseau TTN ou FFEE pour le réseau Chirpstack. Cette mac est l'identifiant du device pour chacun des deux réseaux
    - myserver doit être remplacé par le DNS du réseau qui héberge votre serveur chirpstack.
- le fichier main.py:
    - gère la connexion au réseau lorawan
    - envoie avec la boucle pour / for la valeur value = 22.5 pendant 60 itérations de 2 minutes afin de simuler une valeur de température
- le fichier boot.py gère le démarrage du Lopy 4.


https://docs.pycom.io/pymakr/installation/atom/

## 2.3. Codage Decodage Capteur: les Codec
---

### 2.3.1. modification du decodage pour chirpstack -> thingsboard
---
source: https://www.chirpstack.io/application-server/integrations/thingsboard/

Decoded uplink data is prefixed with the **data_ prefix**. Make sure to configure a coded in the Device Profile.

### 2.3.2. Codage Decodage Capteur Codec ADEUNIS
---
source: https://codec-adeunis.com/download

**utiliser https://cryptii.com/ bytes en hexa a gauche, encode base 64 rfc 3548, text à droite**
**le port a utiliser est le 1**
**périodicité de l'envoi de la mesure: toutes les X mesures**
0x41 0x41 register to modify 301
envoi toute les mesures
S301 : trame  41 01 00 01 (register to modify is 300+1 01-> 41 01 -> valeur de 1 toutes les mesures 00 01 -> 41 01 00 01  )->en text "QQEAAQ=="
envoi toute les 6 mesures (soit 1h si la périodicité est a 10 minutes)
S301 : trame  41 01 00 06 (register to modify is 300+1 01-> 41 01 -> valeur de 6 toutes les 6 mesures 00 06 -> 41 01 00 06  )->en text "QQEABg=="
envoi toute les 24 mesures (soit 4h si la périodicité est a 10 minutes)
S301 : trame  41 01 00 18 (register to modify is 300+1 01-> 41 01 -> valeur de 6 toutes les 24 mesures 00 18 -> 41 01 00 18  )->en text "QQEAGA=="
envoi toute les 48 mesures (soit 8h si la périodicité est a 10 minutes)
S301 : trame  41 01 00 30 (register to modify is 300+1 01-> 41 01 -> valeur de 48 toutes les 48 mesures 00 30 -> 41 01 00 30  )->en text "QQEAMA=="
envoi toute les 72 mesures (soit 12h si la périodicité est a 10 minutes)
S301 : trame  41 01 00 48 (register to modify is 300+1 01-> 41 01 -> valeur de 72 toutes les 72 mesures 00 48 -> 41 01 00 48  )->en text "QQEASA=="
envoi toute les 144 mesures (soit 24h si la périodicité est a 10 minutes)
S301 : trame  41 01 00 90 (register to modify is 300+1 01-> 41 01 -> valeur de 144 toutes les 144 mesures 00 90 -> 41 01 00 90  )->en text "QQEAkA=="

**périodicité de la mesure**
0x41 register to modify 321
réglage à 600s soit 10 minutes
s321 :  trame 41 15 01 2c (register to modify 300+21-> 41 15 (21=16+5->15)-> 1 point toute les 10 min 300*2s on envoi 300 -> 41 15 01 2C) )-> en text "QRUBLA=="
**reboot**
0x48
pour un reboot dans 120 minutes après l'envois du message
120 minutes = 0x0078 la trame est donc 48 00 78 -> en text "SAB4"
30 minutes = 0x001E -> en text "SAAe"
10 minutes = 0x000A -> en text "SAAK"
5 minutes la trame est 48 00 05 -> en text "SAAF"

on peut envoyer deux informations a la fois... 41 15 01 2C 01 00 06 -> 10 minutes / envois toutes les 6 mesures soit toute les heures
-> QRUBLAEABg==
10 minutes toutes les 3h soit toutes les 18 mesures (12 en hexa)... 41 15 01 2C 01 00 12
-> QRUBLAEAEg==

## 2.4. Codage Decodage Capteur Codec NKE
---

source: https://support.nke-watteco.com/downloads/
pour du flashO : https://github.com/TheThingsNetwork/lorawan-devices/blob/master/vendor/nke-watteco/flasho-sensor.js

périodicité de la mesure
réglage à 600s en downlink message sur le **port 125** (en bas de la partie stat du device sur chirpstack)
/* pas ok
trame 11 06 00 0f 00 04 02 23 00 00 02 58 00 00 00 00 -> en text "EQYADwAEAiMAAAJYAAAAAA=="
réglage à 600s avec un envoi toutes les 6 mesures sur le **port 125** (en bas de la partie stat du device sur chirpstack)
trame 11 06 00 0f 00 04 02 23 00 00 02 58 00 00 00 06- > en text "EQYADwAEAiMAAAJYAAAABg=="
pas ok */

EQYADwAEAiMAAAJYAAAAAA==

PLUTOT
d'après l'exemple de la configuration https://support.nke-watteco.com/configuration-cluster/
example: report the battery level once a day.
Send on the fport 125: 11 06 00 50 00 00 06 41 800A 85A0 05 00 04 00C8 00
with 800A : 8000(minutes) | 000A (10)  => periodicity of measure all 10 minutes
with 85A0 : 8000(minutes) | 05A0 (1440)  => periodicity of sending all 1440 minutes = 1 day
with 04: set a delta variation on disposable battery.
with 00C8 : the delta variation for which a report will be sent is 200 mV

c'est ici que les trame peuvent etre encodé.
http://support.nke.fr/Lora/LoraEncoder/Index.html
```
Choisissez tout d'abord le modèle de capteur, puis sélectionnez une commande et éditez les paramètres disponibles.

① Choisissez un produit : 
Flash'O (50-70-071)
② Choisissez une fonction : 
Comptage - Configurer les rapports de nombre de changements d'état

Avancé
③ Modifiez les paramètres suivants afin de générer la trame souhaitée :
Paramètre	Valeur	Commentaire
EndPoint	
0
---
Type de rapport	
Batch // c'est batch qui défini que l'on veut de l'historisation cad un envoi périodique de plusieurs mesures
---
Intervalle de rapport minimal	
10 minutes --- (0 à 32767 secondes) // mesures toutes les 10 minutes
Intervalle de rapport maximal	
180 minutes --- (0 à 32767 secondes) // périodicité de l'envois toutes les 3 h
Delta	
0 // IMPORTANT ENFIXANT A 0 ON FORCE LE COMPORTEMENT D 4UN ENVOIS TOUTES LES TROIS HEURE SINON CELA SEMBLE ETRE UN DELTA MAX POUR DECLENCHER UN ENVOI 5 CE COMPORTEMENT PERMET DE SURVEILLER DES FUITE 6 ON DECLENCHE UN ENVOIS PREMATRURE SUR DELTA TROP IMPORTANT
--- (0 à 32767 )
Résolution	
1 --- (0 à 32767 )
TagLabel	
0 --- (0 à 31 )
TagSize	
1 --- (1 à 7 )
```
Downlink sur port 125
1106000f01040200800a80b4000000000000000101
-> "EQYADwEEAgCACoC0AAAAAAAAAAEB"
1106000f1d040200800a80b4000000000000000101
plutot
1106000f11005500800a80b4000101

quand on configure le state
```
Decoded frame (json) : 1106000f11005500800a80b4000101
{"version": "NKE_Frame_Codec_v_1.0.svn5087", "TimeStamp": "2022-01-15 19:09:18.814959"}
{
 "EndPoint": 0,
 "Report": "Standard",
 "CommandID": "ConfigureReporting",
 "ClusterID": "BinaryInput",
 "ReportParameters": {
  "Batch": "Yes",
  "Size": 8
 },
 "AttributeID": "PresentValue",
 "Batches": [
  {
   "FieldIndex": 0,
   "MinReport": {
    "Unit": "Minutes",
    "Value": 10
   },
   "MaxReport": {
    "Unit": "Minutes",
    "Value": 180
   },
   "Delta": false,
   "Resolution": true,
   "TagValue": {
    "TagLabel": 0,
    "TagSize": 1
   }
  }
 ]
}
```


quand on configure le count
```
Decoded frame (json) : 110Decoded frame (json) : 1106000f1d040200800a80b40000000000000001016000f1d040200800a80b4000000000000000101
{"version": "NKE_Frame_Codec_v_1.0.svn5087", "TimeStamp": "2022-01-15 19:16:33.117499"}
{
 "EndPoint": 0,
 "Report": "Standard",
 "CommandID": "ConfigureReporting",
 "ClusterID": "BinaryInput",
 "ReportParameters": {
  "Batch": "Yes",
  "Size": 14
 },
 "AttributeID": "Count",
 "Batches": [
  {
   "FieldIndex": 0,
   "MinReport": {
    "Unit": "Minutes",
    "Value": 10
   },
   "MaxReport": {
    "Unit": "Minutes",
    "Value": 180
   },
   "Delta": 0,
   "Resolution": 1,
   "TagValue": {
    "TagLabel": 0,
    "TagSize": 1
   }
  }
 ]
}
```

read de la configuration version du codec
1108000f000055
-> EQgADwAAVQ==
read de la configuration from manual jyria
11080050000006
-> EQgAUAAABg==

downlink  simple flash O configure reporting report standart min 10 max 180 reportable change 0
1106000f00040223800a80b400000000
->EQYADwAEAiOACoC0AAAAAA==
trame up chirpstack
data:"EQcADwAABAI="
attributID:"0x0402"
clusterdID:"0x000F"
cmdID:"0x07"
decodedBatch:0
endpoint:0
report:"standard"
status:0

## 2.5. Recuperation des données: le protocole MQTT
---
Le protocole MQTT (Message Queuing Telemetry Transport) permet de recuperer les données de TTN via un noeud MQTT avec Nodered


Subscribing to Upstream Traffic
The Application Server publishes uplink traffic on the following topics:

v3/{application id}@{tenant id}/devices/{device id}/join
v3/{application id}@{tenant id}/devices/{device id}/up
v3/{application id}@{tenant id}/devices/{device id}/down/queued
v3/{application id}@{tenant id}/devices/{device id}/down/sent
v3/{application id}@{tenant id}/devices/{device id}/down/ack
v3/{application id}@{tenant id}/devices/{device id}/down/nack
v3/{application id}@{tenant id}/devices/{device id}/down/failed
v3/{application id}@{tenant id}/devices/{device id}/service/data
v3/{application id}@{tenant id}/devices/{device id}/location/solved


db.frames.find({$where:"JSON.stringify(this).indexOf('adpul')!=-1", "uplink_message.frm_payload":{"$exists": true}},{_id:1, "end_device_ids.device_id":1, received_at:1, "uplink_message.frm_payload":1}).sort({"_id" : -1})






# 3. Serveur - on stock et on affiche
## 3.1. LoRaWAN Network Server (LNS)Chirpstack - on gère les élément de notre réseau
---
Voici détaillé les éléments de parmétrage d'un serveur LNS de type Chripstack

### 3.1.1. Chirpstack quickstart
---
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

```
sudo systemctl start chirpstack-gateway-bridge
```
- au démarrage:
```
sudo systemctl enable chirpstack-gateway-bridge
```

**Installation du ChirpStack Network Server**
Installation des paquet en utilisant apt apt:

```
sudo apt install chirpstack-network-server
```

Le fichier de configuration est situé /etc/chirpstack-network-server/chirpstack-network-server.toml et doit être configuré pour correspondre avec les bases de données, les utilisateur et les mots de passe PostgreSQL. Il doit aussi correspondre aux réglage des fréquence d'émission. Pour l'Europe c'est le EU868 et pour les USA US915. Pour plus d'option voir avec la partie ChirpStack Network Server configuration

Après la modification du fichier de configuration, vous devez redémarrer Chirpstack Network Server et valider qu'il n'y a pas d'erreur.

Il y a deux manières de démarrer les service de ce server:
- Manuellement:
```
sudo systemctl start chirpstack-network-server
```
- au démarrage
```
sudo systemctl enable chirpstack-network-server
```

Afin de visualiser les log du network server.
```
sudo journalctl -f -n 100 -u chirpstack-network-server
```

Pour la configuration détaillée voir la partie chirpstack server ci-dessous.

**Installation de  ChirpStack Application Server**
Installation des paquets en utilisant apt:

```
sudo apt install chirpstack-application-server
```

le chemin du fichiers de configuration est le suivant /etc/chirpstack-application-server/chirpstack-application-server.toml et doit être mis à jour pour correspondre à la configuration de la base de données PostgreSQL.

Pour la configuration détaillée voir la partie chirpstack application server ci-dessous.

Note: il faut impérativement remplacé le paramètre jwt_secret avec une chaine de sécurité! Voupouvez utiliser la commande suivante openssl rand -base64 32 pour générer une chaine de sécurité secret.

Le ChirpStack Application Server service peut être démarré de deux manières:

- manuellement:
```
sudo systemctl start chirpstack-application-server
```

- au démarrage:
```
sudo systemctl enable chirpstack-application-server
```

Afin de voir si il n'y a pas d'erreur vous pouvez visualiser le log de ChirpStack Application Server avec la commande suivante:

```
sudo journalctl -f -n 100 -u chirpstack-application-server
```


### 3.1.2. Chirpstack bridge
---
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

### 3.1.3. Chirpstack Bridge TROUBLESHOOTING
---

https://www.chirpstack.io/guides/troubleshooting/gateway/
Il s'agit de verifier que l'on recoive bien des informations de la gateway

Tout d'abord il faut s'assurer que le Semtech Packet Forwarder de la gateway recoive bien des données du capteur. Ainsi on utilise la commande TCP dump pour suivre les messages échangés. Le port doit correspondre à celui de la configuration de ChirpStack Gateway Bridge.
- Lorsqque ChirpStack Gateway Bridge tourne sur la gateway l'instruction suivante vérifiera cela: 
```
sudo tcpdump -AUq -i lo port 1700
```
- Lorsque ChirpStack Gateway Bridge est installé sur une machine / serveur différents dans ce cas c'est l'intruction suivante:

```
sudo tcpdump -AUq port 1700
```

On doit constater une réponse équivalente à ci-dessous pour valider le bon fonctionement
```
11:42:00.114726 IP localhost.34268 > localhost.1700: UDP, length 12 E..(..@.@."................'.....UZ.....
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
  ```
  journalctl -f -n 100 -u chirpstack-gateway-bridge
tail -f -n 100 /var/log/chirpstack-gateway-bridge/chirpstack-gateway-bridge.log
```

On devrait ainsi avoir ce type de contenu à l'écran
```
INFO[0013] mqtt: subscribing to topic qos=0 topic=gateway/7276ff002e062c18/command/#

INFO[0267] mqtt: publishing message qos=0 topic=gateway/7276ff002e062c18/event/up
```

Si le contenu de l'écran n'est pas de ce type il faut
- revérifier la configuration de la gateway
- vérifier que le service du ChirpStack Gateway Bridge est en fonctionnement. Pour vérifier on utilise la commande suivante:
```
ps aux |grep chirpstack-gateway-bridge
```
Le résultat devrait ressembler à cela:

```
root      6403  0.0  0.2  12944  1088 pts/0    S+   12:53   0:00 grep --color=auto chirpstack-gateway-bridge
gateway+ 23060  0.1  2.1 214260 10664 ?        Ssl  Aug30  47:55 /usr/bin/chirpstack-gateway-bridge
```
- Vérifier ChirpStack Gateway Bridge configuration pour s'assurer des réglages machine:port dans le fichier de configuration chirpstack-gateway-bridge.toml.

- Vérifier que ChirpStack Gateway Bridge publie des données sur le broker MQTT. On effectue cela en souscrivant "au fil" concernant les gateway: gateway/# MQTT. on effectue cela avec l'instruction mosquitto_sub:

```
mosquitto_sub -v -t "gateway/#"
```
Si vous ne voyer aucun message lorsque le capteur envoie des données, il faut alors s'assurer que  ChirpStack Gateway Bridge est autorisé de publier des données sur le sujet MQTT et que le client  mosquitto_sub client est autorisé de souscrire à ce sujet MQTT Ce problème apparait habituellement lorsque vous avec configuré le MQTT Broker afin que les client doivent s'authentifier lors de la connexion.

### 3.1.4. Chirpstack server
---
Configuration file
Par défaut chirpstack-network-server va regarder dans l'ordre les chemins suivant si l'instruction en comporte pas explicitement la spécification suivante --config:

- chirpstack-network-server.toml (current working directory)
- $HOME/.config/chirpstack-network-server/chirpstack-network-server.toml
- /etc/chirpstack-network-server/chirpstack-network-server.toml

Le fichier de configuration est présent dans la partie settings

Dans le fichier de configuration le minimum a vérifier est le chemin vers la base de données postgres
```
# * verify-full - Always SSL (verify that the certification presented by the server was signed by a trusted CA and the server host name matches the one in the certificate)
dsn="postgres://localhost/chirpstack_ns?sslmode=disable"
```

Le détail de toute les options est présent à l'adresse suivante https://www.chirpstack.io/network-server/install/config/


### 3.1.5. Chirpstack application server
---
Configuration file
Par défaut chirpstack-application-server va regarder dans l'ordre les chemins suivant si l'instruction en comporte pas explicitement la spécification suivante --config:
- chirpstack-application-server.toml (current working directory)
- $HOME/.config/chirpstack-application-server/chirpstack-application-server.toml
- /etc/chirpstack-application-server/chirpstack-application-server.toml

Le fichier de configuration est présent dans la partie settings

Dans le fichier de configuration le minimum a vérifier est le chemin vers la base de données postgres
```
# * verify-full - Always SSL (verify that the certification presented by the server was signed by a trusted CA and the server host name matches the one in the certificate)
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
```
# MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
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
```
# JWT secret used for api authentication / authorization
  # You could generate this by executing 'openssl rand -base64 32' for example
  jwt_secret=""
  ```
Commme les différentes partie du serveur sont sur la même machine je ne me suis pas occupé de sécuriser la communication interne comme spécifié. La partie Nginx s'occupe de cela.

Le détail de toute les options est présent à l'adresse suivante https://www.chirpstack.io/application-server/install/config/

## 3.2. Thingsboard - on gère les tableaux de bord et les alertes
---

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

 **1. Installation de composents tiers Java 8 (OpenJDK)**

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
**2. Installation des services ThingsBoard**

Télécharger les paquets d'installation
```
wget https://github.com/thingsboard/thingsboard/releases/download/v2.4.3/thingsboard-2.4.3.deb
```

Installation du service ThingsBoard.
```
sudo dpkg -i thingsboard-2.4.3.deb
```
**3. Configuration de la base de données ThingsBoard**
     
    
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
   **- Configuration ThingsBoard**

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
  **6. Démarrage des services ThingsBoard**

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

**7. Réglages complémentaires - conflits**

Le fichier de configuration utilisé est présent dans la partie settings.
Du fait que thingsboard est installé sur la même machine que Chirpstack leur port de l'explorateur web sont en conflit sur le 8080
Il vous faut de la meme manière que le fichier de configuration éditer le fichier Thingsboard.yml et le modifier comme indiqué sur le port 8085:
```
# Server bind port
  port: "${HTTP_BIND_PORT:8085}"
```
Le protocole MQTT est aussi en conflit pour des raisons identiques sur le port 8080. Pour Thingsboard vous pouvez le configurer sur le port 8883 dans le fichier /usr/share/thingsboard/conf/thingsboard.yml
```
mqtt:
    # Enable/disable mqtt transport protocol.
    enabled: "${MQTT_ENABLED:true}"
    bind_address: "${MQTT_BIND_ADDRESS:0.0.0.0}"
    bind_port: "${MQTT_BIND_PORT:8883}"
```
L'erreur suivante:
```
[main] ERROR o.s.boot.SpringApplication - Application run failed
```
provient du fait que mosquitto est démarré. Executer la commande suivante:
```
sudo service mosquitto stop
```

pour chirpstack: erreur / error context deadline exceeded (code: 2) 
réglage pour la partie via l'interface web network server 192.168.1.101:8000 doit correspondre a la partie public_host="192.168.1.101:8001" du fichier /etc/chirpstack-application-server/chirpstack-application-server.toml

### 3.2.1. Intégration Thingsboard - Chirpstack
---

Le détail de l'intégration est présent à l'adresse suivante: https://www.chirpstack.io/guides/thingsboard/

Pour l'installation de ThingsBoard se référer au partie adequat du guide de démarrrage. La parie importante est d'avoir créer un capteur (device) au sein de Thingsboard.

**Récuperer Device Auth Token**

Il faut récuperer le Device Auth Token afin que Chirpstack puisse pousser les données vers le capteur Thingsboard. Dans ThingsBoard, ouvrez le capteur et cliquer sur le button Copy Access Token. This will copy the Access Token to your clipboard.

** Regler Device Auth Token dans ChirpStack Application Server**

Désormais ouvrez l'interface web du ChirpStack Application et rendez vous dans la partie du capteur / Device. Cliquez sur Configuration, puis sur  Variables.

Ajoutez une variable nomée ThingsBoardAccessToken avec la valeur du ThingsBoard Device Access Token. Cette étape est aussi documentéedans la partie ChirpStack Application Server ThingsBoard Integration.

**Réglage de ChirpStack Application Server ThingsBoard integration**

Toujours dans l'interface web ChirpStack Application Server, naviguez vers l'application qui contient le capteur / Device. Cliquez sur intégration puis creer/ + Create.

type d'intégration: ThingsBoard.io.

ThingsBoard.io server: Pour OpenEnergy le réglage est http://host_name:8085 car l'installation de Thingsboard est sur le port 8085.(ERREUR l'installation de chirpstack est sur le port 8080) Les réglages peuvent varier http://host:9090...

**Valider l'integration**

Si vous avez suivi toutes ces étapes alors ThingsBoard est pret à recevoire les données montantes aussi appelée  telemetry et ChirpStack Application Server est réglé pour faire suivre les données vers le capteur / Device, en utilisant Access Token for authentication.

La dernière étape est de laisser le capteur / device envoyer des données et valider que ces données sont recu par Thingsboard. Vous trouverez les données dans l'onglet Latest Telemetry en navigant vers le capteur / Device au sein de Thingsboard.

**MQTT thingsboard: Sheevaplug l'exemple d'un envois de données par un device (sheeva plug / current cost**

Dans les paramètre d'un device thingsboard récuperer device id et access token
Dans le script de lecture du current cost /home/eluser/ccRead.pl ajouter les lignes de publication mqtt.
8883 est le port de mqtt thingsboard.
```
for (my $i=0;$i<$#measures;$i++){
      if ($measures[$i] != 0){ 
          $sock->send("local.el.channel$i.VA ".$measures[$i]." $timestamp\n");
	  system('mosquitto_pub -d -q 1 -h "192.168.1.101" -p "8883" -t "v1/devices/me/telemetry" -u "access_token" -m {"consommation'.$i.'":'.$measures[$i].'}');
      }
    }
    $sock->send("local.el.temp $temp $timestamp\n");
    system('mosquitto_pub -d -q 1 -h "192.168.1.101" -p "8883" -t "v1/devices/me/telemetry" -u "access_token" -m {"temperature":'.$temp.'}');
```


### 3.2.2. Thingsboard TROUBLESHOOTING
---

Si le service Thingsboard ne démarre pas malgré les modifications ci-dessus il vous faut analyser les éléments plus précisement à l'aide des instructions suivantes:
Les logs de ThingsBoard logs sont enregistré dans le répertoire suivant:
```
/var/log/thingsboard

```
Vous pouvez toujours utiliser la commande suivante pour vérifier les erreur du coté "backend":
```
cat /var/log/thingsboard/thingsboard.log | grep ERROR
```

#### 3.2.2.1. ERROR o.s.w.s.s.s.DefaultHandshakeHandler - Handshake failed due to invalid Upgrade header: null
---

Il faut valider les web socket dans nginx pour permettre l'affichage des widget et eviter cette erreur
ajouter ces lignes

```
# handle websocket for thingsboard widget like showing latest telemetry
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
```

#### 3.2.2.2. Error HikaryPool
---

Au bout d'un moment mon service exit...
thingsboard service status
oct. 09 06:17:37 raspberrypi thingsboard.jar[19855]: /usr/share/thingsboard/bin/thingsboard.jar : ligne 278 : 19869 Processus arrêté      "$javaexe" "${argum
oct. 09 06:17:38 raspberrypi systemd[1]: thingsboard.service: Main process exited, code=exited, status=137/n/a
oct. 09 06:17:38 raspberrypi systemd[1]: thingsboard.service: Failed with result 'exit-code'.

pi@raspberrypi:~ $ cat /var/log/thingsboard/thingsboard.log | grep ERROR
2021-10-09 06:12:39,420 [sql-queue-0-ts latest-7-thread-1] ERROR o.h.e.jdbc.spi.SqlExceptionHelper - HikariPool-1 - Connection is not available, request timed out after 139526ms.
2021-10-09 06:12:51,602 [sql-queue-0-ts latest-7-thread-1] ERROR o.h.e.jdbc.spi.SqlExceptionHelper - This connection has been closed.
2021-10-09 06:12:59,689 [pool-7-thread-1] ERROR o.h.e.jdbc.spi.SqlExceptionHelper - HikariPool-1 - Connection is not available, request timed out after 116121ms.
2021-10-09 06:13:07,792 [pool-7-thread-1] ERROR o.h.e.jdbc.spi.SqlExceptionHelper - This connection has been closed.
2021-10-09 06:14:51,473 [sql-queue-0-ts-3-thread-1] ERROR o.h.e.jdbc.spi.SqlExceptionHelper - HikariPool-1 - Connection is not available, request timed out after 273688ms.
2021-10-09 06:14:54,849 [sql-queue-0-ts-3-thread-1] ERROR o.h.e.jdbc.spi.SqlExceptionHelper - This connection has been closed.
2021-10-09 06:14:57,508 [ForkJoinPool-11-worker-3] ERROR o.h.e.jdbc.spi.SqlExceptionHelper - HikariPool-1 - Connection is not available, request timed out after 127704ms.
2021-10-09 06:15:57,842 [ForkJoinPool-11-worker-3] ERROR o.h.e.jdbc.spi.SqlExceptionHelper - This connection has been closed.
2021-10-09 06:14:56,439 [sql-queue-0-ts latest-7-thread-1] ERROR o.t.s.dao.sql.TbSqlBlockingQueue - [TS Latest] Failed to save 1 entities
2021-10-09 06:15:57,609 [sql-queue-0-ts-3-thread-1] ERROR c.g.c.u.concurrent.AggregateFuture - Got more than one input Future failure. Logging failures after the first
2021-10-09 06:15:58,070 [sql-queue-0-ts-3-thread-1] ERROR o.t.s.dao.sql.TbSqlBlockingQueue - [TS] Failed to save 1 entities

trouvé une information sur HikariPool
source: https://stackoverflow.com/questions/60301008/failed-to-validate-connection-this-connection-has-been-closed-possibly-consi
changement des setting du coté database en decommentant les trois parametres suivants dans le fichier /etc/postgresql/11/main/postgresql.conf
```
# - TCP Keepalives -
# see "man 7 tcp" for details

#tcp_keepalives_idle = 0		# TCP_KEEPIDLE, in seconds;
					# 0 selects the system default
#tcp_keepalives_interval = 0		# TCP_KEEPINTVL, in seconds;
					# 0 selects the system default
#tcp_keepalives_count = 0		# TCP_KEEPCNT;
					# 0 selects the system default
```
redemarrer le service postgres puis le service thingsboard

#### 3.2.2.3. Error lwM2MServiceImpl
---
2022-03-31 19:23:59,738 [main] INFO  o.t.s.c.SystemInfoController - System build info: {"version":"3.3.3","artifact":"application","name":"ThingsBoard Server Application"}
2022-03-31 19:23:59,899 [main] INFO  o.t.s.c.t.c.ssl.SslCredentialsConfig - LWM2M Server DTLS Credentials: Initializing SSL credentials.
2022-03-31 19:23:59,903 [main] WARN  o.s.b.w.s.c.AnnotationConfigServletWebServerApplicationContext - Exception encountered during context initialization - cancelling refresh attempt: org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'lwM2MServiceImpl' defined in URL [jar:file:/usr/share/thingsboard/bin/thingsboard.jar!/BOOT-INF/classes!/org/thingsboard/server/service/lwm2m/LwM2MServiceImpl.class]: Unsatisfied dependency expressed through constructor parameter 0; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'lwM2MTransportServerConfig': Unsatisfied dependency expressed through field 'credentialsConfig'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'lwm2mServerCredentials': Invocation of init method failed; nested exception is java.lang.RuntimeException: LWM2M Server DTLS Credentials: Invalid SSL credentials configuration. None of the PEM or KEYSTORE configurations can be used!
Error starting ApplicationContext. To display the conditions report re-run your application with 'debug' enabled.
2022-03-31 19:23:59,966 [main] ERROR o.s.boot.SpringApplication - Application run failed
org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'lwM2MServiceImpl' defined in URL [jar:file:/usr/share/thingsboard/bin/thingsboard.jar!/BOOT-INF/classes!/org/thingsboard/server/service/lwm2m/LwM2MServiceImpl.class]: Unsatisfied dependency expressed through constructor parameter 0; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'lwM2MTransportServerConfig': Unsatisfied dependency expressed through field 'credentialsConfig'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'lwm2mServerCredentials': Invocation of init method failed; nested exception is java.lang.RuntimeException: LWM2M Server DTLS Credentials: Invalid SSL credentials configuration. None of the PEM or KEYSTORE configurations can be used!

Dans thingsboard.yml mettre le enabled a false...
```
 # 4. Local LwM2M transport parameters
  lwm2m:
    # Enable/disable lvm2m transport protocol.
    enabled: "${LWM2M_ENABLED:false}"
```    

#### 3.2.2.4. Error jdbc connection / connection refused
---
Caused by: java.net.ConnectException: Connection refused (Connection refused)

2022-05-09 11:04:30,851 [main] ERROR com.zaxxer.hikari.pool.HikariPool - HikariPool-1 - Exception during pool initialization.
org.postgresql.util.PSQLException: Connection to localhost:5432 refused. 
Check that the hostname and port are correct and that the postmaster is accepting TCP/IP connections.
Caused by: java.net.ConnectException: Connection refused (Connection refused)

2022-05-09 11:04:30,853 [main] ERROR o.h.e.jdbc.spi.SqlExceptionHelper - Connection to localhost:5432 refused.
 Check that the hostname and port are correct and that the postmaster is accepting TCP/IP connections.

Error starting ApplicationContext. To display the conditions report re-run your application with 'debug' enabled.
2022-05-09 11:04:30,981 [main] ERROR o.s.boot.SpringApplication - Application run failed
org.springframework.context.ApplicationContextException: Unable to start web server;
 nested exception is org.springframework.boot.web.server.WebServerException: Unable to start embedded Tomcat

Caused by: org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'thingsboardSecurityConfiguration': Unsatisfied dependency expressed through field 'oauth2AuthenticationSuccessHandler'; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'oauth2AuthenticationSuccessHandler' defined in URL [jar:file:/usr/share/thingsboard/bin/thingsboard.jar!/BOOT-INF/classes!/org/thingsboard/server/service/security/auth/oauth2/Oauth2AuthenticationSuccessHandler.class]: Unsatisfied dependency expressed through constructor parameter 6; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'defaultSystemSecurityService': Unsatisfied dependency expressed through field 'mailService'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'defaultMailService': Invocation of init method failed; nested exception is org.springframework.dao.DataAccessResourceFailureException:
 Unable to acquire JDBC Connection;
  nested exception is org.hibernate.exception.JDBCConnectionException:
   Unable to acquire JDBC Connection

Caused by: org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'oauth2AuthenticationSuccessHandler' defined in URL [jar:file:/usr/share/thingsboard/bin/thingsboard.jar!/BOOT-INF/classes!/org/thingsboard/server/service/security/auth/oauth2/Oauth2AuthenticationSuccessHandler.class]: Unsatisfied dependency expressed through constructor parameter 6; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'defaultSystemSecurityService': Unsatisfied dependency expressed through field 'mailService'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'defaultMailService': Invocation of init method failed; nested exception is org.springframework.dao.DataAccessResourceFailureException:
 Unable to acquire JDBC Connection;
  nested exception is org.hibernate.exception.JDBCConnectionException:
   Unable to acquire JDBC Connection

Caused by: org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'defaultSystemSecurityService': Unsatisfied dependency expressed through field 'mailService'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'defaultMailService': Invocation of init method failed; nested exception is org.springframework.dao.DataAccessResourceFailureException:
 Unable to acquire JDBC Connection; 
 nested exception is org.hibernate.exception.JDBCConnectionException:
  Unable to acquire JDBC Connection

Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'defaultMailService': Invocation of init method failed; nested exception is org.springframework.dao.DataAccessResourceFailureException:
 Unable to acquire JDBC Connection;
  nested exception is org.hibernate.exception.JDBCConnectionException: Unable to acquire JDBC Connection

Caused by: org.springframework.dao.DataAccessResourceFailureException:
 Unable to acquire JDBC Connection;
  nested exception is org.hibernate.exception.JDBCConnectionException:
   Unable to acquire JDBC Connection

Caused by: org.hibernate.exception.JDBCConnectionException: Unable to acquire JDBC Connection

Caused by: org.postgresql.util.PSQLException: Connection to localhost:5432 refused.
 Check that the hostname and port are correct and that the postmaster is accepting TCP/IP connections.

**On monte le répertoire supplémentaire**
```
./thingsboard/logpostgres:/var/log/postgres dans le docker compose
```

ainsi on obtient cela dans posgres.log de var/log/postgres
2022-05-09 16:42:08.499 UTC [9] FATAL:  lock file "postmaster.pid" already exists
2022-05-09 16:42:08.499 UTC [9] HINT:  Is another postmaster (PID 10) running in data directory "/data/db"?

**il faut virer le postmaster.pid dans le repertoire data du bon container /var/lib/docker,ce fichier empeche les acces concurrent à la db**
```
sudo find /var/lib/docker/ -name "*.pid"
/var/lib/docker/volumes/thingsboarddata/_data/db/postmaster.pid
/var/lib/docker/volumes/compose_thingsboarddata/_data/db/postmaster.pid
```

**redemarrer le container DANS TOUS LES CAS PREFERER UN ARRET CORRECT DES CONTAINER ;-) docker-compose stop.**




## 3.3. Node-red - pour aider au décryptage des messages
---

Node-red peut permettre d'effectuer des opérations plus complexe sur les messages des capteurs. Chirpstack et The things network permettent d'écrire des éléments decoder et encoder afin de realiser cela. Openenergy utilise la partie decoder pour transformer le meassage payload d'hexadecimal en chaine de caractère (string)

### 3.3.1. Installation
---

Les explications d'installations sont ici:
https://nodered.org/docs/getting-started/raspberrypi

Nodered propose un script pour installer Node.js, npm et Node-RED onto sur un  Raspberry Pi. Ce script peut aussi être utilisé pour faire une mise à jour d'une installation existante quand une nouvelle émission est disponnible.

La commande suivante télécharge et joue le script. ELLE PERMET DE FAIRE UNE MISE A JOUR...

```
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)

```
**Mise en route**

- Manuelle
Vous pouvez utiliser la commande **node-red** dans un terminal. La mémoire limité d'un Raspberry Pi vous pouvez utiliser la commande suivante.
```
node-red-pi --max-old-space-size=256
```
- En tant que service: Les commandes suivante sont fournie pour démarrer node-red en tant que service:

    - node-red-start - démarre Node-RED service et affiche les logs.  Ctrl-C ferme la fenetre mais node-red continu en arrière plan
    - node-red-stop - arret du service Node-RED.
    - node-red-restart - redemarrage du service Node-RED.
    - node-red-log - affiche les  log du service.
    
- Démarrage automatique: il faut jouer une des commandes suivantes:
    - pour activer le service
    ```
    sudo systemctl enable nodered.service
    ```
    - pour désactiver le service
    ```
    sudo systemctl disable nodered.service
    ```
**Ouverture de l'éditeur**
Opening the editor
L'éditeur est accessble à l'adresse suivante: http://localhost:1880.

### 3.3.2. PRE DECODAGE DU PAYLOAD PAR TTN OU CHIRPSTACK CONVERSION EN STRING
---

Pour:
    - The Things Network (TTN) dans la partie application / payload format
    - Chirpstack dans la partie device profil / codec / custom javascript codec function
On peut choisir de decoder ou d'encoder les messages.

Pour le codec ADEUNIS désormais plusieurs exemples sont présents ici https://codec-adeunis.com/download

Afin que l'appel par Nod-Red du codec via un noeud Exec node fonctionne, il ne faut pas oublier d'installer le codec via Npm. Pour cela se rendre dans le répertoire contenant la dernière librairie du codec et executé la commande suivante en respectant la version du codec.

```
npm adeunis-codec-version.tgz
```
Dans les différentes version on peut regarder si le codec est installé
```
pi@raspberrypi:~/codec-adeunis-14 $ npm list |grep @adeunis
@adeunis/codecs@1.4.0 /home/pi/codec-adeunis-14

pi@raspberrypi:~/codec-adeunis-13 $ npm list |grep @adeunis
@adeunis/codecs@1.3.2 /home/pi/codec-adeunis-13
```


Voici un exemple pour convertir le message d'un capteur ADEUNIS modèle Pulse sur l'interface TTN. Le message contient 10 octet en Hexa que l'on doit transformer en chaine de caractère - on doit ajouter un 0 à la chaine de caractère si la valeur de l'octet est inférieur à F. La partie du décodage est envoyé dans la partie adeunis_raw du message global.

```
function Decoder(bytes, port) {
  // Decode an uplink message from a buffer
  // (array) of bytes to an object of fields.
  //var decoded = {};

  // if (port === 1) decoded.led = bytes[0];

  //return decoded;
  
  var result={};
  
  if (bytes[0]<=0xF){
    result="0"+bytes[0].toString(16);
  } else
  {
    result=bytes[0].toString(16);
  }
  
  if (bytes[1]<=0xF){
    result+="0"+bytes[1].toString(16);
  } else
  {
    result+=bytes[1].toString(16)
  }
  
  
  if (bytes[2]<=0xF){
    result+="0"+bytes[2].toString(16);
  } else
  {
    result+=bytes[2].toString(16)
  }
  
  if (bytes[3]<=0xF){
    result+="0"+bytes[3].toString(16);
  } else
  {
    result+=bytes[3].toString(16)
  }
  
  if (bytes[4]<=0xF){
    result+="0"+bytes[4].toString(16);
  } else
  {
    result+=bytes[4].toString(16)
  }
  
  if (bytes[5]<=0xF){
    result+="0"+bytes[5].toString(16);
  } else
  {
    result+=bytes[5].toString(16)
  }
  
  if (bytes[6]<=0xF){
    result+="0"+bytes[6].toString(16);
  } else
  {
    result+=bytes[6].toString(16)
  }
  
  if (bytes[7]<=0xF){
    result+="0"+bytes[7].toString(16);
  } else
  {
    result+=bytes[7].toString(16)
  }
  
  if (bytes[8]<=0xF){
    result+="0"+bytes[8].toString(16);
  } else
  {
    result+=bytes[8].toString(16)
  }
  
  if (bytes[9]<=0xF){
    result+="0"+bytes[9].toString(16);
  } else
  {
    result+=bytes[9].toString(16)
  }
  
  
  return {
    adeunis_raw:result
  }
  
  
}


```

Voici un exemple de décodage sur Chirpstack d'une valeur de température transmis en octet et pour le transformer en flottant (valeur décimale float)

```

// Decode decodes an array of bytes into an object.
//  - fPort contains the LoRaWAN fPort number
//  - bytes is an array of bytes, e.g. [225, 230, 255, 0]
//  - variables contains the device variables e.g. {"calibration": "3.5"} (both the key / value are of type string)
// The function must return an object, e.g. {"temperature": 22.5}
function Decode(fPort, bytes, variables) {
  //return {};
  // Based on https://stackoverflow.com/a/37471538 by Ilya Bursov
  function bytesToFloat(bytes) {
    // JavaScript bitwise operators yield a 32 bits integer, not a float.
    // Assume LSB (least significant byte first).
    var bits = bytes[3]<<24 | bytes[2]<<16 | bytes[1]<<8 | bytes[0];
    var sign = (bits>>>31 === 0) ? 1.0 : -1.0;
    var e = bits>>>23 & 0xff;
    var m = (e === 0) ? (bits & 0x7fffff)<<1 : (bits & 0x7fffff) | 0x800000;
    var f = sign * m * Math.pow(2, e - 150);
    return f;
  }  

```

### 3.3.3. Exemple de Flux / Flow nodered
---

Pour décoder les données d'un capteur adeunis et le transmettre dans une variable d'un device dans le logiciel ubidots on peut utiliser les noeux / nodes suivants:
    - ttn uplink node pour souscrire aux informations d'un capteur en précisant le nom de l'application et le device id
    - function node pour ecrire eventuellement un script supplémentaire
    - exec node qui permet d'appeler la librairie de décodage codec adéunis par exemple:
    ```
    /home/pi/codec-adeunis-10/bin/codec decode --deviceType comfort --json
    ```
    - Json node pour convertir le message en Convert between Json string & object
    - function node pour extraire la partie / variable que vous souhaitez transmettre à Ubidots
    ```
    var payload_out = {
    "humidity":msg.payload.humidity.values[0]
    };
node.log("payload_out:humidity");
node.log(payload_out);

//var msg_out;
msg.payload = payload_out;

return msg;
    ```
    - ubidots_out node pour envoyer les données en précisant le nom de la variable / le jeton d'authentification / le label du capteur défini dans ubidots

## 3.4. Securisation

Les éléments qui participent à la sécurisation de la solution openenergy sont décrite ci-dessous. D'autres éléments peuvent être mis en place afin de sécuriser l'ensemble et les instructions ci-dessous sont loins d'être exhaustive.

### 3.4.1. Sécurisation de Node-Red

Les différents éléments de sécurisation de Node-red sont décrit ici:
https://nodered.org/docs/user-guide/runtime/securing-node-red

Par défaut l'éditeur Node-RED n'est pas sécurisé - quiconque peut acccéder à son IP peut accéder à l'éditeur et effectuer des changements. Cette partie décrit comment vous pouvez sécuriser node-red et propose différentes solution. Ce guide ne reprendra que la partie de sécurisation de l'API attendu que la sécurisation https est effectué via Nginx.

L'éditeur et l'API ne permmettent que les authentification suivante:
- par utilisateur / mot de passe: username/password credential based authentication
- authentification OAuth / Open ID: authentication against any OAuth/OpenID provider such as Twitter or GitHub

C'est la première solution qui a été retenue ici. Dans le fichier settings.js il faut décommenter les ligne suivantes afin de permettre l'authentification utilisateur:
```
adminAuth: {
    type: "credentials",
    users: [
        {
            username: "admin",
            password: "$2a$08$zZWtXTja0fB1pzD4sHCMyOCMYz2Z6dNbM6tl8sJogENOMcxWV9DN.",
            permissions: "*"
        },
        {
            username: "John DOE",
            password: "$2b$08$wuAqPiKJlVN27eF5qJp.RuQYuy6ZYONW7a/UWYxDTtwKFCdB8F19y",
            permissions: "read"
        }
    ]
}
```

Les propriétés de chaque utilisateurs sont définies dans un tableau d'utilisateurs permmettant ainsi à de multiples utilisateur d'acceder à node-red avec différentes permissions. L'exemple ci-dessus défini un admin avec un accès intégral et John DOE avec un accès en lecture

Les mots de passe sont encryptés via l'algorythm Bcrypt et l'instruction suivante permet de générer la clé. L 'installation de l'outil est décrite juste après:
```
node-red-admin hash-pw
```
L'outil va vous demander le mot de passe que vous souhaitez utiliser puis afficher la clé que vous devrez copier dans le fichier de configuration.
De manière alternative vous pouvez utiliser l'instruction suivante depuis le répertoire d'installation de Node-RED pour génerer la clé:
```
node -e "console.log(require('bcryptjs').hashSync(process.argv[1], 8));" your-password-here
```

L'instruction d'installation suivante vous permettra de l'utiliser directement depuis le chemin de votre profil utilisateur.:
```
npm install -g node-red-admin
```

### 3.4.2. Sécurisation de Chirpstack

La sécurisation de Chirpstack s'effectue en changeant le login et le mot de passe par défaut à minima de l'administrateur. Le passage au protocole https s'effectue avec NGINX.

Par défaut le login de Chirpstack est le suivant
```
Username: admin
Password: admin
```
Il vous faut le modifier pour une utilisation en production. En haut à droite cliquer sur Admin et changer de mot de passe.

### 3.4.3. Sécurisation de ThingsBoard


La sécurisation de Thingsboard s'effectue en changeant le login et le mot de passe par défaut à minima de l'administrateur. Le passage au protocole https s'effectue avec NGINX.

Si vous avez installer ThingsBoard avec les éléments de démonstration, les utilisateurs ci-dessous ont été créé. Il vous faudra soit les modifier soit les supprimer pour une utilisation de production

https://thingsboard.io/docs/samples/demo-account/

```
System Administrator
Default system administrator account:

login - sysadmin@thingsboard.org.
password - sysadmin.
Demo Tenant
Default tenant administrator account:

login - tenant@thingsboard.org.
password - tenant.
Demo tenant customers:

Customer A users - customer@thingsboard.org or customerA@thingsboard.org.
Customer B users - customerB@thingsboard.org.
Customer C users - customerC@thingsboard.org.
all users have “customer” password.
```

### 3.4.4. Génération manuelle des Certificats pour le protocole https
Le tuto permettant de générer des certificats tout en simulant une autorité de certification est disponnible à l'adresse suivante:
https://fabianlee.org/2018/02/17/ubuntu-creating-a-trusted-ca-and-san-certificate-using-openssl-on-ubuntu/

Il explique les limitations des derniers navigateurs tel que Firefox ou Chrome concernant les certificats autosignés. Les certificats ne fonctionnant pas seuls, il doivent faire parti d'une chaine de confiance à partir d'un certificat racine / root.

Pour des certificats non autosignés avec chaine de confiance préférer la partie suivante génération des certificats via Certbot de LetsEncrypt

**Pré requis**

Il faut tout d'abord s'assurer que les paquet SSL sont installés:
```
$ sudo apt-get install libssl1.0.0 -y
```
**Modification du fichier de configuration des certificats openssl.cnf**

Puis modifier le fichier de configuration de openssl afin de générer des certificats personalisés openssl.cnf

La première étape est de trouver le modèle de openssl.cnf sur votre ordinateur.  Sur ubuntu on peut le trouver “/usr/lib/ssl/openssl.cnf”.  Sur mac OS c'est plutot  “/System/Library/OpenSSL/”, et sur les variantes Redhat “/etc/pki/tls”.
```
export prefix="mydomain"

cp /usr/lib/ssl/openssl.cnf $prefix.cnf
```

“$prefix.cnf” doit être modifié en fonction des information spécifique concernant les certificat que nous voulons générer. Ainsi les modifications suivantes peuvent être effectuées.

Dans la section [ v3_ca ] ajouter les valeurs suivantes.  Pour le CA CA, cela signifie que nous allons créer un CA qui va etre utiliser pour signer la clé / key signing.
```
[ v3_ca ]
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid:always,issuer
basicConstraints = critical, CA:TRUE, pathlen:3
keyUsage = critical, cRLSign, keyCertSign
nsCertType = sslCA, emailCA
```

Dans la section “[ v3_req ]”, spécifier les éléments suivants avec des nom alternatifs valide pour ce certificat.
```
[ v3_req ]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
#extendedKeyUsage=serverAuth
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = mydomain.com 
DNS.2 = *.dydomain.com
Also uncomment the following line under the “[ req ]” section so that certificate requests are created with v3 extensions.

req_extensions = v3_req
When we generate each type of key, we specify which extension section we want to use, which is why we can share $prefix.cnf for creating both the CA as well as the SAN certificate.
```
**Création du certificat CA: ca.key.pem**

Maintenant nous allons commencer à utiliser OpenSSL pour creer les clé nécessaires et les certificat. Premièrement générons la paire de clés RSA publique et privée / private/public RSA key pair:
```
openssl genrsa -aes256 -out ca.key.pem 2048

chmod 400 ca.key.pem
```
Ceci encode la clé en utilisant une phrase mot de passe / passphrase basée sur l'encryptage AES256.  Ensuite nous avons besoin de créer un certificat auto signé racine / self-signed root CA certificate.
```
openssl req -new -x509 -subj "/CN=myca" -extensions v3_ca -days 3650 -key ca.key.pem -sha256 -out ca.pem -config $prefix.cnf
```
Vous pouvez vérifier ce certificat / root CA certificate en utilisant:
```
openssl x509 -in ca.pem -text -noout
```
Cela vous montre le certificat CA racine / root CA certificate. Ceci nous montre l'émetteur / ‘Issuer’ et le sujet / ‘Subject’ seront les mêmes attendu que le certificat est auto signé / self-signed. Ceci est marqué avec le drapeau / flagged comme “CA:TRUE” signifiant que qu'il sera reconnu comme un certificat racine. Ainsi les navigateur/ browsers et les systèmes d'exploitation / OS vont autoriser l'imprtation de ce certificat dans le magasint / store de certificat racine de confiance / trusted root certificate.
```
Issuer: CN=myca 
... 
Subject: CN=myca 
... 
X509v3 Basic Constraints: 
 critical CA:TRUE, pathlen:3 
X509v3 Key Usage: 
 critical Certificate Sign, CRL Sign 
Netscape Cert Type: 
 SSL CA, S/MIME CA
```
**Création du certificat serveur signé par CA**

Avec le certificat racine CA maintenant créé, nous basculons du coté du certificat serveur. Premièrement générons la paire clés RSA publiques / privées / private/public RSA key pair:
```
openssl genrsa -out $prefix.key.pem 2048
```
Nous n'avons pas utilisé de phrase mot de pass / passphrase sur cette clé simplement parce que le CA est une cible plus éléevée et que nous pouvons toujours générer de nouveau le certificat serveur mais soyez libre de prendre cette précaution supplémentaire.

La commande suivante permet d'effectuer la requete de signature du certificat serveur:
```
openssl req -subj "/CN=$prefix" -extensions v3_req -sha256 -new -key $prefix.key.pem -out $prefix.csr
```
Générer le certificat serveur en utilisant la requete de signature ci-dessus, la clé CA et le certificat CA
```
openssl x509 -req -extensions v3_req -days 3650 -sha256 -in $prefix.csr -CA ca.pem -CAkey ca.key.pem -CAcreateserial -out $prefix.crt -extfile $prefix.cnf
```
Le “$prefix.key.pem” étant la clé privé serveur / server private key et “$prefix.crt” étant le certificat serveur / server certificate.  Vérifion les certificats:
```
openssl x509 -in $prefix.crt -text -noout
```
Ceci nous montre l'émetteur / ‘Issuer’ qui va être le nom du CA / CA name, alors que le sujet est le prefix. Le réglage n'est pas éffectué pour être un CA, et le champ du nom alternatif du sujet / ‘Subject Alternative Name’ contien l'URL qui va être considéré comme valide par les navigateurs.
```
Issuer: 
  CN=myca 
... 
Subject: 
  CN=mydomain 
... 
X509v3 Basic Constraints: 
  CA:FALSE 
X509v3 Key Usage: 
 Digital Signature, Non Repudiation, Key Encipherment 
X509v3 Subject Alternative Name:
 DNS:mydomain.com, DNS:*.mydomain.com
```

**Déploiemeent serveur**

Certains serveur comme HAProxy nécessitent une chaine complète / full chain de certificats comme clé privée / private key (server certificate+CA cert+server private key). Windows IIs nécessite un fichier .pfx. Vous pouvez générer ces fichiers avec les instructions suivantes.
```
cat $prefix.crt ca.pem $prefix.key.pem > $prefix-ca-full.pem

openssl pkcs12 -export -out $prefix.pfx -inkey $prefix.key.pem -in $prefix.crt -certfile ca.pem
```

**Evaluation navigateur**

Lorsque vous utilisez l'url de votre site dans firefox ou chrome avec votre certificat SAN avec la signature CA cela va renvoyer la même erreur qu'avec un certificat auto signé SAN /self-signed SAN cert.  C'est parce que votre certificat racine CA / root CA cert n'est pas connu comme une source de confiance pour les certificats signés / signed certificates.

Dans les réglages de Chrome (chrome://settings), recherchez la partie Certificat / “certificates” et cliquer sur Gérez les certificats / “Manage Certificates”.  Sur windows cela va ouvrir la page Windows certificate manager et vous importerez le fichier “ca.pem”  dans l'onglet “Trusted Root Certification Authorities”. 

D'autre variantes en anglais ci-dessous:

On windows, This is equivalent to adding it through mmc.exe, in the “local user” trusted root store (not the computer level).  On Linux, Chrome manages its own certificate store and again you should import “ca.pem” into the “Authorities” tab.  This should now make the security icon turn green.

In Firefox Options (about:preferences), search for “certificates” and click “View Certificates”.  Go to the “Authorities” tab and import “ca.pem”.  Check the box to have it trust websites, and now the lock icon should turn green when you visit the page.

Although there is a little friction doing this import, it is a one-time cost because any other certificates that you sign with this CA are now trusted.  So if a cert expires and you have to replace it, or you need to change the URLs in a SAN and refresh it, none of the browsers will have an issue with trust.

SUR ANDROID parametre / sécurité et confidentialité / autres paramètres / cryptage et référence / certificat de confiance / onglet utilisateur  On retrouve le certificat MyCa installé via carte mémoire / openssl / certel001 / Ca.pem

**Génération des certificats via Certbot de LetsEncrypt**

https://janw.me/raspberry-pi/install-lets-encrypt-ssl-on-raspberry-pi/

Se connecter au RaspberryPi

```
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot

sudo ln -s /snap/bin/certbot /usr/bin/certbot

sudo certbot --nginx
```

trop la classe
il retrouve tout seul les éléments du serveur nginx www.el001.is-a-green.com et el001.is-a-green.com

ca bug pour www parce qu'il n'y a pas de dns et pour el001 tout cours

je rajoute le port 80 pour raspberrypi dans le natpat de la livebox... cette fois ci j'ai un message de félicitation...

By default Certbot should have installed auto renewal. But we are going to check it with the command: systemctl list-timers --all
The command to renew the certificates is sudo certbot renew
You can also run this command by itself to test it out.

As it is run by root we will also add it to the crontab of the root user.

sudo crontab -e
Inside we add the following command.

0 0 * * 1 certbot renew
Here we set it to run every Monday at 0:00 (so Sunday to Monday night)
That’s more then enough, you can run it more if you want, I would not run it less.

Test your SSL connection.
Finally go to ssllabs.com and test your site. Behind the scenes Certbot also adds a bunch of security settings which will help get that A+.

Dans les fichiers de configuration de nginx aussi bien pour default que pour votre nom de domaine, toutes les entrées ssl doivent être remplacé par celle écrite automatiquement et commentée par # cerbot 

```
ssl_certificate /etc/letsencrypt/live/el001.is-a-green.com/fullchain.pem; # managed by Certbot
ssl_certificate_key /etc/letsencrypt/live/el001.is-a-green.com/privkey.pem; # managed by Certbot
```


### 3.4.5. HTTPS avec Nginx

Il est maintenant tant de procéder à la sécurisation du protocole Http en le passant en Https et en utilisant Nginx.
La documentation ci-dessous s'inspire largement de la mise en place de Nginx telle que décrite ici: https://projetsdiy.fr/securiser-node-red-nginx-openssl-ubuntu/

#### 3.4.5.1. Installation de Nginx
Nginx s’installe très simplement à l’aide d’une simple commande apt-get.
```
sudo apt-get update
sudo apt-get install nginx
```
Acceptez l’installation de toutes les dépendances qui sont demandées durant l’installation.

** Nginx fonctionne avec des sites-disponnible / sites-available que l'on peut utiliser ou non en créant un lien symbolique dans la partie sites-enabled**

Le fichier de configuration final utilisé est disponible dans la partie settings/nginx/sites-available/my_server.com. Il permet de rediriger les ports:
- 1446 vers node-red
- 1447 vers Chirpstack
- 1448 vers Thingsboard

#### 3.4.5.2. Configurer Nginx pour utiliser une connexion SSL

Dans le chapitre précédent nous avons générer une clé et un certificat, nous allons créer un fichier de configuration. Nous pourrons l’appeler my_server.securise.com.

Ouvrez un nouveau fichier de configuration avec nano

sudo nano /etc/nginx/sites-available/my_server.securise.com

Adaptez l’exemple ci-dessous en fonction de vos besoins et collez le dans le fichier puis enregistrez avec CTRL+X puis O.
```
server {
    listen 80;
    listen 443 ssl http2;
    server_name my_server.securise.com;
    # les deux ligne ci-dessous sont à adapter en fonction des fichiers de certificat
    ssl_certificate /etc/nginx/ssl/nginx.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx.key;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+$
    ssl_prefer_server_ciphers On;
    ssl_session_cache shared:SSL:128m;
    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 8.8.8.8;

    location / {
        if ($scheme = http) {
            return 301 https://$server_name$request_uri;
        }
        proxy_pass http://localhost:1880;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location '/.well-known/acme-challenge' {
        root /var/www/html;
    }
}
```
Quelques explications (rapides)

- La clé server_name permet de définir le nom du site internet par lequel on obtiendra une connexion sécurisée via Nginx.
- Les clés ssl_certificate et ssl_certificate_key permettent de définir le dossier dans lequel se trouvent le certificat et la clé créée précédemment.
- Le bloc “if ($scheme = http) { return 301 https://$server_name$request_uri; }" permet de renvoyer toutes les connexions http non sécurisées vers une liaison HTTPS
- "proxy_pass http://localhost:1880;" permet de pointer vers la page de Node-RED

Il reste à créer un lien symbolique vers le dossier sites-enabled pour rendre actif la configuration.
```
sudo ln -s /etc/nginx/sites-available/node-red.securise.com /etc/nginx/sites-enabled/
```
#### 3.4.5.3. Configuration du fichier hosts
Pour que l’URL soit accessible depuis un navigateur, il faut modifier le fichier hosts. Récupérez l’adresse IP de votre PC avec la commande ifconfig ou ipconfig sur windows puis modifiez le fichier /etc/hosts
```
sudo nano /etc/hosts
```
et ajoutez par exemple
```
127.0.0.1       localhost
192.168.2.2     my_server.securise.com
```
Enregistrez avec CTRL+X puis O.


Il se peut que des éléments de configuration du firewall soient nécessaires. Ceci est détaillé dans le fichier d'origine de ce chapitre

#### 3.4.5.4. Autre fichier de configuration de Nginx
Attendu que le redémarrage de Nginx ne s'effectuait pas correctement du notamment à des problématiques lié à la ligne ssl_ciphers 
le fichier de configuration suivant present dans cette documentation à été largement utilisé car il était bien commenté sur la redirection des requetes http vers https: https://korben.info/nginx-rediriger-http-https.html

Si vous utilisez Nginx en reverse proxy et que vous cherchez la méthode pour rediriger de manière permanente (en 301) tout le trafic arrivant sur le HTTP vers du HTTPS pour apporter confort, sécurité et volupté à vos visiteurs, voici comment faire…

Ouvrez votre nginx.conf (qui se trouve surement dans un répertoire comme /etc/nginx/)
```
nano nginx.conf
```
Et faites en sorte d’y placer la ligne de reécriture suivante, dans la section réservée à la config HTTP.
```
return 301 https://$server_name$request_uri;
```

Les autres sections sont dédiées au HTTPS et à la config SSL.
```
## le serveur http sur le port 80

server {
      listen      1.2.3.4:80 default;
      server_name example.com www.example.com;
      ## Redirige le HTTP vers le HTTPS ##
      return 301 https://$server_name$request_uri;
}

## Le serveur https sur le port 443. N'oubliez pas vote config SSL
server {
      access_log  logs/example.com/ssl_access.log main;
      error_log   logs/example.com/ssl_error.log;
      index       index.html;
      root        /usr/local/nginx/html;
      
      ## Début de la config SSL ##
      listen      1.2.3.4:443 ssl;
      server_name example.com www.example.com;
      fastcgi_param HTTPS on;

     ## Redirection de l url avec www vers une url sans www
      if ($host = 'www.example.com' ) {
         rewrite  ^/(.*)$  https://example.com/$1  permanent;
      }

    ### config SSL - A vous de jouer ###
     ssl_certificate      ssl/example.com/example.com_combined.crt;
     ssl_certificate_key  ssl/example.com/example.com.key_without_password;
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
        proxy_pass  http://exampleproxy;
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503;
        proxy_set_header        Host            $host;
        proxy_set_header        X-Real-IP       $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
      }
}
```

Sauvegardez le fichier (CTRL+X puis O) et relancez nginx
```
nginx -s reload
```
Pour vérifier que tout fonctionne correctement, allez faire un tour sur la version HTTP de votre site. Si vous êtes rebasculé automatiquement sur la version en HTTPS et que tout fonctionne, vous avez réussi !

### 3.4.6. Nginx et démarrage des services
Il faut que Nginx attende que les services de chirpstack nodered et thingsboard soient démarré.
Il faut editer la configuration du service
```
sudo systemctl edit --full nginx.service
```
Il faut ajouter les éléments des autre service dans la ligne After= qui impose à Nginx d'attendre que les autres services soient actif.
```
[Unit]
Description=A high performance web server and a reverse proxy server
Documentation=man:nginx(8)
After=network.target nss-lookup.target chirpstack-application-server.service chirpstack-gateway-bridge.service chirpstack-network-server.service nodered.service  thingsboard.service
```




### 3.4.7. Oauth2-Proxy: Nginx et 2 facteur authentication
Afin de permettre la sécurite sur nginx avant d'autoriser l'acces a chirpstack nodered et thingsboard

source: https://oauth2-proxy.github.io/oauth2-proxy/docs/

la version armv6 de oauth2-proxy est celle fonctionnelle sur raspberry pi 3 B+

Générer un cookie secret 
```
python -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(16)).decode())'
```
Choisir google par défaut comme fournisseur de oauth2 (effectuer avec pas mal d'intuition l'ensemble des instructions afin de parvenir au résultat ci dessous)

Il faut choisir un "provider d'autorisation oauth2" comme Google.
Les actions a effectuer pour permettre cela sont présente ici en fonction du "provider".
https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/oauth_provider

Pour google il faut créer une application web, choisir les url authorisé pour les demande d'autorisation et récuperer client id et client secret. Le fichier json mentionné n'a pas été utilisé

On peut ainsi lancer oauth2-proxy en ligne de commande
```
## exemple de ligne de commande complete
/usr/local/lib/oauth2-proxy/./oauth2-proxy    
--cookie-secret=   \ 
--cookie-secure=true    \
--provider=google    \
--reverse-proxy=true    \
--authenticated-emails-file=/etc/oauth2-proxy/authenticated-emails    \
--client-id=  \  
--client-secret=

```
ou via un fichier de configuration
```
## exemple de ligne de commande pour appeler oauth2-proxy
/usr/local/lib/oauth2-proxy/./oauth2-proxy --config=/etc/oauth2-proxy/oauth2-proxy.cfg
```
Le fichier des email autorisé doit contenir une adresse mail par ligne encadrée par des  "".

Nginx et Oauth2 fonctionnent sur la meme machine et donc les éléments liés a la securité ssl n'ont pas été implémentés.
```
 --tls-cert-file=/path/to/cert.pem \
 --tls-key-file=/path/to/cert.key \
```

Afin de gérer l'accès aux différentes applications on passe par des sous domaines.
Attention a bien étendre le certificat certbot à l'ensemble des sous domaines utilisés.

Ainsi les fichier de configuration nginx sont les suivants

default
```
server {
    listen 443 default ssl;
    server_name el001.energyleaks.org; #el001.is-a-green.com;
    ssl_certificate /etc/letsencrypt/live/el001.is-a-green.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/el001.is-a-green.com/privkey.pem; # managed by Certbot

    add_header Strict-Transport-Security max-age=2592000;

	root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                try_files $uri $uri/ =404;
        }
#   location /authenticator {
	# authentification avec les login 	
#                auth_pam "Secure area";
#                auth_pam_service_name "nginx";
#        }
#   location /oauth2 {
#        proxy_pass http://127.0.0.1:4180;
#        proxy_set_header Host $host;
#        proxy_set_header X-Real-IP $remote_addr;
#        proxy_set_header X-Scheme $scheme;
#        proxy_connect_timeout 1;
#        proxy_send_timeout 30;
#        proxy_read_timeout 30;
#    }

}

```
Cette partie laisse un libre acces à la partie cartographique de mon application. Les parties authenticator et oauth2 étaient présentes à des fins de tests.


par exemple l'application chirpstack
```

server {
	# chirpstack
  #include ssl/ssl.conf

  #listen 80;
  #listen 1447 ssl http2;
	listen 443 ssl http2;

  server_name chirpstack.el001.energyleaks.org; #chirpstack.el001.is-a-green.com;
    ssl_certificate /etc/letsencrypt/live/el001.is-a-green.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/el001.is-a-green.com/privkey.pem; # managed by Certbot

    
   location /oauth2/ {
    proxy_pass       http://127.0.0.1:4180;
    proxy_set_header Host                    $host;
    proxy_set_header X-Real-IP               $remote_addr;
    proxy_set_header X-Scheme                $scheme;
    proxy_set_header X-Auth-Request-Redirect $request_uri;
  }

  location /
  {
    auth_request /oauth2/auth;
    error_page 401 = /oauth2/sign_in;

    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-Port $server_port;
    proxy_set_header X-Forwarded-Proto "https";
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass http://localhost:8080;
	#proxy_bind 127.0.0.1:8080;
	#proxy_pass http://el001.is-a-green.com/chirpstack;


# handle websocket 
#for thingsboard widget like showing latest telemetry
# for node-red connection lost message:Lost connection to server, reconnecting
# for chirpstack
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";


  }

}
```
le auth_request permet d'effectuer du controle d'accès. Le proxy_pass permet d'indiquer l'url à ouvrir à la fin du processus d'authentification.


le fichier authenticated-emails permet de gérer les mails autorisés.


POUR THINGSBOARD on peut mettre en place oauth2 comme décrit ici afin de laisser les éléments public accessible
https://thingsboard.io/docs/user-guide/oauth-2-support/

Le réglage de administration paramètre système général est sur http://thingsboard.el001.energyleaks.org

Les réglages de l'uri autorisé est
http://localhost:8085/login/oauth2/code/ pour la machine hote
https://thingsboard.el001.energyleaks.org/login/oauth2/code/ pour le général

ainsi sur le réseau local https://192.168.1.101:1448/login il n'est pas possible de se connecter via google car ce type d'URI n'est pas admise meme avec le nom dns de la machine raspberrypi.

Sur nginx il faut permettre l'affichage du button dans l'écran de login
```
#this settings allow google oauth2 button to show
       proxy_set_header  Host               $host;
       proxy_set_header  X-Real-IP          $remote_addr;
       proxy_set_header  X-Forwarded-For    $proxy_add_x_forwarded_for;
       proxy_set_header  X-Forwarded-Proto  $scheme;
       proxy_pass http://localhost:8085;
```

### 3.4.8. Oauth2-Proxy: service sur RaspberryPi
https://github.com/oauth2-proxy/oauth2-proxy/blob/master/contrib/oauth2-proxy.service.example
et
https://www.raspberrypi.org/documentation/linux/usage/systemd.md

Editer le fichier suivant dans  /etc/systemd/system/oauth2-proxy.service en tant que root pour un raspberrypi
```
# Systemd service file for oauth2-proxy daemon
#
# Date: Feb 9, 2016
# Author: Srdjan Grubor <sgnn7@sgnn7.org>

[Unit]
Description=oauth2-proxy daemon service
After=syslog.target network.target

[Service]
# www-data group and user need to be created before using these lines
User=www-data
Group=www-data

# ligne de commande a faire correspondre dans la ligne execstart pour notre configuration
# /usr/local/lib/oauth2-proxy/./oauth2-proxy --config=/etc/oauth2-proxy/oauth2-proxy.cfg

#ExecStart=/usr/local/bin/oauth2-proxy --config=/etc/oauth2-proxy.cfg
ExecStart=/usr/local/lib/oauth2-proxy/oauth2-proxy --config=/etc/oauth2-proxy/oauth2-proxy.cfg
ExecReload=/bin/kill -HUP $MAINPID

KillMode=process
Restart=always

[Install]
WantedBy=multi-user.target
```
Once this has been copied, you have to inform systemd that a new service has been added. This is done with the following command:
```
sudo systemctl daemon-reload
```
Now you can attempt to start the service using the following command:
```
sudo systemctl start oauth2-proxy.service
```
Stop it using following command:
```
sudo systemctl stop oauth2-proxy.service
```
When you are happy that this starts and stops your app, you can have it start automatically on reboot by using this command:

```
sudo systemctl enable oauth2-proxy.service
```
The systemctl command can also be used to restart the service or disable it from boot up!

### 3.4.9. frontend: login
---
tutorial: https://www.youtube.com/watch?v=b91XgdyX-SM
github: https://github.com/mehulmpt/node-auth-youtube

dans la partie server.js il faut faire pointer la partie mongoose vers l'adresse ip du container mongo db. -> cf mongo / mongo express container
mongoose.connect('mongodb://root:example@172.25.0.5:27017/login-app-db?authSource=admin', {	
	useNewUrlParser: true,
	useUnifiedTopology: true,
	useCreateIndex: true
})


### 3.4.10. frontend: Cartographie / Leaflet / Progressive web app
---

#### 3.4.10.1. Debugage smartphone / android
---
démarrer le android debug bridge
adb start-server
passer en mode developper sur le smartphone autoriser le mode USB debugage
système / option pour les dévelopeur / debogage USB
autoriser le transfert de fichier (plutot que le mode recharge batterie uniquement)
sur chrome du PC aller chrome://inspect/#devices ce qui permet d'utiliser les outils de développement
sur le smartphone démarrer chrome
se rendre sur OpenEnergy Mobile Leaflet Map
https://el001.is-a-green.com/
et sur chrome du pc choisir le bon onglet et cliquer sur inspect

#### 3.4.10.2. mongodb et cartographie
---
schema mongodb pour mongoose: https://transform.tools/json-to-mongoose
mongo db geospatial query:  https://examples.javacodegeeks.com/software-development/mongodb/mongodb-geospatial-query-operators-example/
                            http://thecodebarbarian.com/80-20-guide-to-mongodb-geospatial-queries

# 4. Docker Architecture

After playing with raspberry we implemented on real infrastructure thanks to Echinix ;)

## 4.1. install
---
source https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

Avant toute chose - et pour eviter tout ennui lié à l'installation - s'assurer d'une bonne désinstallation ;-)
Uninstall Docker Engine
Uninstall the Docker Engine, CLI, and Containerd packages:
```
 sudo apt-get purge docker-ce docker-ce-cli containerd.io
```
Images, containers, volumes, or customized configuration files on your host are not automatically removed. To delete all images, containers, and volumes:
```
 sudo rm -rf /var/lib/docker
 sudo rm -rf /var/lib/containerd
```

Install using the repository
Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker repository. Afterward, you can install and update Docker from the repository.

Set up the repository
Update the apt package index and install packages to allow apt to use a repository over HTTPS:
```
 sudo apt-get update
 sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```
Add Docker’s official GPG key:
```
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
Use the following command to set up the stable repository. To add the nightly or test repository, add the word nightly or test (or both) after the word stable in the commands below. Learn about nightly and test channels.

Note: The lsb_release -cs sub-command below returns the name of your Ubuntu distribution, such as xenial. Sometimes, in a distribution like Linux Mint, you might need to change $(lsb_release -cs) to your parent Ubuntu distribution. For example, if you are using Linux Mint Tessa, you could use bionic. Docker does not offer any guarantees on untested and unsupported Ubuntu distributions.

Pour mon linux mint la liste des correspondance avec ubuntu est ici. Pour ma par Uma 20.2 correspond a Ubuntu Focal a modifier dans la source des logiciel de mintupdate.
https://linuxmint.com/download_all.php
```
 echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
Install Docker Engine
Update the apt package index, and install the latest version of Docker Engine and containerd, or go to the next step to install a specific version:

 sudo apt-get update
 sudo apt-get install docker-ce docker-ce-cli containerd.io
 ```
Verify that Docker Engine is installed correctly by running the hello-world image.
```
 sudo docker run hello-world
```
REBOOT!!!!!!! to avoid pb with sudo rights

to have a home .docker folder you must login to docker hub

## 4.2. Change Docker’s root dir
---
Par défaut les images sont dans /var/lib/docker

source: https://tienbm90.medium.com/how-to-change-docker-root-data-directory-89a39be1a70b
The standard data directory used for docker is /var/lib/docker, and since this directory will store all your images, volumes, etc. it can become quite large in a relative small amount of time.
If you want to move the docker data directory on another location you can follow the following simple steps.
1. Stop the docker daemon
sudo service docker stop
2. Add a configuration file to tell the docker daemon what is the location of the data directory
Create docker daemon configuration with following content:
  Version before v17.05.0
```
{ 
   "graph": "/path/to/your/new/docker/root" 
}
```
“"/path/to/your/new/docker/root”” is the new location you want to use for your new docker data directory.
  v17.05.0 and newer
From v17.05.0, the -g or --graph flag for the dockerd or docker daemon command was used to indicate the directory in which to store persistent data and resource configuration and has been replaced with the more descriptive --data-root flag. We create daemon configuration file:

Pour creer un daemon config file il faut creer le fichier daemon.json dans le répertoire /etc/docker et copier les lignes suivantes
```
{ 
   "data-root": "/path/to/your/new/docker/root"
}
```
These flags “graph” were added before Docker 1.0, so will not be removed, only hidden. You still use this flag but simply discourage from using it.
3. Copy the current data directory to the new one
We can use both rsync and cp command:
```
sudo rsync -aP /var/lib/docker/ "/path/to/your/new/docker/root"
sudo cp -rp /var/lib/docker/* "/path/to/your/new/docker/root/"
```
4. Rename the old docker directory
Rename old directory to ensure that docker daemon can’t use old directory.
```
sudo mv /var/lib/docker /var/lib/docker.old
```
5. Restart the docker daemon
```
sudo service docker start
```
6. Test
If everything is ok you should see no differences in using your docker containers.
pour tester on peut utiliser la commande
```
docker info
```
le résultat de la commande doit contenir le chemin dans le flag : Docker Root Dir
7. Clean old data.
Alter all, we should clean old data:
```
rm -rf /var/lib/docker.old
```

## 4.3. Docker-compose
---
Docker compose permet d'orchester plusieurs container.

source: https://docs.docker.com/compose/install/
installation - choisir la version plus récente en se reportant au lien ci dessus
```
 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

```
rendre l'élément executable
```
sudo chmod +x /usr/local/bin/docker-compose
```
rendre la commande executable pour l'utilisateur
```
 sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```


vérification que tout est ok
```
docker-compose --version
```


## 4.4. Docker developement
---

Use vs codium with docker plugin
source: https://vscodium.com/#install
source plugin: Nom : Docker
ID : ms-azuretools.vscode-docker
Description : Makes it easy to create, manage, and debug containerized applications.
Version : 1.17.0
Serveur de publication : ms-azuretools
Lien de la Place de marché pour VS : https://open-vsx.org/vscode/item?itemName=ms-azuretools.vscode-docker

### 4.4.1. Nginx container
---
https://hub.docker.com/_/nginx
abandonné
preferez certbot nginx container

### 4.4.2. Cerbot nginx container
---
https://hub.docker.com/r/certbot/certbot
tuto / howto: https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71
script: https://github.com/wmnnd/nginx-certbot

#192.168.1.48	docker.is-a-green.com
192.168.1.48	docker.energyleaks.org
192.168.1.48	docker-chirpstack.energyleaks.org
192.168.1.48	docker-nodered.energyleaks.org
192.168.1.48	docker-thingsboard.energyleaks.org
192.168.1.48	docker-grafana.energyleaks.org
192.168.1.48	docker-grafana-pub.energyleaks.org

 docker.energyleaks.org docker-chirpstack.energyleaks.org docker-nodered.energyleaks.org docker-thingsboard.energyleaks.org docker-grafana.energyleaks.org	docker-grafana-pub.energyleaks.org

dans la partie domains de ./init-letsencypt.sh on met les domaines à la suite et son adresse mail dans la partie email
 ```
 docker.energyleaks.org chirpstack.docker.energyleaks.org nodered.docker.energyleaks.org thingsboard.docker.energyleaks.org grafana.docker.energyleaks.org	grafana-pub.docker.energyleaks.org
```

 Pour plusieurs domain dans le app.conf on met tous les domaines séparés par une virgule.
 Les liens vers les ssl_certificate doivent reprendre UNIQUEMENT le premier domaine de ./init-letsencrypt.sh ici c'est docker.el001.energyleaks.org

 /var/root/certbot cad dans le volume certbot/www va contenir les fichier des page html.
 le proxy_pass et les trois lignes suivantes permettent de pointer vers chirpstack / nodered / grafana / thingsboard

```
server {
    listen 80;
    server_name docker.el001.energyleaks.org, grafana.docker.el001.energyleaks.org;
    server_tokens off;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}
 
server {
    listen 443 ssl;
    server_name docker.el001.energyleaks.org;
    server_tokens off;

    ssl_certificate /etc/letsencrypt/live/docker.el001.energyleaks.org/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/docker.el001.energyleaks.org/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        root /var/www/certbot;
        #proxy_pass  http://docker.energyleaks.org;
        #proxy_set_header    Host                $http_host;
        #proxy_set_header    X-Real-IP           $remote_addr;
        #proxy_set_header    X-Forwarded-For     $proxy_add_x_forwarded_for;
    }
}


server {
    listen 443 ssl;
    server_name grafana.docker.el001.energyleaks.org;
    server_tokens off;

    ssl_certificate /etc/letsencrypt/live/docker.el001.energyleaks.org/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/docker.el001.energyleaks.org/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        root /var/www/certbot;
        #proxy_pass  http://grafana.docker.energyleaks.org;
        #proxy_set_header    Host                $http_host;
        #proxy_set_header    X-Real-IP           $remote_addr;
        #proxy_set_header    X-Forwarded-For     $proxy_add_x_forwarded_for;
    }
}
```
#certbot nginx renew certificate renouvellement de certificat

modifier dans ./init-letsencrypt.sh
staging=1 # Set to 1 if you're testing your setup to avoid hitting request limits
bien remettre à 0 pour de la production...

depuis le répertoire /el/compose lancer la commande suivante lors de l'ajout d'un nouveau domaine
certbot-nginx/init-letsencrypt.sh


ATTENTION ne pas utiliser directement ./init-letsencrypt.sh depuis le répertoire certbot-nginx car dans ce cas la la commande va appeler le docker-compose.yml présent dans ce répertoire et donner l'illusion d'un comportement correct.


pour le lancer dans /el/compose
```
docker-compose run --rm --entrypoint " certbot renew --dry-run " certbot
```
et sans le dry-run ensuite (le dry run effectue un essai de renouvellement)
```
docker-compose run --rm --entrypoint " certbot renew" certbot
```
faut faire relire les certificats par le nginx cad redemmarrer le container


#### 4.4.2.1. certbot nginx container TROUBLESHOOTING
---
Troubleshoot sur le ./init-letsencrypt.sh
Certbot failed to authenticate some domains (authenticator: webroot). The Certificate Authority reported these problems:
  Domain: nodered.echinix.energyleaks.org
  Type:   connection
  Detail: Fetching http://nodered.echinix.energyleaks.org/.well-known/acme-challenge/rABa5ysKBBo_SR_4viMYBWqKa6EDZrivQqtv5AnVFoI: Timeout during connect (likely firewall problem)

NE PAS OUBLIER QUE LE PORT HHTP:80 DOIT ETRE OUVERT VERS L EXTERIEUR!!!!!!!



On doit s'intéresser au docker networking
youtube: https://www.youtube.com/watch?v=c6Ord0GAOp8
on a les principe des network jusqu'a du ping entre les container

A priori on peut définir des adresses ip fixes comme dans l'exemple suivant
```
version: '2'

services:
  redis:
    image: redis:2.8
    networks:
      frontapp:
        ipv4_address: 172.25.0.11

  elasticsearch:
    image: elasticsearch:2.2
    networks:
      frontapp:
        ipv4_address: 172.25.0.12

  postgres:  
    image: postgres:9.5
    environment:
      POSTGRES_USER: elephant
      POSTGRES_PASSWORD: smarty_pants
      POSTGRES_DB: elephant
    volumes:
      - /var/lib/postgresql/data
    networks:
      frontapp:
        ipv4_address: 172.25.0.10

networks:
  frontapp:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.25.0.0/16
          gateway: 172.25.0.1
```
          


### 4.4.3. Oauth2-proxy container
---
source: https://hub.docker.com/r/bitnami/oauth2-proxy
command line to launch direct: docker run -p 4180:4180 -p 8443:8443 bitnami/oauth2-proxy:7     --cookie-secure=false     --upstream="file:///dev/null"     --http-address="0.0.0.0:4180"     --https-address="0.0.0.0:8443"     --redirect-url="http://internal.website.com/oauth2/callback"     --cookie-secret="NXA4K2lMUGsrSnFLYnprWnZESE5GUDNINzIrc2NHUnQ="     --client-id=changeme     --client-secret=changeme     --email-domain=*
via docker compose pour configurer le proxy et les email autorisé via des volumes sur l'hote:
volumes:
      #configuation file
      - "./oauth2-proxy/oauth2-proxy.cfg:/opt/bitnami/oauth2-proxy/bin/oauth2-proxy.cfg"
      # authenthicated emails file
      - "./oauth2-proxy/authenticated-emails.cfg:/opt/bitnami/oauth2-proxy/bin/authenticated-emails.cfg"

    command:  /opt/bitnami/oauth2-proxy/bin/oauth2-proxy --config=/opt/bitnami/oauth2-proxy/bin/oauth2-proxy.cfg

    dans le fichier de config modifier la ligne 
    #http_address = "127.0.0.1:4180" #when operating on same server
 http_address = "0.0.0.0:4180" #when operating frome another server

### 4.4.4. mongo / mongo-express container
---
source: https://hub.docker.com/_/mongo

ajouter les element suivant au docker-compose.yml
il faut ouvrir le port 27017 pour un acces direct.
```
mongo:
    image: mongo
    restart: always
    ports:
      - 27017:27017
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example

  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 8081:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: example
      ME_CONFIG_MONGODB_URL: mongodb://root:example@mongo:27017/

```
On peut ajouter les address ip v4 pour avoir un adressage static à ce service.

On peut acceder via le plugin mongodb de vs codium 
```
Nom : MongoDB for VS Code
ID : mongodb.mongodb-vscode
Description : Connect to MongoDB and Atlas directly from your VS Code environment, navigate your databases and collections, inspect your schema and use playgrounds to prototype queries and aggregations.
Version : 0.7.0
Serveur de publication : mongodb
Lien de la Place de marché pour VS : https://open-vsx.org/vscode/item?itemName=mongodb.mongodb-vscode
mongodb.mongodb-vscode
```
avec la chaine suivante. authSource=admin permet de ne pas avoir de problème d'authentification. login-app-db est la base active.
```
mongodb://root:example@172.25.0.5:27017/login-app-db?authSource=admin&readPreference=primary&directConnection=true&ssl=false
```
source: https://docs.mongodb.com/manual/reference/connection-string/

voir comment creer un utilisateur:
source : https://docs.mongodb.com/manual/tutorial/create-users/#std-label-create-users

Pour que le plugin fonctionne il faut installer MONGO SHELL
source: https://www.mongodb.com/try/download/shell
sudo dpkg -i path to deb file
sudo dpkg -i /home/eleq/Downloads/mongodb-mongosh_1.1.7_amd64.deb 
optionnellement sudo apt-get install -f

avec un echinix et un remote desktop rdp j'ai l'erreur suivante lorsque je cherche a me connecter
mongodb vscodium extension unable to create connexion: Error or unsupported transport disabled for adress disabled





pour convertir les élément openstreetmap osm en schéma mongoos utiliser l'outil suivant.
https://transform.tools/json-to-mongoose



### 4.4.5. Nodejs container
---
source: https://hub.docker.com/_/node
instructions: https://github.com/nodejs/docker-node/blob/main/README.md#how-to-use-this-image





### 4.4.6. Nodered Container
---
https://hub.docker.com/r/nodered/node-red

### 4.4.7. Thingsboard container
---
thingsboard docker documentation here: https://thingsboard.io/docs/user-guide/install/docker/?ubuntuThingsboardQueue=inmemory
https://hub.docker.com/r/thingsboard/tb-postgres

Ce container contient une base postgres et un mqtt mosquitto

DIFFICULTE A DEMARRER...SUREMENT CONFLIT PORT 5432...port postgresql......

Il faut changer les droit des répertoires suivants
```
$ mkdir -p ~/.mytb-data && sudo chown -R 799:799 ~/.mytb-data
$ mkdir -p ~/.mytb-logs && sudo chown -R 799:799 ~/.mytb-logs
```
MAJ image et base de données

Le $choisir_la_version permet d'incrémenter d'une version a une version
```
#Original Instructions
docker pull thingsboard/tb-postgres
docker-compose stop
docker run -it -v ~/.mytb-data:/data --rm thingsboard/tb-postgres upgrade-tb.sh
docker-compose rm mytb
docker-compose up

#JEM modified Instructions
# a utiliser dans le home eleq el compose directory
/home/jemesmain/dockerFile/compose/thingsboard/data

docker pull thingsboard/tb-postgres:$choisir_la_version
docker-compose stop thingsboard
#docker run -it -v thingsboarddata:/data --rm thingsboard/tb-postgres:latest upgrade-tb.sh
docker run -it -v /home/eleq/el/compose/thingsboard/data:/data --rm thingsboard/tb-postgres:$choisir_la_meme_version upgrade-tb.sh
docker run -it -v /home/jemesmain/dockerFile/compose/thingsboard/data:/data --rm thingsboard/tb-postgres:latest upgrade-tb.sh
docker-compose rm thingsboard
docker-compose up -d thingsboard
```
L'instruction avec thingsboarddata ne fonctionne pas pour la maj de la database
CREATE DATABASE
cat: /data/.upgradeversion: No such file or directory
Starting ThingsBoard upgrade ...
FROM_VERSION variable is invalid or unspecified!
L'instruction avec le chemin complet fonctionne ici on a lancé un upgrade depuis 3.3.4.1 (version de l'image) depuis une database en version 3.3.1. On a la version actuelle dans thingsboard/data/.upgradeversion
SI LE PROCESSUS PLANTE UNE MANIERE DE S EN SORTIR EST DE PULL UNE VERSION IDENTIQUE A upgradeversion DU CONTAINER
```
The files belonging to this database system will be owned by user "thingsboard".
This user must also own the server process.

The database cluster will be initialized with
 locale "C.UTF-8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /data/db ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... Etc/UTC
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok

initdb: warning: enabling "trust" authentication for local connections
You can change this by editing pg_hba.conf or using the option -A, or
--auth-local and --auth-host, the next time you run initdb.

Success. You can now start the database server using:

    /usr/lib/postgresql/12/bin/pg_ctl -D /data/db -l logfile start

Starting ThingsBoard upgrade ...
  ______    __      _                              ____                               __
 /_  __/   / /_    (_)   ____    ____ _   _____   / __ )  ____   ____ _   _____  ____/ /
  / /     / __ \  / /   / __ \  / __ `/  / ___/  / __  | / __ \ / __ `/  / ___/ / __  /
 / /     / / / / / /   / / / / / /_/ /  (__  )  / /_/ / / /_/ // /_/ /  / /    / /_/ /
/_/     /_/ /_/ /_/   /_/ /_/  \__, /  /____/  /_____/  \____/ \__,_/  /_/     \__,_/
                              /____/

 ===================================================
 :: ThingsBoard ::       (v3.3.4.1)
 ===================================================

Starting ThingsBoard Upgrade from version 3.3.1 ...
Upgrading ThingsBoard from version 3.3.1 to 3.3.2 ...
Upgrading ThingsBoard from version 3.3.2 to 3.3.3 ...
Failed updating schema!!!
org.postgresql.util.PSQLException: FATAL: database "thingsboard" does not exist
```

POUR MODIFIER LES PORTS DE LA CONNECTION VERS LA BASE DE DONNEES
trois fichiers:
docker-compose.yml: modifier la ligne dans le service thingsboard 5432->15432
thingsboard.yml: ligne 522 / 5432->15432
postgresql.conf: ligne 64 / 5432 ->15432
pour des probleme de jdbc connection.


#### 4.4.7.1. Thingsboard container TROUBLESHOOTING
---
see also Thingsboard TROUBLESHOOTING part

##### 4.4.7.1.1. ERROR lwM2M
---
2022-03-31 19:23:59,966 [main] ERROR o.s.boot.SpringApplication - Application run failed
org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'lwM2MServiceImpl' defined in URL [jar:file:/usr/share/thingsboard/bin/thingsboard.jar!/BOOT-INF/classes!/org/thingsboard/server/service/lwm2m/LwM2MServiceImpl.class]: Unsatisfied dependency expressed through constructor parameter 0; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'lwM2MTransportServerConfig': Unsatisfied dependency expressed through field 'credentialsConfig'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'lwm2mServerCredentials': Invocation of init method failed; nested exception is java.lang.RuntimeException: LWM2M Server DTLS Credentials: Invalid SSL credentials configuration. None of the PEM or KEYSTORE configurations can be used!

SOLUTION 
fichier thingsboard.yml passer la ligne ~721 a enabled =false
```
lwm2m:
    # Enable/disable lvm2m transport protocol.
    enabled: "${LWM2M_ENABLED:false}"
```

### 4.4.8. Grafana container
---
https://hub.docker.com/r/grafana/grafana
https://grafana.com/docs/grafana/latest/administration/configure-docker/

le lien ci dessus contient les chemins vers les data et la config de grafana.

### 4.4.9. Chirpstack container
---
 https://hub.docker.com/r/chirpstack/chirpstack-application-server
 https://hub.docker.com/r/chirpstack/chirpstack-network-server
 https://hub.docker.com/r/chirpstack/chirpstack-gateway-bridge

 si besoin de géolocalisation: https://hub.docker.com/r/chirpstack/chirpstack-geolocation-server

chirpstack docker-compose INSTRUCTIONS: https://github.com/brocaar/chirpstack-docker


Ce container contient une base postgres et un mqtt mosquitto que l'on peut enlever dans le docker-compose.yml a condition que le cablage réseau des container soit adapté.

PROBLEME AVEC LE FICHIER COMPOSE QUE J AI CREE... POUR LES VOLUMES MOSQUITTO ET LES VOLUME CHIRPSTACK...par exemple mosquitto.conf qui est pris pour un dossier

### 4.4.10. XTRMUS XTR container
---
pour faire tourner le site web d xtremus il faut:
-apache
-php
-sql

source: https://gist.github.com/jcavat/2ed51c6371b9b488d6a940ba1049189b

import de la base sql xtremus dans xtr
renommer table user en User

pb pour le ogin sql>5.7 jouer la commande suivante dans adminer
```
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
```
Création d'un répertoire partagé xtr: /shared/xtr
```

mkdir -p /shared/work
mount --bind /x/y/z/work /shared/work
```
That wouldn't survive across reboots though, so in case you want it to persist, append the following line to /etc/fstab :
```
/x/y/z/work /shared/work none bind
```

usefull instruction to setup people in xtr group

```
525  addgroup xtr
  526  sudo addgroup xtr
  527  man usermod
  528  sudo usermod -a -G xtr eleq
  529  sudo usermod -a -G xtr xtrmus
  530  sudo chgrp xtr /home/eleq/el/compose/apache/www/
  531  sudo chmod g+rwx /home/eleq/el/compose/apache/www/
  532  sudo usermod -a -G xtr jemesmain
  533  sudo chgrp -R xtr /home/eleq/el/compose/apache/www/
  534  ls /
  535  mkdir -p /shared/xtr
  536  sudo mkdir -p /shared/xtr
  537  ls /
  538  chmod 777 /shared/
  539  sudo chmod 777 /shared/
  540  chmod -w /shared/
  541  sudo chmod -w /shared/
  542  sudo chmod ugo -w /shared/
  543  sudo chmod g-r  /shared/
  544  sudo chmod o-r  /shared/
  545  ls -l /
  546  sudo chmod o-w  /shared/
  547  sudo chmod g-w  /shared/
  548  ls -l
  549  ls
  550  ls -l /
  551  sudo chmod g+r  /shared/
  552  sudo chmod o+r  /shared/
  553  ls -l /
  554  sudo mount --bind /home/eleq/el/compose/apache/www/ /shared/xtr/
  555  cd /shared/
  556  ls -l
  557  id
  558  sudo usermod -a -G xtr jemesmain
  559  id
  560  cat /etc/group
  561  id
  562  sudo nano /etc/fstab 
  563  sudo usermod -a -G xtr xtrmus
  564  cat /etc/group
  565  ls -l /shared
```
other instructions
```
cd /shared/xtr/
#https://www.linuxnix.com/sgid-set-sgid-linuxunix/
chmod g+s xtr  
find xtr -type d -exec chmod g+s {} \;
#https://www.linuxnix.com/linux-security-hardening-for-beginners-part-04-using-access-control-lists/
setfacl -m "default:group::rwx" xtr
find xtr -type d -exec setfacl -m "default:group::rwx" {} \;
# 6. align existing files : give rw to group xtr to all files in xtr/
find xtr/ -exec chmod g+rw {} \;
```
Jean-Yves Rialhon, 06:07
le test que j'ai fait : 
```
 xtrmus@echinix:/shared/xtr$ ls -l index.html
-rw-r--r--  1 eleq xtr   18925 Apr 17 16:21 index.html
xtrmus@echinix:/shared/xtr$ vi index.html 
xtrmus@echinix:/shared/xtr$ ls -l index.html 
-rw-rw-r-- 1 eleq xtr 18963 Apr 28 05:57 index.html
```
Jean-Yves Rialhon, 08:22
il faut corriger un peu le setfact pour que ce soit bon : 
```
setfacl -dRm u:eleq:rwX,g:xtr:rwX xtr
```
tu vas detester ...
```
 getfacl /shared/xtr/newfile.txt vs ls -l /shared/xtr/newfile.txt. les appearances sont trompeuses
```



# 5. KUBERNETES

finally this has not been implemented yet

## 5.1. Install Kubetcl
---
source: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
Update the apt package index and install packages needed to use the Kubernetes apt repository:
```
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl
```
Download the Google Cloud public signing key:
```
sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
```
Add the Kubernetes apt repository:
```
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
```
Update apt package index with the new repository and install kubectl:
```
sudo apt-get update
sudo apt-get install -y kubectl
```
test
```
kubectl version --client
```
## 5.2. install minikube
---
source:https://kubernetes.io/fr/docs/tasks/tools/install-minikube/

Installez Minikube par téléchargement direct
Si vous n'installez pas via un package, vous pouvez télécharger un binaire autonome et l'utiliser.
```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube
```
Voici un moyen simple d'ajouter l'exécutable Minikube à votre path :
```
sudo mkdir -p /usr/local/bin/
sudo install minikube /usr/local/bin/
```
Confirmer l'installation
Pour confirmer la réussite de l'installation d'un hyperviseur et d'un mini-cube, vous pouvez exécuter la commande suivante pour démarrer un cluster Kubernetes local :

Note: Pour définir le --driver avec minikube start, entrez le nom de l'hyperviseur que vous avez installé en minuscules où <driver_name> est mentionné ci-dessous. Une liste complète des valeurs --driver est disponible dans la documentation spécifiant le pilote VM.
minikube start --driver=<driver_name>
par exemple
```
minikube start --driver=docker
```
Une fois minikube start terminé, exécutez la commande ci-dessous pour vérifier l'état du cluster :
```
minikube status
```
Si votre cluster est en cours d'exécution, la sortie de minikube status devrait être similaire à :
```
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```
si ca marche pas executer les trois commandes suivantes:
```
minikube stop
minikube delete
minikube start

```
## 5.3. install Helm option
---
source www.helm.sh
helm est un package manager pour kubernetes

### 5.3.1. From Apt (Debian/Ubuntu)
---
Members of the Helm community have contributed a Helm package for Apt. This package is generally up to date.

'''
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt-get install apt-transport-https --yes
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
'''

### 5.3.2. from snap
---
```
sudo snap install helm --classic
```

## 5.4. install Kompose docker-compose vers kubenetes
---
source: https://kubernetes.io/fr/docs/tasks/configure-pod-container/translate-compose-kubernetes/

install on linux
```
curl -L https://github.com/kubernetes/kompose/releases/download/v1.16.0/kompose-linux-amd64 -o kompose
chmod +x kompose
sudo mv ./kompose /usr/local/bin/kompose
```

1. Allez dans le répertoire contenant votre fichier docker-compose.yml
2. Lancez la commande kompose up pour déployer directement sur Kubernetes, ou passez plutôt à l'étape suivante pour générer un fichier à utiliser avec kubectl.
3. Pour convertir le fichier docker-compose.yml en fichiers que vous pouvez utiliser avec kubectl, lancez kompose convert et ensuite kubectl apply -f <output file>.
```
$ kompose convert                           
INFO Kubernetes file "frontend-service.yaml" created         
INFO Kubernetes file "redis-master-service.yaml" created     
INFO Kubernetes file "redis-slave-service.yaml" created      
INFO Kubernetes file "frontend-deployment.yaml" created      
INFO Kubernetes file "redis-master-deployment.yaml" created  
INFO Kubernetes file "redis-slave-deployment.yaml" created   
$ kubectl apply -f frontend-service.yaml,redis-master-service.yaml,redis-slave-service.yaml,frontend-deployment.yaml,redis-master-deployment.yaml,redis-slave-deployment.yaml
service/frontend created
service/redis-master created
service/redis-slave created
deployment.apps/frontend created
deployment.apps/redis-master created
deployment.apps/redis-slave created
```
Vos déploiements fonctionnent sur Kubernetes.

Accédez à votre application.

Si vous utilisez déjà minikube pour votre processus de développement :
```
$ minikube service nom du service présent dans le docker-compose
```

## 5.5. Kubernetes course
---
absolute beginer: https://www.youtube.com/watch?v=s_o8dwzRlu4
exemple of a project 40 min.

basic commands: https://www.youtube.com/watch?v=azuwXALfyRg

yaml explained: https://www.youtube.com/watch?v=qmDzcu5uY1I

volume explained: https://www.youtube.com/watch?v=0swOh5C3OVM

config file: https://www.youtube.com/watch?v=FAnQTgr04mU

## 5.6. kubernetes cert-manager
---

source nginx/letsencrypt: https://medium.com/avmconsulting-blog/encrypting-the-certificate-for-kubernetes-lets-encrypt-805d2bf88b2a
and: https://github.com/jetstack/cert-manager/
and https://cert-manager.io/docs/installation/helm/

version has changed from the page
```
kubectl apply --validate=false \
> -f https://github.com/jetstack/cert-manager/releases/download/v1.6.1/cert-manager.yaml
```
download file from here: https://github.com/jetstack/cert-manager/releases/
kubectl apply -f cert-manager.yaml
kubectl create ns cert-manager
Error from server (AlreadyExists): namespaces "cert-manager" already exists
helm search repo
NAME                                   	CHART VERSION	APP VERSION	DESCRIPTION                                    
jetstack/cert-manager                  	v1.6.1       	v1.6.1     	A Helm chart for cert-manager                  
jetstack/cert-manager-approver-policy  	v0.2.0       	v0.2.0     	A Helm chart for cert-manager-approver-policy  
jetstack/cert-manager-csi-driver       	v0.2.1       	v0.2.0     	A Helm chart for cert-manager-csi-driver       
jetstack/cert-manager-csi-driver-spiffe	v0.1.0       	v0.1.0     	A Helm chart for cert-manager-csi-driver-spiffe
jetstack/cert-manager-istio-csr        	v0.3.1       	v0.3.0     	A Helm chart for istio-csr                     
jetstack/cert-manager-trust            	v0.1.1       	v0.1.0     	A Helm chart for cert-manager-trust

RELIABLE INSTRUCTION HERE
https://cert-manager.io/docs/installation/helm/

kubectl apply -f cert-manager.crds.yaml 
helm install   cert-manager jetstack/cert-manager   --namespace cert-manager   --create-namespace   --version v1.6.1   #--set installCRDs=true


## 5.7. kubernetes chirpstack
---

source chirpstack deploy: https://github.com/Mekrache/chirpstack-kubernetes

peut etre qu'il faut élargir les ports possible: minikube start --driver=docker --mount-string="$HOME/el/mnt:/mnt" --mount --extra-config=apiserver.service-node-port-range=1-65535   

Chirpstack a un problème a se connecter au broker mqtt
level=error msg="integration/mqtt: connecting to broker error, will retry in 2s: network Error : dial tcp 10.104.213.62:1883: connect: connection refused"

dans tous les cas le mosquitto en version 2 provoque le démarrage suivant avec un error adress not available
eleq@vbdeb10:~/el$ utils/kube-logs.sh mosquitto                                                                                                
1640006624: mosquitto version 2.0.14 starting                                                                                                  
1640006624: Config loaded from /mosquitto/config/mosquitto.conf.                                                                               
1640006624: Starting in local only mode. Connections will only be possible from clients running on this machine.                               
1640006624: Create a configuration file which defines a listener to allow remote access.                                                       
1640006624: For more details see https://mosquitto.org/documentation/authentication-methods/                                                   
1640006624: Opening ipv4 listen socket on port 1883.                                                                                           
1640006624: Opening ipv6 listen socket on port 1883.                                                                                           
1640006624: Error: Address not available                                                                                                       
1640006624: mosquitto version 2.0.14 running

il faut pull une version 1.6
eleq@vbdeb10:~/el$ utils/kube-logs.sh mosquitto                                                                                                
1640007573: mosquitto version 1.6.15 starting                                                                                                  
1640007573: Config loaded from /mosquitto/config/mosquitto.conf.                                                                               
1640007573: Opening ipv4 listen socket on port 1883.                                                                                           
1640007573: Opening ipv6 listen socket on port 1883.                                                                                           
1640007573: mosquitto version 1.6.15 running                                                                                                   
1640007577: New connection from 172.17.0.1 on port 1883.                                                                                       
1640007577: New client connected from 172.17.0.1 as auto-1B76F76D-B3BF-4C13-0A1C-9E27EA9AD1F6 (p2, c1, k30).                                   
1640007577: New connection from 172.17.0.1 on port 1883.                                                                                       
1640007577: New client connected from 172.17.0.1 as auto-70E31A1F-81EF-15CE-EF19-0453112E7B4F (p2, c1, k30).

et chirpstack demarre sans pb
eleq@vbdeb10:~/el$ utils/kube-logs.sh chirpstack-app                                                                                           
time="2021-12-20T13:39:30.388446945Z" level=info msg="starting ChirpStack Application Server" docs="https://www.chirpstack.io/" version=       
time="2021-12-20T13:39:30.388475254Z" level=info msg="storage: setting up storage package"                                                     
time="2021-12-20T13:39:30.388481075Z" level=info msg="storage: setup metrics"                                                                  
time="2021-12-20T13:39:30.388488233Z" level=info msg="storage: setting up Redis client"                                                        
time="2021-12-20T13:39:30.388503604Z" level=info msg="storage: connecting to PostgreSQL database"                                              
time="2021-12-20T13:39:31.404274577Z" level=warning msg="storage: ping PostgreSQL database error, will retry in 2s" error="dial tcp 10.102.47.2
03:5432: connect: connection refused"                                                                                                          
time="2021-12-20T13:39:34.416603506Z" level=warning msg="storage: ping PostgreSQL database error, will retry in 2s" error="dial tcp 10.102.47.2
03:5432: connect: connection refused"                                                                                                          
time="2021-12-20T13:39:36.427421614Z" level=info msg="storage: applying PostgreSQL data migrations"                                            
time="2021-12-20T13:39:37.674133652Z" level=info msg="storage: PostgreSQL data migrations applied" from_version=0 to_version=60                
time="2021-12-20T13:39:37.683402895Z" level=info msg="integration: configuring global integrations"                                            
time="2021-12-20T13:39:37.683574087Z" level=info msg="integration/mqtt: TLS config is empty"                                                   
time="2021-12-20T13:39:37.683625668Z" level=info msg="integration/mqtt: connecting to mqtt broker" server="tcp://mosquitto:1883"               
time="2021-12-20T13:39:37.684300567Z" level=info msg="api/as: starting application-server api" bind="0.0.0.0:8001" ca_cert= tls_cert= tls_key= 
time="2021-12-20T13:39:37.684596088Z" level=info msg="api/external: starting api server" bind="0.0.0.0:8080" tls-cert= tls-key=                
time="2021-12-20T13:39:37.684691246Z" level=info msg="integration/mqtt: connected to mqtt broker"                                              
time="2021-12-20T13:39:37.684710374Z" level=info msg="integration/mqtt: subscribing to tx topic" qos=0 topic=application/+/device/+/command/dow
n                                                                                                                                              
time="2021-12-20T13:39:37.785049752Z" level=info msg="api/external: registering rest api handler and documentation endpoint" path=/api         
time="2021-12-20T13:39:37.785088907Z" level=info msg="api/js: starting join-server api" bind="0.0.0.0:8003" ca_cert= tls_cert= tls_key=

Le serveur est accessible ici en ssh
http://127.0.0.1:30001/#/network-servers

ensuite on a cette erreur dans la config -comme lors de l'installation sur le raspberry pi:
pour chirpstack: erreur / error context deadline exceeded (code: 2) 
réglage pour la partie via l'interface web network server 192.168.1.101:8000 doit correspondre a la partie public_host="192.168.1.101:8001" du fichier /etc/chirpstack-application-server/chirpstack-application-server.toml
ainsi le config map est ok mais il faut utiliser ceci pour le network serveur add
la solution est ici: https://github.com/brocaar/chirpstack-docker
```
Add Network Server
When adding the Network Server in the ChirpStack Application Server web-interface (see Network Servers), you must enter chirpstack-network-server:8000 as the Network Server hostname:IP.
```

## 5.8. UDP tunnelling dans miniKube
---
Pour passer les elements via SSH qui ne fait pas du tunnelling pour le port 1701/30002
http://zarb.org/~gc/html/udp-in-ssh-tunneling.html

config ssh:
```
#gateway bridge udp 1700/1701->30002
  #LocalForward 30002 192.168.49.2:30002 #ne marche pas car UDP
  #http://zarb.org/~gc/html/udp-in-ssh-tunneling.html
  LocalForward 6667 localhost:6667
```
du coté serveur 49.2 etant l'ip du minikube
```
mkfifo /tmp/fifo
nc -l -p 6667 < /tmp/fifo | nc -u 192.168.49.2 30002 > /tmp/fifo
   ``` 
du coté client
```
mkfifo /tmp/fifo
sudo nc -l -u -p 1700 < /tmp/fifo | nc localhost 6667 > /tmp/fifo
   ``` 
    
    
 gateway rakwireless -> 192.168.1.48 : 1700 




# 6. various linux command

lorsque un process  comme ssh ne souhaite plus se connecter
ps -eaf |grep ssh
netstat -apne
kill pid


# 7. Alternatives
## 7.1. The thing network
---
## 7.2. Grafana
---
source: https://simonhearne.com/2020/pi-influx-grafana/
video illustrative notamment les noeud node red à utiliser pour inserer des données dans influxdb
video: https://www.youtube.com/watch?v=JdV4x925au0


after installing influxdb problem to start executer ceci
```
sudo chmod +x /usr/lib/influxdb/scripts/influxd-systemd-start.sh

```
and then 
```
sudo systemctl unmask influxdb.service
sudo systemctl start influxdb
sudo systemctl enable influxdb.service
```

Lors du démarrage j'ai l'erreur suivante: influxd-systemd-start.sh[PID]: Failed to reach influxdb http endpoint at http://localhost:8086/health
Fix:
in ./usr/lib/influxdb/scripts/influxd-systemd-start.sh:

increase the sleep timer (in my case from 1 to 5):
...
while [ "$result" != "200" ]; do
  sleep 5
  result=$(curl -k -s -o /dev/null $url -w %{http_code})
...
Done!


Grafana oauth2 authentification.
https://grafana.com/docs/grafana/latest/auth/google/

# 8. Technical data
## 8.1. port list
---
voir l'illustration architecture

## 8.2. Graphique Path
---

## 8.3. LGM Centrale solaire du lycée du Grésivaudan
---


## 8.4. INPG acepi polygone pulse atex
adeunis pulse atex
ttn and nodered ttn uplink node: pulse_atex app device_id pulse_atex_polygone
nodered  flow inpg acepi polygon pulse atex
nodered ubidot out node:  account type ubidot / token = api credential sous dans le menu sous le nom du compte prendre le default token / device inpgpulseatex
ubidots inpgpulseatex device
chanela_index variable
