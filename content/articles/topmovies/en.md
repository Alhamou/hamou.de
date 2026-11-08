---
title: TopMovies: a native Mac app to discover movies and TV series, with a local library
short_title: TopMovies
seo_title: TopMovies: native Mac app to discover movies and TV series
description: TopMovies is an open-source native macOS app for discovering movies and TV series, with curated feeds, filters, a local library and an offline demo mode.
kicker: Open source tool
dek: TopMovies helps you decide what to watch on your Mac. It has curated discovery feeds such as For You, Tonight and Hidden Gems, filters across type, country, year, score and runtime, and a local library for favorites, a watchlist and your own ratings. It works offline in a demo mode and connects to TMDB for real data. It is built with SwiftUI and open under the MIT license.
keywords: TopMovies, movie discovery app Mac, TV series tracker macOS, what to watch tonight, hidden gems movies, TMDB API, watchlist app Mac, SwiftUI, native macOS app, Swift, MIT license
product_line: Open-source native macOS app for discovering movies and TV series: curated feeds, filters, a local library and an offline demo mode. Uses the TMDB API.
requirements: macOS 14 or later · Apple silicon or Intel · TMDB token for live data · MIT license
---

## What is TopMovies?

TopMovies is a native macOS app for discovering movies and TV series, built with SwiftUI and Swift 6. Its README describes it as privacy-first: your library stays on your Mac, it has no third-party dependencies, and it runs sandboxed. It has curated feeds, deep filters, a local library and a complete offline demo mode.

## Discovery feeds

- **Discover:** browse worldwide catalogs across the major film and television genres.
- **For You:** deterministic recommendations based on your favorite genres and ratings, with no AI or machine-learning tracking.
- **Tonight:** a time-bounded picker, 120 minutes by default, that leaves out titles you have already watched.
- **Hidden Gems:** highly rated titles with a moderate number of votes.
- **Trending and Best New Releases:** what is getting attention daily and weekly, with verified audience participation.

## Filters

Filter by media type (All, Movies or TV Shows), by origin language and regional groupings, by release date range, year or decade, and by minimum audience score, vote threshold and runtime cap. Content filtering is conservative: explicit and adult titles are blocked by default.

## Your library stays on your Mac

Favorites, the Watchlist, Watched items and your personal 1 to 10 star ratings are stored locally. The app runs in the macOS App Sandbox, and your TMDB token is kept in the macOS Keychain, not in a file.

## Demo mode and connecting TMDB

TopMovies works right away with an illustrative offline catalog: generated poster artwork, fictional plots, casts and scores. To see real movies and series, connect it to TMDB, The Movie Database:

1. Create a TMDB account and request an API key for noncommercial use in your account settings.
2. Copy the API Read Access Token (the long v4 token, not the short API key).
3. In TopMovies open Settings & Sources with `⌘,`, paste the token and choose Save & Connect.

Removing the token returns the app to Demo Mode without wiping your local library or preferences. TopMovies uses the TMDB API but is not endorsed or certified by TMDB.

## Content filtering

According to the README, explicit and adult titles, NC-17 and TV-MA are excluded by default, and R-rated titles stay hidden unless you enable them in the content preferences.

## Shortcuts

- `⌘F` focuses the search bar and `⌘R` refreshes the catalog and feeds.
- `⇧⌘F` toggles the filter panel and `⇧⌘0` resets all filters.
- `⌘,` opens Settings & Sources and Escape dismisses a detail or settings sheet.

## Install

TopMovies needs macOS 14 Sonoma or later, on Apple silicon or Intel. The README points to a prebuilt review build in the repository, or you can build it from source: clone the repository, run `swift test`, then `./scripts/run-mac.sh`, which builds a release, signs it locally and launches it.

## Open source

The application code and the original demo artwork are released under the MIT license. TMDB branding, provider data and Apple frameworks keep their own terms. Emad Alhamou, the author of this site, publishes TopMovies on [GitHub](https://github.com/Alhamou/topMoves). The repository has contribution guidelines, a code of conduct and a security policy.

<!-- faq -->
## Frequently asked questions

### What is TopMovies?

TopMovies is an open-source native macOS app for discovering movies and TV series. It has curated feeds, filters, a local library and an offline demo mode, and it is built with SwiftUI.

### What discovery feeds does it have?

Discover, For You, Tonight, Hidden Gems, and Trending and Best New Releases. For You is deterministic and uses no AI or machine learning, and Tonight lets you pick by how much time you have.

### Do I need an account to use it?

Not to try it. It works immediately in an offline demo mode. To see real movies and series you connect it with a TMDB API Read Access Token.

### How do I connect TMDB?

Create a TMDB account, request an API key for noncommercial use, copy the API Read Access Token, open Settings & Sources with `⌘,`, paste the token and choose Save & Connect.

### Where are my favorites and ratings stored?

On your Mac. Favorites, the Watchlist, Watched items and your 1 to 10 star ratings are stored locally, and your TMDB token is kept in the macOS Keychain.

### Does TopMovies filter adult content?

Yes. Explicit and adult titles, NC-17 and TV-MA are excluded by default, and R-rated titles stay hidden unless you enable them in the content preferences.

### Which Macs and macOS versions are supported?

macOS 14 Sonoma or later, on Apple silicon or Intel.

### Is TopMovies affiliated with TMDB?

No. It uses the TMDB API but is not endorsed or certified by TMDB.
