# How-to: Mit Manus und GitHub nach dem Delivery-System entwickeln

**Stand:** 17.11.2026 · **Ziel:** Ein GitHub-Repository je Anwendungsprojekt;
Manus plant und implementiert darin nach den Delivery-Regeln.

## Verbindliche Reihenfolge bis zur ersten Implementierung

**Repository vorbereiten → Manus einrichten und Quellenzugriff prüfen → Projekt
bootstrapen → Spec und Tasks freigeben → Anwendung implementieren → prüfen und
veröffentlichen.** Das Kopieren der Delivery-Dateien und die Einrichtung des
Manus-Addons schließen den Projekt-Bootstrap noch nicht ab.

| Reihenfolge | Ergebnis vor dem nächsten Schritt | Anleitung |
| --- | --- | --- |
| A. Repository und Delivery-Dateien bereitstellen | Richtiger Projektstand ist in GitHub verfügbar; vorhandene Dateien bleiben erhalten | Abschnitte 1–2 |
| B. Manus einrichten und Lesen prüfen | Projektanweisung, tatsächlicher Branch und relevante Regeln sind nachweislich geladen | Abschnitt 3 |
| C. Projekt-Bootstrap bearbeiten | Schritt 0 passend behandelt; Schritte 1–12 abgeschlossen oder ausdrücklich zurückgestellt; Entscheidungen dokumentiert | Abschnitte 4–5 |
| D. Umsetzungsbereitschaft prüfen | Bootstrap-Gate erfüllt, konkrete Spec/Tasks freigegeben, keine offenen abhängigen Blocker | Abschlussprüfung in Abschnitt 5 |
| E. Implementieren und verifizieren | Freigegebener Plan mit Tests, Status und Abnahmen bearbeitet | Abschnitt 6 |
| F. Review und Veröffentlichung | Freigegebener Quellstand; bestehende Git-/Release-Regeln eingehalten | Abschnitt 7 |

