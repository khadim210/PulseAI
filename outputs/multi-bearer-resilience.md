# Multi-Bearer Resilience: A Comparative Analysis of Communication Bearers

**Date:** 2026-07-19  
**Scope:** Comparative analysis of communication bearer technologies from a resilience perspective — architectures, metrics, empirical evidence, standards, and application domains for multi-bearer continuity.

---

## 1. Introduction

Resilient communications depend on the ability to maintain service continuity when any single transmission medium (bearer) fails. Whether caused by submarine cable cuts, natural disasters, cyber-attacks, equipment failure, or deliberate jamming, single-bearer dependence represents a critical vulnerability. The concept of **multi-bearer resilience** — diversifying across heterogeneous transmission technologies to ensure continuity — spans domains from military command-and-control (where it is formalized as the PACE methodology) to enterprise SD-WAN, telecom backhaul, and national critical infrastructure protection.

This review synthesizes the literature on comparative bearer analysis and multi-bearer architectures, addressing: (1) the resilience properties of individual bearer types, (2) architectures enabling multi-bearer operation, (3) metrics for quantifying bearer and path resilience, (4) empirical measurement studies, (5) application-domain requirements, and (6) the standards and regulatory landscape.

---

## 2. Bearer Taxonomy and Resilience Properties

### 2.1 Bearer Types

| Bearer | Typical Bandwidth | Latency (one-way) | Key Vulnerability | Geographic Reach | Deployment Speed |
|--------|-------------------|-------------------|-------------------|------------------|------------------|
| **Fiber optic (terrestrial)** | 100 Gbps+ per λ | 2–5 ms/1000 km | Physical cut (excavation, earthquake) | Fixed routes | Weeks–months |
| **Submarine cable** | Multi-Tbps | ~5 ms/1000 km | Anchor drag, sabotage, seismic | Intercontinental | Months–years |
| **Microwave (PtP)** | 1–10 Gbps | <1 ms per hop | Rain fade, LoS obstruction, tower damage | LoS limited (~50 km hops) | Days–weeks |
| **Cellular 4G/LTE** | 50–300 Mbps | 15–40 ms | Tower failure, congestion, power loss | Cell coverage area | Existing infrastructure |
| **Cellular 5G NR** | 100 Mbps–1+ Gbps | 5–20 ms | Same as 4G but denser; mmWave blocked by foliage | Urban/suburban | Existing infrastructure |
| **LEO Satellite (Starlink)** | 50–250 Mbps | 25–60 ms | LoS blockage (urban), rain, orbital gaps | Near-global | Hours (terminal deploy) |
| **LEO Satellite (OneWeb)** | 30–150 Mbps | 40–100 ms | LoS blockage, fewer ground stations | Near-global (polar-optimized) | Hours (terminal deploy) |
| **GEO Satellite** | 10–100 Mbps | 500–700 ms | Rain fade, transponder failure | Global (excl. poles) | Hours (terminal) |
| **HF Radio** | 2.4–9.6 kbps | Variable (100+ ms) | Ionospheric variation, interference | Beyond line of sight, global | Minutes |
| **Troposcatter** | 1–50 Mbps | <10 ms | Weather, large equipment | 100–300 km | Hours–days |

### 2.2 Failure Mode Diversity

The core principle of multi-bearer resilience is **failure mode independence**. Effective diversification requires bearers whose failure modes are uncorrelated:

- **Fiber + Satellite:** No shared physical path; satellite immune to terrestrial cuts but vulnerable to LoS blockage.
- **Fiber + Microwave:** Both terrestrial but geometrically diverse; microwave unaffected by underground/undersea cuts.
- **5G + LEO Satellite:** Complementary in urban (5G strong, satellite weak due to blockage) vs. rural/disaster (satellite strong, 5G infrastructure may be destroyed).
- **Multiple cellular operators:** Partial diversity (different towers) but shared vulnerabilities (regional power loss, shared RAN sites).

