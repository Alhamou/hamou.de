# RemoteDesk: ein Open-Source-Remotedesktop von Mac zu Mac für dein lokales Netzwerk

> RemoteDesk teilt den Bildschirm eines Macs und lässt dich ihn von einem anderen Mac über dein lokales Netzwerk steuern. Es nimmt den Bildschirm mit ScreenCaptureKit auf, komprimiert ihn mit Hardware-H.264 und sendet ihn über TCP. Es hat weder Verschlüsselung noch Anmeldung und ist deshalb nur für vertrauenswürdige private Netze gedacht. Der Code ist offen unter der MIT-Lizenz.

- Author: [Emad Alhamou](https://hamou.de/), Founder & Product Builder
- Published: 2026-11-08 (updated 2026-11-08)
- Language: Deutsch
- Web page: https://hamou.de/de/articles/remotedesk/
- Other languages: [English](https://hamou.de/articles/remotedesk/index.md), [العربية](https://hamou.de/ar/articles/remotedesk/index.md)
- Tool: [RemoteDesk](https://github.com/Alhamou/RemoteDesk) · macOS 14 oder neuer auf beiden Macs · gleiches lokales Netzwerk · MIT-Lizenz
- Source code: https://github.com/Alhamou/RemoteDesk (MIT license)

## Was ist RemoteDesk?

RemoteDesk ist ein Open-Source-Remotedesktop für macOS, der zwischen zwei Macs im selben lokalen Netzwerk funktioniert. Ein Mac teilt seinen Bildschirm, der andere zeigt ihn an und schickt Maus, Tastatur, Scrollen und Zwischenablage zurück. Es ist in Swift geschrieben und nutzt nur Apples eigene Frameworks, keine Bibliotheken von Dritten.

Es ist ein fokussiertes Werkzeug: von Mac zu Mac, über ein lokales Netzwerk. Es ist kein Cloud-Dienst, es gibt kein Konto, und es ist nicht für das offene Internet gebaut. Lies den Abschnitt zur Sicherheit, bevor du es benutzt.

## So funktioniert es

- **Der Host** ist der gesteuerte Mac. Er nimmt den Bildschirm mit ScreenCaptureKit auf, komprimiert ihn mit Hardware-H.264 über VideoToolbox und sendet ihn über einen TCP-Socket mit Längenpräfix. Maus- und Tastatureingaben aus der Ferne werden mit `CGEvent` eingespielt.
- **Der Client** ist der Mac, an dem du sitzt. Er dekodiert den H.264-Strom in Hardware, zeichnet ihn über einen `CALayer` und erfasst Maus-, Tastatur-, Scroll- und Zwischenablage-Ereignisse.

Das README beschreibt ein eigenes binäres Protokoll ohne B-Frames und mit adaptiver Staukontrolle, ausgelegt auf niedrige Latenz. Die Architekturhinweise im Repository erklären das Protokoll und das Nebenläufigkeitsmodell.

## Was es kann

- **Vollständige Eingabeweiterleitung:** präzise Zeigerbewegung, Klicks mit der linken, rechten und mittleren Taste, pixelgenaues Scrollen in beiden Richtungen und Tastatureingaben.
- **Vollbildmodus „Capture All Input“:** Im Vollbild gehen Systemkürzel wie Cmd+Tab, Cmd+Leertaste und Mission Control an den entfernten Mac statt an deinen eigenen.
- **Trackpad-Gesten und Spaces:** Im Vollbild wirken Spaces-Wischgesten, Mission Control, App Exposé und Zoomgesten auf den entfernten Mac, entsprechend deinen Trackpad-Einstellungen.
- **„Match Remote Resolution to This Screen“:** Der Host wechselt zu der Auflösung, die am besten zum Display des Clients passt, damit das Vollbild es ausfüllt, und stellt sie beim Trennen wieder her.
- **Saubere Ränder im Vollbild:** Das lokale Dock bleibt verborgen, und nur der obere Rand zeigt deine lokale Menüleiste und die Fensterknöpfe.
- **Text-Zwischenablage in beide Richtungen** mit Schleifenunterdrückung.
- **Erkennung ohne Konfiguration:** Hosts melden sich über Bonjour (`_remotedesk._tcp`) in deinem WLAN oder Ethernet, oder du verbindest dich direkt per IP-Adresse.

## Sicherheit: bitte zuerst lesen

RemoteDesk ist nur für vertrauenswürdige private lokale Netze gedacht, und sein README nennt die Grenzen klar:

- **Keine Verschlüsselung.** Der Verkehr läuft über einfaches TCP ohne TLS, Bildschirmbilder und eingetippte Tasten gehen also im Klartext durch dein Netzwerk.
- **Keine Authentifizierung.** Jedes Gerät im selben Netzwerk, das den Port des Hosts erreicht, bekommt volle Kontrolle.
- **Zwischenablage wird verteilt.** Text, den du kopierst, wird automatisch an den verbundenen Mac gesendet.

Betreibe es nie in unsicheren öffentlichen WLANs wie an Flughäfen, in Hotels oder Cafés. Um einen Mac über das Internet zu erreichen, leite den Verkehr durch einen verschlüsselten Kanal wie Tailscale, WireGuard oder SSH-Portweiterleitung. TLS mit einem vorab geteilten Schlüssel und eine PIN- oder Einmalpasswort-Abfrage am Host stehen auf der Roadmap, sind aber noch nicht in der App.

## Berechtigungen

- **Host:** Bildschirmaufnahme und Bedienungshilfen, beides in den Systemeinstellungen unter „Datenschutz & Sicherheit“. Starte RemoteDesk nach dem Erteilen der Bildschirmaufnahme neu.
- **Client:** Bedienungshilfen, und zwar nur für den Vollbildmodus „Capture All Input“.

## Installation

RemoteDesk braucht auf beiden Macs macOS 14 Sonoma oder neuer. Die App ist ein Universal Binary und läuft daher auf Apple Silicon und auf Intel. Lade das DMG vom neuesten Release auf GitHub herunter und ziehe RemoteDesk in den Ordner „Programme“. Das Release wird ohne bezahlte Apple Developer ID verteilt, deshalb kann macOS den ersten Start verweigern: Klicke die App bei gedrückter Control-Taste an, wähle „Öffnen“ und bestätige. Das README nennt außerdem eine Alternative im Terminal, die das Quarantäne-Attribut mit `xattr -cr` entfernt.

Zum Selbstbauen brauchst du die Swift-Toolchain (Xcode oder die Command Line Tools). Klone das Repository und führe `./scripts/make-app.sh` aus.

## Benutzung

Öffne RemoteDesk auf beiden Macs. Wähle auf dem Host-Mac **Share This Mac** und erteile die Berechtigungsabfragen. Wähle auf dem Client-Mac **Connect to a Mac**, nimm den Host aus der Bonjour-Liste oder gib seine lokale IP-Adresse ein (der Standardport ist 8790) und wähle **Connect**. Das Host-Fenster blendet sich aus, solange ein Client verbunden ist; über das Dock-Symbol siehst du den Status oder trennst die Verbindung.

Kürzel am Client: Ctrl+Cmd+F schaltet den Vollbildmodus um, Ctrl+Opt+Cmd+G schaltet die Eingabeerfassung ein oder aus, und Ctrl+Opt+Cmd+Q trennt sofort und wird nie an den Host weitergeleitet.

RemoteDesk lässt sich auch über die Kommandozeile starten, einschließlich eines Hosts ohne Fenster mit `--host --no-ui`.

## Open Source

RemoteDesk steht unter der MIT-Lizenz. Emad Alhamou, der Autor dieser Website, veröffentlicht es auf [GitHub](https://github.com/Alhamou/RemoteDesk). Die Roadmap nennt TLS-Verschlüsselung, eine PIN- oder Einmalpasswort-Abfrage, Audio-Streaming und die Auswahl mehrerer Monitore. Fehlerberichte und Pull Requests sind willkommen.

## Häufige Fragen

### Was ist RemoteDesk?

RemoteDesk ist ein Open-Source-Remotedesktop für macOS. Er teilt den Bildschirm eines Macs und lässt dich ihn von einem anderen Mac im selben lokalen Netzwerk steuern, mit Hardware-H.264-Streaming und vollständiger Eingabeweiterleitung.

### Ist RemoteDesk sicher?

Nur in einem vertrauenswürdigen privaten Netzwerk. Es sendet den Verkehr über einfaches TCP ohne Verschlüsselung und hat keine Anmeldung: Jedes Gerät im Netzwerk, das den Port des Hosts erreicht, bekommt volle Kontrolle. Nutze es nicht in öffentlichen WLANs.

### Kann ich RemoteDesk über das Internet nutzen?

Nicht direkt. Laut README leitest du den Verkehr durch einen verschlüsselten Kanal wie Tailscale, WireGuard oder SSH-Portweiterleitung und setzt es nie in unsicheren Netzen aus.

### Welche Macs und macOS-Versionen werden unterstützt?

macOS 14 Sonoma oder neuer auf Host und Client. Die App ist ein Universal Binary für Apple Silicon und Intel.

### Welche Berechtigungen braucht RemoteDesk?

Der Host braucht Bildschirmaufnahme und Bedienungshilfen. Der Client braucht Bedienungshilfen nur für den Vollbildmodus „Capture All Input“.

### Wie verbinde ich zwei Macs?

Öffne RemoteDesk auf beiden. Wähle am Host „Share This Mac“. Wähle am Client „Connect to a Mac“, nimm den Host aus der Bonjour-Liste oder gib seine lokale IP-Adresse ein und wähle „Connect“.

### Was kann RemoteDesk noch nicht?

Es verschlüsselt den Verkehr nicht und fragt keine PIN ab. Audio-Streaming und die Auswahl mehrerer Monitore stehen ebenfalls auf der Roadmap. Der Zwischenablage-Abgleich umfasst nur Text.

### Warum warnt macOS mich beim Öffnen von RemoteDesk?

Das Release wird ohne bezahltes Apple-Developer-ID-Zertifikat verteilt. Klicke die App bei gedrückter Control-Taste an und wähle „Öffnen“, oder entferne das Quarantäne-Attribut mit `xattr -cr`.
