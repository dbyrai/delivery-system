# How-to: Mit Manus und GitHub nach dem Delivery-System entwickeln

**Stand:** 17.11.2026 · **Ziel:** Ein GitHub-Repository je Anwendungsprojekt;
Manus plant und implementiert darin nach den Delivery-Regeln.

## 1. Projekt und GitHub-Arbeitsmodus festlegen

Du benötigst einen Manus-Account und Zugriff auf das ausgewählte GitHub-Repository.
Der Account-Inhaber richtet die Verbindung in Manus ein. Das Addon richtet keine
separate API-Anbindung ein. Bestehende App-Daten und Konfiguration erhalten;
den Delivery-Template-README nicht über die Anwendungs-README kopieren.

Die offiziellen Manus-Seiten beschreiben zwei unterschiedliche GitHub-Wege:

| GitHub-Weg | Dokumentiertes Verhalten | Einsatz im Delivery-System |
| --- | --- | --- |
| GitHub-Connector | In Manus unter Connectors GitHub verbinden, Repository-Zugriff auswählen; Arbeit auf Branches und PRs möglich | Empfohlener Weg für ein bestehendes Repository mit Review-Prozess |
| GitHub-Sync eines Manus-Web-App-Projekts | Export in ein neues privates Repository, automatische Übertragung nach `main` und Aktualisierung vor Änderungen | Nur mit bewusst akzeptiertem Sync-Verhalten für das betreffende Projekt |

