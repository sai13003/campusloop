import streamlit as st

st.set_page_config(
    page_title="CampusLoop | Smart Student Exchange",
    layout="wide",
)

# Custom CSS styling
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
        border-radius: 12px 12px 0 0;
        padding: 1.2rem;
        border: 1px solid #E2E8F0;
        border-bottom: none;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }
    
    .card-img {
        width: 100%;
        height: 190px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 0.8rem;
    }
    
    /* Badges */
    .badge-type {
        background-color: #0F172A;
        color: #FFFFFF;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
    }
    .badge-verified {
        background-color: #ECFDF5;
        color: #065F46;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
    }
    
    .item-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
        margin: 0.5rem 0 0.2rem 0;
    }
    
    .item-category {
        color: #64748B;
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .item-owner {
        font-size: 0.85rem;
        color: #475569;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .card-footer {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-top: 0.8rem;
        padding-top: 0.6rem;
        border-top: 1px solid #F1F5F9;
    }
    
    .price-tag {
        font-weight: 700;
        color: #0F172A;
        font-size: 1.1rem;
    }
    
    /* Streamlit Action Button */
    div.stButton > button:first-child {
        width: 100%;
        background-color: #0F172A;
        color: white;
        border-radius: 0 0 12px 12px;
        border: 1px solid #0F172A;
        font-weight: 600;
        font-size: 0.9rem;
        padding: 0.55rem 1rem;
        transition: all 0.2s ease;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #1E293B;
        color: #F8FAFC;
        border-color: #1E293B;
    }
</style>
""", unsafe_allow_html=True)

# Top Hero Section
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">CampusLoop</h1>
    <p class="hero-subtitle">The student gear exchange and academic rotation marketplace.</p>
</div>
""", unsafe_allow_html=True)

# Default Image Fallbacks based on category
CATEGORY_IMAGES = {
    "Books & Notes": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=700&q=80",
    "Gadgets & Calculators": "https://images.unsplash.com/photo-1594980596870-8aa52a78d8cd?auto=format&fit=crop&w=700&q=80",
    "Sports Gear": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=700&q=80",
    "Uniforms & Merch": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=700&q=80"
}

# Initialize session state listings
if "listings" not in st.session_state:
    st.session_state.listings = [
        {
            "title": "Oswaal Class 10 Sample Papers",
            "category": "Books & Notes",
            "type": "Swap",
            "price": "Swap for RD Sharma",
            "owner": "Aarav (Class 10)",
            "image": CATEGORY_IMAGES["Books & Notes"]
        },
        {
            "title": "Scientific Calculator Casio fx-991ES",
            "category": "Gadgets & Calculators",
            "type": "Sell",
            "price": "INR 450",
            "owner": "Rohan (Class 12)",
            "image": CATEGORY_IMAGES["Gadgets & Calculators"]
        },
        {
            "title": "Yonex Nanoray Badminton Racket",
            "category": "Sports Gear",
            "type": "Swap",
            "price": "Swap for Table Tennis Bat",
            "owner": "Priya (Class 11)",
            "image": CATEGORY_IMAGES["Sports Gear"]
        }
    ]

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigation", ["Browse Marketplace", "List an Item", "Parent Approval Log"])

if menu == "Browse Marketplace":
    st.subheader("Available Gear")
    
    filter_type = st.selectbox("Filter by Listing Mode", ["All", "Swap", "Sell"])
    
    # Filter items
    filtered_items = [
        item for item in st.session_state.listings 
        if filter_type == "All" or item["type"] == filter_type
    ]
    
    # Render two-column grid
    cols = st.columns(2)
    for idx, item in enumerate(filtered_items):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="swap-card">
                <img class="card-img" src="{item.get('image', CATEGORY_IMAGES['Books & Notes'])}" alt="{item['title']}">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span class="badge-type">{item['type']}</span>
                    <span class="badge-verified">Parent Verified</span>
                </div>
                <div class="item-title">{item['title']}</div>
                <div class="item-category">{item['category']}</div>
                <div class="item-owner">Owner: {item['owner']}</div>
                <div class="card-footer">
                    <div>
                        <span class="price-tag">{item['price']}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Request {item['title']}", key=f"req_{idx}_{item['title']}"):
                st.success(f"Request sent. A WhatsApp verification prompt has been routed to {item['owner']}'s registered parent.")
            st.write("")

elif menu == "List an Item":
    st.subheader("List an Item")
    st.caption("Post pre-owned student gear for swap or sale within your verified school network.")
    
    with st.form("listing_form", clear_on_submit=True):
        title = st.text_input("Item Name (e.g., Concepts of Physics Vol 1)")
        category = st.selectbox("Category", ["Books & Notes", "Gadgets & Calculators", "Sports Gear", "Uniforms & Merch"])
        listing_type = st.selectbox("Listing Mode", ["Swap", "Sell"])
        
        if listing_type == "Sell":
            price = st.text_input("Selling Price (e.g., INR 500)")
        else:
            price = st.text_input("Desired Item in Return (e.g., Swap for Class 11 Biology Guide)")
            
        owner = st.text_input("Your Name and Section (e.g., Kabir - 11B)")
        parent_phone = st.text_input("Parent WhatsApp Contact (Required for verification)")
        
        submitted = st.form_submit_button("Publish Listing")
        
        if submitted:
            if not title or not owner or not price:
                st.error("Please fill in the item title, price/trade details, and your name.")
            else:
                st.session_state.listings.append({
                    "title": title,
                    "category": category,
                    "type": listing_type,
                    "price": price,
                    "owner": owner,
                    "image": CATEGORY_IMAGES.get(category, CATEGORY_IMAGES["Books & Notes"])
                })
                st.success(f"Listing for '{title}' submitted successfully. It is now live in the marketplace.")

