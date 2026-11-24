import streamlit as st

st.set_page_config(page_title="CampusLoop Beta", page_icon="", layout="centered")

# App Title & Branding
st.title(" CampusLoop: Student Swap, Rent & Sell")
st.markdown("*(Approved for School Beta Test)*")

# Initialize fake database in session state if it doesn't exist
if "listings" not in st.session_state:
    st.session_state.listings = [
        {"title": "Oswaal Class 10 Sample Papers", "category": "Books", "type": "Rent", "price": "₹50 / month", "owner": "Aarav (Class 10)"},
        {"title": "Scientific Calculator (Casio fx-991ES)", "category": "Gadgets", "type": "Sell", "price": "₹450", "owner": "Rohan (Class 12)"},
        {"title": "Badminton Racket", "category": "Sports", "type": "Swap", "price": "Swap for Novel", "owner": "Priya (Class 11)"}
    ]

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigation", ["Browse Marketplace", "List an Item", "Parent Approval Status"])

if menu == "Browse Marketplace":
    st.header("Available Gear in Your School")
    
    # Filter by type
    filter_type = st.selectbox("Filter by Mode", ["All", "Swap", "Rent", "Sell"])
    
    for item in st.session_state.listings:
        if filter_type == "All" or item["type"] == filter_type:
            with st.container():
                st.subheader(item["title"])
                st.write(f" **Type:** {item['type']} |  **Price/Value:** {item['price']}")
                st.write(f"👤 **Owner:** {item['owner']}")
                if st.button(f"Request {item['title']}", key=item['title']):
                    st.success(f"Request sent! A WhatsApp approval link has been triggered for {item['owner']}'s parents.")
                st.divider()

elif menu == "List an Item":
    st.header("List Your Item (Swap, Rent, or Sell)")
    
    with st.form("listing_form"):
        title = st.text_input("Item Name (e.g., Physics HC Verma Vol 1)")
        category = st.selectbox("Category", ["Books & Notes", "Gadgets & Calculators", "Sports Gear", "Uniforms & Merch"])
        listing_type = st.selectbox("Listing Mode", ["Swap", "Rent", "Sell"])
        price = st.text_input("Price (if Sell/Rent) or What you want in return (if Swap)")
        owner = st.text_input("Your Name & Class (e.g., Kabir - 11B)")
        parent_phone = st.text_input("Parent's WhatsApp Number (for safety check)")
        
        submitted = st.form_submit_button("Post Listing")
        
        if submitted and title and owner:
            st.session_state.listings.append({
                "title": title,
                "category": category,
                "type": listing_type,
                "price": price if listing_type != "Swap" else f"Swap: {price}",
                "owner": owner
            })
            st.success(" Item listed successfully! It is now live for your schoolmates.")

elif menu == "Parent Approval Status":
    st.header("Parent Safety & Verification Log")
    st.info("Every transaction involving money (Rent/Sell) or high-value swaps automatically pings parents via WhatsApp before locking in.")
    st.write(" **Status:** 3 Pending Approvals | 12 Verified Trades Completed This Week.")
    import streamlit as st

st.set_page_config(
    page_title="CampusLoop | Smart Student Exchange",
    layout="wide",
)

# Custom CSS styling without emojis
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Top Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 2.2rem 2.5rem;
        border-radius: 12px;
        color: #FFFFFF;
        margin-bottom: 2rem;
        border: 1px solid #334155;
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        color: #F8FAFC;
        margin: 0;
    }
    .hero-subtitle {
        color: #94A3B8;
        font-size: 1rem;
        margin-top: 0.5rem;
        font-weight: 400;
    }
    
    /* Listing Cards */
    .swap-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 1.4rem;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 1.2rem;
    }
    .swap-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.07);
        border-color: #CBD5E1;
    }
    
    /* Badges */
    .badge-location {
        background-color: #F1F5F9;
        color: #334155;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 4px 10px;
        border-radius: 4px;
        display: inline-block;
    }
    .badge-verified {
        background-color: #ECFDF5;
        color: #065F46;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 4px 10px;
        border-radius: 4px;
        display: inline-block;
    }
    
    /* Typography & Tags */
    .item-category {
        color: #64748B;
        font-size: 0.85rem;
        font-weight: 500;
        margin-top: 0.35rem;
        margin-bottom: 0.6rem;
    }
    .item-condition {
        color: #0F172A;
        font-weight: 600;
    }
    .item-description {
        font-size: 0.9rem;
        color: #334155;
        line-height: 1.45;
        min-height: 2.6rem;
    }
    .card-footer {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-top: 1rem;
        padding-top: 0.75rem;
        border-top: 1px solid #F1F5F9;
    }
    .credit-tag {
        font-weight: 700;
        color: #0F172A;
        font-size: 1.15rem;
    }
    .mrp-tag {
        font-size: 0.8rem;
        color: #94A3B8;
        margin-left: 6px;
    }
</style>
""", unsafe_allow_html=True)

# Top Hero Section
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">CampusLoop</h1>
    <p class="hero-subtitle">The zero-cash student gear and academic rotation exchange.</p>
</div>
""", unsafe_allow_html=True)
