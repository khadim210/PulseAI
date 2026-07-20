import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import folium
from streamlit_folium import st_folium
from fpdf import FPDF
import base64
from pulse_ai.src.data_mgmt.manager import DataManager
from pulse_ai.src.engine.calculator import NDRSCalculator
from pulse_ai.src.engine.prediction_engine import RegionalPredictionEngine, CableRiskEngine
from pulse_ai.src.api.weather_client import ClimateAPIClient
from pulse_ai.src.ai.assessment import RiskAssessor

# --- Constants & Data ---
DIMENSION_INTERPRETATIONS = {
    "Telecommunications Connectivity": "Mesure la disponibilité et la qualité des infrastructures de transport de données. Un score bas indique des zones blanches ou des réseaux saturés.",
    "Emergency Communications": "Capacité du pays à maintenir des réseaux de secours et des protocoles d'urgence prioritaires lors d'une crise.",
    "Digital Sovereignty": "Niveau de contrôle national sur les données, le cloud et les infrastructures critiques pour éviter la dépendance étrangère.",
    "Critical Services Continuity": "Capacité des services essentiels (santé, banque, administration) à rester opérationnels via des canaux numériques.",
    "Cybersecurity": "Niveau de protection contre les intrusions, les ransomwares et la robustesse des protocoles de chiffrement.",
    "Data Governance": "Qualité du cadre légal et technique pour la gestion, la protection et le partage sécurisé des données nationales.",
    "Inclusion and Accessibility": "Mesure l'accès équitable aux services numériques pour toutes les couches de la population, incluant les zones rurales.",
    "AI and IoT Readiness": "Capacité technique et humaine à déployer des solutions d'IA et de capteurs IoT pour la gestion des crises.",
    "Energy Resilience": "Stabilité de l'alimentation électrique des centres de données et des tours télécoms via des sources redondantes.",
    "Interoperability": "Capacité des différents systèmes et réseaux à communiquer entre eux, surtout lors de l'intervention de partenaires internationaux."
}

def render_radar_chart(scores, title):
    """Renders a Plotly radar chart for the 10 dimensions."""
    categories = list(scores.keys())
    values = list(scores.values())

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Resilience'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=False,
        title=title,
        margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig, width='stretch')

def render_map(country_data, selected_region=None, event_coords=None):
    """Renders an interactive map of the country's regions and cable stations."""
    regions = country_data["regions"]
    first_reg = list(regions.values())[0]
    m = folium.Map(location=first_reg["center"], zoom_start=6)

    for reg_id, reg_info in regions.items():
        color = "blue" if reg_id == selected_region else "gray"
        folium.CircleMarker(
            location=reg_info["center"],
            radius=10,
            popup=f"Region: {reg_id}",
            color=color,
            fill=True,
            fill_color=color
        ).add_to(m)

    for station in country_data.get("landing_stations", []):
        folium.Marker(
            location=station["coords"],
            popup=f"Cable Station: {station['name']}",
            icon=folium.Icon(color="red", icon="anchor", prefix="fa")
        ).add_to(m)

    if event_coords:
        folium.Marker(
            location=event_coords,
            popup="Active Disaster Event",
            icon=folium.Icon(color="orange", icon="warning")
        ).add_to(m)

    return st_folium(m, width=700, height=500)

