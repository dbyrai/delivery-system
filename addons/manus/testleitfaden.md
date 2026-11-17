# Manus-Addon im GitHub-Projekt testen

**Stand:** 17.11.2026 · **Status:** Preview; echte Manus-Prüfung offen.

## Vorbereitung

Der Tester nutzt seinen eigenen Manus-Account und ein GitHub-Testrepository mit
dem Delivery-System. Keine Account-Zugänge teilen. Zugriff, tatsächlichen Branch,
Connector-/Sync-Modus und dessen Schreibverhalten vor Änderungen prüfen. Bei
automatischem Sync einen ausdrücklich dafür freigegebenen Testbereich verwenden.
Keine Produktionsdaten einsetzen. Es werden keine Manus-API-Zugangsdaten benötigt.

Das [How-to](howto.md) und den [Integrationsprompt](integration-prompt.md) verwenden.
Eine lokale Addon-Kopie ist noch kein Live-Nachweis. Vorbereitete Dateien müssen
über den freigegebenen Git-Weg im tatsächlich ausgewählten Repository verfügbar sein.

## Gemeinsame Prüffälle

| Fall | Erwartetes Verhalten |
| --- | --- |
| Quellen laden | Manus nennt richtige Repository-/Branch-Identität und konkrete Inhalte aus Regeln und Task-Dateien |
| Fehlender Zugriff | Abhängige Arbeit stoppt; kein erfundener Kontext |
| Freigegebener Plan mit zwei abhängigen Tasks | Manus arbeitet in korrekter Reihenfolge ohne unnötige erneute Einzelbestätigung |
| Blockierende Frage in einem Test-Task | Abhängige Umsetzung stoppt; Antwort/Deferral wird dokumentiert |
| Testausführung | Reale Kommandos und Resultate sind je Task nachvollziehbar; Prüflücken ausdrücklich benannt |
| Review und Nacharbeit | Befund wird am bestehenden Task behoben; Done nur mit erforderlicher Evidenz und Abnahme |
| Neuer Manus-Chat | Aktuelle Regeln, Quellenstand und nächste Tasks werden erneut gelesen |
| Parallele Änderung | Unterschied zum aktuellen GitHub-Stand wird erkannt und vor Überschreiben geklärt |
| Deaktivierung | Offene Arbeiten bleiben erhalten; nur zugehöriges Routing/Zugriff wird im erlaubten Umfang beendet |

Für einen kleinen Umsetzungspilot eine freigegebene Spec mit zwei Tasks wählen,
z. B. eine lokale Funktion plus darauf aufbauende UI. Kriterien und Testkommandos
vorher im Testprojekt festlegen; vorhandene Templates und IDs verwenden.

## Stufe 1: bestehendes Projekt

Ein Testrepository mit vorhandenem Code und Dokumenten nutzen. Prüfen, dass Manus
keine Dateien blind durch Templates ersetzt und bestehende Task-IDs erhält.
Bei bereits adoptiertem Delivery-System darf kein kompletter Bootstrap neu starten.
Bei erstmaliger Adoption muss Manus dagegen erst Repository-Review und Bootstrap
nach Handbuch berücksichtigen. Anschließend den freigegebenen Pilot ausführen.

## Stufe 2: neues Projekt

Ein frisches Repository mit generischer Delivery-Struktur verwenden. Schritt 0
muss als nicht anwendbar gelten. Prüfen, ob Manus Bootstrap-Schritte 1–12 in
Reihenfolge bearbeitet, konkrete Fragen stellt und Entscheidungen dokumentiert.
Mindestens eine offene Frage absichtlich noch nicht beantworten: keine davon
abhängigen Tasks/Features erzeugen lassen. Danach Antwort oder ausdrückliche
Deferral festhalten, erste Spec und Task-Plan prüfen und konkret freigeben.
Vor dem Umsetzungspilot die Bootstrap-Abschlussprüfung aus dem How-to mit
Schrittstatus und Ergebnisreferenzen verlangen. Einrichten des Addons oder ein
pauschaler Abschluss im Chat allein darf keine Implementierung auslösen.
Erst anschließend den Umsetzungspilot ausführen und seine Nachweise prüfen.

## Befund und Weitergabe

Je Fall Datum, Manus-Oberfläche, Paket-/Repository-Stand, Arbeitsmodus, Branch,
Testschritte, Erwartung und tatsächliches Ergebnis festhalten. Status:
**bestanden**, **fehlgeschlagen** oder **ungeprüft**. Diff-/Commit-/PR-Referenzen,
bereinigte Logs und Testresultate beifügen. Zugangsdaten und private Projektinhalte
nicht in öffentliches Feedback übernehmen. Laufzeit und beobachtete Kosten notieren.

Beide Stufen werden direkt in Manus getestet. Der Account-Inhaber kann sie ohne
einen von uns betriebenen API-Adapter prüfen. Bis tatsächliche Befunde vorliegen,
keinen Live-Test als bestanden oder das Addon als produktiv verifiziert ausweisen.
