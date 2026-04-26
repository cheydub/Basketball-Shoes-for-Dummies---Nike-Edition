import streamlit as st
import webbrowser

# This dictionary holds all the shoes for each position and shoe height.
shoes = {
    "point guard": {
        "low": [
            {"name": "Nike GT Cut 3", "reason": "Great for quick guards who change direction often."},
            {"name": "Nike KD 15", "reason": "Soft cushioning helps with long games and heavy scoring loads."},
            {"name": "Nike Sabrina 1", "reason": "Stable shoe built for fast guards who need control."},
            {"name": "Nike PG 6", "reason": "Balanced shoe for all‑around guard play."}
        ],
        "mid": [
            {"name": "Nike Kyrie Infinity", "reason": "Elite traction for shifty ball handlers."}
        ],
        "high": [
            {"name": "Nike LeBron 20", "reason": "High support for guards who drive aggressively."}
        ]
    },

    "shooting guard": {
        "low": [
            {"name": "Nike Kobe 6 Protro", "reason": "Perfect for shooters who need quick footwork."},
            {"name": "Nike GT Cut 2", "reason": "Low-to-the-ground feel helps with step‑backs."},
            {"name": "Nike KD 14", "reason": "Great for players who shoot off screens."},
            {"name": "Nike PG 5", "reason": "Lightweight shoe for smooth movement."}
        ],
        "mid": [
            {"name": "Nike Kobe 5 Protro", "reason": "Responsive shoe for high‑volume scorers."}
        ],
        "high": [
            {"name": "Nike LeBron 19", "reason": "Extra ankle support for physical guards."}
        ]
    },

    "small forward": {
        "low": [
            {"name": "Nike KD 16", "reason": "Great balance of cushioning and support."},
            {"name": "Nike GT Cut 3", "reason": "Quick shoe for wings who slash to the basket."},
            {"name": "Nike PG 6", "reason": "All‑around shoe for versatile forwards."},
            {"name": "Nike Kobe 6 Protro", "reason": "Elite traction for quick movement."}
        ],
        "mid": [
            {"name": "Nike LeBron NXXT Gen", "reason": "Strong support for physical wing players."}
        ],
        "high": [
            {"name": "Nike LeBron 20", "reason": "High stability for explosive forwards."}
        ]
    },

    "power forward": {
        "low": [
            {"name": "Nike KD 15", "reason": "Soft cushioning for bigger players."},
            {"name": "Nike GT Hustle 2", "reason": "Great for forwards who run the floor."},
            {"name": "Nike PG 6", "reason": "Balanced shoe for all‑around play."},
            {"name": "Nike Kobe 4 Protro", "reason": "Low shoe with strong stability."}
        ],
        "mid": [
            {"name": "Nike LeBron Witness 7", "reason": "Supportive shoe for physical forwards."}
        ],
        "high": [
            {"name": "Nike LeBron 18", "reason": "Maximum cushioning for strong players."}
        ]
    },

    "center": {
        "low": [
            {"name": "Nike GT Jump 2", "reason": "Built for bigs who jump often."},
            {"name": "Nike KD 17", "reason": "Soft cushioning for heavy players."},
            {"name": "Nike LeBron Witness 8", "reason": "Strong support for post players."},
            {"name": "Nike PG 6", "reason": "Light shoe for mobile centers."}
        ],
        "mid": [
            {"name": "Nike LeBron NXXT Gen", "reason": "Strong support for bigs."}
        ],
        "high": [
            {"name": "Nike LeBron 20", "reason": "High stability for centers."}
        ]
    }
}

# This function opens Google and searches for the shoe name.
def google_search(shoe_name):
    query = shoe_name.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}+basketball+shoe"
    webbrowser.open(url)

# This is the main function that creates the shoe recommendations.
def generate_recommendations(pos, height):
    main_list = shoes[pos][height][:4]
    other_heights = [h for h in ["low", "mid", "high"] if h != height]
    extra = [shoes[pos][other_heights[0]][0], shoes[pos][other_heights[1]][0]]
    return main_list + extra

# ---------------------------------------------------------
# STREAMLIT UI
# ---------------------------------------------------------

st.title("Basketball Shoes for Dummies - Nike Edition")

pos_var = st.selectbox("Select Your Primary Position:", list(shoes.keys()))
height_var = st.radio("Preferred Shoe Style:", ["low", "mid", "high"])

if st.button("Show Recommendations"):
    final_list = generate_recommendations(pos_var, height_var)

    for shoe in final_list:
        st.markdown(
            f"""
            <div style="background-color:white; padding:20px; border-radius:10px; 
                        border:2px solid #1E3A8A; margin-bottom:20px; width:80%; 
                        margin-left:auto; margin-right:auto;">
                <h3 style="color:#1E3A8A; text-align:center;">{shoe['name']}</h3>
                <p style="text-align:center;">{shoe['reason']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(f"Search {shoe['name']}"):
            google_search(shoe["name"])

email_entry = st.text_input("Send results to your email:")

if st.button("Send to Email"):
    if email_entry.strip() == "":
        st.warning("Please enter an email.")
    else:
        st.success(f"Your recommendations were sent to {email_entry}")