def generate_pdf_report(country_name, region_id, event_type, scores, total_score, risk_level):
    """Generates a detailed PDF report."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"PULSE-AI Resilience Report: {country_name}", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Region: {region_id}", ln=True)
    pdf.cell(0, 10, f"Scenario: {event_type if event_type else 'Baseline'}", ln=True)
    pdf.cell(0, 10, f"Final National Digital Resilience Score (NDRS): {total_score:.2f} / 1000", ln=True)
    pdf.cell(0, 10, f"Risk Level: {risk_level}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Detailed Dimension Analysis", ln=True)
    pdf.set_font("Arial", "", 10)

    for dim, score in scores.items():
        pdf.ln(5)
        pdf.set_font("Arial", "B", 10)
        pdf.cell(0, 10, f"{dim}: {score:.2f}/100", ln=True)
        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 10, DIMENSION_INTERPRETATIONS.get(dim, "No interpretation available."))

    return pdf.output(dest="S").encode("latin-1")

def main():
    st.set_page_config(page_title="PULSE-AI | Real-Time Resilience", layout="wide")
    st.title("🌐 PULSE-AI : Système de Surveillance Prédictive")
    st.markdown("### Analyse Régionale, Géoclimatique et Infrastructurelle")

    with open("pulse_ai/data/geodata.json", "r") as f:
        import json
        geodata = json.load(f)

    pred_engine = RegionalPredictionEngine()
    weather_client = ClimateAPIClient()
    cable_engine = CableRiskEngine()

    # Sidebar
    st.sidebar.header("⚙️ Contrôle du Système")
    country_id = st.sidebar.selectbox("Pays à surveiller:", list(geodata["countries"].keys()))
    country_data = geodata["countries"][country_id]

    st.sidebar.subheader("📡 Flux Temps Réel")
    if st.sidebar.button("Scanner les alertes climatiques"):
        events = weather_client.fetch_active_disasters()
        st.sidebar.write(f"🚨 {len(events)} événements détectés mondialement.")
        for e in events:
            st.sidebar.warning(f"{e['type']} - Intensité: {e['intensity']}")
            st.session_state.active_event = e

    region_id = st.sidebar.selectbox("Sélecteur de Région:", list(country_data["regions"].keys()))

    # Session state for predictions
    if 'current_event' not in st.session_state:
        st.session_state.current_event = "None"
    if 'current_intensity' not in st.session_state:
        st.session_state.current_intensity = 1.0

    # Layout: Radar Chart (Angular Schema) Top
    st.subheader("🕸️ Schéma Angulaire de Résilience (Profil Actuel)")

    # Ensure current_scores is initialized for the selected country
    if 'current_scores' not in st.session_state or st.session_state.get('last_country') != country_id:
        st.session_state.current_scores = country_data["baseline_scores"].copy()
        st.session_state.last_country = country_id

    render_radar_chart(st.session_state.current_scores, f"Profil de Résilience : {country_data['name']}")

    st.divider()

    # Layout: Map below Radar Chart
    st.subheader("📍 Carte de Connectivité et Risques")
    event_coords = st.session_state.get("active_event", {}).get("coords") if 'active_event' in st.session_state else None
    render_map(country_data, selected_region=region_id, event_coords=event_coords)

    st.divider()

    col_params, col_res = st.columns([1, 2])

    with col_params:
        st.markdown("**Paramètres de Simulation**")
        event_type = st.selectbox("Simuler un événement:", ["None", "Earthquake", "Flood", "Storm", "CyberAttack"])
        intensity = st.slider("Intensité de l'événement", 1.0, 3.0, 1.0)

        if st.button("Lancer la Prédiction"):
            st.session_state.current_event = event_type
            st.session_state.current_intensity = intensity

    with col_res:
        if st.session_state.current_event != "None":
            res = pred_engine.predict_regional_impact(country_id, region_id, st.session_state.current_event, st.session_state.current_intensity)

            # Cable risk
            cable_mult = 1.0
            if st.session_state.current_event in ["Earthquake", "Flood"]:
                cable_mult = cable_engine.calculate_cable_impact(country_id, [country_data["landing_stations"][0]["name"]], geodata)

            final_survival = res["survival_prob"] * cable_mult
            total_regional_score = NDRSCalculator.calculate_score(res["predicted_scores"])

            st.metric("Survie Prédictive Régionale", f"{final_survival*100:.1f}%")
            st.markdown(f"**Niveau de Risque :** <span style='color:{RiskAssessor.get_risk_color(res['risk_level'])}; font-weight:bold;'>{res['risk_level']}</span>", unsafe_allow_html=True)

            # PDF Export
            pdf_data = generate_pdf_report(country_data["name"], region_id, st.session_state.current_event, res["predicted_scores"], total_regional_score, res["risk_level"])
            st.download_button(
                label="📄 Exporter le rapport détaillé (PDF)",
                data=pdf_data,
                file_name=f"pulse_ai_report_{country_id}_{region_id}.pdf",
                mime="application/pdf"
            )
        else:
            st.info("Veuillez configurer un événement pour voir les prédictions.")

    st.divider()

    # Dimensions Detail Section
    if st.session_state.current_event != "None":
        st.subheader("🔍 Analyse Détaillée des Dimensions")

        res = pred_engine.predict_regional_impact(country_id, region_id, st.session_state.current_event, st.session_state.current_intensity)
        scores_dict = res["predicted_scores"]

        # Table
        df_scores = pd.DataFrame(scores_dict.items(), columns=["Dimension", "Score"])
        st.table(df_scores)

        # Bar Chart
        fig = px.bar(df_scores, x="Dimension", y="Score",
                     title="Score par Dimension",
                     color="Score",
                     color_continuous_scale="Reds_r")
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, width='stretch')

        # Dimension Detail Interactivity
        st.markdown("### 📖 Interprétation des Résultats")
        selected_dim = st.selectbox("Cliquez sur une dimension pour voir le détail :", list(scores_dict.keys()))

        if selected_dim:
            st.info(f"**{selected_dim}**\n\n{DIMENSION_INTERPRETATIONS.get(selected_dim, 'N/A')}")

            # Detail calculations logic
            val = scores_dict[selected_dim]
            baseline = country_data["baseline_scores"][selected_dim]
            loss = baseline - val

            st.write(f"**Détail du calcul :**")
            st.write(f"- Valeur de base : `{baseline:.2f}`")
            st.write(f"- Impact de la catastrophe : `-{loss:.2f}`")
            st.write(f"- Résultat final : `{val:.2f}`")

    st.caption("PULSE-AI v2.0 - Intégration SOTA : Graphes Multiplexes, Courbes de Fragilité et Analyse Topologique. | [Consulter la Méthodologie Scientifique](/Methodology)")

if __name__ == "__main__":
    main()
