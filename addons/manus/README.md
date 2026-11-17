# Manus-Addon für das Delivery-System

**Stand:** 17.11.2026 · **Status:** Preview; Live-Prüfung in Manus offen.

Manus arbeitet direkt mit dem GitHub-Projektrepository und verwendet dessen
Delivery-System als Arbeitsrahmen: Anforderungen klären, Specs und Tasks beachten,
die Anwendung bauen, Tests ausführen und überprüfbare Ergebnisse dokumentieren.
Das Addon liefert Einrichtung, Projektanweisung und Arbeitsablauf. Es installiert
keinen Dienst und benötigt keine externe Manus-API oder API-Zugangsdaten.

## Zwei Einstiegsstufen

| Stufe | Ausgangslage | Vorgehen |
| --- | --- | --- |
| **1 – Bestehendes Projekt übernehmen** | Code und eventuell schon Delivery-Dokumente vorhanden | Bestand prüfen, fehlende Struktur ergänzen, freigegebene Specs/Tasks ausführen |
| **2 – Neues Projekt aufsetzen** | Projektidee und leeres oder frisch angelegtes Repository | Bootstrap durchführen, Anforderungen und erste Spec/Tasks klären, anschließend implementieren |

Beide Stufen laufen direkt in Manus. Sie unterscheiden den Projektstart, nicht
die technische Anbindung. Ein bereits adoptiertes Projekt durchläuft keinen
neuen Bootstrap. Bei erstmaliger Adoption gelten die vorhandenen Bootstrap-Gates.

## Start und enthaltene Dateien

1. Das [Manus-How-to](howto.md) öffnen und GitHub-Zugriff sowie Arbeitsmodus prüfen.
2. Mit dem [Integrationsprompt](integration-prompt.md) das Zielprojekt vorbereiten.
3. Die angepasste [Projektanweisung](templates/manus-projektanweisung.md) in Manus
   verwenden und das tatsächliche Lesen der Repository-Quellen prüfen.
4. Die passende Einstiegsstufe aus dem How-to ausführen und den freigegebenen
   Arbeitsplan mit der [Umsetzungsvorlage](templates/umsetzung.md) konkretisieren.
5. Mit dem [Testleitfaden](testleitfaden.md) beide Einstiegswege prüfen.

Weitere Hilfen: [Betriebsregeln](instructions.md),
[optionale Recherche-/Entwurfsvorlage](templates/auftrag.md) und
[Deaktivierungsprompt](deactivation-prompt.md).

## Besprochener Workflow

![Manus baut entlang der Delivery-Struktur](workflow.svg)

Der [Workflow mit Mermaid-Quelle](workflow.md) zeigt beide Einstiege, die
Blockerbehandlung und die Umsetzungsschleife bis zur Abnahme.

## Leitplanken und Grenzen

Die kanonischen Projektanweisungen und bestehenden Delivery-Dokumente bleiben
maßgeblich. Manus kann innerhalb eines freigegebenen Plans mehrere bereite Tasks
selbstständig abarbeiten. Eine erneute Einzelbestätigung ist nur erforderlich,
wenn Projektregeln, fehlende Autorisierung oder ein vereinbarter Prüfpunkt dies
verlangen. Offene Blocker verhindern die davon abhängige Arbeit.

Die GitHub-Anbindung und der tatsächlich verwendete Branch müssen vor Änderungen
geprüft werden. Das How-to unterscheidet Connector mit Branch/PR und Web-App-Sync;
automatischer Sync lässt sich durch eine Textanweisung nicht technisch begrenzen.
Commit/Push, Merge und Veröffentlichung folgen den jeweiligen Projektfreigaben.
Ein GitHub-Push allein ist keine Abnahme und kein Release.

Die Rollenprofile sind Arbeitsanweisungen, keine automatisch gestarteten
Manus-Subagenten. Automatisches Laden von `AGENTS.md` oder anderen Dateien wird
nicht vorausgesetzt: Der Startprompt verlangt das Lesen der tatsächlichen Quellen.
Die Leitplanken und ihre Befolgung sind im Zielprojekt zu verifizieren.

Der dauerhafte Integrationsnachweis wird im bestehenden Dokumentationsverzeichnis
geführt. Aktive Anweisungen dürfen nach Einrichtung keine entfernbaren `addons/`-
Dateien benötigen. Dieses Template erhält keine fiktiven Projekteinstellungen.

## Verifikation und Entfernung

Links, Grafik und Vorlagen können lokal geprüft werden. Konto, tatsächlicher
Repository-Zugriff, Branch-Verhalten, Tests und Ergebnisqualität benötigen einen
Live-Test. Bis zu dessen Nachweis bleibt das Paket eine Preview.

Zur Deaktivierung zuerst offene Arbeiten und Ergebnisse sichern, dann nur die
addonbezogenen Anweisungen und autorisierten Zugriffe entfernen. Das Löschen
von `addons/manus/` stoppt weder Manus noch einen bestehenden GitHub-Sync.
