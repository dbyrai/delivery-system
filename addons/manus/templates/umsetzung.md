# Manus-Umsetzungsauftrag: <vorhandene Task-ID und Titel>

Die [allgemeine Auftragsvorlage](auftrag.md) um folgende Angaben ergänzen.
Platzhalter vor Übergabe ausfüllen; keine Credentials aufnehmen.

## Verbindliche Quellen und Bereitschaft

- Freigegebene Spec mit Pfad und Stand: <Referenz>
- Vorhandene Task-Datei und ausgewählte Task-IDs: <Referenzen>
- Source Requirement und Abnahmekriterien je Task: <Referenzen/Inhalt>
- Bootstrap-Status und Blocker-/Frage-Dateien: <geprüft; Entscheidungen/Deferrals>
- Abhängigkeiten und vereinbarte Prüfpunkte: <Reihenfolge und Voraussetzungen>
- Delivery-Owner / Responsible Agent: <bestehende Rolle und Rollenanweisungen>
- Projekt-, Architektur-, Sicherheits- und Sprachregeln: <relevante Inhalte>

## Ausführungsumgebung und erlaubte Änderungen

- Manus-Projekt / GitHub-Modus: <Projekt; Connector/PR oder erlaubter Sync>
- Arbeitsbereich: <tatsächlicher Repository-Branch; Sync-Verhalten geprüft>
- Repository-Identität und exakter Basis-Commit: <Referenz>
- Zusätzlich übergebene uncommitted Änderungen: <expliziter Umfang oder keine>
- Erlaubte Schreibbereiche: <Pfade/Module und zu erhaltende lokale Änderungen>
- Setup und verfügbare Laufzeit/Abhängigkeiten: <konkrete Angaben>
- Prüfkommandos und erwartete Ergebnisse: <projektspezifische Kommandos>
- Verifikation dieser Fähigkeiten in Manus: <Nachweis oder offen/blockiert>
- Erlaubnis für Commit/Push: <standardmäßig keine; ggf. exakt erteilte Freigabe>

Nur die ausgewählten Tasks ausführen. Keine externen Nachrichten, Produktivzugriffe,
Merges, Deployments oder zusätzlichen Dienste. Bei fehlendem Kontext, Blockern,
Scope-Änderung oder Konflikten Rückfrage stellen. Bestehende Regeln nicht umgehen,
um Tests erfolgreich erscheinen zu lassen.

## Erforderliche Rückgabe je Task

1. Task-ID, Ergebnis und Zuordnung zu jedem Abnahmekriterium.
2. Diff/Patch oder Commit-/PR-Referenz gegen den angegebenen Basisstand und Liste geänderter Dateien.
3. Tatsächlich ausgeführte Kommandos, Ergebnisse und relevante bereinigte Logs.
4. Nicht ausgeführte Checks mit Grund; offene Fragen und verbleibende Risiken.
5. Hinweise zur sicheren lokalen Übernahme und ggf. Rücknahme der Änderungen.

Status und tatsächliche Verifikation im bestehenden Task-Format pflegen. Done
erfordert die projektspezifischen Akzeptanz-/DoD-Nachweise und vorgeschriebene
Abnahme. Der zuständige Owner prüft Stand, Konflikte, Diff und nötige Zielumgebungs-
Checks an den vereinbarten Prüfpunkten. Vereinbarte Abnahmepunkte vor abhängiger Arbeit einhalten. Innerhalb eines bereits
freigegebenen Ausführungsplans darf Manus ohne erneute Einzelbeauftragung
fortfahren, soweit keine neue Abnahme oder Entscheidung erforderlich ist.