The Taiwan-Matsu cable incidents (2023, 2025) provide a real-world case: when submarine cables were severed, backup microwave transmission was activated within hours by MODA (Taiwan's Ministry of Digital Affairs), maintaining connectivity at reduced capacity until repair.

### 2.3 The Resilience-Performance Trade-off

Bearers offering the highest resilience to infrastructure destruction (HF radio, satellite) typically deliver the lowest bandwidth and highest latency. Conversely, the highest-performance bearers (fiber) have the longest repair times. This inverse relationship makes **multi-bearer architectures** essential rather than optional for high-availability systems.

---

## 3. Multi-Bearer Architectures and Protocols

### 3.1 SD-WAN (Software-Defined Wide Area Network)

SD-WAN has become the dominant enterprise approach to multi-bearer aggregation. Key characteristics:

- **Transport-agnostic overlay:** Aggregates MPLS, broadband internet, LTE/5G, and satellite underlays into a unified fabric.
- **Policy-driven path selection:** Routes traffic based on application SLA requirements (latency, jitter, loss) matched against real-time underlay performance.
- **Sub-second failover:** Detects link degradation and reroutes traffic within 100ms–1s.
- **N+1 redundancy architecture:** Cisco SD-WAN design (2026) specifies dual WAN edge routers, dual ISP circuits, and dual VPN tunnels at each site.

Recent work (Borgianni et al., ICNC 2026) demonstrates a **policy-driven SD-WAN for hybrid terrestrial and non-terrestrial 6G connectivity**, using ONOS as an SDN controller integrating LEO satellite links alongside terrestrial paths — a direct implementation of multi-bearer resilience for the 6G era.

**Key limitation:** SD-WAN operates at the overlay level and cannot control the underlying transport network; it depends on bearer diversity being genuinely independent at the physical layer (EANTC 2023).

### 3.2 Multipath TCP (MPTCP)

MPTCP (RFC 6824, updated RFC 8684) enables a single TCP connection to use multiple network interfaces simultaneously:

- **Resilience mode:** Duplicate packets across paths for reliability (used in URLLC scenarios).
- **Throughput mode:** Aggregate bandwidth across paths.
- **Handover mode:** Seamlessly move traffic from failing to healthy path.

Empirical measurements (Chen et al., IMC 2013; Bui et al., 2019) demonstrate that MPTCP over heterogeneous WiFi+cellular subpaths achieves resilience but faces challenges from path heterogeneity — the high-latency path can become a bottleneck for the head-of-line blocking of in-order delivery.

### 3.3 Hybrid Access (Broadband Forum TR-348/TR-378)

The Broadband Forum defined a **Hybrid Access** architecture enabling residential/enterprise CPE to simultaneously use fixed broadband (DSL/fiber) and 3GPP cellular:

- **GRE Tunnel Bonding (RFC 8157):** Two GRE tunnels (one per bearer) terminate at a Hybrid Access Gateway (HAG) that reassembles traffic.
- **Three transport models:** L3 overlay tunneling, L3 network-based tunneling, L4 multipath.
- **Primary use case:** Extend broadband reach in rural areas where DSL alone is insufficient, but also provides **resilience** through bearer diversification.

### 3.4 3GPP Multi-Connectivity (Dual Connectivity)

3GPP TS 37.340 (Releases 15–18) standardizes **Multi-Radio Dual Connectivity**:

- **EN-DC:** E-UTRA (4G) as master node + NR (5G) as secondary node.
- **NR-NR DC:** Two NR connections simultaneously.
- **NE-DC:** NR master + E-UTRA secondary.

For resilience, **Packet Duplication** (PDCP layer) is specified: the same packet is transmitted on both links, and the receiver discards duplicates. This achieves ultra-reliability (target: 10⁻⁵ block error rate for URLLC) through path diversity at the radio level.

Research by Pocovi et al. (ISWCS 2018) shows that reliability-oriented dual connectivity achieves 99.999% reliability where single connectivity cannot, by exploiting **independent fading** across spatially separated links.

### 3.5 5G/6G Non-Terrestrial Network Integration

The 3GPP NTN standardization (Releases 17–18) and ongoing 6G research are directly pursuing terrestrial-satellite multi-connectivity:

- **Transparent NTN architecture:** Satellite acts as relay; standard 5G protocol stack with timing adjustments.
- **Multi-connectivity TN+NTN:** Terrestrial 5G as primary, satellite as diversity/backup path.
- Fernandez-Muñoz et al. (2025) demonstrate that 5G satellite-terrestrial architectures can support mission-critical (MCX) services through seamless failover.

### 3.6 Military PACE Architecture

The U.S. military formalizes multi-bearer planning as **PACE (Primary, Alternate, Contingency, Emergency)**:

| Layer | Typical Bearer | Bandwidth | Resilience Role |
|-------|---------------|-----------|-----------------|
| **Primary** | MSS/CPCE (satellite mesh), SINCGARS | High | Normal operations |
| **Alternate** | WGS SATCOM VSAT (GEO) | Medium | First fallback on primary loss |
| **Contingency** | Link-16, pLEO VSAT, masked LTE/5G | Low-Medium | Degraded but functional |
| **Emergency** | HF ALE, physical courier, pyrotechnic signals | Minimal | Life-safety communication only |

Key PACE principles (Ryan, Infantry Magazine 2013; Burnett, MIPB):
- Each layer must be **technologically and physically independent** of the others.
- Automated **trigger thresholds** govern transitions (e.g., "2 consecutive missed net checks" → shift to Alternate).
- Graceful degradation of data richness: from full COP to metadata-only to voice-only to paper.

---

## 4. Resilience Metrics and Assessment Frameworks

### 4.1 Traditional Availability Metrics

- **Availability** = (Uptime) / (Total Time) — typically expressed as "nines" (99.9% = three nines, 99.999% = five nines).
- **MTBF** (Mean Time Between Failures): bearer-specific failure rates.
- **MTTR** (Mean Time To Repair): critical differentiator. Fiber MTTR can be hours to weeks; satellite failover is seconds.

Grover & Sack (DRCN 2007) demonstrated that **reducing MTTR is often more effective than adding protection capacity** for achieving high availability in survivable networks — directly relevant to multi-bearer strategies where fast failover to a backup bearer is the primary resilience mechanism.

### 4.2 Path Diversity Metrics

The **ResiliNets** framework (Sterbenz et al., 2010, 2012) provides comprehensive resilience principles:

- **D²R²+DR Strategy:** Defend, Detect, Remediate, Recover + Diagnose, Refine.
- **Path Diversification:** Rohrer, Jabbar & Sterbenz (2012) formalize a quantified diversity measure for selecting multiple paths to maximize flow reliability.
- **Multi-level resilience:** Physical infrastructure → network topology → path routing → inter-realm → end-to-end, each requiring its own diversity measures.

### 4.3 Kenya NRRD Framework

The Communications Authority of Kenya published "Guidelines for Network Redundancy, Resilience and Diversity" (2023) — one of the few regulatory frameworks that explicitly defines all three concepts:

- **Redundancy:** Duplication of components.
- **Resilience:** Ability to recover from disruption.
- **Diversity:** Using different technologies/paths to avoid common-mode failure.

Link availability is calculated per external connection: `A% = ((M - ΣD) / M) × 100`, where D = downtime incidents and M = monitoring period.

### 4.4 Outage Probability and Multi-Connectivity Gain

Ramírez-Arroyo et al. (2025) provide quantitative evidence of resilience gains from multi-connectivity:

| Configuration | Outage Probability (Urban) |
|---------------|---------------------------|
| Starlink alone | ~12% |
| OneWeb alone | ~21% |
| Starlink + OneWeb (NTN-NTN) | ~2% |
| 5G Operator A alone | <1% |
| 5G + Starlink (TN-NTN) | <<1% |

This demonstrates a **6–10× reduction in outage probability** through satellite-satellite multi-connectivity, and near-zero outage when combining terrestrial and non-terrestrial systems.

---

## 5. Empirical Comparative Studies

### 5.1 Ramírez-Arroyo et al. (2025): TN vs. NTN Measurement Campaign

The most comprehensive recent comparative study (Aalborg University / Danish CFB):

**Setup:** Simultaneous measurement of 2× 5G operators + Starlink + OneWeb across urban, suburban, and forest scenarios in Copenhagen. UDP traffic at 5/5 Mbps target representing emergency video streaming.

**Key findings (one-way delay, downlink):**
- 5G terrestrial: median ~15–25 ms
- Starlink: median ~30–45 ms (urban), ~25–35 ms (suburban)
- OneWeb: median ~60–90 ms (higher due to fewer/farther ground stations)
- Forest scenario: satellite severely degraded by canopy obstruction

**Key findings (throughput):**
- 5G: reliably achieves 5 Mbps target in urban/suburban
- Starlink: achieves target in suburban/rural but drops in dense urban due to LoS blockage
- OneWeb: more variable; enterprise antenna provides better obstruction handling

**Multi-connectivity conclusions:**
- TN+NTN combination provides "best of both worlds" — terrestrial dominates in urban, satellite provides backup/extension in rural/disaster scenarios.
- NTN+NTN diversity (Starlink + OneWeb) significantly reduces outage in urban by exploiting different orbital inclinations.

### 5.2 Submarine Cable Cut Events

**Taiwan-Matsu (2023, 2025):** When submarine cables serving Matsu Islands were cut (by ship anchor/wreckage), Taiwan's MODA activated backup microwave links within hours. Capacity was reduced but essential services maintained. This demonstrates practical multi-bearer resilience at the national level.

**Recorded Future analysis (2025):** Median submarine cable repair time is 40+ days and trending upward due to repair vessel shortages and geopolitical access restrictions. "Satellite and microwave links will almost certainly remain partial stop-gaps, restoring only a fraction of cable capacity."

**UK Parliamentary Committee (2025):** Concluded that UK subsea cable resilience requires both route diversity and alternative bearer backup (satellite) given increasing sabotage threats.

### 5.3 SD-WAN Failover Performance

EANTC (2023) white paper on SD-WAN resilience testing:
- Failover detection: 50ms–5s depending on vendor and BFD/health-check configuration.
- Path quality measurement enables preemptive rerouting before hard failure.
- Key challenge: overlay cannot detect or mitigate shared physical failures in underlays that appear diverse but share fiber ducts.

### 5.4 MPTCP Over Heterogeneous Links

Chen et al. (IMC 2013) measured MPTCP over WiFi + 3G/4G:
- Resilience benefit confirmed: seamless handover when one path fails.
- Performance penalty: 10–30% throughput reduction vs. best single path when path RTTs differ by >3×.
- Dual-LTE MPTCP (Bui et al., 2019): high-speed mobility causes correlated degradation across both LTE paths, reducing diversity benefit.

---

## 6. Application Domains

### 6.1 Military / Defense

The PACE methodology is the canonical multi-bearer framework:
- Designed for **contested electromagnetic environments** where adversaries actively deny communication bearers.
- Each PACE layer represents a different physical medium with independent denial mechanisms.
- Modern PACE plans (Torrence, West Point MWI 2025) integrate MSS mesh, WGS SATCOM, Link-16, LEO pLEO, cellular (masked LTE/5G), HF ALE, and physical courier.
- Automated trigger-based switching replaces manual decision-making under stress.

### 6.2 Critical Infrastructure

Telecom networks supporting critical infrastructure require multi-bearer diversity:
- UK Ofcom Resilience Guidance (2024) mandates communications providers to implement "physical diverse routing" and "technology diverse backup" for critical circuits.
- EU CER Directive (2022/2557) requires critical entities to ensure resilience considering interconnections.
- Smart grid SCADA systems increasingly use cellular + satellite + fiber diverse paths.

### 6.3 Enterprise WAN

SD-WAN adoption driven by:
- **Branch office diversity:** MPLS + broadband internet + LTE as three bearer classes.
- **Cloud access resilience:** Direct Internet Access with dual ISP + SD-WAN overlay.
- **Remote/mobile workforce:** VPN over best-available bearer (WiFi, cellular, satellite).
- Cisco (CiscoLive 2026) documents N+1 redundancy across all network layers with explicit transport diversity requirements.

### 6.4 Maritime and Remote

- Ships: VSAT (GEO/MEO) + LEO (Starlink Maritime) + HF as multi-bearer stack.
- Remote mining/oil: Satellite primary + microwave backup to nearest hub.
- Island nations: Submarine cable + satellite backup (as demonstrated by Taiwan-Matsu).

### 6.5 Emergency Communications

- Denmark's Center of Emergency Communication (CFB) requirement: 5 Mbps video streaming via most reliable available bearer.
- Ramírez-Arroyo et al. (2025) recommendations: deploy both terrestrial and satellite terminals for disaster response; in urban areas combine two satellite operators to reduce outage from ~20% to ~2%.

---

## 7. Standards and Regulatory Landscape

### 7.1 3GPP

- **TS 37.340** (Release 15–18): Multi-connectivity (E-UTRA + NR, NR + NR) with packet duplication for reliability.
- **Release 17-18 NTN:** Integration of non-terrestrial networks into 5G standard, enabling TN-NTN multi-connectivity.
- **Release 19 (ongoing):** Enhanced NTN mobility and multi-connectivity procedures.

### 7.2 ITU-T

- **Y.1540:** IP packet transfer and availability performance parameters.
- **Y.1541:** Network performance objectives for IP-based services (delay, loss, availability classes).
- **L-series Supplement 35:** Framework for disaster management and network resilience.

### 7.3 Broadband Forum

- **TR-348:** Hybrid Access Broadband Architecture (fixed + cellular bonding).
- **TR-378:** Nodal requirements for Hybrid Access networks.

### 7.4 IETF

- **RFC 6824 / RFC 8684:** Multipath TCP.
- **RFC 8157:** GRE Tunnel Bonding for hybrid access.
- **RFC 4116:** IPv4 Multihoming with provider-independent addresses.

### 7.5 National/Regional Regulation

- **UK Ofcom** (2024): Network and Service Resilience Guidance — requires geographic and technology diversity for resilient circuits.
- **EU EECC** (European Electronic Communications Code, 2018): Article 40 requires "appropriate and proportionate" security measures.
- **Kenya NRRD** (2023): Explicit quantitative guidelines for redundancy, resilience, and diversity of ICT networks.
- **U.S.** National Security Memorandum 22 (2024): Mandates cross-sector infrastructure resilience, covering telecommunications.

### 7.6 Military Standards

- **PACE Doctrine:** Codified in U.S. Army FM 6-02 (Signal Support to Operations).
- **NATO STANAG 5066:** HF radio data communications standard (emergency bearer).
- **Link-16 (STANAG 5516/MIL-STD-6016):** Tactical data link providing independent bearer class from SATCOM and terrestrial.

---

## 8. Emerging Trends

### 8.1 LEO Mega-Constellation Integration

Starlink (~8,000 satellites), OneWeb (~648), Amazon Kuiper (launching) transform satellite from "last resort" to a viable primary/alternate bearer with latency approaching terrestrial cellular. The empirical evidence (Ramírez-Arroyo 2025) shows Starlink latency at ~30–45 ms — within the envelope of many applications.

### 8.2 6G Multi-Connectivity by Design

6G research explicitly targets heterogeneous multi-connectivity as a native architecture feature, not an add-on:
- Borgianni et al. (ICNC 2026): policy-driven SD-WAN integrating terrestrial + LEO for 6G.
- 3GPP anticipated to standardize TN-NTN multi-connectivity as a baseline mode.

### 8.3 AI-Driven Bearer Selection

Machine learning for predictive path quality and proactive bearer switching before failure manifests — moving from reactive failover to **anticipatory** resilience.

### 8.4 Submarine Cable Vulnerability Acceleration

Geopolitical tensions, limited repair capacity, and aging infrastructure are increasing submarine cable cut frequency and repair times, elevating the importance of satellite and microwave backup bearers from "nice to have" to essential national security infrastructure (UK Parliament 2025; Recorded Future 2025).

### 8.5 Digital Twin for Network Resilience

Planning multi-bearer architectures using digital twins to simulate failure scenarios and optimize bearer portfolio allocation for target availability levels.

---

## 9. Synthesis: Consensus, Disagreements, and Gaps

### 9.1 Points of Consensus

1. **No single bearer achieves sufficient resilience alone.** All literature agrees that multi-bearer architectures are necessary for high-availability communications.
2. **Failure mode independence is the critical design criterion.** Bearer diversity is only valuable when failure modes are uncorrelated.
3. **LEO satellite has crossed a performance threshold** that makes it viable as primary/alternate (not just emergency) bearer for many applications.
4. **SD-WAN is the dominant enterprise implementation pattern** for multi-bearer resilience, providing transport-agnostic aggregation with policy-driven selection.
5. **MTTR matters more than MTBF** for practical availability — fast failover to an alternate bearer is often superior to further hardening the primary (Grover & Sack 2007).
6. **Regulatory pressure is increasing** globally to mandate bearer diversity for critical services.

### 9.2 Active Disagreements

1. **Satellite as primary vs. backup:** Whether LEO constellations are ready to serve as primary bearer for critical services or should remain backup. Latency and urban LoS challenges argue "backup"; global coverage and infrastructure independence argue "primary" for underserved areas.
2. **Cost-effectiveness of full N+1 diversity:** At what point does adding bearer diversity exceed acceptable cost? No standard framework for optimizing the cost-resilience trade-off.
3. **Shared failure modes in apparent diversity:** SD-WAN "dual ISP" may share fiber ducts; "diverse satellite operators" may share ground segment vulnerabilities. How much true independence exists?
4. **Centralized vs. distributed control:** SD-WAN centralizes failover intelligence (single controller = single point of failure) vs. distributed PACE-style where each node decides autonomously.

### 9.3 Research Gaps

1. **Quantitative multi-bearer resilience models:** Few papers provide formal probabilistic frameworks for computing compound availability across heterogeneous bearer portfolios.
2. **Correlated failure analysis:** Limited empirical data on the degree to which "diverse" bearers actually experience correlated failures (e.g., power grid failure disabling both cellular towers and fiber amplifiers simultaneously).
3. **Economic models:** No standard TCO framework for bearer diversification decisions balancing capital cost against availability improvement.
4. **Long-term satellite reliability data:** LEO mega-constellations are too new for multi-year availability statistics; current measurements span days to months.
5. **Standardized multi-bearer resilience benchmarks:** No equivalent of "five nines" that accounts for multi-bearer systems — need composite metrics.
6. **Human factors in bearer switching:** PACE plans assume trained operators execute transitions; limited research on failure rates of the human switching process under stress.
7. **Post-quantum cryptographic overhead on constrained bearers:** Emergency bearers (HF, low-bandwidth satellite) may not support key exchange overhead of PQC algorithms.

---

## 10. Recommended Next Steps

1. **For practitioners:** Adopt the PACE conceptual framework (even in civilian contexts) to ensure systematic bearer diversity planning with explicit, testable trigger criteria.
2. **For researchers:** Develop formal probabilistic models of compound availability for heterogeneous bearer portfolios, incorporating correlated failure modes.
3. **For regulators:** Define minimum bearer diversity requirements for critical service categories (emergency comms, financial systems, healthcare), drawing on the Kenya NRRD model.
4. **For network architects:** Deploy SD-WAN with explicit physical-layer diversity verification — not just logical link diversity. Integrate LEO satellite as a standard alternate bearer.
5. **For empirical validation:** Extend the Ramírez-Arroyo et al. methodology to disaster scenarios (simulated infrastructure destruction) and longer time periods for statistical significance.
6. **For standards bodies:** Develop a unified "multi-bearer resilience score" combining individual bearer availability, failover time, capacity degradation, and failure mode correlation.

---

## Sources

### Measurement Studies
- Ramírez-Arroyo, A., Peñaherrera-Pulla, O.S., & Mogensen, P. (2025). "Toward Reliable Connectivity: Measurement-Driven Assessment of Starlink and OneWeb Non-Terrestrial and 5G Terrestrial Networks." arXiv:2512.19639. [Link](https://arxiv.org/html/2512.19639v2)
- IEEE (2025). "Terrestrial 5G and Starlink NTN Multi-Connectivity Toward 6G Communications Integration Era: An Empirical Assessment." [IEEE Xplore](https://ieeexplore.ieee.org/document/11032162)
- Chen, Y.-C. et al. (2013). "A Measurement-based Study of MultiPath TCP Performance over Wireless Networks." IMC 2013. [PDF](https://conferences.sigcomm.org/imc/2013/papers/imc231-chenA.pdf)
- Bui, D. et al. (2019). "Is Two Greater Than One? Analyzing Multipath TCP over Dual-LTE in the Wild." arXiv:1909.02601. [PDF](https://arxiv.org/pdf/1909.02601)

### Architectures & Protocols
- Borgianni et al. (2026). "Policy-Driven SD-WAN for Hybrid Terrestrial and Non-Terrestrial 6G Connectivity." ICNC 2026. [PDF](http://www.conf-icnc.org/2026/papers/p889-borgianni.pdf)
- Fernandez-Muñoz et al. (2025). "Satellite-Terrestrial Integration: 5G Architectures for Mission Critical Services." IEEE ASMS/SPSC. DOI: [10.1109/asms/spsc64465.2025.10946027](https://doi.org/10.1109/asms/spsc64465.2025.10946027)
- NSF (2022). "Improving SD-WAN Resilience: From Vertical." [PDF](https://par.nsf.gov/servlets/purl/10291898)
- EANTC (2023). SD-WAN White Paper. [PDF](https://eantc.de/wp-content/uploads/2023/11/EANTC-SD-WAN-WhitePaper-Final-v5.pdf)
- Cisco (2026). "SD-WAN Design Case Studies." CiscoLive BRKENT-2660. [PDF](https://www.ciscolive.com/c/dam/r/ciscolive/emea/docs/2026/pdf/BRKENT-2660.pdf)
- Pocovi, G. et al. (2018). "Reliability Oriented Dual Connectivity for URLLC services in 5G New Radio." ISWCS. DOI: [10.1109/iswcs.2018.8491093](https://doi.org/10.1109/iswcs.2018.8491093)

### Resilience Frameworks
- Sterbenz, J.P.G. et al. (2010). "Resilience and survivability in communication networks: Strategies, principles, and survey of disciplines." [PDF](https://resilinets.org/papers/Sterbenz-Hutchison-Cetinkaya-Jabbar-Rohrer-Scholler-Smith-2010.pdf)
- Sterbenz, J.P.G. et al. (2012). "Redundancy, Diversity, and Connectivity to Achieve Multilevel Network Resilience." [PDF](https://cdn.jprohrer.org/documents/publications/Sterbenz-Hutchison-Cetinkaya-Jabbar-Rohrer-Scholler-Smith-2012.pdf)
- Rohrer, J.P., Jabbar, A., & Sterbenz, J.P.G. (2012). "Path Diversification for Future Internet End-to-End Resilience and Survivability." [PDF](https://cdn.jprohrer.org/documents/publications/Rohrer-Jabbar-Sterbenz-2012.pdf)
- Grover, W.D. & Sack, A. (2007). "High availability survivable networks: When is reducing MTTR better than adding protection capacity?" DRCN 2007. DOI: [10.1109/drcn.2007.4762261](https://doi.org/10.1109/drcn.2007.4762261)
- TU Munich (2016). "Resilience Metrics." [PDF](https://www.net.in.tum.de/fileadmin/TUM/NET/NET-2016-09-1/NET-2016-09-1_02.pdf)

### Standards
- 3GPP TS 37.340 v18.1.0 (Release 18): Multi-connectivity. [ETSI](https://www.etsi.org/deliver/etsi_ts/137300_137399/137340/18.01.00_60/ts_137340v180100p.pdf)
- Broadband Forum TR-348: Hybrid Access Architecture. [PDF](https://www.broadband-forum.org/pdfs/tr-348-1-0-0.pdf)
- Broadband Forum TR-378: Hybrid Access Nodal Requirements. [PDF](https://www.broadband-forum.org/pdfs/tr-378-1-0-0.pdf)
- IETF RFC 8157: GRE Tunnel Bonding. [RFC](https://www.ietf.org/rfc/rfc8157.html)
- ITU-T Y.1541: Network performance objectives. [ITU](https://www.itu.int/rec/T-REC-Y.1541)
- ITU-T L-series Supplement 35: Disaster management for network resilience. [ITU](https://www.itu.int/itu-t/recommendations/rec.aspx?id=13344&lang=en)

### Regulation & Policy
- UK Ofcom (2024). "Network and Service Resilience Guidance." [Ofcom](https://www.ofcom.org.uk/internet-based-services/network-security/resilience-guidance)
- UK Government (2024). "Communication providers: ensuring telecom services are resilient." [GOV.UK](https://www.gov.uk/government/publications/communication-providers-how-to-ensure-networks-are-resilient/communication-providers-ensuring-telecom-services-are-resilient)
- UK Parliament Joint Committee on National Security (2025). "Subsea telecommunications cables: resilience and crisis preparedness." [Report](https://publications.parliament.uk/pa/jt5901/jtselect/jtnatsec/723/report.html)
- Kenya Communications Authority (2023). "Guidelines for Network Redundancy, Resilience and Diversity." [PDF](https://www.ca.go.ke/sites/default/files/2023-06/Guidelines-for-Network-RedundancyResilience-and-Diversity-for-ICT-Networks-in-Kenya-1.pdf)
- Taiwan MODA (2025). "Taiwan-Matsu Subsea Cable No. 3 Severed; Backup Microwave Activated." [Press Release](https://ipfs.moda.gov.tw/en/press/press-releases/19582.html)

### Military PACE
- Ryan, S. (2013). "PACE Communications Planning." Infantry Magazine. [PDF](https://www.moore.army.mil/infantry/magazine/issues/2013/Jul-Sep/pdfs/Ryan.pdf)
- Burnett (n.d.). "PACE Plans." MIPB. [PDF](https://mipb.ikn.army.mil/media/rivo5pmp/burnett_pace.pdf)
- Torrence (2025). "PACE Communications Card (MDS2)." Modern War Institute, West Point. [PDF](https://mwi.westpoint.edu/wp-content/uploads/2025/10/Torrence_PACE-Communications-Card.pdf)
- Systematic (n.d.). "Creating Effective Military Communications with PACE Plans." [Web](https://systematic.com/us/industries/defense/products/deep-dives/pace-communications/)

### Submarine Cable & Satellite Backup
- Recorded Future (2025). "Submarine Cable Security at Risk." [Report](https://www.recordedfuture.com/research/submarine-cables-face-increasing-threats)
- New Space Economy (2026). "Satellite Communications Backup for Undersea Cable Threats." [Article](https://newspaceeconomy.ca/2026/05/11/satellite-communications-backup-for-undersea-cable-threats/)

### Multi-Technology Planning
- TU Munich (2025). "Planning for Reliable Multi-Technology Networks." [PDF](https://mediatum.ub.tum.de/doc/1849898/1849898.pdf)
- MDPI Sensors (2022). "Hybrid Satellite–Terrestrial Networks toward 6G: Key Technologies and Open Issues." [Link](https://www.mdpi.com/1424-8220/22/21/8544)
- MDPI Sensors (2025). "Analysis of SD-WAN Architectures and Techniques for Efficient Traffic Control Under Transmission Constraints." [Link](https://www.mdpi.com/1424-8220/25/20/6317)
