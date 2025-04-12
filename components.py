from dash import html
import dash_bootstrap_components as dbc

# 🔹 Google Fonts URL for Fancy Fonts
GOOGLE_FONTS_URL = "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&family=Playfair+Display:wght@400;700&family=Montserrat:wght@400;700&display=swap"

# 🔹 Airbnb Theme Colors
COLORS = {
    "AIRBNB_RED": "#FF5A5F",  # Primary Red
    "AIRBNB_TEAL": "#00A699",  # Teal Accent
    "GOLD": "#FFD700",  # Bright Gold Highlight
    "DARK_GOLD": "#DEB522",  # Muted Gold for Cards
    "BLACK": "#000000",  # Black Background
    "WHITE": "#FFFFFF",  # White Text for Contrast
    "LIGHT_GRAY": "#F7F7F7",  # Soft Gray Background
}

# 🔹 Fancy Font Choices
FONTS = {
    "Modern": "Poppins, sans-serif",
    "Luxury": "Playfair Display, serif",
    "Tech": "Montserrat, sans-serif",
    "Cursive": "cursive",
}


# 🔹 Stats Card Component (Image Beside Value)
def stats_card(title, value, image_path, bg_color=COLORS["AIRBNB_TEAL"]):
    return dbc.Card(
        dbc.CardBody(
            [
                html.Img(src=image_path, style={"width": "50px", "height": "50px", "marginBottom": "10px"}),
                html.H4(value, style={"fontSize": "28px", "fontStyle": FONTS['Cursive'] ,"fontWeight": "bold", "marginBottom": "5px"}),
                html.P(title, style={"fontSize": "28px", "fontWeight": "bold", "margin": "0px"}),
            ],
            className="text-center",
        ),
        style={
            "backgroundColor": bg_color,
            "padding": "20px",
            "borderRadius": "15px",
            "border": "none",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "flexDirection": "column",
            # "width": "80px",  # Reduce card width
            # "height": "80px",  # Reduce card height
        },
    )

# 🔹 Tab Styles
TAB_STYLE = {
    "border": "none",
    "color": COLORS["AIRBNB_TEAL"],  # Teal text for inactive tabs
    "fontWeight": "bold",
    "padding": "12px 20px",
    "textAlign": "center",
    "fontSize": "18px",
}

SELECTED_TAB_STYLE = {
    "borderBottom": f"4px solid {COLORS['AIRBNB_RED']}",  # Bold red bottom border
    "backgroundColor": COLORS["LIGHT_GRAY"],  # Light gray for selected tab
    "color": COLORS["AIRBNB_RED"],  # Red text for selected tab
    "fontWeight": "bold",
    "padding": "12px 20px",
    "textAlign": "center",
    "fontSize": "18px",
}

# 🔹 Tab Component
def tab(label, tab_id):
    return dbc.Tab(label=label, tab_id=tab_id, label_style=TAB_STYLE, active_label_style=SELECTED_TAB_STYLE)
