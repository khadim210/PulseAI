# Critical Infrastructure Interdependency: A Literature Review

**Date:** 2026-07-19  
**Scope:** Definitions, modeling approaches, empirical evidence, resilience assessment, governance, and emerging trends in critical infrastructure interdependency research.

---

## 1. Introduction

Modern societies depend on a tightly coupled web of critical infrastructure systems (CIS) — electric power, telecommunications, water, transportation, natural gas, and healthcare — whose interactions generate emergent vulnerabilities invisible at the single-system level. The study of critical infrastructure interdependency emerged as a distinct field after the cascading failures of the late 1990s and accelerated sharply post-9/11, when national-security concerns motivated systematic analysis of how disruptions propagate across sector boundaries.

This review synthesizes the literature from 2001–2026, organized around six questions: (1) How are interdependencies defined and classified? (2) What modeling methods exist? (3) What do empirical cascading-failure events reveal? (4) How do interdependencies affect resilience quantification? (5) What governance frameworks address cross-sector coupling? (6) What emerging trends are reshaping the field?

---

## 2. Definitions and Taxonomy of Interdependencies

### 2.1 The Rinaldi Framework (2001)

The foundational taxonomy was proposed by Rinaldi, Peerenboom, and Kelly (2001), who defined four classes of interdependency:

| Type | Definition | Example |
|------|-----------|---------|
| **Physical** | Output of one system is a material input to another via a physical linkage | Water cooling for a power plant; electricity for water pumps |
| **Cyber** | State of one system depends on information transmitted through ICT | SCADA control of rail signals via telecom networks |
| **Geographic** | Spatial proximity causes correlated exposure to the same local hazard | Co-located utility conduits damaged by a single excavation |
| **Logical** | All other coupling mechanisms (policy, market, human decisions) | Financial markets reacting to infrastructure outage news |

This framework remains the most widely cited classification (~2,700+ citations on IEEE Xplore as of 2026) and anchors most subsequent work.

### 2.2 Alternative and Extended Classifications

Several authors have refined or replaced the Rinaldi taxonomy:

- **Zimmerman (2001):** Functional vs. Spatial — a simpler two-category scheme.
- **Dudenhoeffer et al. (2006):** Physical, Informational, Geospatial, Policy — replaces "cyber" with "informational" and "logical" with "policy."
- **Zhang & Peeta (2011):** Physical, Functional, Budgetary, Market, Economic — emphasizes economic coupling and introduces the concept of *functional substitutability*.
- **Sharkey et al. (2016):** Operational, Failure, Restoration — classifies by *management phase* rather than coupling mechanism.
- **Sun et al. (2020):** Hazard-related, Damage-related, Restoration-related, Functionality-related — aligns with resilience analysis phases.

### 2.3 Dependency vs. Interdependency

A critical terminological distinction: **dependency** is *unidirectional* (System A relies on System B), while **interdependency** is *bidirectional* (A and B mutually affect each other). In practice, bidirectional interdependencies often emerge from long chains of unidirectional dependencies through intermediate components (Sun et al. 2022).

---

## 3. Modeling Methodologies

The modeling landscape has been comprehensively reviewed by Ouyang (2014) and Sun, Bocchini & Davison (2022). Building on Sun et al.'s implementation-based classification, approaches can be grouped into three families:

### 3.1 Dependency Tables

| Sub-type | Input Data | Strengths | Limitations |
|----------|-----------|-----------|-------------|
| Qualitative tables | Expert judgment, tabletop exercises | Intuitive, no computation | Cannot quantify coupling strength |
| Survey-based quantitative | Structured expert surveys | Captures scenario-specific coupling | Context-dependent, not transferable |
| Correlation-based | Historical failure/recovery data | Empirically grounded | Correlation ≠ causation; post hoc fallacy risk |
| Graph-theory adjacency matrices | Network topology data | Rigorous, component-level | Requires complete topology knowledge; high computational cost |
| Economic input-output tables | National accounts inter-sector transactions | Leverages existing economic data | System-level only; assumes linearity |

### 3.2 Interaction-Rule-Based Models

**Agent-Based Models (ABMs):** Originating at Sandia National Labs in the 1990s (Aspen, SMART II, CIMS), ABMs simulate infrastructure components and operators as autonomous agents following prescribed rules. Strengths include capturing emergent behaviors and heterogeneous decision-making. Weaknesses include calibration difficulty and computational expense for large systems.

