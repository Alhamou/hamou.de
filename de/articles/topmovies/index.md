# TopMovies: eine native Mac-App zum Entdecken von Filmen und Serien, mit lokaler Bibliothek

> TopMovies hilft dir zu entscheiden, was du auf deinem Mac schauen willst. Es bietet kuratierte Entdeckungs-Feeds wie „For You“, „Tonight“ und „Hidden Gems“, Filter nach Typ, Land, Jahr, Bewertung und Laufzeit sowie eine lokale Bibliothek für Favoriten, eine Merkliste und deine eigenen Bewertungen. Es funktioniert offline in einem Demo-Modus und verbindet sich mit TMDB für echte Daten. Es ist mit SwiftUI gebaut und offen unter der MIT-Lizenz.

- Author: [Emad Alhamou](https://hamou.de/), Founder & Product Builder
- Published: 2026-11-08 (updated 2026-11-08)
- Language: Deutsch
- Web page: https://hamou.de/de/articles/topmovies/
- Other languages: [English](https://hamou.de/articles/topmovies/index.md), [العربية](https://hamou.de/ar/articles/topmovies/index.md)
- Tool: [TopMovies](https://github.com/Alhamou/topMoves) · macOS 14 oder neuer · Apple Silicon oder Intel · TMDB-Token für Live-Daten · MIT-Lizenz
- Source code: https://github.com/Alhamou/topMoves (MIT license)

## Was ist TopMovies?

TopMovies ist eine native macOS-App zum Entdecken von Filmen und Serien, gebaut mit SwiftUI und Swift 6. Das README beschreibt sie als datenschutzorientiert: Deine Bibliothek bleibt auf deinem Mac, es gibt keine Abhängigkeiten von Dritten, und sie läuft in der Sandbox. Sie hat kuratierte Feeds, tiefe Filter, eine lokale Bibliothek und einen vollständigen Offline-Demo-Modus.

## Entdeckungs-Feeds

- **Discover:** Stöbere in weltweiten Katalogen über die großen Film- und Fernsehgenres.
- **For You:** deterministische Empfehlungen anhand deiner Lieblingsgenres und Bewertungen, ohne KI- oder Machine-Learning-Tracking.
- **Tonight:** eine zeitbegrenzte Auswahl, standardmäßig 120 Minuten, die Titel auslässt, die du schon gesehen hast.
- **Hidden Gems:** hoch bewertete Titel mit moderater Stimmenzahl.
- **Trending und Best New Releases:** was täglich und wöchentlich Aufmerksamkeit bekommt, mit verifizierter Zuschauerbeteiligung.

## Filter

Filtere nach Medientyp (All, Movies oder TV Shows), nach Originalsprache und regionalen Gruppierungen, nach Zeitraum, Jahr oder Jahrzehnt der Veröffentlichung sowie nach Mindestbewertung, Stimmenschwelle und Laufzeitgrenze. Die Inhaltsfilterung ist zurückhaltend: Explizite und nur für Erwachsene bestimmte Titel sind standardmäßig gesperrt.

## Deine Bibliothek bleibt auf deinem Mac

Favoriten, die Merkliste (Watchlist), gesehene Titel und deine persönlichen Bewertungen von 1 bis 10 Sternen werden lokal gespeichert. Die App läuft in der macOS-App-Sandbox, und dein TMDB-Token liegt im macOS-Schlüsselbund, nicht in einer Datei.

## Demo-Modus und Verbindung mit TMDB

TopMovies funktioniert sofort mit einem anschaulichen Offline-Katalog: erzeugte Plakatgrafiken, fiktive Handlungen, Besetzungen und Bewertungen. Um echte Filme und Serien zu sehen, verbindest du es mit TMDB, The Movie Database:

1. Lege ein TMDB-Konto an und beantrage in deinen Kontoeinstellungen einen API-Schlüssel für die nichtkommerzielle Nutzung.
2. Kopiere das API Read Access Token (das lange v4-Token, nicht den kurzen API-Schlüssel).
3. Öffne in TopMovies mit `⌘,` die „Settings & Sources“, füge das Token ein und wähle „Save & Connect“.

Entfernst du das Token, kehrt die App in den Demo-Modus zurück, ohne deine lokale Bibliothek oder Einstellungen zu löschen. TopMovies nutzt die TMDB-API, wird von TMDB aber weder unterstützt noch zertifiziert.

## Inhaltsfilterung

Laut README sind explizite und nur für Erwachsene bestimmte Titel, NC-17 und TV-MA standardmäßig ausgeschlossen, und Titel mit R-Einstufung bleiben verborgen, bis du sie in den Inhaltseinstellungen aktivierst.

## Kürzel

- `⌘F` fokussiert die Suchleiste und `⌘R` aktualisiert Katalog und Feeds.
- `⇧⌘F` blendet das Filterfeld ein oder aus und `⇧⌘0` setzt alle Filter zurück.
- `⌘,` öffnet „Settings & Sources“, und Escape schließt ein Detail- oder Einstellungsblatt.

## Installation

TopMovies braucht macOS 14 Sonoma oder neuer, auf Apple Silicon oder Intel. Das README verweist auf einen vorgebauten Review-Build im Repository, oder du baust es aus dem Quellcode: Klone das Repository, führe `swift test` und dann `./scripts/run-mac.sh` aus, das ein Release baut, lokal signiert und startet.

## Open Source

Der Anwendungscode und die originalen Demo-Grafiken stehen unter der MIT-Lizenz. TMDB-Markenzeichen, Anbieterdaten und Apple-Frameworks behalten ihre eigenen Bedingungen. Emad Alhamou, der Autor dieser Website, veröffentlicht TopMovies auf [GitHub](https://github.com/Alhamou/topMoves). Das Repository hat Hinweise zum Mitwirken, einen Verhaltenskodex und eine Sicherheitsrichtlinie.

## Häufige Fragen

### Was ist TopMovies?

TopMovies ist eine native Open-Source-macOS-App zum Entdecken von Filmen und Serien. Sie hat kuratierte Feeds, Filter, eine lokale Bibliothek und einen Offline-Demo-Modus und ist mit SwiftUI gebaut.

### Welche Entdeckungs-Feeds gibt es?

Discover, For You, Tonight, Hidden Gems sowie Trending und Best New Releases. „For You“ ist deterministisch und nutzt weder KI noch Machine Learning, und „Tonight“ lässt dich nach der Zeit wählen, die du hast.

### Brauche ich ein Konto, um es zu benutzen?

Nicht zum Ausprobieren. Es funktioniert sofort in einem Offline-Demo-Modus. Um echte Filme und Serien zu sehen, verbindest du es mit einem TMDB API Read Access Token.

### Wie verbinde ich TMDB?

Lege ein TMDB-Konto an, beantrage einen API-Schlüssel für die nichtkommerzielle Nutzung, kopiere das API Read Access Token, öffne mit `⌘,` die „Settings & Sources“, füge das Token ein und wähle „Save & Connect“.

### Wo werden meine Favoriten und Bewertungen gespeichert?

Auf deinem Mac. Favoriten, die Merkliste, gesehene Titel und deine Bewertungen von 1 bis 10 Sternen werden lokal gespeichert, und dein TMDB-Token liegt im macOS-Schlüsselbund.

### Filtert TopMovies Inhalte für Erwachsene?

Ja. Explizite und nur für Erwachsene bestimmte Titel, NC-17 und TV-MA sind standardmäßig ausgeschlossen, und Titel mit R-Einstufung bleiben verborgen, bis du sie in den Inhaltseinstellungen aktivierst.

### Welche Macs und macOS-Versionen werden unterstützt?

macOS 14 Sonoma oder neuer, auf Apple Silicon oder Intel.

### Ist TopMovies mit TMDB verbunden?

Nein. Es nutzt die TMDB-API, wird von TMDB aber weder unterstützt noch zertifiziert.
