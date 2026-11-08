# OpenBlock: ein Open-Source-Werbeblocker für Safari auf dem Mac, ohne Tracking

> OpenBlock blockiert Werbung und Tracker in Safari auf deinem Mac. Der Blocker lädt echte Filterlisten, wandelt sie in Safaris eigenes Regelformat um und überlässt Safari die Durchsetzung, sodass nichts zwischen dir und dem Web steht. Der Code ist offen unter der GPL-3.0-Lizenz.

- Author: [Emad Alhamou](https://hamou.de/), Founder & Product Builder
- Published: 2026-11-08 (updated 2026-11-08)
- Language: Deutsch
- Web page: https://hamou.de/de/articles/openblock/
- Other languages: [English](https://hamou.de/articles/openblock/index.md), [العربية](https://hamou.de/ar/articles/openblock/index.md)
- Tool: [OpenBlock](https://github.com/Alhamou/OpenBlock) · macOS 15 Sequoia oder neuer · Swift · GPL-3.0-Lizenz
- Source code: https://github.com/Alhamou/OpenBlock (GPL-3.0 license)

## Was ist OpenBlock?

OpenBlock ist ein Open-Source-Werbeblocker für Safari auf macOS. Er folgt demselben Rezept wie AdGuard für Safari: Filterlisten laufen durch einen Konverter und werden zu Safari-Inhaltsblockern. Die App lädt die Listen herunter, wandelt sie in Safaris natives Regelformat um und übergibt sie an Safari, das sie in seine eigene Engine kompiliert. Nichts steht zwischen dir und dem Web, und OpenBlock sendet keine Daten über dein Surfen irgendwohin.

Er blockiert nur innerhalb von Safari. Andere Browser und Apps sehen die Regeln nie. DNS-basiertes Blockieren für alle Apps auf dem Mac ist die nächste geplante Funktion.

## Womit er blockiert

- **Vier Safari-Inhaltsblocker:** Werbung, Datenschutz, Störendes und Eigene Regeln. Jeder hat sein eigenes Budget von 150.000 Regeln.
- **Echte Filterlisten:** AdGuard Base, Tracking, Social, Cookie und Popups (die Safari-Versionen), EasyList, EasyPrivacy, regionale Listen oder jede Listen-URL, die du hinzufügst, in AdBlock-Syntax oder als Hosts-Datei.
- **Eigene Regeln und eine Zulassungsliste** in AdBlock-Syntax. Seiten auf der Zulassungsliste bleiben unberührt.
- **Automatische Updates:** Die Listen werden alle 24 Stunden aktualisiert, solange OpenBlock läuft. In der Menüleiste gibt es außerdem „Filter jetzt aktualisieren“ neben „Blockieren pausieren“ und „Beim Anmelden starten“.

## OpenBlock Advanced

Safaris Inhaltsblocker können nicht jede Regel ausdrücken. Für den Rest gibt es OpenBlock Advanced, eine Safari-Web-Erweiterung. Sie führt Scriptlets aus (AdGuards `#%#//scriptlet(...)`-Regeln und die `##+js(...)`-Regeln von uBlock Origin), fügt CSS ein (`#$#`), unterstützt erweiterte CSS-Selektoren (`#?#`, `:has-text()`, `:remove()`) und verarbeitet Regeln für Domains mit Platzhalter-Top-Level-Domain wie `example.*`. Das Projekt nennt YouTube-Werbung und Anti-Adblock-Sperren als Beispiele. Die Symbolleisten-Schaltfläche zeigt den Status der aktuellen Seite und pausiert die erweiterten Regeln für diese Seite.

## Datenschutz

Das README beschreibt OpenBlock als frei von Tracking, und die Sicherheitsrichtlinie nennt als einzigen Netzwerkverkehr den Download der Filterlisten, die du eingeschaltet hast. Es gibt keine Telemetrie, keine Analytik und keine Absturzberichte, und OpenBlock liest deinen Browserverlauf nicht. Weil Safari die Regeln selbst kompiliert, steht die App nie im Weg deines Webverkehrs.

## Installation

OpenBlock braucht macOS 15 Sequoia oder neuer. Lade das DMG vom neuesten Release auf GitHub herunter und ziehe OpenBlock in den Ordner „Programme“. Der Build ist mit einem Apple-Development-Zertifikat signiert und nicht notarisiert, deshalb fragt macOS beim ersten Start nach: Öffne die Systemeinstellungen, gehe zu „Datenschutz & Sicherheit“ und wähle neben OpenBlock „Dennoch öffnen“.

Öffne dann OpenBlock, wähle deine Filterlisten und warte, bis die erste Umwandlung fertig ist. In Safari öffnest du die Einstellungen, dann „Erweiterungen“: Aktiviere die vier OpenBlock-Inhaltsblocker und OpenBlock Advanced und erlaube Letzteres auf allen Websites. Halte nur eine Kopie der App auf dem Datenträger, denn Safari kommt durcheinander, wenn zwei Builds dieselben Erweiterungen registrieren.

Zum Selbstbauen brauchst du Xcode 16 oder neuer und XcodeGen. Safari lädt nur signierte Erweiterungen, ein unsignierter Build blockiert daher nichts.

## Open Source

OpenBlock steht unter der GPL-3.0, weil OpenBlock Advanced die GPL-3-Bibliotheken Scriptlets und ExtendedCss von AdGuard enthält. Die Filterlisten werden beim Ausführen der App heruntergeladen und behalten ihre eigenen Lizenzen. OpenBlock ist nicht mit AdGuard verbunden. Im Repository gibt es außerdem einen Kommandozeilen-Konverter, den du gegen Apples eigenen Regel-Compiler von WebKit prüfen kannst.

Emad Alhamou, der Autor dieser Website, veröffentlicht OpenBlock auf [GitHub](https://github.com/Alhamou/OpenBlock). Fehlerberichte und Pull Requests sind willkommen.

## Häufige Fragen

### Was ist OpenBlock?

OpenBlock ist ein Open-Source-Werbeblocker für Safari auf macOS. Er wandelt echte Filterlisten in Safaris native Inhaltsblocker um und ergänzt eine Web-Erweiterung für erweiterte Regeln.

### Funktioniert OpenBlock in Chrome, Firefox oder anderen Apps?

Nein. OpenBlock blockiert nur innerhalb von Safari, weil Safari die Regeln in seine eigene Engine kompiliert und andere Browser und Apps sie nie sehen. DNS-basiertes Blockieren für alle Apps ist geplant.

### Welche Filterlisten nutzt OpenBlock?

AdGuard Base, Tracking, Social, Cookie und Popups, EasyList, EasyPrivacy und regionale Listen, dazu jede Listen-URL, die du hinzufügst. Die Listen können AdBlock-Syntax nutzen oder Hosts-Dateien sein.

### Sammelt OpenBlock meine Daten?

Laut README und Sicherheitsrichtlinie nein. Es gibt keine Telemetrie, Analytik oder Absturzberichte, und der einzige Netzwerkverkehr ist der Download der Filterlisten, die du eingeschaltet hast.

### Welche macOS-Version braucht OpenBlock?

macOS 15 Sequoia oder neuer.

### Warum warnt macOS mich beim Öffnen von OpenBlock?

Der Release-Build ist mit einem Apple-Development-Zertifikat statt einer Developer ID signiert und nicht notarisiert. Öffne ihn mit „Dennoch öffnen“ in den Systemeinstellungen unter „Datenschutz & Sicherheit“. Signieren mit Developer ID und Notarisierung stehen auf der Roadmap des Projekts.

### Ist OpenBlock mit AdGuard verbunden?

Nein. Es ist auf dieselbe Weise gebaut (Filterlisten, ein Konverter, Safari-Inhaltsblocker) und enthält die Open-Source-Bibliotheken Scriptlets und ExtendedCss von AdGuard, weshalb es unter der GPL-3.0 steht.
