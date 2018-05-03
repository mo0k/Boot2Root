# Boot2Root
<hr/>
<h1>#Script pour generer d'un fichier d'entrer pour l'interpreteur de commande de qemu afin de simuler une saisie clavier<h1/>
<p>#Ce fichier est a rediger dans l'entree standard de l'interpeteur de commande de qemu<p/>
<p>#Pour acceder cet interpreteur depuis le system hote il faut lancer qemu avec l'option monitor telnet<p/>
<br/>
option au lancement de la vm via qemu:<br/>
-monitor telnet:127.0.0.1:25 server,nowait

pour se connecter a l'interpreteur utilser telnet ou netcat<br/>
nc 127.0.0.1

pour utiliser le fichier generer:<br/>
nc 127.0.0.1 < fichier