**System Dynamics:** Using causal-loop and stock-flow diagrams to capture feedback effects over time. CIP/DSS (Los Alamos) is a notable implementation. Effective for understanding temporal dynamics but limited in uncertainty quantification and component-level detail.

**Bayesian Networks:** Model conditional dependencies as directed probabilistic graphs. Excel at uncertainty quantification and allow integration of heterogeneous data (expert judgment, measurements, simulations). Computational complexity grows sharply with network size.

**Discrete Event Simulation:** Fault trees (top-down) and event trees (bottom-up) capture cascading sequences through Boolean logic. Extended by Petri nets for temporal dynamics.

**Input-Output Models (IIM/DIIM):** Based on Leontief's economic framework, Haimes & Jiang (2001) developed the Inoperability Input-Output Model to propagate disruptions through economic interdependency matrices. The Dynamic IIM (Lian & Haimes 2006) adds temporal evolution. Computationally efficient due to linearity but limited to system-level economic coupling.

**Optimization Models:** Minimize/maximize resilience objectives under interdependency constraints (resource sharing, precedence, functionality dependencies). Often integrated with network models for restoration planning.

### 3.3 Data-Driven Approaches

A nascent but growing category (Sun et al. 2022 classify it as "low development maturity"):

- **Text mining:** Zhou et al. (2020) extracted interdependent failure patterns from newspaper reports of Hong Kong pipe bursts.
- **Social media analytics:** Roy et al. (2020) used supervised learning on social media to detect co-occurring service disruptions.
- **Reinforcement learning:** Lopez et al. (2018) trained agents on i2Sim emergency-response simulations.
- **Machine learning for recovery prediction:** Ghaneshvar (2019) predicted recovery times from optimization-generated scenarios.

### 3.4 Network Science: Interdependent Networks Theory

A parallel theoretical tradition developed in statistical physics after Buldyrev et al. (2010) published "Catastrophic cascade of failures in interdependent networks" in *Nature*. This seminal paper (4,376+ citations) demonstrated that coupled networks exhibit first-order (abrupt) percolation transitions — fundamentally different from the continuous transitions in isolated networks. Key findings:

- Random failure of a small fraction of nodes in one network can trigger a complete collapse of both networks.
- Interdependent networks are inherently more fragile than their isolated counterparts.
- The cascading failure process follows iterative rounds of mutual dependency checking.

This theoretical framework has generated a large body of work on robustness, targeted attacks, and design strategies for interdependent network resilience.

### 3.5 Comparative Summary

```
┌────────────────────────��────────────────────────────────────────────┐
│              INTERDEPENDENCY MODELING APPROACHES                      │
├──────────────────────┬──────────────────────┬───────────────────────┤
│  DEPENDENCY TABLES   │  INTERACTION RULES   │    DATA-DRIVEN        │
├──────────────────────┼──────────────────────┼───────────────────────┤
│ • Qualitative tables │ • Agent-based models │ • Text mining         │
│ • Survey-based       │ • System dynamics    │ • Social media NLP    │
│ • Correlation-based  │ • Bayesian networks  │ • Reinforcement       │
│ • Graph adjacency    │ • Discrete event sim │   learning            │
│ • Input-output (IIM) │ • Optimization       │ • Supervised ML       │
│                      │ • Population mobility│ • Digital twins       │
└──────────────────────┴──────────────────────┴───────────────────────┘
         High maturity        Medium-High            Low maturity
         Low-Med compute      Med-High compute       Variable compute
```

---

## 4. Empirical Case Studies of Cascading Failures

### 4.1 The 2003 Italy Blackout

On September 28, 2003, a 380 kV transmission line in Switzerland tripped due to tree contact. The resulting overload cascaded through interconnectors, isolating Italy from the European grid within 12 seconds. Over 56 million people lost power for up to 48 hours. The event demonstrated **power–internet interdependency**: the internet relied on power for routers and switches, while power grid management relied on internet-based SCADA. Buldyrev et al. (2010) used this event to validate their theoretical model of interdependent network cascades.

### 4.2 Hurricane Katrina (2005)

Katrina exposed physical and geographic interdependencies across power, water/wastewater, transportation, and oil/gas systems in the Gulf Coast. Flooding disabled pumping stations (water depends on power), power restoration required road access (power depends on transport), and oil refineries required both power and water.

### 4.3 Fukushima Daiichi (2011)

The earthquake-tsunami sequence demonstrated how geographic co-location (geographic interdependency) and physical interdependency (cooling water depending on electrical pumps, backup generators flooded) could cascade beyond design-basis scenarios.

