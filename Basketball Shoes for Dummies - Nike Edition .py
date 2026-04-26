import streamlit as st
import webbrowser

# This dictionary holds all the shoes for each position and shoe height.
# I added a picture link for each shoe so the app can show images.
# (This helps the user see what the shoe looks like, like showing a picture in a book.)
shoes = {
    "point guard": {
        "low": [
            {"name": "Nike GT Cut 3", "reason": "Great for quick guards who change direction often.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/3c9f5ad4-2d0a-4b5e-9f1d-2e8e9e06cfaf/gt-cut-3.jpg"},
            {"name": "Nike KD 15", "reason": "Soft cushioning helps with long games and heavy scoring loads.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/4b6c9e4f-7e7c-4b6f-9c1c-2e8e9e06cfaf/kd15.jpg"},
            {"name": "Nike Sabrina 1", "reason": "Stable shoe built for fast guards who need control.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/sabrina1.jpg"},
            {"name": "Nike PG 6", "reason": "Balanced shoe for all‑around guard play.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/pg6.jpg"}
        ],
        "mid": [
            {"name": "Nike Kyrie Infinity", "reason": "Elite traction for shifty ball handlers.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/kyrie-infinity.jpg"}
        ],
        "high": [
            {"name": "Nike LeBron 20", "reason": "High support for guards who drive aggressively.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/lebron20.jpg"}
        ]
    },

    "shooting guard": {
        "low": [
            {"name": "Nike Kobe 6 Protro", "reason": "Perfect for shooters who need quick footwork.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/kobe6.jpg"},
            {"name": "Nike GT Cut 2", "reason": "Low-to-the-ground feel helps with step‑backs.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/gt-cut-2.jpg"},
            {"name": "Nike KD 14", "reason": "Great for players who shoot off screens.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/kd14.jpg"},
            {"name": "Nike PG 5", "reason": "Lightweight shoe for smooth movement.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/pg5.jpg"}
        ],
        "mid": [
            {"name": "Nike Kobe 5 Protro", "reason": "Responsive shoe for high‑volume scorers.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/kobe5.jpg"}
        ],
        "high": [
            {"name": "Nike LeBron 19", "reason": "Extra ankle support for physical guards.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/lebron19.jpg"}
        ]
    },

    "small forward": {
        "low": [
            {"name": "Nike KD 16", "reason": "Great balance of cushioning and support.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/kd16.jpg"},
            {"name": "Nike GT Cut 3", "reason": "Quick shoe for wings who slash to the basket.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/gt-cut-3.jpg"},
            {"name": "Nike PG 6", "reason": "All‑around shoe for versatile forwards.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/pg6.jpg"},
            {"name": "Nike Kobe 6 Protro", "reason": "Elite traction for quick movement.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/kobe6.jpg"}
        ],
        "mid": [
            {"name": "Nike LeBron NXXT Gen", "reason": "Strong support for physical wing players.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/nxxt-gen.jpg"}
        ],
        "high": [
            {"name": "Nike LeBron 20", "reason": "High stability for explosive forwards.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/lebron20.jpg"}
        ]
    },

    "power forward": {
        "low": [
            {"name": "Nike KD 15", "reason": "Soft cushioning for bigger players.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/kd15.jpg"},
            {"name": "Nike GT Hustle 2", "reason": "Great for forwards who run the floor.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/gt-hustle-2.jpg"},
            {"name": "Nike PG 6", "reason": "Balanced shoe for all‑around play.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/pg6.jpg"},
            {"name": "Nike Kobe 4 Protro", "reason": "Low shoe with strong stability.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/kobe4.jpg"}
        ],
        "mid": [
            {"name": "Nike LeBron Witness 7", "reason": "Supportive shoe for physical forwards.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/witness7.jpg"}
        ],
        "high": [
            {"name": "Nike LeBron 18", "reason": "Maximum cushioning for strong players.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/lebron18.jpg"}
        ]
    },

    "center": {
        "low": [
            {"name": "Nike GT Jump 2", "reason": "Built for bigs who jump often.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/gt-jump-2.jpg"},
            {"name": "Nike KD 17", "reason": "Soft cushioning for heavy players.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/kd17.jpg"},
            {"name": "Nike LeBron Witness 8", "reason": "Strong support for post players.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/witness8.jpg"},
            {"name": "Nike PG 6", "reason": "Light shoe for mobile centers.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/pg6.jpg"}
        ],
        "mid": [
            {"name": "Nike LeBron NXXT Gen", "reason": "Strong support for bigs.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/nxxt-gen.jpg"}
        ],
        "high": [
            {"name": "Nike LeBron 20", "reason": "High stability for centers.",
             "img": "https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/lebron20.jpg"}
        ]
    }
}

# This function opens Google and searches for the shoe name.
# I changed it so Streamlit opens the link correctly.
def google_search(shoe_name):
    query = shoe_name.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}+basketball+shoe"
    st.markdown(f"[Click here to search **{shoe_name}** on Google]({url})")

# This is the main function that creates the shoe recommendations.
def generate_recommendations(pos, height):
    main_list = shoes[pos][height][:4]
    other_heights = [h for h in ["low", "mid", "high"] if h != height]
    extra = [shoes[pos][other_heights[0]][0], shoes[pos][other_heights[1]][0]]
    return main_list + extra


# Streamlit Window


st.title("Basketball Shoes for Dummies - Nike Edition")

pos_var = st.selectbox("Select Your Primary Position:", list(shoes.keys()))
height_var = st.radio("Preferred Shoe Style:", ["low", "mid", "high"])

if st.button("Show Recommendations"):
    final_list = generate_recommendations(pos_var, height_var)

    for shoe in final_list:

        # I added a picture of the shoe so the user can see it.
        st.image(shoe["img"], width=300)

        # I kept your card design exactly the same.
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

        # I changed the search button so it works in Streamlit.
        if st.button(f"Search {shoe['name']}"):
            google_search(shoe["name"])

email_entry = st.text_input("Send results to your email:")

if st.button("Send to Email"):
    if email_entry.strip() == "":
        st.warning("Please enter an email.")
    else:
        st.success(f"Your recommendations were sent to {email_entry}")