elif menu == "Parent Approval Log":
    st.subheader("Parent Safety and Verification Registry")
    st.info("All transactions and high-value item exchanges require one-tap parent authorization via WhatsApp before completion.")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Pending Approvals", "3")
    m2.metric("Verified Swaps", "14")
    m3.metric("Safety Compliance", "100%")

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
import streamlit as st

st.set_page_config(
    page_title="CampusLoop | Smart Student Exchange",
    layout="wide",
)

# Custom CSS for styling
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
        border-radius: 12px 12px 0 0;
        padding: 1.2rem;
        border: 1px solid #E2E8F0;
        border-bottom: none;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }
    
    .card-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 0.8rem;
    }
    
    /* Badges */
    .badge-location {
        background-color: #F1F5F9;
        color: #334155;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
    }
    .badge-verified {
        background-color: #ECFDF5;
        color: #065F46;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
    }
    
    .item-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
        margin: 0.5rem 0 0.2rem 0;
    }
    
    .item-category {
        color: #64748B;
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 0.6rem;
    }
    
    .item-condition {
        color: #0F172A;
        font-weight: 600;
    }
    
    .item-description {
        font-size: 0.88rem;
        color: #334155;
        line-height: 1.4;
        min-height: 2.5rem;
    }
    
    .card-footer {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-top: 0.8rem;
        padding-top: 0.6rem;
        border-top: 1px solid #F1F5F9;
    }
    
    .credit-tag {
        font-weight: 700;
        color: #0F172A;
        font-size: 1.1rem;
    }
    
    .mrp-tag {
        font-size: 0.78rem;
        color: #94A3B8;
        margin-left: 4px;
    }
    
    /* Custom Streamlit Button Styling */
    div.stButton > button:first-child {
        width: 100%;
        background-color: #0F172A;
        color: white;
        border-radius: 0 0 12px 12px;
        border: 1px solid #0F172A;
        font-weight: 600;
        font-size: 0.9rem;
        padding: 0.55rem 1rem;
        transition: all 0.2s ease;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #1E293B;
        color: #F8FAFC;
        border-color: #1E293B;
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

# Sample listings with images
items = [
    {
        "title": "HC Verma Concepts of Physics (Vol 1 & 2)",
        "category": "Academic",
        "condition": "Annotated",
        "credits": 280,
        "location": "Prestige Shantiniketan",
        "equivalent_mrp": "INR 950",
        "image": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=700&q=80",
        "description": "Complete solved exercises. Formulae highlighted with zero torn pages."
    },
    {
        "title": "Yonex Nanoray 18i Badminton Racket",
        "category": "Sports",
        "condition": "Like New",
        "credits": 550,
        "location": "Sobha Forest View",
        "equivalent_mrp": "INR 2,290",
        "image": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=700&q=80",
        "description": "Strung at 24 lbs with new grip tape. Includes padded carry case."
    },
    {
        "title": "Scientific Calculator fx-991EX",
        "category": "Gadgets",
        "condition": "Mint Condition",
        "credits": 420,
        "location": "Allen Career Hub",
        "equivalent_mrp": "INR 1,500",
        "image": "https://images.unsplash.com/photo-1594980596870-8aa52a78d8cd?auto=format&fit=crop&w=700&q=80",
        "description": "Solar dual-power, Class 11-12 lab approved, clean protective cover."
    },
    {
        "title": "Acoustic Guitar 38-Inch with Gig Bag",
        "category": "Hobby",
        "condition": "Play-Grade",
        "credits": 600,
        "location": "Godrej Woods",
        "equivalent_mrp": "INR 2,800",
        "image": "https://images.unsplash.com/photo-1510915361894-db8b60106cb1?auto=format&fit=crop&w=700&q=80",
        "description": "Barely played over vacation. Clean fretboard, fresh nylon strings attached."
    }
]

# Grid display
cols = st.columns(2)
for idx, item in enumerate(items):
    with cols[idx % 2]:
        st.markdown(f"""
        <div class="swap-card">
            <img class="card-img" src="{item['image']}" alt="{item['title']}">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span class="badge-location">{item['location']}</span>
                <span class="badge-verified">Parent Verified</span>
            </div>
            <div class="item-title">{item['title']}</div>
            <div class="item-category">{item['category']} | Condition: <span class="item-condition">{item['condition']}</span></div>
            <div class="item-description">{item['description']}</div>
            <div class="card-footer">
                <div>
                    <span class="credit-tag">{item['credits']} Credits</span>
                    <span class="mrp-tag">(MRP: {item['equivalent_mrp']})</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Action button attached directly underneath each card
        if st.button(f"Request Swap ({item['credits']} Credits)", key=f"btn_{idx}"):
            st.success(f"Trade requested for {item['title']}. Verification prompt sent to registered parent.")
        st.write("")  # Small bottom spacing