### 4.4 Texas Winter Storm Uri (2021)

A landmark case for electricity–natural gas interdependency. Key findings from the literature:

- Natural gas supply failed because wellheads and processing plants lost electric power (physical interdependency) and froze (climate exposure).
- Power generation failed because ~48% of Texas generation capacity was offline — significantly from gas plants that lost fuel supply.
- Water systems failed because treatment plants and pumping stations lost power.
- Over 4.5 million customers lost power at peak; estimated $130 billion in economic losses (Busby et al. 2021).
- The event highlighted that **electricity-gas interdependency has become the dominant vulnerability** in modern energy systems, a coupling that intensifies as gas displaces coal and nuclear.

### 4.5 COVID-19 Pandemic (2020–2022)

The pandemic revealed *logical* and *functional* interdependencies: workforce disruptions cascading through labor-intensive infrastructure operations; supply chain failures affecting spare parts for maintenance; demand shifts (reduced transport, increased telecom/power for remote work) altering the baseline coupling structure.

---

## 5. Resilience and Risk Assessment

### 5.1 Resilience Metrics Under Interdependency

The resilience "triangle" (Bruneau et al. 2003) — measuring functionality loss and recovery time — must be extended when systems are coupled. Key frameworks:

- **Multi-layer resilience curves:** Separate functionality tracking per system with coupling constraints on recovery sequencing.
- **Multiplex network resilience:** Dong et al. (2024) conducted a systematic review finding increasing use of multiplex (multi-layer) networks to represent infrastructure coupling under disasters.
- **Community-scale resilience:** NIST's IN-CORE platform (Interdependent Networked Community Resilience Modeling Environment) combines hazard, infrastructure, and socioeconomic models.

### 5.2 Risk Amplification Through Coupling

Interdependencies amplify risk in three ways:
1. **Cascade amplification:** Initial failure propagates to dependent systems (multiplicative rather than additive impact).
2. **Recovery complication:** Restoration is sequentially constrained — you cannot restore the water system without restoring power first.
3. **Common-mode exposure:** Geographic interdependency means multiple systems face correlated hazard intensities.

---

## 6. Policy and Governance Frameworks

### 6.1 United States

- **Presidential Policy Directive 21 (PPD-21, 2013):** Established 16 critical infrastructure sectors and mandated consideration of "cross-sector dependencies" in risk assessments.
- **National Security Memorandum 22 (NSM-22, April 2024):** Replaced PPD-21. Explicitly recognizes "global interconnectedness and interdependencies of critical infrastructure" and mandates that federal efforts account for cross-sector coupling. Designates DHS/CISA as the lead coordinating agency.
- **NIST Community Resilience Planning Guide:** Provides methodology for assessing infrastructure interdependencies at the community scale.
- **IN-CORE (NIST-funded):** Open-source computational environment for quantitative interdependent infrastructure resilience assessment.

### 6.2 European Union

- **EU Critical Entities Resilience (CER) Directive 2022/2557:** Entered force January 2023; transposition deadline October 2024. Shifts from protecting *assets* to strengthening resilience of *entities*. Explicitly acknowledges "increasingly interdependent Union economy" and mandates that Member States identify critical entities considering cross-sector dependencies.
- **NIS2 Directive (2022/2555):** Companion cybersecurity directive covering "essential" and "important" entities, recognizing cyber-physical interdependency.

### 6.3 International

The UN Sendai Framework for Disaster Risk Reduction (2015–2030) and various NATO Civil Preparedness standards reference infrastructure interdependency, though specific modeling mandates remain limited.

---

## 7. Emerging Trends and Open Challenges

### 7.1 Digital Twins for CI Interdependency

Multiple 2023–2024 papers explore digital twin frameworks for interdependent infrastructure:
- Real-time monitoring and predictive simulation of cascading failures.
- Integration of physical models with data streams for "living" interdependency models.
- Applications to power grid restoration considering road network interdependencies (NSF-funded research, 2024).
- Urban CI resilience assessment as complex socio-technical systems (Samod, 2024).

### 7.2 Cyber-Physical Coupling

As operational technology (OT) networks increasingly connect to IT systems, the *cyber* interdependency dimension intensifies. Recent work addresses:
- Multi-stage cyberattack propagation through smart grids (IET, 2023).
- Safety analysis for CPS under attack using digital twins (CSR 2024).
- The convergence of physical cascading failures with cyber-attack propagation.

### 7.3 Climate Change and Infrastructure Coupling

