import tkinter as tk
from tkinter import ttk, messagebox
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
# It helps the user find the shoe online without the app storing any links, when trying to use the Nike link, it fails.
def google_search(shoe_name):
    query = shoe_name.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}+basketball+shoe"
    webbrowser.open(url)

# This is the main function that creates the shoe recommendations.
# It reads what the user picked, finds the matching shoes, and creates the cards.
def generate_recommendations():
    pos = pos_var.get()
    height = height_var.get()

    # If the user forgot to choose something, show a warning.
    if not pos or not height:
        messagebox.showwarning("Missing Info", "Please select both position and shoe style.")
        return

    # This clears old recommendation cards so new ones can appear.
    for widget in results_frame.winfo_children():
        widget.destroy()

    # This finds the shoes that match the user's choices.
    main_list = shoes[pos][height][:4]

    # These two extra shoes come from the other heights.
    other_heights = [h for h in ["low", "mid", "high"] if h != height]
    extra = [shoes[pos][other_heights[0]][0], shoes[pos][other_heights[1]][0]]

    # This is the final list of six shoes.
    final_list = main_list + extra

    # This loop creates a card for each shoe.
    for shoe in final_list:
        # A card is just a frame with text and a button inside it.
        card = tk.Frame(results_frame, bg="white", bd=2, relief="ridge")
        card.pack(pady=15, anchor="center")

        # This sets the card width so all cards line up neatly.
        card.configure(width=700)

        # This shows the shoe name.
        tk.Label(card, text=shoe["name"], font=("Arial", 18, "bold"),
                 bg="white", fg="#1E3A8A").pack(pady=8)

        # This shows the reason why the shoe is recommended.
        tk.Label(card, text=shoe["reason"], wraplength=650, justify="center",
                 font=("Arial", 13), bg="white").pack(pady=5)

        # This button lets the user search the shoe on Google.
        tk.Button(
            card,
            text="Search Shoe",
            bg="#1E3A8A", fg="white",
            font=("Arial", 12, "bold"),
            command=lambda name=shoe["name"]: google_search(name)
        ).pack(pady=10)

# This function checks if the user typed an email.
# If they did, it shows a message pretending to send the recommendations.
def send_email():
    email = email_entry.get().strip()
    if not email:
        messagebox.showwarning("Missing Email", "Please enter an email.")
        return

    messagebox.showinfo("Sent", f"Your recommendations were sent to {email}")

# This creates the main window of the app.
root = tk.Tk()
root.title("Basketball Shoes for Dummies - Nike Edition")
root.geometry("950x900")
root.configure(bg="#F0F4FF")

# This is the title at the top of the app.
tk.Label(root, text="Basketball Shoes for Dummies - Nike Edition",
         font=("Arial", 24, "bold"), bg="#F0F4FF", fg="#1E3A8A").pack(pady=15)

# This section lets the user choose their position.
tk.Label(root, text="Select Your Primary Position:", font=("Arial", 16),
         bg="#F0F4FF").pack(pady=5)
pos_var = tk.StringVar()
ttk.Combobox(root, textvariable=pos_var, values=list(shoes.keys()),
             width=30, state="readonly").pack()

# This section lets the user choose their shoe height.
tk.Label(root, text="Preferred Shoe Style:", font=("Arial", 16),
         bg="#F0F4FF").pack(pady=10)
height_var = tk.StringVar()
tk.Radiobutton(root, text="Low", variable=height_var, value="low",
               bg="#F0F4FF").pack()
tk.Radiobutton(root, text="Mid", variable=height_var, value="mid",
               bg="#F0F4FF").pack()
tk.Radiobutton(root, text="High", variable=height_var, value="high",
               bg="#F0F4FF").pack()

# This button starts the recommendation process.
tk.Button(root, text="Show Recommendations", command=generate_recommendations,
          bg="#1E3A8A", fg="white", font=("Arial", 14, "bold")).pack(pady=15)

# This creates the scrollable area where the cards appear.
container = tk.Frame(root, bg="#F0F4FF")
container.pack(fill="both", expand=True, pady=10)

# The canvas allows scrolling.
canvas = tk.Canvas(container, bg="#F0F4FF", highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

# This is the scrollbar on the right side.
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# This frame holds all the recommendation cards.
results_frame = tk.Frame(canvas, bg="#F0F4FF")
canvas.create_window((0, 0), window=results_frame, anchor="n")

# This function updates the scroll area whenever new cards appear.
def update_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

results_frame.bind("<Configure>", update_scroll)

# This is the email section at the bottom.
tk.Label(root, text="Send results to your email:", font=("Arial", 14),
         bg="#F0F4FF").pack(pady=10)
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Button(root, text="Send to Email", command=send_email,
          bg="#1E3A8A", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

# This keeps the window open.
root.mainloop()
