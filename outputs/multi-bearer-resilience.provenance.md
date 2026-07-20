# Provenance Record: Multi-Bearer Resilience Literature Review

**Date:** 2026-07-19  
**Slug:** `multi-bearer-resilience`  
**Final artifact:** `outputs/multi-bearer-resilience.md`

---

## Sources Consulted vs. Accepted vs. Rejected

### Accepted (cited in final review)

| # | Source | Type | Role |
|---|--------|------|------|
| 1 | Ramírez-Arroyo et al. (2025), arXiv:2512.19639 | Measurement paper | Primary quantitative TN vs. NTN comparison (read in detail) |
| 2 | Borgianni et al. (ICNC 2026) | Conference paper | SD-WAN + NTN 6G architecture |
| 3 | Fernandez-Muñoz et al. (IEEE ASMS/SPSC 2025) | Conference paper | 5G MCX satellite-terrestrial integration |
| 4 | Pocovi et al. (ISWCS 2018) | Conference paper | Dual connectivity URLLC reliability |
| 5 | Sterbenz et al. (2010, 2012) | Framework papers | ResiliNets resilience/survivability principles |
| 6 | Rohrer, Jabbar & Sterbenz (2012) | Paper | Path diversification metric |
| 7 | Grover & Sack (DRCN 2007) | Paper | MTTR vs. protection capacity |
| 8 | Chen et al. (IMC 2013) | Measurement paper | MPTCP over WiFi+cellular |
| 9 | Bui et al. (2019), arXiv:1909.02601 | Measurement paper | Dual-LTE MPTCP |
| 10 | 3GPP TS 37.340 (R15–R18) | Standard | Multi-connectivity specification |
| 11 | Broadband Forum TR-348, TR-378 | Standard | Hybrid access architecture |
| 12 | IETF RFC 8157 | Standard | GRE tunnel bonding |
| 13 | ITU-T Y.1540, Y.1541, L-Supp.35 | Standards | Performance objectives and disaster resilience |
| 14 | UK Ofcom (2024) Resilience Guidance | Regulation | National telecom resilience mandate |
| 15 | UK Parliament (2025) Subsea cables report | Policy | Cable resilience and backup needs |
| 16 | Kenya CA (2023) NRRD Guidelines | Regulation | Redundancy/Resilience/Diversity framework |
| 17 | Taiwan MODA (2025) Cable cut response | Press release | Real-world multi-bearer activation |
| 18 | Recorded Future (2025) | Threat intelligence | Submarine cable vulnerability analysis |
| 19 | Ryan (2013) Infantry Magazine; Burnett MIPB | Military doctrine | PACE methodology |
| 20 | Torrence (2025) West Point MWI | Military doctrine | Modern PACE card example |
| 21 | EANTC (2023) SD-WAN White Paper | Industry | SD-WAN resilience testing |
| 22 | Cisco CiscoLive (2026) BRKENT-2660 | Industry | SD-WAN design with N+1 |
| 23 | NSF (2022) "Improving SD-WAN Resilience" | Paper | SD-WAN failover mechanisms |
| 24 | TU Munich (2025) Multi-Technology Planning | Paper | Reliable multi-technology path planning |
| 25 | TU Munich (2016) Resilience Metrics | Technical report | Metrics taxonomy |
| 26 | MDPI Sensors (2022) Hybrid Sat-Terrestrial 6G | Review | NTN-TN challenges |
| 27 | New Space Economy (2026) | Article | Satellite backup for cable threats |

### Consulted but not prominently cited

- Politecnico di Milano / Europacable (2021): Energy efficiency comparison fiber vs. microwave/satellite — tangential (energy, not resilience)
- SAJST paper on Starlink/fiber/cellular — general overview, less rigorous than Ramírez-Arroyo
- WaveTel IoT article on industrial router uplinks — informative but vendor-focused
- UPC thesis on satellite-terrestrial backhauling — background for 5G NTN
- UPC conference paper on satellite backup for mobile backhaul — informed Section 3.5
- Wikipedia PACE article — used for cross-reference only
- MDPI Electronics (2021) multi-path routing resilience evaluation — general, less specific to bearer comparison

### Rejected / Not used

- Multiple duplicate 3GPP spec versions (cited only v18.1.0)
- Blog post on SD-WAN design (eawtech.net) — useful framing but not citable

---

## Verification Status

| Claim | Verified? | Method |
|-------|-----------|--------|
| Starlink+OneWeb outage drops from 12-21% to ~2% in urban | ✓ | Read directly from arXiv:2512.19639v2 abstract |
| Starlink has ~8000 satellites at 550-700 km | ✓ | Stated in Ramírez-Arroyo et al. Section II |
| OneWeb has ~648 satellites at 1200 km | ✓ | Stated in Ramírez-Arroyo et al. Section II |
| Taiwan-Matsu cable cut and microwave backup activation | ✓ | MODA official press release |
| Submarine cable median repair >40 days | ✓ | Recorded Future 2025 report |
| UK Ofcom resilience guidance published 2024 | ✓ | Ofcom website confirms |
| 3GPP TS 37.340 covers multi-connectivity R15-R18 | ✓ | ETSI PDF confirms |
| RFC 8157 is GRE Tunnel Bonding | ✓ | IETF page confirms |
| PACE = Primary, Alternate, Contingency, Emergency | ✓ | Multiple military sources confirm |
| Grover & Sack (2007) finding on MTTR vs. protection capacity | ✓ | Paper title and abstract confirm |
| Kenya NRRD guidelines published 2023 | ✓ | CA Kenya website |

---

## Intermediate Files

- `outputs/.plans/multi-bearer-resilience.md` — Planning document
- Fetched and read: arXiv:2512.19639v2 (Ramírez-Arroyo et al.) — primary quantitative source

---

## Limitations

1. **Alpha search service unavailable** — no arXiv-native paper search could be performed.
2. **Subagent delegation failed** due to usage limits — all research conducted by primary agent.
3. **Full-text access** obtained only for Ramírez-Arroyo et al. (2025). Other papers characterized from abstracts and metadata.
4. **Military doctrine sources** are limited to unclassified publications; classified PACE annexes and STANAG details not accessible.
5. **No formal meta-analysis possible** — studies use heterogeneous metrics, scenarios, and methodologies.
6. **Recency**: Papers published after mid-2026 not covered.
7. **Language scope**: Search conducted in English; French-language sources on "analyse comparative des supports" not separately searched (topic is primarily anglophone in the technical literature).
