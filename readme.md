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
 12. Repeat steps 7 - 11 for the folder containing the second scenario.
 13. Run `sudo gedit /etc/environment` to add another environment variable.
 14. Add `ION_NODE_LIST_DIR="/Path/to/Szenario_1"`or `ION_NODE_LIST_DIR="/Path/to/Szenario_2"`depending on which scenario you want to run. **This variable has to be changed every time when switching scenarios!**
 15. Restart your machine or run `source /etc/environment` to load the changes.

## Running a scenario
Each folder containing a scenario also contains the scripts needed to run the scenario:

| name | function |
|--|--|
| nns<span>.</span>sh | Sets up the network namespaces for the scenario. |
| run_alt<span>.</span>sh | Runs ION using a configuration that works without running the framework. |
| run_ion<span>.</span>sh | Runs ION using a configuration that necessitates running the framework. |
| run_framework<span>.</span>sh | Runs the framework. |
| stop<span>.</span>sh | Stops ION and kills all processes associated with it. |
  
When switching scenarios, it is important to change the ION_NODE_LIST_DIR environment variable as described above. Also all network namespaces have to be deleted using `sudo ipn -all netns delete`.
    
## Running tests
The "Tests" directory found in each scenario folder contains scripts for running the automated tests as described in the bachelors thesis.  These tests can be run via the terminal.

## Configuring the framework
Every node's directory contains a file called "config_X.ini" where X is the node number. These files contain the node's configuration options such as the node's neighbours, trust recovery rate and others as explained in the thesis. If you want to change the number of worker threads which are available for the nodes, you have to edit line 174 of the framework<span>.</span>py file in the Bachelorarbeit/framework directory. This file is copied to the directories of all nodes when running the framework.

---

---

## Installation
Die Installation ist  durch die Verwendung von Setup-Skripts so einfach wie möglich gehalten. Trotzdem gibt es einige Schritte, die manuell ausgeführt werden müssen. Im Folgenden sind alle Schritte zur erfolgreichen Installation des Frameworks aufgeführt:

 1. Klonen Sie dieses Repository mittels `git clone https://github.com/tobinatore/Bachelorarbeit.git`.
 2. Öffnen Sie ein Terminal in dem neu angelegten Verzeichnis.
 3. Führen Sie `sudo ./install_dependencies.sh` aus, um die benötigten Packages, sowie ION Version 4.0.0 herunterzuladen und zu installieren.
 4. Wenn das Skript fertig ausgeführt wurde, muss das ION-Installationsverzeichnis manuell zu der /etc/environment Datei hinzugefügt werden. Eine Anleitung dazu wird von dem install_dependencies Skript ausgegeben.
 5. Führen Sie `sudo ./install_pyion.sh` aus, um das pyion Package herunterzuladen und zu bauen. Dieses wird für die automatisierten Tests benötigt.
 6. Nach Schritt 5  sind alle benötigten Abhängigkeiten installiert. Nun muss noch ide ION Umgebung konfiguriert werden. Die folgenden Schritte gelten dabei sowohl für den Ordner Szenario_1 als auch für den Ordner Szenario_2.
 8. Führen Sie `cd Szenario_1` aus, um in den Ordner des ersten Szenarios zu wechseln.
 9. Führen Sie `touch ion_nodes`  aus, um eine leere Datei anzulegen, welche ION für das Knotenmanagement nutzt.
 10. Für jeden der Ordner 1 bis 9 (oder 1 bis 29 im Falles des 2. Szenarios) führen Sie die folgenden Schritte aus:
 11. Wechseln Sie in den Ordern und öffnen Sie die "nX.ionconfig" Datei .
 12. Bearbeiten Sie die Zeile, welche mit "pathName" beginnt, sodass sie den Pfad zu dem Ordner enthält. Beispielsweise könnte statt `/home/tobias/Desktop/Bachelorarbeit/Szenario_1/1` nun der Pfad `/home/User/Downloads/Bachelorarbeit/Szenario_1/1`dort stehen.
 13. Wiederholen Sie die Schritte 7 - 11 für den Ordner des zweiten Szenarios.
 14. Führen Sie `sudo gedit /etc/environment` aus, um eine weitere Umgebungsvariable hinzufügen zu können.
 15. Fügen Sie`ION_NODE_LIST_DIR="/Path/to/Szenario_1"`oder `ION_NODE_LIST_DIR="/Path/to/Szenario_2"`in die Datei ein, je nachdem welches Szenario Sie ausführen möchten. **Diese Variable muss jedes Mal, wenn Sie das Szenario wechseln, geändert werden!**
 16. Starten Sie Ihre Maschine neu, oder führen Sie `source /etc/environment` aus, um die Änderungen zu laden.

## Ausführen eines Szenarios
Jedes Szenarioverzeichnis enthält auch die Skripte, um das Szenario auszuführen.

| Name | Funktion |
|--|--|
| nns<span>.</span>sh | Richtet die benötigten Network Namespaces ein. |
| run_alt<span>.</span>sh | Führt ION Mit einer Konfiguration aus, die das Framework nicht benötigt. |
| run_ion<span>.</span>sh | Führt ION Mit einer Konfiguration aus, die das Framework unbedingt benötigt. |
| run_framework<span>.</span>sh | Führt das Framework aus. |
| stop<span>.</span>sh | Stoppt ION beendet alle mit ihm assoziierten Prozesse. |
  
Wenn Sie ein anders Szenario ausführen möchten, ist es wichtig, dass Sie die ION_NODE_LIST_DIR Umgebungsvariable wie oben beschrieben anpassen. Außerdem müssen alle Network Namespaces mittels `sudo ipn -all netns delete` gelöscht werden.
    
## Ausführen von Tests
In jedem Szenarioverzeichnis befindet sich ein "Tests"-Ordner. Dieser enthält Skripts zum Ausführen der in der Bachelorarbeit beschriebenen automatisierten Tests. Diese können über die Konsole ausgeführt werden.

## Konfigurierung des Frameworks
Jedes Verzeichnis dessen Name lediglich eine Zahl ist, enthält eine Datei namens "config_X.ini", wobei X für die Nummer des in diesem Verzeichnis initialisierten Knotens ist. Diese Dateien enthalten die Konfiguration des jeweiligen Knotens. Mit ihnen lassen sich Einstellungen wie beispielsweise die Nachbariknoten und die Trust-Wiederherstellungsrate anpassen. Eine Auflistung aller Optionen findet sich in der Bachelorarbeit. Falls die Anzahl der Worker-Threads angepasst werden soll, so muss Zeile 174 der framework<span>.</span>py Datei im Verzeichnis Bachelorarbeit/framework angepasst werden. Diese Datei wird dann bei Start des Frameworks in alle Knotenverzeichnisse kopiert.
