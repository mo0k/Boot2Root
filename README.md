# Boot2Root

#Creation d'un fichier d'entrer pour l'interpreteur de commande de qemu afin de simuler une saisie clavier 
#Ce fichier est a rediger dans l'entree standard de l'interpeteur de commande de qemu
#Pour acceder cet interpreteur depuis le system hote il faut lancer qemu avec l'option monitor telnet

option au lancement de la vm via qemu:
-monitor telnet:127.0.0.1:25 server,nowait

pour se connecter a l'interpreteur utilser telnet ou netcat
nc 127.0.0.1

pour utiliser le fichier generer:
nc 127.0.0.1 < fichier
