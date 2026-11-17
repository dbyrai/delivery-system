# Integrationsprompt für Manus und GitHub

Im Zielprojekt mit Repository-Zugriff verwenden. Dieser Prompt bereitet die
Einrichtung vor; die Anwendungsumsetzung wird anschließend konkret beauftragt.

```text
Richte das optionale Manus-Addon für die direkte Arbeit im GitHub-Projekt ein.

Lies die anwendbaren Projektanweisungen, addons/manus/README.md, howto.md,
instructions.md und templates/manus-projektanweisung.md innerhalb dieses Addons.
Prüfe Arbeitskopie, Dokumentationswurzel, vorhandene Integrationen und Rollen.
Erhalte vorhandenen Code, Dokumentation, IDs und lokale Anpassungen.

Wähle anhand des Bestands Stufe 1 (bestehendes Projekt) oder Stufe 2 (neues Projekt).
Wenn der Zustand unklar ist, kläre ihn vor abhängiger Arbeit. Stelle fest, ob das
Delivery-System bereits adoptiert ist; keinen abgeschlossenen Bootstrap wiederholen.
Bei erstmaliger Adoption erst Repository-Review, dann Bootstrap nach Handbuch.
Bei neuem Projekt Schritt 0 als nicht anwendbar behandeln und Schritte 1–12 nutzen.
Führe in diesem Einrichtungsschritt noch keine Anwendungsimplementierung aus.

Prüfe GitHub-Repository, Branch, tatsächlichen Zugriff und Arbeitsmodus: Connector
mit Branch/PR oder Web-App-Sync. Erfasse automatisches Schreibverhalten. Ein
Prompt deaktiviert keinen Main-Sync. Fehlende Freigabe oder Konflikt mit den
Projektregeln blockiert davon abhängige Änderungen. Keine Verbindung eigenmächtig
herstellen, kein Repository exportieren und keinen Sync aktivieren.

Erstelle/ergänze den dauerhaften Manus-Integrationsnachweis im bestehenden
Dokumentationsverzeichnis: Owner, Einstieg, Quellenversion, tatsächliche Pfade,
Arbeitsmodus, Freigaben, Bootstrap-Status, Plan, Prüfpunkte, Checks und Entfernung.
Übertrage benötigte laufende Regeln dorthin; offene Angaben ausdrücklich benennen.
Bereite eine angepasste Manus-Projektanweisung aus der Vorlage vor. Dokumentiere,
wie sie im Manus-Projekt oder am Anfang jedes Auftrags verfügbar gemacht wird.
Kein automatisches Lesen von AGENTS.md oder erfundenen Manus-Konfigurationspfaden
voraussetzen. Aktive Regeln dürfen keine addons/-Dateien benötigen.

Ergänze einen kurzen bedingten Verweis aus den kanonischen gemeinsamen Anweisungen
auf den tatsächlichen Nachweis. Keine Workflow-/Rollenduplikate erzeugen. Prüfe
lokale Links, wiederholbares Setup ohne Duplikate und Quellenverfügbarkeit. Lasse
in Manus vor Codeänderungen Repository, Branch, gelesene Regeln, Rolle und offene
Blocker benennen. Unverfügbare Live-Prüfungen offenlassen.

Keine externe Manus-API, API-Keys, Dienste, Automationen oder Ticket-Synchronisierung
einrichten. Gib geänderte Dateien, vorhandene Freigaben und verbleibende Schritte
an. Ohne dafür erteilte Autorisierung kein Commit, Push, Merge oder Release.
```
