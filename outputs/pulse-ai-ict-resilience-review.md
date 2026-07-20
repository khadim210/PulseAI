# Peer Review: PULSE-AI — Digital Sovereignty and Disaster Resilience

**Artifact:** `BrouillonArticle.md`  
**Verdict: REJECT (Major Revision required before any resubmission)**  
**Review date:** 2026-07-19

---

## Verdict Summary

This draft proposes PULSE-AI, a framework for assessing national ICT resilience in disaster contexts. The topic is timely and relevant. However, the paper has **multiple fatal and major issues** that preclude acceptance at any peer-reviewed venue in its current form: (1) the manuscript is materially incomplete — it ends abruptly after the NDRS formula with no Discussion, Evaluation, Limitations, Conclusion, or References; (2) it misses the most directly relevant prior work, including the **ISOC Pulse Internet Resilience Index** (which shares both the name "Pulse" and the domain of per-country internet/ICT resilience scoring) and the **UN ESCAP E-Resilience Monitoring Toolkit** (a 5-pillar ICT resilience framework with pilot country data); (3) there is zero empirical validation — no case study, pilot data, expert survey, or simulation; (4) the AI layer is purely aspirational with no technical substance; and (5) the scoring methodology lacks justification for equal weighting, indicator operationalization, and data sources. The paper reads as a concept note or early proposal outline, not a submittable research paper.

---

## Criterion-by-Criterion Assessment

### 1. Novelty — FATAL

**The paper's central novelty claim is that no framework integrates digital sovereignty, telecommunications resilience, AI-enabled disaster management, emergency communications, data governance, and inclusion. This claim is not adequately supported and is partially falsified by existing work the paper does not cite.**

Key missing prior work:

| Framework | Overlap with PULSE-AI | Citation in paper |
|-----------|----------------------|-------------------|
| **ISOC Pulse Internet Resilience Index (IRI)** | Same name ("Pulse"), per-country ICT resilience scoring (out of 100), weighted indicators, covers infrastructure redundancy, routing resilience, market concentration | ❌ Not cited |
| **UN ESCAP E-Resilience Monitoring Toolkit** | 5 pillars (Infrastructure, Policy, Digital, Data, Hazard & Exposure), pilot country profiles, ICT + disaster resilience integration | ❌ Not cited |
| **UNDP Digital Disaster Risk Reduction Maturity Model (DDRRMM)** | Maturity model for digital DRR, aligned with Sendai, SDGs | ❌ Not cited |
| **Digital Sovereignty Assessment Matrix (SDIA)** | Assesses data sovereignty, infrastructure sovereignty, operational sovereignty for policymakers | ❌ Not cited |
| **BRICS Digital Sovereignty Index (DSI)** | Multi-country digital sovereignty index with structured assessment | ❌ Not cited |
| **ITU L.Sup35** | Framework for disaster management, network resilience and recovery | ❌ Not cited |
| **ATU/AFRINIC/ISOC Model Framework for Internet Resilience in Africa** | Internet resilience framework specifically for Africa/developing countries | ❌ Not cited |
| **UNDP Digital Readiness Assessment (DRA)** | National digital transformation assessment with actionable recommendations | ❌ Not cited |

**The ISOC Pulse IRI is an especially critical omission.** It is an operational, data-backed, per-country internet resilience index — precisely what PULSE-AI aspires to be — and it shares the "Pulse" name. Any reviewer familiar with the ISOC ecosystem will immediately flag this. The authors must either differentiate clearly from Pulse IRI or rename the framework.

The UN ESCAP E-Resilience Toolkit is equally damaging: it already integrates ICT infrastructure assessment with disaster resilience across 5 pillars and has been piloted in multiple countries. PULSE-AI's claimed gap (no integrated ICT + disaster resilience framework) is substantially weakened by this prior work.

**Section 2 (Related Works)** lists 7 indices/frameworks as bullet points but provides no substantive analysis of any of them — no comparison of what each covers vs. what it misses, no table, no gap analysis. The claim that "few frameworks simultaneously consider [the listed dimensions]" is asserted without evidence.

> **Recommendation:** Conduct a systematic comparison table of existing frameworks (NCSI, GCI, NRI, IDI, INFORM, Sendai, E-Resilience Toolkit, Pulse IRI, DDRRMM, DRA, DSI) showing which dimensions each covers. Demonstrate concretely what PULSE-AI adds. Address the naming conflict with ISOC Pulse.

