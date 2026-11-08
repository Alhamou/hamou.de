# SafeShare: private Apps beim Teilen deines Mac-Bildschirms in Teams, Zoom oder Meet verbergen

> SafeShare löst ein Dilemma beim Bildschirmteilen: den ganzen Bildschirm teilen und private Chats und Benachrichtigungen riskieren, oder ein Fenster teilen und auf Multitasking verzichten. Es baut ein gefiltertes Safe-View-Fenster, das die von dir geschützten Apps auslässt. Dieses Fenster teilst du in Teams, Zoom oder Meet, und auf deinem echten Desktop arbeitest du weiter. Der Code ist offen unter der MIT-Lizenz.

- Author: [Emad Alhamou](https://hamou.de/), Founder & Product Builder
- Published: 2026-11-08 (updated 2026-11-08)
- Language: Deutsch
- Web page: https://hamou.de/de/articles/safeshare/
- Other languages: [English](https://hamou.de/articles/safeshare/index.md), [العربية](https://hamou.de/ar/articles/safeshare/index.md)
- Tool: [SafeShare](https://github.com/Alhamou/SafeShare) · macOS 14 oder neuer · Berechtigung „Bildschirm- und Systemaudioaufnahme“ · MIT-Lizenz
- Source code: https://github.com/Alhamou/SafeShare (MIT license)

## Was ist SafeShare?

SafeShare (auch ScreenGuard genannt) ist ein Open-Source-Dienstprogramm für macOS für alle, die ihren Desktop in Remote-Meetings zeigen. Es verbirgt die Apps und Fenster, die du als privat markierst, vor dem, was das Meeting sieht, während du auf deinem echten Bildschirm ganz normal weiterarbeitest.

## Das Problem, das es löst

Wenn du von einem Mac aus präsentierst, hat jede der eingebauten Möglichkeiten ihren Preis. Teilst du den ganzen Bildschirm, können ein privater Chat, ein Passwortmanager, ein Posteingang oder eine Benachrichtigung ins Meeting gelangen. Teilst du ein einzelnes Anwendungsfenster, kannst du nicht mehr zwischen Apps wechseln oder einen Ablauf zeigen, der mehrere Apps durchquert.

## So funktioniert es

SafeShare ergänzt eine dritte Möglichkeit, eine gefilterte Vorschau namens **Safe View**:

1. Es nimmt deinen Bildschirm mit Apples ScreenCaptureKit auf.
2. Es entfernt mit einem Inhaltsfilter die Apps und Fenster, die du schützt, aus dieser Aufnahme.
3. Es zeigt den bereinigten Desktop in einem eigenen Fenster, Safe View.
4. In Teams, Zoom oder Google Meet teilst du das Safe-View-Fenster statt deines Bildschirms.

Du siehst auf deinem echten Desktop alles. Die Teilnehmenden sehen nur, was du erlaubst.

## Mit Teams, Zoom oder Meet nutzen

Öffne zuerst SafeShare über das Schild-Symbol in der Menüleiste, markiere die sensiblen Apps als geschützt und wähle „Start Safe View“ (solange das SafeShare-Fenster offen ist, schaltet `⌘⇧S` es um). Dann in deiner Meeting-App (die Beschriftungen stehen hier wie im README auf Englisch und heißen in deutscher Oberfläche etwas anders):

- **Microsoft Teams:** Wähle „Share“, dann unter „Window“ die Option „SafeShare — Safe View“.
- **Zoom:** Wähle „Share Screen“, nimm in der Liste das Fenster „SafeShare — Safe View“ und wähle „Share“.
- **Google Meet:** Wähle „Present now“, dann „A window“, und nimm „SafeShare — Safe View“.

Teilst du statt des Safe-View-Fensters deinen ganzen Bildschirm, wird nichts gefiltert. Wähle also immer das Fenster.

## Das Safe-View-Fenster groß halten

Meeting-Apps teilen ein Fenster in seiner Größe auf dem Bildschirm, ein in eine Ecke geschrumpftes Safe-View-Fenster ist für die Teilnehmenden daher unlesbar. Laut README sperrt SafeShare das Fenster auf das Seitenverhältnis des Displays, geht nicht unter die halbe Displaygröße und zeigt beim Verkleinern einen Hinweis mit der genauen Auflösung, die die Zuschauenden erhalten. Die Schaltfläche „Send to Back“ im Menü legt das Fenster in voller Größe hinter deine Arbeit, und der Strom läuft weiter, solange das Fenster verdeckt ist.

## Was es kann

- **Schutz mit einem Klick:** Schalte jede laufende App in der Menüleiste auf geschützt.
- **Steuerung pro Fenster und Instanz:** Gruppiere Apps mit mehreren Fenstern, etwa einen Browser oder ein Terminal, und setze jedes Fenster auf „Visible“, „Protected“ oder „Inherit“.
- **Fail-closed-Abdunkelung:** Der Strom wird bei Bildschirmsperre, Ruhezustand oder einer Änderung der Berechtigungen leer, sodass kein Bild durchsickert.
- **Mehrere Displays:** Wähle, welches physische Display aufgenommen wird.
- **Stromqualität:** Wechsle zwischen 15, 30 und 60 Bildern pro Sekunde, ohne den Strom neu zu starten.
- **Benachrichtigungen automatisch ausblenden:** Banner der Mitteilungszentrale bleiben aus dem Strom heraus.
- **Beim Anmelden starten, VoiceOver-Beschriftungen und Tastenkürzel.**

## Datenschutz und Berechtigungen

SafeShare braucht eine einzige Berechtigung, den üblichen Zugriff auf Bildschirm- und Systemaudioaufnahme, ohne Root-Rechte und ohne Kernel-Erweiterungen. Laut README speichert es keine Videobilder oder Fenstertitel auf dem Datenträger, hat keine Telemetrie und macht keine Netzwerkaufrufe. Das Repository enthält eine Sicherheitsrichtlinie mit den Einzelheiten.

## Installation

SafeShare braucht macOS 14 Sonoma oder neuer. Lade das DMG vom neuesten Release auf GitHub herunter, öffne es und ziehe SafeShare in den Ordner „Programme“. Zum Selbstbauen brauchst du Xcode 15 oder neuer: Klone das Repository, führe `swift test` und dann `./scripts/build_app.sh` aus, und `./scripts/package_dmg.sh`, wenn du ein DMG willst.

## Open Source

SafeShare steht unter der MIT-Lizenz. Emad Alhamou, der Autor dieser Website, veröffentlicht es auf [GitHub](https://github.com/Alhamou/SafeShare). Das Repository hat einen Continuous-Integration-Workflow. Fehlerberichte und Pull Requests sind willkommen.

## Häufige Fragen

### Was ist SafeShare?

SafeShare ist ein Open-Source-Dienstprogramm für macOS, das private Apps und Fenster verbirgt, während du deinen Bildschirm in Teams, Zoom oder Google Meet teilst. Es tut das über ein gefiltertes Vorschaufenster namens Safe View.

### Wie verbirgt SafeShare Apps beim Bildschirmteilen?

Es nimmt deinen Bildschirm mit ScreenCaptureKit auf, filtert die Apps und Fenster heraus, die du als geschützt markiert hast, und zeigt das Ergebnis im Safe-View-Fenster. Dieses Fenster teilst du in deiner Meeting-App statt deines ganzen Bildschirms.

### Funktioniert es mit Teams, Zoom und Google Meet?

Ja. In jedem davon teilst du das Fenster „SafeShare — Safe View“: in Teams über „Share“ und „Window“, in Zoom über „Share Screen“ und in Google Meet über „Present now“ und „A window“.

### Was, wenn ich meinen ganzen Bildschirm statt des Safe-View-Fensters teile?

Dann wird nichts gefiltert, und die Teilnehmenden sehen alles. Der Schutz gilt nur für das, was im Safe-View-Fenster erscheint. Wähle in deiner Meeting-App also immer dieses Fenster.

### Warum sollte das Safe-View-Fenster groß bleiben?

Meeting-Apps teilen ein Fenster in seiner Größe auf dem Bildschirm, ein winziges Fenster ist daher schwer lesbar. SafeShare behält das Seitenverhältnis des Displays, geht nicht unter die halbe Displaygröße und hat eine Schaltfläche „Send to Back“, die das Fenster in voller Größe aus dem Weg räumt.

### Welche Berechtigung braucht SafeShare, und sendet es Daten irgendwohin?

Es braucht den Zugriff auf Bildschirm- und Systemaudioaufnahme. Laut README hat es keine Telemetrie, macht keine Netzwerkaufrufe und speichert keine Videobilder oder Fenstertitel auf dem Datenträger.

### Was passiert, wenn der Bildschirm gesperrt wird oder der Mac in den Ruhezustand geht?

Der Strom wird bei Bildschirmsperre, Ruhezustand und Änderungen der Berechtigungen leer, was das README Fail-closed-Abdunkelung nennt. Banner der Mitteilungszentrale bleiben ebenfalls aus dem Strom heraus.

### Welche macOS-Version braucht SafeShare?

macOS 14 Sonoma oder neuer.
