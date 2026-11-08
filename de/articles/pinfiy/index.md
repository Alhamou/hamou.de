# pinFiy: farbige Haftnotizen für den Mac, mit einer kleinen Pinnnadel in der Menüleiste

> pinFiy gibt deinem Mac farbige Haftnotizen, die hinter einer kleinen Pinnnadel in der Menüleiste wohnen. Jede Notiz ist ein eigenes Fenster, arabischer Text läuft von rechts nach links und englischer von links nach rechts, und eine angeheftete Notiz bleibt über deinen anderen Fenstern. Es gibt kein Konto, keine Cloud-Synchronisation und keinen Netzwerkzugriff. Der Code ist offen unter der MIT-Lizenz.

- Author: [Emad Alhamou](https://hamou.de/), Founder & Product Builder
- Published: 2026-11-08 (updated 2026-11-08)
- Language: Deutsch
- Web page: https://hamou.de/de/articles/pinfiy/
- Other languages: [English](https://hamou.de/articles/pinfiy/index.md), [العربية](https://hamou.de/ar/articles/pinfiy/index.md)
- Tool: [pinFiy](https://github.com/Alhamou/pinFiy) · macOS 13 oder neuer · Swift 5.9 oder neuer zum Bauen · MIT-Lizenz
- Source code: https://github.com/Alhamou/pinFiy (MIT license)

## Was ist pinFiy?

pinFiy ist eine Open-Source-Haftnotizen-App für macOS. Jede Notiz ist ein eigenes farbiges Fenster. Die App selbst ist eine kleine Pinnnadel in der Menüleiste und erscheint nicht im Dock, sie bleibt also aus dem Weg, bis du eine Notiz brauchst.

Sie behandelt Arabisch und Englisch gleichberechtigt nebeneinander. Die Schreibrichtung folgt dem ersten starken Zeichen deines Textes: Arabisch läuft von rechts nach links und Englisch von links nach rechts, in derselben App und sogar auf benachbarten Notizen.

## Was es kann

- **Ein Fenster pro Notiz,** sodass du jede Notiz dorthin legen kannst, wo du sie brauchst.
- **„Pin“ hält eine Notiz im Vordergrund.** Eine angeheftete Notiz bleibt über normalen Fenstern und verdeckt die Menüleiste nicht. Die Ecke der Nadel folgt der Textrichtung: rechts für Arabisch, links für Englisch.
- **Zwanzig Farben:** zehn helle und zehn dunkle. Standard ist ein warmes Bernstein (`#F3C15B`). Dunkler Text steht auf hellen Farben und heller Text auf dunklen.
- **Schriftgröße von 12 bis 36** für jede Notiz, und in den Einstellungen für neue Notizen oder für alle Notizen.
- **Eine Notiz sperren,** um Änderungen an Text, Farbe, Größe und Position zu blockieren und das Schließen zu verhindern.
- **Ein Sicherheitsnetz:** Beim Schließen einer Notiz mit Text wird zuerst nachgefragt.
- **Beim Anmelden öffnen,** über die Einstellungen oder das Nadelmenü.

## Wo deine Notizen liegen

Die Notizen liegen auf deinem Mac, in `~/Library/Application Support/pinFiy/notes.json`, mit einer Sicherungsdatei. Laut README gibt es kein Konto, keine Cloud-Synchronisation und keinen Netzwerkzugriff. Das Repository enthält eine Datenschutzerklärung und eine Sicherheitsrichtlinie.

## Kürzel

- **Neue Notiz:** die Plus-Schaltfläche, `⌘N` oder das Nadelmenü.
- **Notiz schließen:** die Schließen-Schaltfläche oder `⌘W`.
- **Über Fenstern halten:** die Pin-Schaltfläche oder `⌘P`.
- **Einstellungen:** `⌘,` oder das Nadelmenü.
- **Beenden:** `⌘Q` oder das Nadelmenü.

## Installation

pinFiy braucht macOS 13 oder neuer und Swift 5.9 oder neuer, das die mit Xcode gelieferte Toolchain enthält. Klone das Repository von GitHub, führe `swift test` und dann `./scripts/build-app.sh` aus und öffne `PinFiy.app`. Das Skript signiert die App ad hoc. Das ist keine Apple-Developer-Signatur und kein App-Store-Release.

## Open Source

pinFiy steht unter der MIT-Lizenz. Der Code ist aufgeteilt in eine Kernbibliothek für Modell und Speicherung, ohne AppKit, und ein App-Target für die Notizfenster und die Menüleiste. Der Kern hat XCTest-Tests.

Emad Alhamou, der Autor dieser Website, veröffentlicht pinFiy auf [GitHub](https://github.com/Alhamou/pinFiy). Das Repository enthält Hinweise zum Mitwirken und einen Verhaltenskodex, und Sicherheitsprobleme werden vertraulich gemeldet, wie es die Sicherheitsrichtlinie beschreibt.

## Häufige Fragen

### Was ist pinFiy?

pinFiy ist eine Open-Source-Haftnotizen-App für macOS. Sie gibt dir farbige Notizen, jede in einem eigenen Fenster, gesteuert über eine kleine Pinnnadel in der Menüleiste.

### Unterstützt pinFiy Arabisch und Text von rechts nach links?

Ja. Die Schreibrichtung folgt dem ersten starken Zeichen: Arabisch läuft von rechts nach links und Englisch von links nach rechts. Die Nadelecke einer Notiz folgt der Richtung ebenfalls.

### Was macht „Pin“?

„Pin“ hält eine Notiz über normalen Fenstern, ohne die Menüleiste zu verdecken. Nutze die Pin-Schaltfläche der Notiz oder drücke `⌘P`.

### Wo werden meine Notizen gespeichert, und nutzt pinFiy das Netzwerk?

Die Notizen liegen lokal in `~/Library/Application Support/pinFiy/notes.json`, mit einer Sicherung. Laut README gibt es kein Konto, keine Cloud-Synchronisation und keinen Netzwerkzugriff.

### Was bewirkt das Sperren einer Notiz?

Eine gesperrte Notiz lässt sich nicht bearbeiten, umfärben, in der Größe ändern oder verschieben und nicht schließen, bis du sie entsperrst.

### Welche macOS-Version braucht pinFiy?

macOS 13 oder neuer. Zum Bauen braucht es Swift 5.9 oder neuer.

### Wie installiere ich pinFiy?

Klone das Repository, führe `swift test` und `./scripts/build-app.sh` aus und öffne dann `PinFiy.app`. Der Build ist ad hoc signiert, nicht mit einem Apple-Developer-Zertifikat.

### Kann ich Schriftgröße und Farben ändern?

Ja. Jede Notiz hat Farbfelder und Schaltflächen für die Schriftgröße, von 12 bis 36. In den Einstellungen legst du die Größe für neue Notizen oder für alle Notizen fest.