---

### 2. Empirical Rigor — FATAL

There is **no empirical content whatsoever** in this draft:

- No case study applying NDRS to any country
- No pilot data or illustrative scoring
- No expert survey validating dimensions or weights
- No simulation or scenario analysis
- No comparison of PULSE-AI scores against existing index scores for the same countries

For a framework paper proposing a composite index, the absolute minimum expected is either (a) a pilot application to 2–3 countries with real data demonstrating the index produces meaningful, discriminating scores, or (b) an expert validation (e.g., Delphi method) of the dimension selection and weighting.

Without any empirical grounding, the reviewer cannot assess whether NDRS produces useful, valid, or discriminating results. The 10 equally-weighted dimensions could be redundant, could fail to differentiate countries, or could be impossible to operationalize with available data.

> **Recommendation:** Apply NDRS to at least 3 countries (e.g., one high-income, one middle-income, one low-income) using publicly available data. Show indicator-level scores, discuss data availability challenges, and demonstrate the index discriminates meaningfully.

---

### 3. Baselines & Comparisons — MAJOR

The paper cites 7 existing indices but makes **no quantitative or structured qualitative comparison**. There is no:

- Feature comparison table (which dimensions each index covers)
- Correlation analysis (how would NDRS relate to existing index scores?)
- Gap analysis showing where existing indices fail and PULSE-AI fills in

The Related Works section (§2) is entirely enumerative — it lists names without analyzing their methodologies, strengths, or limitations.

> **Recommendation:** Add a structured comparison table. For each cited framework, specify: dimensions covered, scoring methodology, data sources, geographic scope, update frequency, and whether it addresses disaster resilience specifically.

---

### 4. Reproducibility — MAJOR

The NDRS is defined as a simple additive formula of 10 sub-scores, each out of 100, totaling 1000. However:

- **No indicator definitions**: What specific measurable indicators compose "Telecommunications Connectivity" or "Digital Sovereignty"? How many sub-indicators per dimension?
- **No data sources specified**: Where would a practitioner obtain the data to compute each sub-score?
- **No scoring rules**: How are raw data values mapped to the 0–100 scale? Min-max normalization? Threshold-based? Expert scoring?
- **No weighting justification**: All 10 dimensions are equally weighted (100 points each). This is a methodological choice that requires explicit justification (see §5 below).

The formula `NDRS = ICTR + EC + DS + CSC + CYB + DG + IA + AI + ER + INT` uses abbreviations not all of which are defined in the preceding text.

**There is a structural mismatch between §3 and §4:** The PULSE-AI acronym defines 6 dimensions (P, U, L, S, E, AI), but the NDRS table lists 10 scoring dimensions. The mapping between the 6 conceptual dimensions and the 10 scored dimensions is never explained. For example, where does "Cybersecurity" (a scored dimension) sit within the PULSE acronym? This creates confusion about whether PULSE-AI is a 6-dimension or 10-dimension framework.

> **Recommendation:** (1) Provide a mapping table from PULSE acronym → NDRS dimensions. (2) Define 3–5 measurable indicators per NDRS dimension with data sources. (3) Specify the scoring/normalization methodology. (4) Justify the weighting scheme.

---

### 5. Methodological Soundness — MAJOR

**Equal weighting** is the most common but also the most criticized approach in composite index construction. The literature is clear that equal weighting implicitly assumes all dimensions are equally important and uncorrelated — both of which are unlikely to hold for PULSE-AI's dimensions:

- *Correlation concern*: "Telecommunications Connectivity" and "Ubiquity" likely overlap substantially. "Cybersecurity" and "Data Governance" share considerable conceptual space. Countries with high "AI & IoT Readiness" almost certainly have high "Telecommunications Connectivity." Equal weighting of correlated dimensions effectively double-counts certain underlying factors.

- *Importance concern*: Is "Energy Resilience" truly as important as "Emergency Communications" for disaster resilience? The framework provides no argument.

The OECD/JRC Handbook on Constructing Composite Indicators (2008) — the standard methodological reference — explicitly warns against unjustified equal weighting and recommends sensitivity analysis. The Australian Natural Disaster Resilience Index (Parsons et al., 2020) provides a good example of methodological rigor in this exact domain.

A comparative analysis of disaster resilience composite indicators (Beccari, 2016, PLOS Currents Disasters) found that ~⅔ of resilience indices use equal weighting with simple addition, but also noted this as a methodological weakness requiring robustness checks.

