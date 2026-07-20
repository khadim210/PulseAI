import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from pulse_ai.src.engine.calculator import NDRSCalculator
from pulse_ai.src.engine.simulator import DisasterSimulator
from pulse_ai.src.ai.assessment import RiskAssessor
from pulse_ai.src.ai.predictive import PredictiveModule
from pulse_ai.src.ai.anomaly import AnomalySimulator

def render_radar_chart(scores: dict, title: str):
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
    st.plotly_chart(fig)

def render_metrics_panel(country_name: str, current_scores: dict, total_score: float):
    """Renders the key KPIs at the top of the page."""
    risk_level = RiskAssessor.assess_risk(total_score)
    risk_color = RiskAssessor.get_risk_color(risk_level)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("National Resilience Score", f"{total_score:.1f} / 1000")
    with col2:
        st.markdown(f"### Risk Level: :{risk_color}[{risk_level}]")
    with col3:
        st.metric("Global Rank (Simulated)", "Top 15%")

def render_simulation_panel(current_scores: dict):
    """Renders the disaster simulation controls."""
    st.subheader("🌪️ Disaster Simulation Center")

    disasters = DisasterSimulator.get_available_disasters()
    selected_disaster = st.selectbox("Select a catastrophe to simulate:", disasters)

    if st.button("Trigger Disaster"):
        # Apply degradation
        new_scores = DisasterSimulator.apply_disaster(selected_disaster, current_scores)
        return new_scores, selected_disaster

    return None, None

def render_ai_insights(scores: dict, selected_disaster: str):
    """Renders predictions and anomalies."""
    st.subheader("🤖 AI Intelligence Layer")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Predictive Failure Analysis**")
        predictions = PredictiveModule.predict_failures(scores, selected_disaster)
        for p in predictions:
            st.warning(f"⚠️ Risk of failure: {p}")

    with col2:
        st.markdown("**Infrastructure Anomaly Stream**")
        sim = AnomalySimulator()
        # We simulate a real-time feel by generating a snapshot
        is_disaster = True if selected_disaster else False
        snapshot = sim.generate_metric_stream(is_disaster)
        anomalies = sim.detect_anomalies(snapshot)

        if anomalies:
            for a in anomalies:
                st.error(f"🚨 {a}")
        else:
            st.success("✅ Network Health: Stable")

    st.json(snapshot)
