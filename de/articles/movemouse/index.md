# moveMouse: eine Mac-Menüleisten-App, die hilft, RDP-Verbindungen offen zu halten

> moveMouse hilft, eine Remotedesktop-Verbindung (RDP) offen zu halten. Es bewegt den Mauszeiger in einem Intervall, das du wählst, und hält den Mac wach, solange es läuft, damit eine ruhige Sitzung seltener getrennt wird. Es sitzt in der Menüleiste, und sein Code ist offen unter der MIT-Lizenz.

- Author: [Emad Alhamou](https://hamou.de/), Founder & Product Builder
- Published: 2026-11-08 (updated 2026-11-08)
- Language: Deutsch
- Web page: https://hamou.de/de/articles/movemouse/
- Other languages: [English](https://hamou.de/articles/movemouse/index.md), [العربية](https://hamou.de/ar/articles/movemouse/index.md)
- Tool: [moveMouse](https://github.com/Alhamou/moveMouse) · macOS 11 oder neuer · Build für Apple Silicon · Bedienungshilfen-Berechtigung · MIT-Lizenz
- Source code: https://github.com/Alhamou/moveMouse (MIT license)

## Was ist moveMouse?

moveMouse ist eine kleine Open-Source-App für die macOS-Menüleiste. In einem Intervall, das du wählst, bewegt sie den Mauszeiger von selbst, und solange sie läuft, hält sie den Mac davon ab, wegen Inaktivität in den Ruhezustand zu gehen. Gebaut wurde sie für ein praktisches Problem: eine Remotedesktop-Verbindung (RDP), die abbricht, wenn du den Mac nicht anfasst. Der Tooltip der App in der Menüleiste sagt das selbst, auf Arabisch: Sie soll verhindern, dass RDP-Verbindungen getrennt werden.

Das README beschreibt sie allgemeiner als automatische Mausbewegung nach deinem Zeitplan: nützlich für Demonstrationen am Desktop, zum Testen von Mausinteraktionen oder um einen Mac während einer Aufgabe aktiv zu halten. Sie ist in Swift und AppKit geschrieben und läuft ohne Dock-Symbol.

## Warum eine RDP-Verbindung abbricht

Remotedesktop-Sitzungen enden meist aus banalen Gründen. Der Mac, von dem aus du dich verbindest, geht in den Ruhezustand und nimmt die Netzwerkverbindung mit, oder die Gegenseite hält eine Sitzung ohne Eingaben für untätig und beendet oder sperrt sie. moveMouse arbeitet von deinem Mac aus und packt beides an: Es verhindert den Ruhezustand durch Inaktivität, solange es läuft, und erzeugt Zeigeraktivität im eingestellten Intervall.

Zwei ehrliche Grenzen. Die App weiß nichts von deinem RDP-Client: Sie bewegt den Zeiger auf deinem Mac, die Aktivität erreicht die entfernte Sitzung also nur, solange das RDP-Fenster unter dem Zeiger liegt. Halte das Remotedesktop-Fenster deshalb dort, wo sich der Zeiger bewegt, beim Standardmuster ist das die Bildschirmmitte. Und moveMouse ändert nichts am entfernten Rechner, eine dort erzwungene Sitzungsgrenze bleibt also bestehen.

## Was es kann

- **Sechs Intervalle:** alle 15, 30 oder 45 Sekunden oder alle 1, 2 oder 5 Minuten. Beim ersten Start gilt 30 Sekunden.
- **Zwei Bewegungsmuster:** „Bildschirmmitte“ führt den Zeiger zur Mitte des Bildschirms, dann nach rechts und links und endet in der Mitte. „Aktuelle Zeigerposition“ bewegt ihn ein kurzes Stück nach rechts und links und bringt ihn an den Ausgangspunkt zurück.
- **Ein optionaler Linksklick** nach jeder Bewegung, mit optionalem Ton. Der Klick geschieht an der letzten Zeigerposition und trifft alles, was darunter liegt.
- **Einfache Steuerung in der Menüleiste:** Start oder Pause, „Move Now“ (funktioniert auch während der Pause) und Beenden. Eine Statuszeile zeigt, ob die Bewegung läuft und wann der letzte Vorgang stattfand.
- **Gespeicherte Einstellungen:** Intervall, Muster, Klick und Ton bleiben zwischen den Starts erhalten.
- **Ruhezustand verhindern:** Der Ruhezustand durch Inaktivität wird blockiert, solange die automatische Bewegung läuft. Pause oder Beenden gibt ihn wieder frei.

moveMouse beginnt zu bewegen, sobald es startet, mit deinen gespeicherten Einstellungen. Die Menübeschriftungen sind auf Arabisch, mit englischen Bezeichnungen für mehrere Steuerelemente: Start, Pause, Move Now, Interval und Left Click.

## Berechtigungen

Simulierte Mauseingaben brauchen die Berechtigung „Bedienungshilfen“. Beim ersten Start fragt macOS möglicherweise danach: Öffne die Systemeinstellungen, gehe zu „Datenschutz & Sicherheit“, dann „Bedienungshilfen“, und aktiviere moveMouse. Der Eintrag für die Bedienungshilfen im Menü der App öffnet diese Seite für dich. Laut README braucht vor allem das Klicken diese Berechtigung. Wenn das Klicken nach einem Neubau oder Verschieben der App nicht mehr funktioniert, entferne ihren Eintrag bei den Bedienungshilfen, füge die App erneut hinzu und starte sie neu.

## Installation

moveMouse braucht macOS 11 Big Sur oder neuer. Die mitgelieferte App und das Build-Skript zielen auf Apple Silicon (arm64). Klone das Repository von GitHub und führe dann `./build.sh` und `./run.sh` aus. Zum Bauen brauchst du die Xcode Command Line Tools, die `xcode-select --install` installiert. Das Skript signiert die App lokal mit einer Ad-hoc-Signatur.

Damit moveMouse beim Anmelden startet, füge `MoveMouse.app` in den Systemeinstellungen unter „Allgemein“ zu den Anmeldeobjekten hinzu. Zum Beenden wählst du „Beenden“ im Menü oder führst `./stop.sh` im Projektordner aus.

## Open Source

moveMouse steht unter der MIT-Lizenz. Es nutzt nur native macOS-Frameworks und wird direkt mit `swiftc` gebaut, ohne Abhängigkeiten von Dritten und ohne Xcode-Projekt. Der Code besteht aus wenigen Swift-Dateien: der Menüleisten-Oberfläche, dem Bewegungs-Timer mit Zeigereingabe und gespeicherten Einstellungen sowie der Verhinderung des Ruhezustands.

Emad Alhamou, der Autor dieser Website, veröffentlicht moveMouse auf [GitHub](https://github.com/Alhamou/moveMouse). Fehlerberichte, Ideen und Pull Requests sind willkommen; nenne deine macOS-Version, die Schritte zum Nachstellen und was du erwartet hast.

## Häufige Fragen

### Was ist moveMouse?

moveMouse ist eine Open-Source-Menüleisten-App für macOS, die den Mauszeiger automatisch in einem Intervall bewegt, das du wählst, und den Mac wach hält, solange sie läuft. Sie wurde gebaut, um eine RDP-Verbindung vor dem Abbruch zu bewahren.

### Wie hilft moveMouse bei einer RDP-Verbindung?

Es arbeitet von deinem Mac aus. Es verhindert den Ruhezustand durch Inaktivität, der die Verbindung sonst kappen würde, und erzeugt Zeigeraktivität im gewählten Intervall, damit eine Sitzung nicht völlig still bleibt. Die Aktivität erreicht die entfernte Sitzung nur, solange das RDP-Fenster unter dem Zeiger liegt, und moveMouse ändert keine Einstellung auf dem entfernten Rechner.

### Kann der Klick etwas treffen, das ich nicht wollte?

Ja, das ist möglich. Der optionale Linksklick geschieht an der letzten Zeigerposition und trifft alles, was darunter liegt. Wenn du nur die Bewegung willst, schalte „Left Click“ im Menü aus. Standardmäßig ist er an.

### Welche Intervalle und Bewegungsmuster gibt es?

Die Intervalle sind 15, 30 und 45 Sekunden sowie 1, 2 und 5 Minuten, mit 30 Sekunden als Standard. Die zwei Muster sind „Bildschirmmitte“ (Mitte, rechts, links, zurück zur Mitte) und „Aktuelle Zeigerposition“ (ein kleines Wackeln nach rechts und links, dann zurück zum Start).

### Welche Berechtigung braucht moveMouse?

„Bedienungshilfen“, für simulierte Mauseingaben, vor allem das Klicken. Aktiviere moveMouse in den Systemeinstellungen unter „Datenschutz & Sicherheit“, dann „Bedienungshilfen“.

### Welche Macs und macOS-Versionen werden unterstützt?

macOS 11 Big Sur oder neuer. Die mitgelieferte App und das Build-Skript zielen auf Apple Silicon (arm64).

### Wie pausiere oder beende ich moveMouse?

Wähle im Menüleisten-Menü „Pause“, um die geplante Bewegung zu stoppen und die Verhinderung des Ruhezustands freizugeben, oder „Beenden“, um die App zu schließen. „Move Now“ führt eine Bewegung auf Abruf aus, auch während der Pause.

### Ist moveMouse Open Source?

Ja. Es steht unter der MIT-Lizenz, und der Quellcode liegt auf GitHub.
