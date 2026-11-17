# Workflow: Manus baut im GitHub-Projekt nach dem Delivery-System

Beide Einstiegsstufen laufen direkt in Manus mit demselben Projektrepository.
Die Grafik zeigt die fachlichen Gates; Connector oder Sync sind Arbeitsmodi,
keine weiteren Integrationsstufen. Live-Verifikation steht noch aus.

![Zwei Einstiege und gemeinsame Umsetzungsschleife](workflow.svg)

## Bearbeitbare Diagrammquelle

```mermaid
flowchart TD
    A[Manus mit GitHub-Projekt verbinden und Arbeitsmodus prüfen] --> B[Projektregeln und Repository-Quellen lesen]
    B --> C{Einstiegsstufe}
    C -->|1: Bestehendes Projekt| D[Bestand und Adoptionsstatus prüfen; fertige Dokumentation erhalten]
    C -->|2: Neues Projekt| E[Schritt 0 nicht anwendbar; Bootstrap 1 bis 12 durchführen]
    D --> F{Delivery bereits adoptiert?}
    F -->|Ja| G[Freigegebene Specs und Tasks auswählen]
    F -->|Nein| H[Repository-Review Schritt 0; Bootstrap 1 bis 12]
    H --> I[Fragen und Entscheidungen in Projektquellen dokumentieren]
    E --> I
    I --> J{Bootstrap und Quellenblocker geklärt oder ausdrücklich zurückgestellt?}
    J -->|Nein| I
    J -->|Ja| G
    G --> K{Plan freigegeben und nächster Task bereit?}
    K -->|Blockiert| L[Konkrete Rückfrage; abhängige Arbeit stoppen]
    L --> G
    K -->|Ja| M[Manus implementiert Task im erlaubten Arbeitsbereich]
    M --> N[Tests ausführen; Status und Evidenz dokumentieren]
    N --> O{Vorgeschriebener Prüfpunkt erreicht?}
    O -->|Nein, weiterer bereiter Task| K
    O -->|Ja oder Plan bearbeitet| P[Diff, Kriterien und Testbefunde prüfen]
    P -->|Nacharbeit| M
    P -->|Angenommen, weitere Tasks| K
    P -->|Plan abgenommen| Q[Merge und Release gemäß bestehender Freigabe und Pipeline]
```

## Übergaben und Fortsetzung

| Punkt | Verantwortung | Nachweis |
| --- | --- | --- |
| Einrichtung | Projekt-Owner | Repository, Modus, Branch, Zugriff, tatsächlich gelesene Regeln |
| Projektklärung | Fachlicher Owner; Manus bereitet vor | Bootstrap-Status, Antworten/Deferrals, freigegebene Quellen |
| Ausführung | Manus mit zuständigem Rollenprofil | Task-IDs, erlaubter Umfang, Diff und ausgeführte Checks |
| Abnahme | Nach Projektregeln zuständiger Prüfer/Owner | Kriterienabdeckung, DoD und vorgeschriebene Abnahme |
| Veröffentlichung | Bestehender Release-Owner | Freigegebener Commit und vorhandener Deployprozess |

Im freigegebenen Plan darf Manus ohne erneute Einzelbeauftragung weiterarbeiten.
Blocker, Abhängigkeiten und vereinbarte Abnahmen begrenzen die Fortsetzung. Eine
Deferral hebt nicht automatisch weitere Voraussetzungen auf. Im neuen Chat den
aktuellen Repository- und Aufgabenstand erneut lesen lassen.

Der dokumentierte Web-App-Sync kann Code bereits vor einer fachlichen Abnahme
übertragen. Deshalb dessen Verhalten vor Umsetzung klären; ein Push erfüllt
keine Abnahmekriterien. Details und Startprompts stehen im [How-to](howto.md).