Quellen: [Manus GitHub-Connector](https://www.manus.im/connectors/github) und
[Manus GitHub Integration](https://manus.im/docs/website-builder/github-integration).
Der dokumentierte Web-App-Export ist kein allgemeiner Import beliebiger bestehender
Repositories. Ein vorhandenes Projekt daher über die tatsächlich verfügbare
Connector-Funktion prüfen. Oberfläche und Fähigkeiten können sich ändern.

Vor Änderungen Repository-URL, Arbeitsbranch, Lese-/Schreibzugriff und aktive
Sync-Funktion feststellen. Bei vorgeschriebenem Branch/PR-Prozess nur fortfahren,
wenn dieser Weg tatsächlich unterstützt wird. Bei automatischem Main-Sync zuerst
dessen Commit-/Push-Verhalten ausdrücklich klären und freigeben; bei Konflikt mit
Projektregeln diesen Modus nicht für die Umsetzung verwenden. Ein Prompt wie
„nicht pushen“ hebt die automatische Synchronisierung nicht technisch auf.

## 2. Delivery-System im Repository bereitstellen

Bei vorhandenem Delivery-System dessen Dokumentationswurzel, Anweisungen und IDs
beibehalten. Sonst die benötigten generischen Dateien aus dem Delivery-System
gezielt übernehmen: `delivery-system.md`, `.github/copilot-instructions.md`,
relevante `.github/agents/` und die passenden Dokumentvorlagen unter `docs/`.
Vorhandene Dateien abgleichen statt überschreiben. `AGENTS.md` kann als Router
beibehalten werden; sein automatisches Laden durch Manus wird nicht vorausgesetzt.

Den [Integrationsprompt](integration-prompt.md) im Zielprojekt ausführen. Er
bereitet eine dauerhafte Projektanweisung und einen Integrationsnachweis vor,
beispielsweise `docs/project/integrations/manus.md`. Dort stehen die tatsächlichen
Pfade, gewählter Einstieg, Repository/Branch, Zugriffsmodus, Owner, laufende Regeln,
Freigaben, Testkommandos und offene Prüfungen. Rollen- und Workflowregeln werden
über ihre kanonischen Quellen referenziert und nicht nochmals kopiert.

Die wiederverwendbare [Projektanweisung](templates/manus-projektanweisung.md)
anpassen und im Manus-Projekt als Projektanweisung hinterlegen, soweit diese
Funktion verfügbar ist. Andernfalls den Inhalt am Beginn jedes neuen Manus-Auftrags
mitgeben. Den tatsächlichen Ablageort im Nachweis dokumentieren. Keine erfundene
Manus-Konfigurationsdatei oder automatische Regel-Erkennung voraussetzen.

Wenn ein anderes Werkzeug die Dateien vorbereitet, muss der freigegebene Stand
zuerst durch den zuständigen Git-Owner im Zielrepository verfügbar gemacht werden.
Eine lokale Änderung auf deinem Computer ist noch nicht in Manus angekommen.

## 3. Lesezugriff und Leitplanken in Manus prüfen

Nach Auswahl des richtigen Repositorys diesen Startprompt in Manus verwenden.
Beispielpfade an die tatsächliche Struktur anpassen:

```text
Verwende ausschließlich das ausgewählte Projekt <Repository-URL>.
Arbeitsmodus: <GitHub-Connector mit Branch/PR oder ausdrücklich erlaubter Sync>.
Lies die kanonischen Anweisungen unter .github/copilot-instructions.md und den
Manus-Integrationsnachweis unter <tatsächlicher Pfad>. Wähle darüber die passende
Rolle und lies nur den relevanten Projektkontext samt verlinkten Blockern.

Nenne vor Änderungen: Repository, Branch und Quellenstand, gelesene verbindliche
Dateien, gewählte Rolle, Bootstrap-Status sowie bereite und blockierte Aufgaben.
Belege das Lesen durch kurze konkrete Angaben aus den relevanten Dateien.
Wenn Zugriff oder maßgebliche Quellen fehlen, melde das und stoppe davon abhängige
Arbeit. Erfinde weder Projektentscheidungen noch bestandene Checks.
Beginne zunächst nur mit dieser Bestandsaufnahme.
```

Wenn Manus nur Chat-Inhalte statt Repository-Dateien gelesen hat, ist die
Integration noch nicht verifiziert. Fehlenden Zugriff zuerst beheben; keine
umfangreiche Umsetzung mit unvollständigen Regeln starten.

## 4. Stufe 1: Bestehendes Projekt übernehmen

1. **Bestand prüfen:** Code, bestehende Dokumente, IDs, Architektur, CI/CD,
   Testkommandos und vorhandene Änderungen erfassen. Fremde Arbeit erhalten.
2. **Adoptionsstatus feststellen:** Bei bereits abgeschlossenem Bootstrap nur
   relevante Lücken behandeln. Bei erstmaliger Adoption erst den Repository-Review
   aus Schritt 0 des Handbuchs und anschließend den Bootstrap in Reihenfolge
   durchführen. Vorhandenes Wissen übernehmen, keine fertigen Dokumente ersetzen.
3. **Arbeitsumfang wählen:** Eine freigegebene Spec und ihre bereiten Tasks oder
   einen explizit freigegebenen Anwendungsplan bestimmen. Bestehende IDs verwenden.
4. **Ausführen:** Die Umsetzungsschleife aus Abschnitt 6 beauftragen.

```text
Arbeite im bestehenden Projekt nach den gelesenen Delivery-Anweisungen.
Prüfe den Adoptions-/Bootstrap-Status und erhalte abgeschlossene Dokumentation.
Bearbeite anschließend nur <freigegebene Spec-/Task-IDs> in <erlaubte Pfade>.
Beachte Abhängigkeiten, verlinkte Fragen und <vereinbarte Prüfpunkte>.
Nutze <Arbeitsbranch>. Commit/Push/PR: <konkret freigegebener Umfang>.
Keine automatische Veröffentlichung. Melde blockierte Voraussetzungen konkret.
```

## 5. Stufe 2: Neues Projekt vollständig aufsetzen

1. **Repository bereitstellen:** Neues Projektrepository mit der generischen
   Delivery-Struktur verbinden. Falls Manus zunächst einen technischen Container
   benötigt, nur ausdrücklich vereinbartes Gerüst erstellen; keine Feature-Umsetzung
   vor dem Bootstrap-Gate. Einen Web-App-Export als eigenen Vorgang autorisieren.
2. **Bootstrap durchlaufen:** Den [Bootstrap im Handbuch](../../delivery-system.md#bootstrap-sequence)
   verwenden: Schritt 0 als nicht anwendbar markieren, Schritte 1–12 in Reihenfolge
   abarbeiten. Die Detailanforderungen des Handbuchs bleiben maßgeblich.
3. **Fragen klären:** Manus stellt konkrete Fragen zu fehlenden Anforderungen.
   Antworten oder ausdrückliche Deferrals in den zuständigen Dokumenten erfassen.
   Bei Blockern keine davon abhängigen Tasks oder Implementierung erzeugen.
4. **Plan freigeben:** Anforderungen, erste Spec, Task-Datei und Qualitätsregeln
   prüfen. Bootstrap-Abschluss bzw. explizite Deferrals dokumentieren. Eine
   Deferral ist keine pauschale Freigabe für weiterhin blockierte Operationen.
5. **Anwendung bauen:** Den vereinbarten Spec-/Task-Plan über Abschnitt 6 ausführen.

```text
Setze das neue Projekt <Projektziel> nach delivery-system.md auf.
Markiere Bootstrap-Schritt 0 als nicht anwendbar und bearbeite Schritte 1–12
in Reihenfolge. Schreibe Projektentscheidungen in die vorhandene Dokumentations-
struktur; halte das Handbuch generisch. Frage fehlende Angaben gezielt ab und
dokumentiere Antworten. Erfinde keine Anforderungen und beginne keine Feature-
Implementierung vor abgeschlossenem oder ausdrücklich zurückgestelltem Bootstrap.
Bereite die erste Spec und bereite Tasks mit Kriterien und Verifikation vor,
sobald deren Quellenblocker geklärt sind. Lege mir den Plan zur Freigabe vor.
```

## 6. Anwendung entlang der Specs und Tasks bauen

Den freigegebenen Plan über die [Umsetzungsvorlage](templates/umsetzung.md)
konkretisieren. Manus arbeitet im Repository, aktualisiert Fortschritt und
Verifikation im vorhandenen Task-Format und verwendet die relevanten Rollenprofile.
Diese Profile erzeugen keine automatisch getrennten Manus-Agenten.

```text
Setze den freigegebenen Plan <Spec-/Task-Referenzen> im vereinbarten Repository
und Branch um. Prüfe vor jedem Task dessen Quellen, offene Fragen, Abhängigkeiten
und Akzeptanzkriterien. Arbeite bereite Tasks innerhalb dieses Plans selbstständig
ab; frage nicht erneut nach bereits erteilter Autorisierung.

Führe die erforderlichen Tests, Build-/Lint-/Typprüfungen aus und dokumentiere
Kommandos und tatsächliche Ergebnisse je Task. Melde fehlende Umgebung separat.
Halte an <vereinbarte Review-/Abnahmepunkte>. Stoppe abhängige Arbeit bei Blockern,
Scope-Konflikten oder fehlender Freigabe. Liefere dort eine konkrete Rückfrage.

Halte Task-Status, Übersicht und Nachweise konsistent. Done erfordert die
projektspezifischen Akzeptanz- und DoD-Nachweise sowie vorgeschriebene Abnahme.
Liefere zu Prüfpunkten Task-IDs, Diff/Commit-Referenzen, Testbefunde und offene Punkte.
Commit/Push/PR: <konkrete Erlaubnis>. Merge und Release nur gemäß Projektfreigabe.
```

Der freigegebene Plan kann mehrere Specs bis zur vollständigen Anwendung umfassen.
Freigaben und Prüfpunkte bestimmen die Autonomie; es gibt keinen pauschalen Stopp
nach jedem Task. Gleichzeitige lokale und Manus-Änderungen vor Fortsetzung abgleichen.

## 7. Review, Fortsetzung und Veröffentlichung

Der zuständige Owner prüft Diff, Kriterienabdeckung und Testnachweise am richtigen
Quellstand. Fehlende oder umgebungsspezifische Checks nachholen. Bei Nacharbeit
Befund am vorhandenen Task festhalten, keinen zweiten widersprüchlichen Plan anlegen.

Bei einem neuen Manus-Chat erneut die Projektanweisung laden lassen. Repository,
Branch, offenen Stand und nächste bereite Tasks frisch lesen; der Chat-Verlauf
ersetzt keinen dauerhaft dokumentierten Projektstand.

Merge, Release und Deployment verwenden die bestehenden Freigaben und Pipelines.
Dieses Addon veröffentlicht keine Anwendung und installiert keine Automationen.
Mit dem [Testleitfaden](testleitfaden.md) das reale Verhalten beider Einstiege prüfen.