Climate change acts as a *threat multiplier* for interdependencies by:
- Increasing the frequency of extreme weather events that trigger correlated multi-system failures.
- Widening the geographic envelope of hazards (e.g., Texas freeze extending to unprepared southern systems).
- Stressing cooling-water/energy interdependencies under drought and heat.

### 7.4 Machine Learning and AI

- Graph neural networks for learning interdependency structures from operational data.
- Reinforcement learning for optimal restoration sequencing under uncertainty.
- Natural language processing for extracting interdependency information from unstructured reports.

### 7.5 Open-Source Tools

| Tool | Organization | Description |
|------|-------------|-------------|
| **IN-CORE** | NIST / Colorado State | Community resilience modeling with interdependent infrastructure |
| **HELICS** | DOE / GMLC | Co-simulation framework linking heterogeneous infrastructure simulators |
| **InfraRisk** | Academic | Python platform for interdependent water-power-transport failure simulation |
| **CI-network-sim** | Academic | Network-based cascading failure and resilience simulator |

---

## 8. Synthesis: Consensus, Disagreements, and Gaps

### 8.1 Points of Consensus

1. **Interdependencies amplify vulnerability.** Essentially all literature agrees that coupled systems are more fragile than isolated ones (Buldyrev et al. 2010; Ouyang 2014; Sun et al. 2022).
2. **The Rinaldi taxonomy remains useful** as a first-order classification, though extensions are needed for emerging coupling types.
3. **No single modeling approach dominates.** The choice depends on available data, analysis scale, and decision context.
4. **Data scarcity is the primary practical barrier** to applying interdependency models in real-world decision-making (Sun et al. 2022).
5. **Energy-telecom and energy-gas couplings are the most critical** interdependencies in modern infrastructure systems.

### 8.2 Active Disagreements

1. **Granularity:** System-level models (IIM) vs. component-level models (network/ABM). No consensus on which level is "correct" — likely context-dependent.
2. **Transferability:** Whether interdependency structures identified in one community/event generalize to others.
3. **Role of human factors:** Some argue that logical/organizational interdependencies are under-studied relative to physical coupling.
4. **First-order vs. continuous transitions:** The Buldyrev et al. theoretical prediction of abrupt collapse applies to idealized random networks; real infrastructure may exhibit intermediate behavior due to partial coupling and mitigation strategies.

### 8.3 Research Gaps

1. **Validation deficit:** Most models are validated only against single historical events or not at all. Systematic multi-event validation is rare.
2. **Dynamic interdependencies:** Coupling structures change over time (aging, upgrades, policy changes) — few models capture this evolution.
3. **Socio-technical coupling:** Integration of human behavior, organizational response, and social vulnerability with physical interdependency models remains underdeveloped.
4. **Scalability:** Moving from proof-of-concept demonstrations to city-scale or national-scale operational tools.
5. **Cross-border interdependencies:** Most frameworks are national; international coupling (energy grids, internet backbone, supply chains) is under-addressed.
6. **Standardized benchmarks:** No equivalent of well-known test cases (like IEEE bus systems for power grids) for interdependent infrastructure analysis.

---

## 9. Recommended Next Steps

For researchers entering this field:

1. **Start with:** Rinaldi et al. (2001) for conceptual foundations, Ouyang (2014) for modeling overview, Buldyrev et al. (2010) for network theory, Sun et al. (2022) for implementation-focused classification.
2. **Prioritize empirical validation:** Design studies around well-documented cascading events (Texas 2021 is particularly data-rich).
3. **Explore digital twin integration:** The convergence of IoT data, simulation models, and ML offers a path to real-time interdependency monitoring.
4. **Address the data challenge:** Contribute to open datasets and standardized benchmarks.
5. **Engage with policy:** The NSM-22 and EU CER Directive create mandates that practitioners must fulfill — academic models need to become usable tools.

---

## Sources

