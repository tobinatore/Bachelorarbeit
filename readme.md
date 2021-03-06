# Framework mitigating flooding attacks on Delay-tolerant networks
## Setup
[-> to the german part of the readme](#Installation)    
Setup is kept as simple as possible by using the provided scripts in the Top-Level directory. Although most of the installation of dependencies has been automated this way, you will have to do a few manual changes to ensure everything runs smoothly. Following are the steps needed to install everything:

 1. Clone this repository `git clone https://github.com/tobinatore/Bachelorarbeit.git`.
 2. Open a terminal in the newly created directory.
 3. Run `sudo ./install_dependencies.sh` to install needed packages and to download and install ION v4.0.0.
 4. When the script has finished, you'll have to manually add the home directory of your ION installation to the /etc/environment file. Instructions for doing this will be given at the end of the install_dependencies script.
 5. Run `sudo ./install_pyion.sh` to download and build the pyion package needed for the automatic tests.
 6. After step 5 all needed dependencies should have been installed. Now all that's left to do is to configure the ION environment. You'll have to repeat the following steps both for the Szenario_1 and the Szenario_2 folders.
 7. Execute `cd Szenario_1` to change into the folder containing the first scenario.
 8. Execute `touch ion_nodes` to create an empty file which ION will use to manage the nodes.
 9. For each of the folders 1 to 9 (or 1 to 29 for the second scenario) repeat the following steps:
 10. Change into the folder and open the "nX.ionconfig" file .
 11. Edit the line starting with "pathName" to reflect the path to that folder. So instead of `/home/tobias/Desktop/Bachelorarbeit/Szenario_1/1` it should have the actual fully qualified pathname, for example `/home/User/Downloads/Bachelorarbeit/Szenario_1/1`.
 12. Repeat the previous step for the config_X.ini file, changing the line starting with "node_dir".
 13. Repeat steps 7 - 12 for the folder containing the second scenario.
 14. Run `sudo gedit /etc/environment` to add another environment variable.
 15. Add `ION_NODE_LIST_DIR="/Path/to/Szenario_1"`or `ION_NODE_LIST_DIR="/Path/to/Szenario_2"`depending on which scenario you want to run. **This variable has to be changed every time when switching scenarios!**
 16. Restart your machine or run `source /etc/environment` to load the changes.

There may occur an error on the first run of the framework stating that the psutil module is missing. In this case run `sudo pip3 install psutil` and it should disappear.

## Running a scenario
Each folder containing a scenario also contains the scripts needed to run the scenario:

| name | function |
|--|--|
| nns<span>.</span>sh | Sets up the network namespaces for the scenario. |
| run_alt<span>.</span>sh | Runs ION using a configuration that works without running the framework. |
| run_ion<span>.</span>sh | Runs ION using a configuration that necessitates running the framework. |
| run_framework<span>.</span>sh | Runs the framework. |
| stop<span>.</span>sh | Stops ION and kills all processes associated with it. |
  
When switching scenarios, it is important to change the ION_NODE_LIST_DIR environment variable as described above. Also all network namespaces have to be deleted using `sudo ip -all netns delete`.
    
## Running tests
The "Tests" directory found in each scenario folder contains scripts for running the automated tests as described in the bachelors thesis.  These tests can be run via the terminal.

## Configuring the framework
Every node's directory contains a file called "config_X.ini" where X is the node number. These files contain the node's configuration options such as the node's neighbours, trust recovery rate and others as explained in the thesis. If you want to change the number of worker threads which are available for the nodes, you have to edit line 174 of the framework<span>.</span>py file in the Bachelorarbeit/framework directory. This file is copied to the directories of all nodes when running the framework.

---

---

## Installation
Die Installation ist  durch die Verwendung von Setup-Skripts so einfach wie m??glich gehalten. Trotzdem gibt es einige Schritte, die manuell ausgef??hrt werden m??ssen. Im Folgenden sind alle Schritte zur erfolgreichen Installation des Frameworks aufgef??hrt:

 1. Klonen Sie dieses Repository mittels `git clone https://github.com/tobinatore/Bachelorarbeit.git`.
 2. ??ffnen Sie ein Terminal in dem neu angelegten Verzeichnis.
 3. F??hren Sie `sudo ./install_dependencies.sh` aus, um die ben??tigten Packages, sowie ION Version 4.0.0 herunterzuladen und zu installieren.
 4. Wenn das Skript fertig ausgef??hrt wurde, muss das ION-Installationsverzeichnis manuell zu der /etc/environment Datei hinzugef??gt werden. Eine Anleitung dazu wird von dem install_dependencies Skript ausgegeben.
 5. F??hren Sie `sudo ./install_pyion.sh` aus, um das pyion Package herunterzuladen und zu bauen. Dieses wird f??r die automatisierten Tests ben??tigt.
 6. Nach Schritt 5  sind alle ben??tigten Abh??ngigkeiten installiert. Nun muss noch die ION Umgebung konfiguriert werden. Die folgenden Schritte gelten dabei sowohl f??r den Ordner Szenario_1 als auch f??r den Ordner Szenario_2.
 7. F??hren Sie `cd Szenario_1` aus, um in den Ordner des ersten Szenarios zu wechseln.
 8. F??hren Sie `touch ion_nodes`  aus, um eine leere Datei anzulegen, welche ION f??r das Knotenmanagement nutzt.
 9. F??r jeden der Ordner 1 bis 9 (oder 1 bis 29 im Falles des 2. Szenarios) f??hren Sie die folgenden Schritte aus:
 10. Wechseln Sie in den Ordern und ??ffnen Sie die "nX.ionconfig" Datei .
 11. Bearbeiten Sie die Zeile, welche mit "pathName" beginnt, sodass sie den Pfad zu dem Ordner enth??lt. Beispielsweise k??nnte statt `/home/tobias/Desktop/Bachelorarbeit/Szenario_1/1` nun der Pfad `/home/User/Downloads/Bachelorarbeit/Szenario_1/1`dort stehen.
 12. Wiederholen Sie den vorigen Schritt f??r die Datei "config_X.ini" und ??ndern Sie dort die Zeile die mit "node_dir" beginnt.
 13. Wiederholen Sie die Schritte 7 - 12 f??r den Ordner des zweiten Szenarios.
 14. F??hren Sie `sudo gedit /etc/environment` aus, um eine weitere Umgebungsvariable hinzuf??gen zu k??nnen.
 15. F??gen Sie`ION_NODE_LIST_DIR="/Path/to/Szenario_1"`oder `ION_NODE_LIST_DIR="/Path/to/Szenario_2"`in die Datei ein, je nachdem welches Szenario Sie ausf??hren m??chten. **Diese Variable muss jedes Mal, wenn Sie das Szenario wechseln, ge??ndert werden!**
 16. Starten Sie Ihre Maschine neu, oder f??hren Sie `source /etc/environment` aus, um die ??nderungen zu laden.

Bei der ersten Ausf??hrung zeigt dass Framework m??glicherweise an, dass das Modul psutils fehlt. Dieser sollte nach Ausf??hrung von `sudo pip3 install psutil` verschwinden.


## Ausf??hren eines Szenarios
Jedes Szenarioverzeichnis enth??lt auch die Skripte, um das Szenario auszuf??hren.

| Name | Funktion |
|--|--|
| nns<span>.</span>sh | Richtet die ben??tigten Network Namespaces ein. |
| run_alt<span>.</span>sh | F??hrt ION Mit einer Konfiguration aus, die das Framework nicht ben??tigt. |
| run_ion<span>.</span>sh | F??hrt ION Mit einer Konfiguration aus, die das Framework unbedingt ben??tigt. |
| run_framework<span>.</span>sh | F??hrt das Framework aus. |
| stop<span>.</span>sh | Stoppt ION und beendet alle mit ihm assoziierten Prozesse. |
  
Wenn Sie ein anders Szenario ausf??hren m??chten, ist es wichtig, dass Sie die ION_NODE_LIST_DIR Umgebungsvariable wie oben beschrieben anpassen. Au??erdem m??ssen alle Network Namespaces mittels `sudo ip -all netns delete` gel??scht werden.
    
## Ausf??hren von Tests
In jedem Szenarioverzeichnis befindet sich ein "Tests"-Ordner. Dieser enth??lt Skripts zum Ausf??hren der in der Bachelorarbeit beschriebenen automatisierten Tests. Diese k??nnen ??ber die Konsole ausgef??hrt werden.

## Konfigurierung des Frameworks
Jedes Verzeichnis dessen Name lediglich eine Zahl ist, enth??lt eine Datei namens "config_X.ini", wobei X f??r die Nummer des in diesem Verzeichnis initialisierten Knotens ist. Diese Dateien enthalten die Konfiguration des jeweiligen Knotens. Mit ihnen lassen sich Einstellungen wie beispielsweise die Nachbariknoten und die Trust-Wiederherstellungsrate anpassen. Eine Auflistung aller Optionen findet sich in der Bachelorarbeit. Falls die Anzahl der Worker-Threads angepasst werden soll, so muss Zeile 174 der framework<span>.</span>py Datei im Verzeichnis Bachelorarbeit/framework angepasst werden. Diese Datei wird dann bei Start des Frameworks in alle Knotenverzeichnisse kopiert.