> **Recommendation:** (1) Justify equal weighting or explore alternatives (PCA, expert-derived weights, benefit-of-the-doubt). (2) Conduct sensitivity analysis showing NDRS rankings are stable under alternative weighting schemes. (3) Test for dimension correlations.

---

### 6. AI Layer Substance — MAJOR

The "AI" in PULSE-AI is its distinguishing branding, yet the AI component (§3, "AI: Artificial Intelligence Layer") consists of 5 bullet points:

- Predictive analytics
- Infrastructure anomaly detection
- Risk assessment
- Disaster simulation
- Dynamic resilience scoring

There is **no technical detail** on any of these:

- What models or algorithms? (ML classifiers? Time-series forecasting? Graph neural networks for infrastructure modeling?)
- What training data?
- What does "dynamic resilience scoring" mean operationally? How does AI modify the static NDRS?
- What IoT data sources feed the AI layer?
- What is the architecture? Edge? Cloud? Federated?

As written, the AI layer is indistinguishable from a wish list. A reviewer at any AI-adjacent venue (ACM, IEEE) will expect at minimum an architectural diagram, a description of the inference pipeline, and ideally a prototype or proof-of-concept.

> **Recommendation:** Either (a) provide technical substance for the AI layer (architecture, algorithms, data pipeline, prototype results) or (b) reframe the paper as a non-AI framework paper and drop "AI-enabled" from the title. Option (a) is strongly preferred if targeting an AI venue.

---

### 7. Completeness — FATAL

The manuscript **ends abruptly** after the NDRS formula in §4. The following standard sections are entirely missing:

- **§5 Discussion**: Interpretation of the framework, comparison with existing approaches, implications for policymakers
- **§6 Case Study / Evaluation**: Application to real-world data
- **§7 Limitations**: Acknowledged weaknesses, data availability challenges, scope constraints
- **§8 Conclusion**: Summary of contributions, future work
- **References**: Zero citations — the paper names 7 frameworks/indices in §2 but provides no bibliographic references

The absence of a References section alone would be grounds for desk rejection at any academic venue.

> **Recommendation:** Complete all missing sections. The References section should cite at minimum 25–30 sources for a framework paper of this scope.

---

### 8. Writing Quality — MAJOR

- **Citation density**: Zero inline citations throughout the entire text. Every factual claim ("The increasing frequency of natural disasters…", "Telecommunications networks have become essential…") needs supporting references.
- **Bullet-point overreliance**: Sections 2, 3, and 4 are almost entirely bullet lists. ACM venues expect flowing prose with argumentation, not taxonomic lists.
- **Abstract length**: At ~180 words, the abstract is adequate but could be more specific about contributions (currently reads as aspirational rather than reporting results).
- **Formality**: Generally appropriate, though some phrases are vague ("attempts to bridge these dimensions").
- **Section balance**: §1 Introduction is reasonable; §2 Related Works is thin; §3 Framework description is skeletal; §4 is incomplete.

> **Recommendation:** Convert bullet lists to structured prose. Add inline citations. Ensure each section makes an argument, not just a list.

---

## Structural Issues

### Mismatch between PULSE dimensions (6) and NDRS dimensions (10)

| PULSE Dimension | Plausible NDRS mapping | Confirmed in text? |
|----------------|----------------------|-------------------|
| P: Preparedness | ? (possibly Critical Services Continuity?) | ❌ |
| U: Ubiquity | Telecommunications Connectivity? Inclusion? | ❌ |
| L: Localization | Digital Sovereignty? | ❌ |
| S: Sustainability | Energy Resilience? | ❌ |
| E: Emergency | Emergency Communications? | ❌ |
| AI: Artificial Intelligence | AI and IoT Readiness? | ❌ |

This leaves Cybersecurity, Data Governance, Interoperability, and possibly others unmapped. The reader cannot determine the relationship between the conceptual framework (§3) and the scoring model (§4).

---

## Constructive Path Forward (Prioritized)

### Must-do before any resubmission (FATAL fixes)

1. **Complete the manuscript**: Add Discussion, Case Study/Evaluation, Limitations, Conclusion, and References sections.
2. **Add references**: Cite all named frameworks, add 25–30 relevant sources minimum.
3. **Address ISOC Pulse IRI and UN ESCAP E-Resilience Toolkit**: These are the two most directly relevant prior works. Either differentiate clearly or acknowledge significant overlap.
4. **Resolve the PULSE naming conflict**: ISOC's operational "Pulse" Internet Resilience Index creates a direct naming collision. Consider renaming or explicitly positioning against it.
5. **Add empirical content**: Pilot NDRS on 2–3 countries with real data.

