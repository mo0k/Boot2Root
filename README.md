# Boot2Root
<hr/>
<h1>Outils</h1>
<h2>Script pour générer un fichier d'entrée pour l'interpréteur de commande de qemu afin de simuler une saisie clavier</h2>
<p>Ce fichier doit être rediger dans l'entrée standard de l'interpréteur de commande de qemu<br/>
Pour acceder cet interpréteur depuis le systeme host il faut lancer qemu avec l'option monitor telnet</p>
<ul>
<li>Option au lancement de la vm via qemu:<br/>
-monitor telnet:127.0.0.1:25 server,nowait</li>

<li>Commande pour se connecter a l'interpreteur, utilser telnet ou netcat<br/>
nc 127.0.0.1 25</li>

<li>Commande pour utiliser le fichier generer:<br/>
nc 127.0.0.1 25 < fichier</li>
<ul>
