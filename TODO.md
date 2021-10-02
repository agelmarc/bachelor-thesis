## Vor Abgabe

- PDFA in Präambel einschalten (pdfa=false auf pdfa=true setzen), sowie Metadata entkommentieren
- Quellen für Grundlagen einfügen

## Struktur

1. Einleitung
2. Grundlagen
   1. Physik
   2. Machine Learning
3. Framework
   1. Erklärung aller Hyperparameter, Aufbau der Netze, Struktur der Daten, Evaluation + Motivation davon (Warum 3 Sequencen? etc..)
   2. Trainings + Validation + Benchmark Set einführen
   3. Unterschiede M vs SMSI (semi local momentum space)
   4. Wie geschieht die Auswertung
   5. Fehlerbeschreibung (Wie kommt man von den Vorhersagen vieler Netze zu einem Wert + Konfidenzintervall?)
   6. Klassische Exponentialfits
4. Reproduktion der Bekannten Kerne (H2, H3, He4)
   1. Präsentieren der Resultate für H2, H3, He4
   2. (Wie viele WW bei welchen Kernen?)
   3. Wie gut reproduziert das Netz die bekannten Kerne
   4. Diskutieren + H2 herausheben + Vergleich mit Klassischer Extrapolation
5. Erweiterte Modi (Nmax, Srg) für H2, H3, Li6
   1. Für jeden Trainingsmodus:
      1. Motivation des Trainingsmodus
      2. Erklärung des Trainingsmodus anhand eines Beispiels
      3. Präsentieren der Resultate für das Benchmark Set
      4. Diskutieren
   2. Vergleich der Trainingsmodi + Vergleich mit Klassicher Extrapolation
6. Diskussion Li6 ähnlich aber kürzer als 5 + Übergang zu Diff mit Motivation
7. Übertragung auf Diff. Ab hier alle 4 Kerne
   1. Nicht mehr jeden Modus einzeln zeigen -> Alle Modi in 1 Plot.
   2. Vergleich Abs Diff, Conclusion diff besser
8. Ausblick / Neue Ansätze
   1. Idee Frequenzfilter: Trainieren und evaluieren mit Freq. links oder rechts vom maximum ()
   2. Idee Frequenzselektion: Zwei Plots zeigen, wo es gut gehen kann und wo es schief gehen kann (chi2bSMSI3B srg0400 He4) -> Große Konsequenz
   3. Idee H2: Normed Plot zeigen. Nichts hilft. Ausblick Normed für andere Kerne.Mit Frequenzselektion viel besser
9. Conclusion

## Benchmark Set

- H2, H3, He4: 3B oder 4B 0400 + 0800

### Welche Plots

- 3.2: Plots von NCSM Sequenzen, Netzinputs
- 4.1, 5.1.3: für jeden Modus ein Plot (so wie immer)

### Seiten (sehr grob geschätzt)

- Einleitung: 1
- Grundlagen: 10
- Framework: 8
- Vanilla: 3
- Erweiterte Modi: 2x4 + 2 = 10
- Li6: 3
- Diff: 8
- Outlook: 5
- Conclusion: 1

== ~50 Seiten
