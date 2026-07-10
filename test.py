from ui.components.metric_card import metric_card

col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card("Reports", 12, "🩺")

with col2:
    metric_card("Medication", 5, "💊")

with col3:
    metric_card("AI Chats", 24, "🤖")

with col4:
    metric_card("Success", "98%", "✅")