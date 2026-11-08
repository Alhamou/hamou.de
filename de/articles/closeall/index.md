# closeAll: jede Dock-App mit einer Schaltfläche in der Menüleiste auf dem Mac sofort beenden

> closeAll beendet jede normale Dock-App mit einer Schaltfläche in der Menüleiste sofort. Du prüfst zuerst die Liste, entfernst das Häkchen bei allem, was offen bleiben soll, und drückst „Force Quit“. Das sofortige Beenden fordert Apps nicht zum Sichern auf, nicht gesicherte Arbeit geht also verloren. Der Code ist offen unter der MIT-Lizenz.

- Author: [Emad Alhamou](https://hamou.de/), Founder & Product Builder
- Published: 2026-11-08 (updated 2026-11-08)
- Language: Deutsch
- Web page: https://hamou.de/de/articles/closeall/
- Other languages: [English](https://hamou.de/articles/closeall/index.md), [العربية](https://hamou.de/ar/articles/closeall/index.md)
- Tool: [closeAll](https://github.com/Alhamou/closeAll) · macOS 14 oder neuer · Build für Apple Silicon · MIT-Lizenz
- Source code: https://github.com/Alhamou/closeAll (MIT license)

## Was ist closeAll?

closeAll ist eine kleine Open-Source-Menüleisten-App für macOS mit einer einzigen Aufgabe: alle laufenden normalen Apps auf einen Schlag zu schließen. Ihr Symbol in der Menüleiste ist ein kleiner Stapel von Fenstern. Klicke darauf, prüfe die Liste und drücke dann **Force Quit**. Die angehakten Apps werden per „Sofort beenden“ geschlossen.

Lies das einmal, bevor du es benutzt: „Sofort beenden“ fordert eine App nicht zum Sichern auf. Nicht gesicherte Arbeit in den geschlossenen Apps geht verloren.

## So benutzt du es

1. Klicke oben am Bildschirm auf das Symbol mit dem Fensterstapel.
2. Lass bei jeder App, die geschlossen werden soll, das Häkchen stehen. Entferne es, damit eine App offen bleibt; closeAll merkt sich diese Wahl.
3. Hake unter **Background apps** jede Menüleisten-App an, die ebenfalls geschlossen werden soll.
4. Drücke **Force Quit**.

Jede Zeile zeigt das eigene Symbol der App, sodass du sie erkennst, bevor sie sich schließt. Schließe oder entferne zuerst das Häkchen bei allem, was nicht gesicherte Arbeit enthält.

## Was geschlossen wird

- **Jede normale Anwendung,** also die Art, die du sonst im Dock mit der rechten Maustaste anklickst und beendest. Editoren, Browser und Chat-Apps gehören dazu, entferne also das Häkchen bei denen, die du behalten willst.
- **Hintergrund-Apps, die du anhakst.** Der Bereich „Background apps“ listet Menüleisten-Apps, die du in `/Applications` oder `~/Applications` installiert hast, etwa einen Zwischenablage-Manager oder einen VPN-Client. Sie sind zunächst nicht angehakt, dort wird also nichts geschlossen, solange du es nicht anhakst.

closeAll prüft, ob jede App wirklich beendet wurde. Überlebt eine App das sofortige Beenden oder kommt sie gleich zurück, sendet closeAll ein hartes Kill (SIGKILL), bis zu dreimal. Jede App, die sich trotzdem nicht schließen ließ, wird in Rot genannt.

## Was offen bleibt

- **Finder,** damit der Schreibtisch stehen bleibt, und **closeAll** selbst, damit die Schaltfläche noch da ist.
- Das Dock, das Kontrollzentrum, WindowServer und die anderen Prozesse, die deine Anmeldesitzung am Leben halten.
- Jede App, bei der du das Häkchen entfernst, und Hintergrund-Apps, die du nicht angehakt hast.
- Apples eigene Menüleisten-Agenten, Helfer innerhalb einer anderen App, Updater in Library-Ordnern und Prozesse ohne Fenster oder Menü werden gar nicht aufgelistet. Sie schließen sich meist zusammen mit ihrer Eltern-App.

## Datenschutz und Berechtigungen

closeAll läuft nicht in der Sandbox, weil die App Sandbox es daran hindern würde, andere Anwendungen zu beenden. Laut README nutzt es das Netzwerk nicht und sammelt keine Analysedaten. Deine Behalten-Liste liegt nur in deinen lokalen Einstellungen.

## Installation

closeAll braucht macOS 14 oder neuer. Die App, die `make app` auf einem Apple-Silicon-Mac baut, ist eine Apple-Silicon-App. Klone das Repository von GitHub, führe `make app` aus und öffne `build/closeAll.app`. Kopiere sie nach `/Applications`, wenn sie installiert bleiben soll. Sie zeigt kein Dock-Symbol.

Der Build ist ad hoc signiert, damit er auf deinem Mac starten kann, und nicht notarisiert. Blockiert macOS den ersten Start, klicke `closeAll.app` bei gedrückter Control-Taste an, wähle „Öffnen“ und bestätige. Damit sie beim Anmelden startet, füge sie in den Systemeinstellungen unter „Allgemein“ zu den Anmeldeobjekten hinzu. Zum Beenden öffnest du das Fenster und wählst „Quit closeAll“.

## Den Plan prüfen, ohne etwas zu schließen

`swift run closeAll -- --dry-run` gibt den Beenden-Plan als JSON aus und endet, ohne eine App zu schließen. `make check` führt die Unit-Tests aus und gibt dann den aktuellen Plan aus, und es schlägt fehl, wenn der Plan den Finder, closeAll selbst oder einen anderen Sitzungsprozess enthält.

## Open Source

closeAll steht unter der MIT-Lizenz. Die Beenden-Regeln liegen in einem eigenen Kernmodul ohne AppKit, abgedeckt durch Unit-Tests, und die Menüleisten-App ist darauf aufgebaut. Das Repository hat außerdem ein arabisches README.

Emad Alhamou, der Autor dieser Website, veröffentlicht closeAll auf [GitHub](https://github.com/Alhamou/closeAll). Hinweise zum Mitwirken, ein Verhaltenskodex und eine Sicherheitsrichtlinie liegen im Repository.

## Häufige Fragen

### Was ist closeAll?

closeAll ist eine Open-Source-Menüleisten-App für macOS, die jede normale Dock-App mit einer Schaltfläche sofort beendet, nachdem du die Liste geprüft und bei allem, was offen bleiben soll, das Häkchen entfernt hast.

### Verliere ich nicht gesicherte Arbeit?

Ja. „Sofort beenden“ fordert Apps nicht zum Sichern auf. Schließe oder entferne das Häkchen bei allem mit nicht gesicherter Arbeit, bevor du die Schaltfläche drückst.

### Welche Apps schließt closeAll, und welche bleiben offen?

Es schließt jede normale Anwendung, die macOS im Dock zeigt, dazu die Hintergrund-Menüleisten-Apps, die du anhakst. Finder, closeAll selbst, das Dock, das Kontrollzentrum, WindowServer und andere Sitzungsprozesse bleiben immer offen, ebenso jede App, bei der du das Häkchen entfernst.

### Kann ich einzelne Apps offen lassen?

Ja. Entferne in der Liste das Häkchen bei einer App, dann lässt closeAll sie offen und merkt sich die Wahl.

### Schließt es Menüleisten-Apps wie einen VPN-Client?

Nur wenn du sie anhakst. Der Bereich „Background apps“ listet Menüleisten-Apps aus `/Applications` und `~/Applications`, und sie sind zunächst nicht angehakt.

### Was, wenn eine App sich nicht beenden lässt?

closeAll prüft, ob jede App wirklich beendet wurde. Überlebt eine App oder kommt sie sofort zurück, sendet es ein hartes Kill (SIGKILL), bis zu dreimal, und nennt jede App, die sich trotzdem nicht schließen ließ, in Rot.

### Nutzt closeAll das Netzwerk oder sammelt es Daten?

Laut README nein. Es läuft nicht in der Sandbox, nutzt das Netzwerk nicht und sammelt keine Analysedaten. Deine Behalten-Liste bleibt in den lokalen Einstellungen.

### Welche Macs und macOS-Versionen werden unterstützt?

macOS 14 oder neuer. Die App, die `make app` auf einem Apple-Silicon-Mac baut, ist eine Apple-Silicon-App.