### Foundational Papers
- Rinaldi, S.M., Peerenboom, J.P., & Kelly, T.K. (2001). "Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies." *IEEE Control Systems Magazine*, 21(6), 11–25. DOI: [10.1109/37.969131](https://doi.org/10.1109/37.969131)
- Haimes, Y.Y. & Jiang, P. (2001). "Leontief-Based Model of Risk in Complex Interconnected Infrastructures." *J. Infrastructure Systems*, 7(1), 1–12. DOI: [10.1061/(ASCE)1076-0342(2001)7:1(1)](https://doi.org/10.1061/(asce)1076-0342(2001)7:1(1))
- Buldyrev, S.V. et al. (2010). "Catastrophic cascade of failures in interdependent networks." *Nature*, 464, 1025–1028. DOI: [10.1038/nature08932](https://www.nature.com/articles/nature08932)

### Major Reviews
- Ouyang, M. (2014). "Review on modeling and simulation of interdependent critical infrastructure systems." *Reliability Engineering & System Safety*, 121, 43–60. DOI: [10.1016/j.ress.2013.06.040](https://www.sciencedirect.com/science/article/abs/pii/S0951832013002056)
- Sun, W., Bocchini, P., & Davison, B.D. (2022). "Overview of Interdependency Models of Critical Infrastructure for Resilience Assessment." *Natural Hazards Review*, ASCE. [PDF](https://www.cse.lehigh.edu/~brian/pubs/2022/naturalhazardsreview/ASCE_ReviewInterdependencyModel_V2.pdf)
- Dong et al. (2024). "Multiplex networks in resilience modeling of critical infrastructure systems: A systematic review." *Reliability Engineering & System Safety*, 250. [Link](https://ideas.repec.org/a/eee/reensy/v250y2024ics0951832024003727.html)
- Palliyaguru et al. (2024). "Redefining Dependencies/Interdependencies of Critical Infrastructure." [PDF](https://radar.brookes.ac.uk/radar/file/16f6ccd3-1d8f-463e-8ba1-1ad1079f08c1/1/Redefining%20dependencies-interdependencies%20of%20critical%20infrastructure%20-%202024%20-%20Dasuni%20Palliyaguru%20Amaratunga%20Liyanawatta.pdf)
- "Resilience of interdependent infrastructure networks: Review and future directions." *Int. J. Critical Infrastructure Protection* (2025). DOI: [10.1016/j.ijcip.2025.100793](https://doi.org/10.1016/j.ijcip.2025.100793)

### Economic Models
- Santos, J.R. & Haimes, Y.Y. (2004). "Modeling the demand reduction input-output (I-O) inoperability due to terrorism." *Risk Analysis*.
- Haimes, Y.Y. et al. (2005). "Inoperability Input-Output Model for Interdependent Infrastructure Sectors. I: Theory and Methodology." *J. Infrastructure Systems*, 11(2). DOI: [10.1061/(ASCE)1076-0342(2005)11:2(67)](https://doi.org/10.1061/(asce)1076-0342(2005)11:2(67))
- Lian, C. & Haimes, Y.Y. (2006). "Managing the risk of terrorism to interdependent infrastructure systems through the dynamic inoperability input–output model." *Systems Engineering*, 9(3). DOI: [10.1002/sys.20051](https://doi.org/10.1002/sys.20051)

### Case Studies
- Busby, J.W. et al. (2021). "Cascading risks: Understanding the 2021 winter blackout in Texas." *Energy Research & Social Science*, 77. [Link](https://www.sciencedirect.com/science/article/pii/S2214629621001997)
- UCTE (2004). "Final Report of the Investigation Committee on the 28 September 2003 Blackout in Italy." [PDF](https://eepublicdownloads.entsoe.eu/clean-documents/pre2015/publications/ce/otherreports/20040427_UCTE_IC_Final_report.pdf)

### Policy Documents
- White House (2013). Presidential Policy Directive 21 (PPD-21). [CISA PDF](https://www.cisa.gov/sites/default/files/2023-01/ppd-21-critical-infrastructure-and-resilience-508_0.pdf)
- White House (2024). National Security Memorandum on Critical Infrastructure Security and Resilience (NSM-22). [CISA](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-security-memorandum-critical-infrastructure-security-and-resilience)
- EU (2022). Directive 2022/2557 on the resilience of critical entities (CER Directive). [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2557/oj)

### Digital Twins & Emerging Work
- "Improving the resilience of socio-technical urban critical infrastructures with digital twins." *Sustainable Analytics and Modeling* (2024). DOI: [10.1016/j.samod.2024.100036](https://doi.org/10.1016/j.samod.2024.100036)
- "Safety Analysis for Cyber-Physical Systems Under Cyber Attacks Using Digital Twin." *CSR 2024*. DOI: [10.1109/csr61664.2024.10679484](https://doi.org/10.1109/csr61664.2024.10679484)

### Open-Source Tools
- IN-CORE: https://github.com/IN-CORE/IN-CORE
- HELICS: https://github.com/GMLC-TDC/HELICS
- InfraRisk: https://github.com/srijithbalakrishnan/dreaminsg-integrated-model