### Should-do for competitive submission (MAJOR fixes)

6. **Operationalize indicators**: Define measurable sub-indicators per dimension with data sources.
7. **Map PULSE acronym → NDRS dimensions** explicitly.
8. **Justify or analyze weighting**: Sensitivity analysis under alternative weighting schemes.
9. **Substantiate the AI layer**: Architecture, algorithms, or prototype — or drop "AI-enabled" framing.
10. **Convert to prose**: Replace bullet-list sections with argumented text.

### Nice-to-have for strong submission (SUGGESTIONS)

11. Expert validation of dimensions (Delphi method or similar).
12. Comparison with an established index (e.g., correlate NDRS scores with NRI or GCI scores).
13. Open-source the scoring tool or provide a spreadsheet calculator for reproducibility.

---

## Sources

All external sources consulted during this review:

1. **ISOC Pulse Internet Resilience Index (IRI)** — per-country internet resilience scoring, weighted indicators  
   https://pulse.internetsociety.org/en/resilience/

2. **ISOC Pulse IRI Methodology (April 2025, v1.0)**  
   https://pulse.internetsociety.org/documents/19/Internet-Society-Pulse-IRI-Methodology-Apr-2025-v1.0-Final-EN.pdf

3. **UN ESCAP E-Resilience Monitoring Toolkit** — 5-pillar ICT resilience framework with pilot country profiles  
   https://www.unescap.org/sites/default/d8files/knowledge-products/E-resilience-Monitoring-Toolkit-Methodological-Notes-and-Pilot-Countries-Profiles.pdf

4. **UN ESCAP E-Resilience Pillars presentation**  
   https://www.unescap.org/sites/default/d8files/event-documents/E-resilience%2C%20Eng.pdf

5. **UNDP Digital Disaster Risk Reduction Maturity Model (DDRRMM), White Paper v4.0 (2022)**  
   https://www.undp.org/sites/g/files/zskgke326/files/2022-09/DDRRMM%20White%20Paper%20Version%204.0%20%28FINAL%29_1%20September%202022.pdf

6. **UNDP Digital Readiness Assessment (DRA)**  
   https://www.undp.org/digital/dra

7. **Digital Sovereignty Assessment Matrix — Sustainable Digital Infrastructure Alliance**  
   https://ided.digital/governments/policy-tools/digital-sovereignty-assessment-matrix

8. **BRICS Digital Sovereignty Index Report (2026)**  
   https://thetricontinental.org/wp-content/uploads/2026/05/BRICS_Digital_Sovereignty_Index_Report_EN.pdf

9. **ITU L.Sup35 — Framework of disaster management for network resilience and recovery**  
   https://itu.int/rec/recommendation.asp?lang=en&parent=T-REC-L.Sup35-201706-I

10. **ATU/AFRINIC/ISOC Model Framework for Building Internet Resilience in Africa (2025)**  
    https://atuuat.africa/wp-content/uploads/2025/07/Final-Model-Framework-for-Building-and-Sustaining-Internet-Resilience-in-Africa-Post-Validation-0206-3.pdf

11. **Beccari (2016) — A Comparative Analysis of Disaster Risk, Vulnerability and Resilience Composite Indicators, PLOS Currents Disasters**  
    https://currents.plos.org/disasters/article/a-comparative-analysis-of-disaster-risk-vulnerability-and-resilience-composite-indicators/

12. **Greco et al. (2019) — On the Methodological Framework of Composite Indices: A Review of the Issues of Weighting, Aggregation, and Robustness, Social Indicators Research**  
    https://link.springer.com/content/pdf/10.1007/s11205-017-1832-9.pdf

13. **Australian Natural Disaster Resilience Index, Vol. II — Index Design and Computation**  
    https://www.preventionweb.net/files/72870_chapter3publicationready30082019l.pdf

14. **World Bank — Moving toward an outcome-based approach for digital sovereignty (2025)**  
    https://blogs.worldbank.org/en/digital-development/moving-toward-an-outcome-based-approach-for-digital-sovereignty-

15. **PULSE: Platform for European Medical Support during major emergencies (CESS)** — unrelated "PULSE" in emergency domain  
    http://www.cess-net.eu/en/projects/pulse.html
