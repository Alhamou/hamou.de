# Haki (حكي): Push-to-Talk-Diktat für die Mac-Menüleiste, auf Arabisch abgestimmt

> Haki macht aus deiner Stimme überall auf deinem Mac Text. Halte Option+Leertaste, sprich, lass los, und der transkribierte Text wird an deinem Cursor eingefügt. Es ist auf natürliches Arabisch abgestimmt, auch levantinisches und syrisches Sprechen, und beherrscht außerdem Englisch, Deutsch und Französisch. Die Transkription nutzt OpenAI-Modelle mit deinem eigenen API-Schlüssel, dein Audio geht also an OpenAI. Der Code ist offen unter der MIT-Lizenz.

- Author: [Emad Alhamou](https://hamou.de/), Founder & Product Builder
- Published: 2026-11-08 (updated 2026-11-08)
- Language: Deutsch
- Web page: https://hamou.de/de/articles/haki/
- Other languages: [English](https://hamou.de/articles/haki/index.md), [العربية](https://hamou.de/ar/articles/haki/index.md)
- Tool: [Haki](https://github.com/Alhamou/Haki) · macOS 13 oder neuer · OpenAI-API-Schlüssel · Berechtigungen Mikrofon und Bedienungshilfen · MIT-Lizenz
- Source code: https://github.com/Alhamou/Haki (MIT license)

## Was ist Haki?

Haki (حكي, ein levantinisch-arabisches Wort für „Sprechen“) ist eine leichte native macOS-Menüleisten-App für Sprache-zu-Text-Diktat. Klicke in ein beliebiges Textfeld in einer beliebigen App, halte die Push-to-Talk-Taste, sprich und lass los. Haki transkribiert, was du gesagt hast, und fügt es am Cursor ein. Der arabische Slogan lautet „احكي، وحكي بيكتبها“, etwa „du sprichst, Haki schreibt“.

Es ist besonders für natürliches Arabisch und levantinisches Sprechen gedacht, mit Unterstützung für Englisch, Deutsch, Französisch und automatische Spracherkennung. Es hat kein lokales Sprachmodell und keine Python- oder Node.js-Laufzeit: Die App ist natives Swift, und die Transkription übernimmt OpenAI.

## So funktioniert das Diktat

1. Fokussiere ein Textfeld in einer beliebigen Anwendung, etwa Notizen, TextEdit, einem Browser, einer Chat-App oder einem Editor.
2. Halte `⌥ Option + Leertaste` gedrückt und sprich.
3. Lass die Tasten los. Haki sendet die Aufnahme an OpenAI, erhält den Text und fügt ihn an deinem Cursor ein.

Haki sichert deine Zwischenablage vor dem Einfügen und stellt sie danach wieder her, und das, ohne der App, in die du tippst, den Fokus zu nehmen. Eine kleine schwebende Anzeige zeigt, ob gerade aufgenommen, transkribiert oder fertig ist. Versehentliche Antipper, die kürzer als etwa eine Drittelsekunde sind, werden lokal verworfen.

## Sprachen und Modelle

- **Sprachen:** Arabisch (mit Optimierung für levantinisches und syrisches Sprechen), Englisch, Deutsch, Französisch oder automatische Erkennung.
- **Modelle:** `gpt-transcribe` ist der Standard und auf schnelles, latenzarmes Alltagsdiktat ausgelegt. `gpt-4o-transcribe` ist die genauere Option für komplexe Sätze, Dialekte und Fachbegriffe. Du wechselst in den Einstellungen oder in der Menüleiste.
- **Mikrofone:** Wähle das eingebaute Mikrofon, ein USB-Interface oder AirPods. Haki kümmert sich über CoreAudio um das Wiederverbinden und kann AirPods bevorzugen, sobald sie verbunden sind. Eine Pegelanzeige in Echtzeit lässt dich den Eingang testen.

## Datenschutz: was auf deinem Mac bleibt und was an OpenAI geht

Sei dir des Kompromisses bewusst: **Deine Sprachaufnahmen werden an OpenAI gesendet.** Laut README gehen sie direkt von deinem Mac über TLS an den Transkriptions-Endpunkt von OpenAI, ohne Zwischenserver. Das Diktat braucht daher eine Internetverbindung und deinen eigenen OpenAI-API-Schlüssel, genutzt nach den Bedingungen und Preisen von OpenAI.

Auf deinem Mac enthält Haki laut README keine Analytik, Diagnose, Absturzberichte oder SDKs von Dritten. Audio wird in temporäre Dateien aufgenommen und gelöscht, sobald die Transkription fertig ist oder fehlschlägt, es bleibt also kein Audioverlauf. Dein API-Schlüssel liegt im macOS-Schlüsselbund und nicht in Einstellungen, Konfigurationsdateien oder Protokollen.

## Berechtigungen

- **Mikrofon:** um deine Stimme aufzunehmen, und nur, solange du die Taste hältst oder das Diktat über das Menü startest.
- **Bedienungshilfen:** für die globale Push-to-Talk-Taste und zum Einfügen von Text durch simuliertes `⌘V`. Laut README ist „Eingabeüberwachung“ nicht zusätzlich nötig.

## Einrichten

1. Öffne Haki. Erlaube den Mikrofonzugriff, wenn macOS fragt, und aktiviere Haki unter Systemeinstellungen, „Datenschutz & Sicherheit“, „Bedienungshilfen“.
2. Öffne die Einstellungen über das Menüleisten-Symbol oder mit `⌘,`. Füge im Tab „Transcription“ deinen OpenAI-API-Schlüssel ein, wähle „Save“ und dann „Test API Key“.
3. Wähle ein Modell, und wähle im Tab „Audio“ dein Mikrofon.

## Vom iPhone diktieren mit AirMouse

[AirMouse](https://github.com/Alhamou/AirMouse) ist eine eigenständige Open-Source-App, die ein iPhone über dein lokales WLAN zum Trackpad für deinen Mac macht. Ihr Sprach-Tab nimmt auf dem Telefon auf und übergibt das Audio an Haki, das den Text auf deinem Mac eintippt. Haki muss installiert sein und laufen, und es nutzt deinen üblichen API-Schlüssel sowie deine Modell- und Spracheinstellungen.

Die Übergabe ist einfach und auch für andere Absender offen. Eine Aufnahme (`m4a`, `mp4`, `webm`, `wav`, `mp3` oder `ogg`, bis 25 MB) wird nach `~/Library/Caches/Haki/Inbox/` geschrieben, dann wird die URL `haki://transcribe?file=<Dateiname>` geöffnet. Haki transkribiert die Datei, fügt den Text ein und löscht die Datei. Es werden nur einfache Dateinamen im Posteingang akzeptiert, Pfade, versteckte Dateien und Symlinks werden also abgelehnt.

## Selbst bauen

Haki braucht macOS 13 Ventura oder neuer, auf Apple Silicon oder Intel, sowie die Xcode Command Line Tools mit Swift 6.0 oder neuer. Klone das Repository von GitHub, führe `swift test` und dann `./scripts/build_app.sh` aus. Das Skript baut die Release-Binärdatei, stellt `Haki.app` zusammen, signiert sie mit deinem lokalen Apple-Development-Zertifikat oder einer Ad-hoc-Signatur und installiert sie in `/Applications`.

## Open Source

Haki steht unter der MIT-Lizenz. Der Leitfaden zum Mitwirken verlangt keine lokalen Modelle, kein Python, kein Node.js und kein Electron und dass API-Schlüssel nie committet werden. Emad Alhamou, der Autor dieser Website, veröffentlicht Haki auf [GitHub](https://github.com/Alhamou/Haki). Fehlerberichte und Pull Requests sind willkommen, und Sicherheitsbedenken laufen über die Sicherheitsrichtlinie des Repositorys.

## Häufige Fragen

### Was ist Haki?

Haki ist eine Open-Source-macOS-Menüleisten-App für Push-to-Talk-Diktat. Halte `⌥ Option + Leertaste`, sprich und lass los, und der transkribierte Text wird in jeder App an deinem Cursor eingefügt. Es ist auf Arabisch abgestimmt und unterstützt auch Englisch, Deutsch und Französisch.

### Wie diktiere ich mit Haki?

Klicke in ein Textfeld, halte `⌥ Option + Leertaste` gedrückt, sprich und lass dann los. Haki sendet die Aufnahme an OpenAI und fügt den Text an deinem Cursor ein.

### Welche Sprachen und Modelle unterstützt Haki?

Arabisch (mit Optimierung für levantinisches und syrisches Sprechen), Englisch, Deutsch, Französisch und automatische Erkennung. Die Modelle sind `gpt-transcribe`, der Standard, und `gpt-4o-transcribe` für höhere Genauigkeit.

### Sendet Haki meine Stimme an OpenAI?

Ja. Die Transkription übernimmt OpenAI, daher wird jede Aufnahme von deinem Mac direkt über TLS an OpenAI gesendet. Haki löscht die temporäre Audiodatei, sobald die Transkription fertig ist oder fehlschlägt, und führt keinen Audioverlauf.

### Brauche ich einen OpenAI-API-Schlüssel?

Ja. Haki nutzt deinen eigenen OpenAI-API-Schlüssel, den es im macOS-Schlüsselbund speichert. Die Nutzung richtet sich nach den Bedingungen und Preisen von OpenAI.

### Welche Berechtigungen braucht Haki?

Mikrofon, um deine Stimme aufzunehmen, solange du die Taste hältst, und Bedienungshilfen, für die globale Taste und für das Einfügen mit simuliertem `⌘V`.

### Welche Macs und macOS-Versionen werden unterstützt?

macOS 13 Ventura oder neuer, auf Apple Silicon oder Intel. Zum Bauen braucht es Swift 6.0 oder neuer.

### Kann ich vom iPhone aus diktieren?

Ja, mit AirMouse, einer Open-Source-Begleit-App. Ihr Sprach-Tab nimmt auf dem Telefon auf, und Haki tippt den Text auf deinem Mac. Haki muss installiert sein und laufen.
