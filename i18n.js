/* Language: Arabic is the page source; English and German are applied here.
   Order of choice: ?lang= in the URL, then the visitor's saved pick, then the browser languages, then English. */
(function () {
  var SUPPORTED = ['ar', 'en', 'de'];
  var STORE = 'hamou-lang';
  var root = document.documentElement;
  var T = {
 "en": {
  "skip": "Skip to content",
  "nav.about": "About",
  "nav.takecar": "TakeCar",
  "nav.nadhif": "Nadhif",
  "nav.arab": "Arab Solutions",
  "nav.shfli": "Shfli",
  "nav.oss": "Open source",
  "nav.cta": "Let's talk",
  "hero.eyebrow": "<i></i> Founder <span class=\"sep\">·</span> Product builder <span class=\"sep\">·</span> Tech entrepreneur",
  "hero.h1": "I build technology<br>that solves <em>real problems.</em>",
  "hero.lead": "I'm Emad Alhamou, founder of <strong>TakeCar</strong>, <strong>Arab Solutions</strong> and <strong>Shfli</strong>. I work where technology, operations and market insight meet, turning complex ideas into simple products people use every day.",
  "hero.cta": "Explore my journey",
  "hero.more": "More about me",
  "idea.no": "01 / The idea",
  "idea.quote": "Good technology doesn't show off its complexity.<br><span>It makes people's lives simpler.</span>",
  "about.label": "About",
  "about.h2": "Between Germany and Syria,<br>with one vision.",
  "about.p1": "A Syrian-German entrepreneur who loves building digital products for real-world challenges: mobility, maps, operational systems and user experience.",
  "about.p2": "To me a product is more than a nice interface. I care about everything behind it: infrastructure, data, performance, costs and user trust. I learn fast, test in the market, then build better.",
  "about.based": "Germany · Syria",
  "tc.label": "Flagship project",
  "tc.h2": "TakeCar",
  "tc.en": "TakeCar — Syrian mobility, built from the ground up.",
  "tc.h3": "A Syrian mobility platform<br>with global ambition.",
  "tc.p": "TakeCar brings riders and drivers together in one simple experience. Designed for the Syrian market, with a focus on flexibility, ease of use and locally owned technology.",
  "tc.f1": "One experience for riders and drivers",
  "tc.f2": "Flexible pricing and live offers",
  "tc.f3": "Maps and routing tuned for the local market",
  "tc.f4": "Infrastructure built to scale",
  "tc.cta": "Visit TakeCar",
  "tc.play": "Play the TakeCar video",
  "tc.videoCap": "A short video about TakeCar, in Arabic. The video loads from YouTube only when you press play.",
  "tc.article": "Read the full article",
  "nd.status": "<i></i> In development · Sep 2026 — present",
  "nd.label": "Latest project",
  "nd.h2": "Nadhif",
  "nd.tagline": "A cleaner Mac,<br>safer servers and websites.",
  "nd.h3": "A Mac app that cleans calmly, gives developers their own tools and protects your website and server from hackers.",
  "nd.p1": "I'm building Nadhif for Alhamou as a native macOS app. It scans and explains before it deletes: every category comes with a line on what it is and why removing it is safe, and everything cleaned moves to “Recently Cleaned”, where it can be restored for seven days.",
  "nd.p2": "Beyond cleaning, it includes an uninstaller, developer tools, and security checks for your Mac, for Debian and Ubuntu servers over SSH, and for the websites you own. Your personal files are off limits, it collects no data, and your reports stay on your Mac.",
  "nd.f1": "Safe cleaning you can undo for seven days",
  "nd.f2": "Developer tools: Xcode, simulators, node_modules, Homebrew and Docker",
  "nd.f3": "Security checks for Macs, servers and websites",
  "nd.cta": "Visit Nadhif",
  "as.status": "<i></i> In development · since April 2026",
  "as.label": "Current project",
  "as.h2": "Arab Solutions",
  "as.tagline": "Smarter customer support,<br>built for the Arab world.",
  "as.h3": "An AI customer support platform that brings knowledge and channels into one place.",
  "as.p1": "I'm building Arab Solutions as an Arabic-first SaaS platform that helps companies turn their content and knowledge base into a smart assistant that understands customer questions and gives accurate, consistent answers.",
  "as.p2": "The platform supports multichannel conversations, knowledge management and RAG, with special attention to Arabic, privacy, and easy integration with apps and websites.",
  "as.f1": "A smart assistant built on company knowledge",
  "as.f2": "Arabic-first support and unified channels",
  "as.f3": "Flexible integration via web, apps and APIs",
  "as.cta": "Visit Arab Solutions",
  "sh.status": "<i></i> Completed · 2025.2 — 2026.4",
  "sh.label": "Pioneering project",
  "sh.h2": "Shfli",
  "sh.tagline": "A complete online marketplace,<br>connecting people and opportunities in Syria.",
  "sh.h3": "An all-in-one platform for buying, selling and auctions, bringing deals and opportunities into one place.",
  "sh.p1": "I led the tech team and built the backend systems for the Shfli platform and app, Syria's first advanced interactive marketplace, connecting sellers and buyers across cars, real estate, live auctions, bazaars and jobs.",
  "sh.p2": "The cloud infrastructure and REST APIs were designed for very fast performance and 99.9% uptime, with routing and maps tuned to the Syrian market.",
  "sh.f1": "Multi-category marketplace with live auctions and bazaars",
  "sh.f2": "Local maps and a tailored experience on mobile and web",
  "sh.f3": "Fast cloud infrastructure and advanced APIs",
  "sh.cta": "Visit Shfli",
  "oss.h2": "Tools I made,<br>open to anyone who builds with me.",
  "oss.p": "Eight native Mac apps. Small, private, and written because I need them every day. The code is open and contributions are welcome: from a one-line bug fix to an idea that grows with the team.",
  "ob.p": "An open-source ad blocker for Safari on Mac. It downloads real filter lists and converts them into Safari's native rule format, then hands them to the browser, which compiles them with its own engine: nothing sits between you and the web, and nothing is sent anywhere. It lives in the menu bar and refreshes the lists automatically every 24 hours.",
  "ob.b": "<span>Inside</span> Four Safari content blockers with a 150,000-rule budget each, AdGuard, EasyList and EasyPrivacy lists or any URL you add, personal rules and an allowlist, and a web extension for scriptlets and extended CSS that content blockers can't express.",
  "rd.p": "Control one Mac from another over your local network with near-zero latency and no third-party relay. Live, high-resolution screen streaming with full hardware acceleration, precise mouse and keyboard input, and clipboard sync.",
  "rd.b": "<span>Inside</span> Hardware H.264 encoding via VideoToolbox and ScreenCaptureKit, full shortcut capture, and automatic discovery over Bonjour.",
  "pf.p": "Colorful sticky notes that live in the Mac menu bar. Arabic is written right to left and English left to right, and the pin keeps a note above your windows without covering the menu bar. No account, no cloud: what you write stays on your Mac.",
  "pf.b": "<span>Inside</span> Light and dark colors, a lock that prevents editing and closing, and shortcuts for quick writing.",
  "ca.p": "One button closes your Mac apps all at once. You see each app's icon before it closes and keep open what you want. Finder stays running, and your choice is saved for next time.",
  "ca.b": "<span>Inside</span> Force quit for regular apps, an exclusion list, and no network or tracking.",
  "ss.p": "When you share your screen in Teams, Zoom or Meet, it hides the apps and windows you don't want seen. You work with your full desktop, while attendees see only the version you allow.",
  "ss.b": "<span>Inside</span> Protection per app and window, fast local streaming, and hidden notifications. Works offline.",
  "tm.p": "A calm place to discover movies and series on the Mac. Browse, pick what suits your night, and keep your library and ratings with you. Without an API key, a full demo mode works.",
  "tm.b": "<span>Inside</span> Categories and recommendations, a local library, and the API key kept in the Keychain.",
  "mm.p": "Moves the pointer at a rhythm you set: for a presentation, for testing, or to keep the Mac awake during a long task. Start, stop or move now from the menu bar.",
  "mm.b": "<span>Inside</span> Intervals from seconds to minutes, two movement patterns, an optional click, and no sleep while running.",
  "hk.h3": "Haki",
  "hk.p": "Talk, and Haki types. Press and hold, speak in your own dialect, then let go: the text appears at the cursor, in any app. Designed for Arabic and Levantine, and it understands English, German and French.",
  "hk.b": "<span>Inside</span> Voice dictation, a global shortcut, and the key kept in the Keychain. Recordings are not saved.",
  "oss.repo": "Repository",
  "oss.contrib": "Contribute",
  "inv.label": "Join the team",
  "inv.h3": "Let's build it together.",
  "inv.p": "Contributing here isn't only about code. A clearer idea, a sharper translation, a test on your machine, or a small fix: all of it has a place on the team. Open “Contribute” on the project you like, then send your request. Anyone who wants to join is welcome.",
  "inv.cta": "My GitHub profile",
  "work.label": "How I work",
  "work.h2": "From idea<br>to working product.",
  "work.p": "I combine business thinking with technical execution. That lets me see the whole picture, then go down to the details that make the difference.",
  "work.c1h": "I understand the problem",
  "work.c1p": "I start with the user and the market, not the technology. I look for the real problem and what makes a solution useful and able to grow.",
  "work.c2h": "I build the system",
  "work.c2p": "I turn the vision into a complete product: apps, interfaces, backend services, maps, data and operational systems.",
  "work.c3h": "I learn and improve",
  "work.c3p": "I watch real usage, remove points of friction, and keep improving the product based on clear impact on people and the business.",
  "car.label": "Career",
  "car.h2": "More than 10 years<br>building technology.",
  "car.p": "Hands-on experience in Germany and Syria, from building independent products to leading systems and tech teams.",
  "car.t1": "2020 — present",
  "car.t2": "Sep 2026 — present",
  "car.t3": "Apr 2026 — present",
  "car.ibykus": "IBYKUS AG / WIBank · Erfurt, Germany",
  "car.nadhif": "Mac cleaning and security app, in development",
  "car.arab": "Arabic AI customer support platform",
  "car.shfli": "E-commerce and classifieds platform in Syria (shfli.com)",
  "car.tc": "Building and running a complete Syrian mobility platform",
  "car.ps": "E-commerce SaaS platform",
  "car.fs": "Enterprise and freelance projects · Germany and Syria",
  "ct.label": "What's next",
  "ct.h2": "Building for the future,<br><em>one real step every day.</em>",
  "ct.p": "Interested in smart mobility, AI, and digital products that serve emerging markets.",
  "ct.mail": "Email me",
  "ct.arab": "Discover Arab Solutions",
  "aria.nav": "Main navigation",
  "aria.home": "Home",
  "aria.mono": "EA monogram for Emad Alhamou",
  "lang.label": "Language",
  "aria.details": "Details: ",
  "meta.title": "Emad Alhamou | Founder & Product Builder",
  "meta.desc": "Founder & Builder of TakeCar, Shfli, and Arab Solutions. Building technology products for mobility, marketplaces, AI-powered customer support, and emerging markets.",
  "nav.articles": "Articles",
  "nd.play": "Play the Nadhif video",
  "nd.videoCap": "An animated tour of Nadhif. The video loads from YouTube only when you press play.",
  "nd.article": "Read the full article",
  "art.label": "Articles",
  "art.h2": "Stories behind<br>the products.",
  "art.p": "An article for every project and tool I build: what it does, why I built it, and how it works.",
  "art.all": "All articles"
 },
 "de": {
  "skip": "Zum Inhalt springen",
  "nav.about": "Über mich",
  "nav.takecar": "TakeCar",
  "nav.nadhif": "Nadhif",
  "nav.arab": "Arab Solutions",
  "nav.shfli": "Shfli",
  "nav.oss": "Open Source",
  "nav.cta": "Kontakt",
  "hero.eyebrow": "<i></i> Gründer <span class=\"sep\">·</span> Produktentwickler <span class=\"sep\">·</span> Tech-Unternehmer",
  "hero.h1": "Ich baue Technologie,<br>die <em>echte Probleme</em> löst.",
  "hero.lead": "Ich bin Emad Alhamou, Gründer von <strong>TakeCar</strong>, <strong>Arab Solutions</strong> und <strong>Shfli</strong>. Ich arbeite an der Schnittstelle von Technologie, Betrieb und Marktverständnis und mache aus komplexen Ideen einfache Produkte, die Menschen jeden Tag nutzen.",
  "hero.cta": "Meine Reise entdecken",
  "hero.more": "Mehr über mich",
  "idea.no": "01 / Die Idee",
  "idea.quote": "Gute Technologie stellt ihre Komplexität nicht zur Schau.<br><span>Sie macht das Leben der Menschen einfacher.</span>",
  "about.label": "Über mich",
  "about.h2": "Zwischen Deutschland und Syrien,<br>mit einer Vision.",
  "about.p1": "Syrisch-deutscher Unternehmer mit Leidenschaft für digitale Produkte, die echte Herausforderungen lösen: Mobilität, Karten, operative Systeme und Nutzererlebnis.",
  "about.p2": "Ein Produkt ist für mich mehr als eine schöne Oberfläche. Mir ist wichtig, was dahinter steckt: Infrastruktur, Daten, Performance, Kosten und das Vertrauen der Nutzer. Ich lerne schnell, teste am Markt und baue es dann besser.",
  "about.based": "Deutschland · Syrien",
  "tc.label": "Hauptprojekt",
  "tc.h2": "TakeCar",
  "tc.en": "TakeCar — syrische Mobilität, von Grund auf neu gebaut.",
  "tc.h3": "Eine syrische Mobilitätsplattform<br>mit globalem Anspruch.",
  "tc.p": "TakeCar bringt Fahrgäste und Fahrer in einer einfachen App zusammen. Entwickelt für den syrischen Markt, mit Fokus auf Flexibilität, einfache Bedienung und lokal verankerte Technologie.",
  "tc.f1": "Eine App für Fahrgäste und Fahrer",
  "tc.f2": "Flexible Preise und Live-Angebote",
  "tc.f3": "Karten und Routing für den lokalen Markt optimiert",
  "tc.f4": "Skalierbare technische Basis",
  "tc.cta": "TakeCar besuchen",
  "tc.play": "TakeCar-Video abspielen",
  "tc.videoCap": "Ein kurzes Video zu TakeCar, auf Arabisch. Das Video wird erst beim Abspielen von YouTube geladen.",
  "tc.article": "Ganzen Artikel lesen",
  "nd.status": "<i></i> In Entwicklung · Sept. 2026 — heute",
  "nd.label": "Neuestes Projekt",
  "nd.h2": "Nadhif",
  "nd.tagline": "Ein aufgeräumter Mac,<br>sicherere Server und Websites.",
  "nd.h3": "Eine Mac-App, die in Ruhe aufräumt, Entwicklern eigene Tools gibt und deine Website und deinen Server vor Hackern schützt.",
  "nd.p1": "Ich entwickle Nadhif für Alhamou als native macOS-App. Sie prüft und erklärt, bevor sie löscht: Jede Kategorie sagt in einer Zeile, was sie ist und warum das Entfernen sicher ist, und alles Bereinigte landet in „Zuletzt bereinigt“, wo es sieben Tage lang wiederhergestellt werden kann.",
  "nd.p2": "Neben dem Aufräumen bietet sie ein Deinstallationsprogramm, Entwickler-Tools und Sicherheitsprüfungen für deinen Mac, für Debian- und Ubuntu-Server per SSH und für deine eigenen Websites. Persönliche Dateien bleiben tabu, es werden keine Daten gesammelt, und deine Berichte bleiben auf deinem Mac.",
  "nd.f1": "Sicheres Aufräumen, sieben Tage lang umkehrbar",
  "nd.f2": "Entwickler-Tools: Xcode, Simulatoren, node_modules, Homebrew und Docker",
  "nd.f3": "Sicherheitsprüfung für Mac, Server und Websites",
  "nd.cta": "Nadhif besuchen",
  "as.status": "<i></i> In Entwicklung · seit April 2026",
  "as.label": "Aktuelles Projekt",
  "as.h2": "Arab Solutions",
  "as.tagline": "Intelligenter Kundensupport,<br>gemacht für die arabische Welt.",
  "as.h3": "Eine KI-Plattform für Kundensupport, die Wissen und Kanäle an einem Ort vereint.",
  "as.p1": "Ich baue Arab Solutions als Arabic-first-SaaS-Plattform, die Unternehmen hilft, ihre Inhalte und Wissensdatenbank in einen intelligenten Assistenten zu verwandeln, der Kundenfragen versteht und präzise, konsistente Antworten gibt.",
  "as.p2": "Die Plattform unterstützt Gespräche über mehrere Kanäle, Wissensmanagement und RAG, mit besonderem Fokus auf Arabisch, Datenschutz und einfache Integration in Apps und Websites.",
  "as.f1": "Intelligenter Assistent auf Basis des Unternehmenswissens",
  "as.f2": "Arabisch zuerst, mit einheitlichen Kanälen",
  "as.f3": "Flexible Integration über Web, Apps und APIs",
  "as.cta": "Arab Solutions besuchen",
  "sh.status": "<i></i> Abgeschlossen · 2025.2 — 2026.4",
  "sh.label": "Pionierprojekt",
  "sh.h2": "Shfli",
  "sh.tagline": "Ein umfassender Online-Marktplatz,<br>der Menschen und Chancen in Syrien verbindet.",
  "sh.h3": "Eine Plattform für Kaufen, Verkaufen und Auktionen, die Geschäfte und Chancen an einem Ort bündelt.",
  "sh.p1": "Ich habe das Tech-Team geleitet und die Backend-Systeme für Plattform und App von Shfli gebaut, dem ersten fortschrittlichen interaktiven Marktplatz Syriens. Er verbindet Verkäufer und Käufer in den Bereichen Autos, Immobilien, Live-Auktionen, Basare und Jobs.",
  "sh.p2": "Cloud-Infrastruktur und REST-APIs wurden für sehr hohe Geschwindigkeit und 99,9 % Verfügbarkeit ausgelegt, mit Routing und Karten, die auf den syrischen Markt abgestimmt sind.",
  "sh.f1": "Marktplatz mit vielen Kategorien, Live-Auktionen und Basaren",
  "sh.f2": "Lokale Karten und ein angepasstes Erlebnis für Mobil und Web",
  "sh.f3": "Schnelle Cloud-Infrastruktur und moderne APIs",
  "sh.cta": "Shfli besuchen",
  "oss.h2": "Werkzeuge, die ich gebaut habe,<br>offen für alle, die mitbauen.",
  "oss.p": "Acht native Mac-Apps. Klein, privat und geschrieben, weil ich sie jeden Tag brauche. Der Code ist offen, Beiträge sind willkommen: von einer Zeile, die einen Fehler behebt, bis zu einer Idee, die mit dem Team wächst.",
  "ob.p": "Ein Open-Source-Werbeblocker für Safari auf dem Mac. Er lädt echte Filterlisten, wandelt sie in Safaris natives Regelformat um und übergibt sie dem Browser, der sie mit seiner eigenen Engine kompiliert: Nichts steht zwischen dir und dem Web, und nichts wird irgendwohin gesendet. Er lebt in der Menüleiste und aktualisiert die Listen automatisch alle 24 Stunden.",
  "ob.b": "<span>Inhalt</span> Vier Safari-Inhaltsblocker mit je 150.000 Regeln, Listen von AdGuard, EasyList und EasyPrivacy oder jede eigene URL, persönliche Regeln und eine Zulassungsliste sowie eine Web-Erweiterung für Scriptlets und erweitertes CSS, das Inhaltsblocker nicht abbilden können.",
  "rd.p": "Steuere einen Mac von einem anderen über dein lokales Netzwerk, mit nahezu null Latenz und ohne externen Vermittler. Live-Bildschirmübertragung in hoher Auflösung mit voller Hardwarebeschleunigung, präzise Maus- und Tastatureingaben und Abgleich der Zwischenablage.",
  "rd.b": "<span>Inhalt</span> H.264-Hardwarekodierung über VideoToolbox und ScreenCaptureKit, vollständige Erfassung von Tastenkürzeln und automatische Erkennung per Bonjour.",
  "pf.p": "Bunte Haftnotizen in der Menüleiste des Mac. Arabisch wird von rechts nach links geschrieben, Englisch von links nach rechts, und die Pinnadel hält eine Notiz über den Fenstern, ohne die Menüleiste zu verdecken. Kein Konto, keine Cloud: Was du schreibst, bleibt auf deinem Mac.",
  "pf.b": "<span>Inhalt</span> Helle und dunkle Farben, eine Sperre gegen Bearbeiten und Schließen sowie Tastenkürzel zum schnellen Schreiben.",
  "ca.p": "Ein Klick schließt alle Mac-Apps auf einmal. Du siehst vorher das Symbol jeder App und lässt offen, was du willst. Der Finder bleibt aktiv, und deine Auswahl wird für das nächste Mal gespeichert.",
  "ca.b": "<span>Inhalt</span> Sofortiges Beenden normaler Apps, eine Ausnahmeliste und weder Netzwerk noch Tracking.",
  "ss.p": "Wenn du deinen Bildschirm in Teams, Zoom oder Meet teilst, blendet SafeShare die Apps und Fenster aus, die niemand sehen soll. Du arbeitest mit deinem ganzen Schreibtisch, die Teilnehmenden sehen nur, was du freigibst.",
  "ss.b": "<span>Inhalt</span> Schutz pro App und Fenster, schnelles lokales Streaming und ausgeblendete Mitteilungen. Funktioniert ohne Internet.",
  "tm.p": "Ein ruhiger Ort, um Filme und Serien auf dem Mac zu entdecken. Stöbern, das Passende für den Abend wählen und Bibliothek und Bewertungen bei dir behalten. Ohne API-Schlüssel läuft ein vollständiger Demo-Modus.",
  "tm.b": "<span>Inhalt</span> Kategorien und Empfehlungen, eine lokale Bibliothek und der API-Schlüssel im Schlüsselbund.",
  "mm.p": "Bewegt den Mauszeiger in einem Rhythmus, den du festlegst: für eine Präsentation, zum Testen oder damit der Mac während einer langen Aufgabe wach bleibt. Starten, stoppen oder sofort bewegen, direkt aus der Menüleiste.",
  "mm.b": "<span>Inhalt</span> Intervalle von Sekunden bis Minuten, zwei Bewegungsmuster, optionaler Klick und kein Ruhezustand während der Ausführung.",
  "hk.h3": "Haki",
  "hk.p": "Sprich, und Haki schreibt. Gedrückt halten, im eigenen Dialekt sprechen, loslassen: Der Text erscheint am Cursor, in jeder App. Gemacht für Arabisch und Levantinisch, versteht aber auch Englisch, Deutsch und Französisch.",
  "hk.b": "<span>Inhalt</span> Diktat per Stimme, ein globales Tastenkürzel und der Schlüssel im Schlüsselbund. Aufnahmen werden nicht gespeichert.",
  "oss.repo": "Repository",
  "oss.contrib": "Mitmachen",
  "inv.label": "Mach mit",
  "inv.h3": "Lass es uns gemeinsam bauen.",
  "inv.p": "Mitmachen heißt hier nicht nur Code. Eine klarere Idee, eine bessere Übersetzung, ein Test auf deinem Gerät oder ein kleiner Fix: Alles hat seinen Platz im Team. Öffne „Mitmachen“ beim Projekt, das dir gefällt, und schick deinen Beitrag. Wer dabei sein will, ist willkommen.",
  "inv.cta": "Mein GitHub-Profil",
  "work.label": "Wie ich arbeite",
  "work.h2": "Von der Idee<br>zum fertigen Produkt.",
  "work.p": "Ich verbinde unternehmerisches Denken mit technischer Umsetzung. So sehe ich das große Ganze und gehe dann in die Details, die den Unterschied machen.",
  "work.c1h": "Ich verstehe das Problem",
  "work.c1p": "Ich beginne beim Nutzer und beim Markt, nicht bei der Technik. Ich suche das eigentliche Problem und das, was eine Lösung nützlich und wachstumsfähig macht.",
  "work.c2h": "Ich baue das System",
  "work.c2p": "Ich mache aus der Vision ein vollständiges Produkt: Apps, Oberflächen, Backend-Dienste, Karten, Daten und operative Systeme.",
  "work.c3h": "Ich lerne und verbessere",
  "work.c3p": "Ich beobachte die echte Nutzung, beseitige Reibungspunkte und entwickle das Produkt laufend weiter, mit klarer Wirkung für Menschen und Geschäft.",
  "car.label": "Werdegang",
  "car.h2": "Über 10 Jahre<br>in der Tech-Branche.",
  "car.p": "Praktische Erfahrung in Deutschland und Syrien, von eigenen Produkten bis zur Leitung von Systemen und Tech-Teams.",
  "car.t1": "2020 — heute",
  "car.t2": "Sept. 2026 — heute",
  "car.t3": "Apr. 2026 — heute",
  "car.ibykus": "IBYKUS AG / WIBank · Erfurt, Deutschland",
  "car.nadhif": "Mac-App zum Aufräumen und für Sicherheitsprüfungen, in Entwicklung",
  "car.arab": "Arabische KI-Plattform für Kundensupport",
  "car.shfli": "E-Commerce- und Kleinanzeigenplattform in Syrien (shfli.com)",
  "car.tc": "Aufbau und Betrieb einer syrischen Mobilitätsplattform",
  "car.ps": "SaaS-Plattform für E-Commerce",
  "car.fs": "Unternehmens- und freie Projekte · Deutschland und Syrien",
  "ct.label": "Was kommt",
  "ct.h2": "Ich baue für die Zukunft,<br><em>jeden Tag ein echter Schritt.</em>",
  "ct.p": "Mein Interesse gilt smarter Mobilität, KI und digitalen Produkten für Wachstumsmärkte.",
  "ct.mail": "Schreib mir",
  "ct.arab": "Arab Solutions entdecken",
  "aria.nav": "Hauptnavigation",
  "aria.home": "Startseite",
  "aria.mono": "EA-Monogramm von Emad Alhamou",
  "lang.label": "Sprache",
  "aria.details": "Details zu ",
  "meta.title": "Emad Alhamou | Gründer & Produktentwickler",
  "meta.desc": "Gründer und Entwickler von TakeCar, Shfli und Arab Solutions. Ich baue Technologieprodukte für Mobilität, Marktplätze, KI-gestützten Kundensupport und Wachstumsmärkte.",
  "nav.articles": "Artikel",
  "nd.play": "Nadhif-Video abspielen",
  "nd.videoCap": "Ein animierter Rundgang durch Nadhif (auf Englisch). Das Video wird erst beim Abspielen von YouTube geladen.",
  "nd.article": "Ganzen Artikel lesen",
  "art.label": "Artikel",
  "art.h2": "Geschichten hinter<br>den Produkten.",
  "art.p": "Ein Artikel zu jedem Projekt und Tool, das ich baue: was es kann, warum ich es gebaut habe und wie es funktioniert.",
  "art.all": "Alle Artikel"
 }
};

  function valid(l) { return SUPPORTED.indexOf(l) > -1; }

  function initial() {
    try {
      var q = new URLSearchParams(location.search).get('lang');
      if (valid(q)) return q;
    } catch (e) {}
    try {
      var saved = localStorage.getItem(STORE);
      if (valid(saved)) return saved;
    } catch (e) {}
    var list = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ''];
    for (var i = 0; i < list.length; i++) {
      var c = String(list[i] || '').toLowerCase().slice(0, 2);
      if (valid(c)) return c;
    }
    return 'en';
  }

  function setRoot(l) {
    root.lang = l;
    root.dir = l === 'ar' ? 'rtl' : 'ltr';
  }

  var lang = initial();
  setRoot(lang);

  // Hide the Arabic source text until the translation is in, so it does not flash.
  function reveal() { root.classList.remove('i18n-wait'); }
  if (lang !== 'ar') {
    root.classList.add('i18n-wait');
    setTimeout(reveal, 1500);
  }

  var orig = null;

  // Attributes whose value depends on the language. The Arabic value is the
  // attribute itself; the others sit in data-href-en, data-href-de and so on.
  var SWAP = [['href', 'data-href-'], ['src', 'data-src-'], ['data-yt', 'data-yt-'], ['data-title', 'data-title-']];

  function each(sel, fn) { Array.prototype.forEach.call(document.querySelectorAll(sel), fn); }

  function capture() {
    orig = { title: document.title, desc: '' };
    var m = document.querySelector('meta[name="description"]');
    if (m) orig.desc = m.getAttribute('content');
    each('[data-i18n]', function (el) { el.__ar = el.innerHTML; });
    each('[data-i18n-aria], .ossTags[aria-label]', function (el) { el.__arAria = el.getAttribute('aria-label'); });
    SWAP.forEach(function (s) {
      each('[' + s[1] + 'en]', function (el) { el['__ar_' + s[0]] = el.getAttribute(s[0]); });
    });
    each('.ossCard time[datetime]', function (el) { el.__ar = el.textContent; });
  }

  function apply(l) {
    var dict = T[l];
    setRoot(l);
    each('[data-i18n]', function (el) {
      var v = dict ? dict[el.getAttribute('data-i18n')] : el.__ar;
      if (v != null) el.innerHTML = v;
    });
    each('[data-i18n-aria]', function (el) {
      var v = dict ? dict[el.getAttribute('data-i18n-aria')] : el.__arAria;
      if (v != null) el.setAttribute('aria-label', v);
    });
    each('.ossTags[aria-label]', function (el) {
      if (!dict) { el.setAttribute('aria-label', el.__arAria); return; }
      var h = el.closest('.ossCard');
      h = h && h.querySelector('h3');
      el.setAttribute('aria-label', dict['aria.details'] + (h ? h.textContent : ''));
    });
    SWAP.forEach(function (s) {
      each('[' + s[1] + 'en]', function (el) {
        var v = dict ? el.getAttribute(s[1] + l) : el['__ar_' + s[0]];
        if (v != null) el.setAttribute(s[0], v);
      });
    });
    var fmt = null;
    try { fmt = new Intl.DateTimeFormat(l === 'de' ? 'de-DE' : 'en-GB', { day: 'numeric', month: 'long', year: 'numeric' }); } catch (e) {}
    each('.ossCard time[datetime]', function (el) {
      if (!dict || !fmt) { el.textContent = el.__ar; return; }
      var p = el.getAttribute('datetime').split('-');
      el.textContent = fmt.format(new Date(+p[0], +p[1] - 1, +p[2]));
    });
    document.title = dict ? dict['meta.title'] : orig.title;
    var m = document.querySelector('meta[name="description"]');
    if (m) m.setAttribute('content', dict ? dict['meta.desc'] : orig.desc);
    var sel = document.getElementById('langSelect');
    if (sel) sel.value = l;
  }

  document.addEventListener('DOMContentLoaded', function () {
    capture();
    if (lang !== 'ar') apply(lang);
    var sel = document.getElementById('langSelect');
    if (sel) {
      sel.value = lang;
      sel.addEventListener('change', function () {
        var l = sel.value;
        if (!valid(l)) return;
        try { localStorage.setItem(STORE, l); } catch (e) {}
        try {
          var u = new URL(location.href);
          if (u.searchParams.has('lang')) { u.searchParams.delete('lang'); history.replaceState(null, '', u.toString()); }
        } catch (e) {}
        apply(l);
      });
    }
    reveal();
  });
})();