Bei einem bereits adoptierten Projekt den vorhandenen Bootstrap-Nachweis prüfen
und erhalten. Fehlende Angaben gezielt ergänzen; den Bootstrap nicht neu starten.
Bei einem neuen Projekt oder erstmaliger Adoption ist Schritt C erforderlich.
Manus führt den Bootstrap mit dem Projekt-Owner durch: Er bereitet die Dokumente
vor und fragt fehlende Entscheidungen ab. Er darf die Antworten nicht erfinden.

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
struktur; halte das Handbuch generisch. Halte am ersten blockierenden Punkt an, frage fehlende Angaben gezielt ab und
dokumentiere Antworten oder ausdrückliche Deferrals in den zuständigen Quellen. Erfinde keine Anforderungen und beginne keine Feature-
Implementierung vor abgeschlossenem oder ausdrücklich zurückgestelltem Bootstrap.
Bereite die erste Spec und bereite Tasks mit Kriterien und Verifikation vor,
sobald deren Quellenblocker geklärt sind. Lege mir den Plan zur Freigabe vor.
```

### Bootstrap-Schritte in der richtigen Reihenfolge

Diese Übersicht gilt auch für die erstmalige Adoption aus Abschnitt 4. Sie fasst
[die verbindliche Bootstrap-Sequenz](../../delivery-system.md#bootstrap-sequence)
zusammen; die dortigen Detailanforderungen bleiben maßgeblich. `docs/` steht hier
für die bereits etablierte Dokumentationswurzel, falls das Projekt eine andere nutzt.

| Schritt | Was Manus mit dem Owner klärt oder bearbeitet | Maßgebliches Ergebnis |
| --- | --- | --- |
| 0 | Nur bei bestehendem Projekt: Repository, Dokumentation, Code, CI/CD und Risiken prüfen; bei neuem Projekt als nicht anwendbar markieren | Bestandsreview, etwa `docs/project/existing-repository-review.md` |
| 1 | Kopierte Platzhalter und fremde Projektannahmen bereinigen | Angepasste Dateien; offene Angaben ausdrücklich erfasst |
| 2 | Zweck, Ziele, Nicht-Ziele, Stakeholder und Grenzen festlegen | `docs/project/overview.md` |
| 3 | Übergeordnete funktionale, nichtfunktionale und Sicherheitsanforderungen klären | `docs/specs/requirements.md` |
| 4 | Funktionale Baseline auf das Projekt zuschneiden | `docs/specs/baseline/functional-requirements.md` |
| 5 | Nichtfunktionale Baseline und messbare Qualitätsziele prüfen | `docs/specs/baseline/non-functional-requirements.md` |
| 6 | Sicherheit, Datenschutz, Zugriffe und Datenhaltung klären | `docs/specs/baseline/security-policy.md` |
| 7 | Übergreifende Abnahmekriterien konkretisieren | `docs/specs/baseline/acceptance-criteria.md` |
| 8 | Erste Meilensteine, Umfang und Abhängigkeiten planen | `docs/project/roadmap.md` |
| 9 | Definition of Done und Prüfstrategie festlegen | `docs/quality/dod-checklist.md`, `docs/quality/test-strategy.md` |
| 10 | Passende Rollen und deren Nutzung in Manus prüfen | Relevante Profile unter `.github/agents/` und dokumentierte Manus-Einrichtung |
| 11 | Erste detaillierte Spec aus geklärten Anforderungen erstellen oder ausdrücklich zurückstellen | Spec nach `docs/specs/template.md` |
| 12 | Erste Task-Datei mit IDs, Rollen, Kriterien und Prüfungen erstellen oder ausdrücklich zurückstellen | Tasks nach `docs/tasks/template.md` |

**Stopppunkt bei offenen Fragen:** Am ersten blockierenden Punkt anhalten, die
Frage konkret stellen und Antwort oder ausdrückliche Zurückstellung an der
zuständigen Quelle dokumentieren. Erst dann im Bootstrap fortfahren. Aus einer
noch blockierten Spec keine Implementierungstasks erzeugen; einen blockierten
Task nicht implementieren. Eine Deferral erlaubt nur die ausdrücklich gewählte
Fortsetzung und löst andere Voraussetzungen nicht automatisch auf.

### Bootstrap-Abschluss und Freigabe zur Umsetzung

Vor Abschnitt 6 den
[Bootstrap Completion Check](../../delivery-system.md#bootstrap-completion-check)
am tatsächlichen Projektstand durchführen. Im bestehenden Bootstrap-Nachweis
oder, falls keiner vorhanden ist, im dauerhaften Projekt-Integrationsnachweis
festhalten: Schritt, Status, Ergebnisreferenz, offene Frage und dokumentierte
Antwort/Deferral. Keinen zusätzlichen konkurrierenden Projektplan anlegen.

- Schritt 0 ist abgeschlossen oder für das neue Projekt nicht anwendbar.
- Schritte 1–12 sind abgeschlossen oder vom Owner ausdrücklich zurückgestellt.
- Quellenblocker und verlinkte Frage-Dateien sind geklärt oder ausdrücklich
  zurückgestellt; die Entscheidungen stehen in den zuständigen Quellen.
- Projektquellen, Qualitätsregeln und notwendige Prüfkommandos sind verfügbar.
- Der konkret gewählte Umsetzungsumfang ist freigegeben; seine Spec und Tasks
  erfüllen ihre Bereitschaftskriterien. Zurückgestellte erste Specs/Tasks liefern
  noch keinen implementierbaren Auftrag.

Manus soll diese Prüfung vor Implementierung kurz mit den tatsächlichen
Dokumentreferenzen melden. Der Owner prüft den Plan und erteilt die noch fehlende
Umsetzungsfreigabe. Eine bereits ausdrücklich erteilte, weiterhin passende
Freigabe bleibt gültig. Ein pauschales „Bootstrap erledigt“ ohne Nachweise reicht
nicht als Übergabe in die Implementierung.

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
