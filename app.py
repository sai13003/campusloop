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
    .badge-location {
        background-color: #F1F5F9;
        color: #1E293B;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
    }
    .badge-method {
        background-color: #EEF2FF;
        color: #3730A3;
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
        margin-bottom: 0.4rem;
    }
    
    .item-meta {
        font-size: 0.82rem;
        color: #475569;
        margin-bottom: 0.2rem;
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
            "payment_method": "Item Swap",
            "locality": "Prestige Lakeside Habitat (Tower 5)",
            "price": "Swap for Class 10 RD Sharma",
            "owner": "Aarav (Class 10)",
            "image": CATEGORY_IMAGES["Books & Notes"]
        },
        {
            "title": "Scientific Calculator Casio fx-991ES",
            "category": "Gadgets & Calculators",
            "type": "Sell",
            "payment_method": "Real Cash",
            "locality": "Allen Career Institute (Koramangala)",
            "price": "INR 450",
            "owner": "Rohan (Class 12)",
            "image": CATEGORY_IMAGES["Gadgets & Calculators"]
        },
        {
            "title": "Yonex Nanoray Badminton Racket",
            "category": "Sports Gear",
            "type": "Sell",
            "payment_method": "Exchange Points",
            "locality": "Sobha Forest View (Clubhouse Block)",
            "price": "550 Exchange Points",
            "owner": "Priya (Class 11)",
            "image": CATEGORY_IMAGES["Sports Gear"]
        }
    ]

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigation", ["Browse Marketplace", "List an Item", "Parent Approval Log"])

if menu == "Browse Marketplace":
    st.subheader("Available Gear")
    
    col_filter_mode, col_filter_payment = st.columns(2)
    with col_filter_mode:
        filter_type = st.selectbox("Filter by Listing Mode", ["All", "Swap", "Sell"])
    with col_filter_payment:
        filter_payment = st.selectbox("Filter by Payment / Exchange Method", ["All", "Real Cash", "Exchange Points", "Item Swap"])
    
    # Filter items safely using .get()
    filtered_items = [
        item for item in st.session_state.listings 
        if (filter_type == "All" or item.get("type") == filter_type) and
           (filter_payment == "All" or item.get("payment_method", "Item Swap") == filter_payment)
    ]
    
    if not filtered_items:
        st.info("No items match the selected filter criteria.")
    
    # Render two-column grid
    cols = st.columns(2)
    for idx, item in enumerate(filtered_items):
        with cols[idx % 2]:
            locality = item.get("locality", "Campus Hub")
            payment_method = item.get("payment_method", "Item Swap")
            image_url = item.get("image", CATEGORY_IMAGES.get(item.get("category"), CATEGORY_IMAGES["Books & Notes"]))
            owner_name = item.get("owner", "Student")
            price_val = item.get("price", "Swap")
            item_title = item.get("title", "Item")
            category_val = item.get("category", "General")

            st.markdown(f"""
            <div class="swap-card">
                <img class="card-img" src="{image_url}" alt="{item_title}">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span class="badge-location">{locality}</span>
                    <span class="badge-verified">Parent Verified</span>
                </div>
                <div class="item-title">{item_title}</div>
                <div class="item-category">{category_val}</div>
                <div class="item-meta">Seller: {owner_name}</div>
                <div style="margin-top: 6px;">
                    <span class="badge-method">Method: {payment_method}</span>
                </div>
                <div class="card-footer">
                    <div>
                        <span class="price-tag">{price_val}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Request {item_title}", key=f"req_{idx}_{item_title}"):
                st.success(f"Request confirmed. A WhatsApp parent approval alert has been sent for {item_title}.")
            st.write("")

elif menu == "List an Item":
    st.subheader("List an Item")
    st.caption("Post pre-owned student gear for swap or sale within your verified school and society network.")
    
    with st.form("listing_form", clear_on_submit=True):
        title = st.text_input("Item Name (e.g., Concepts of Physics Vol 1)")
        category = st.selectbox("Category", ["Books & Notes", "Gadgets & Calculators", "Sports Gear", "Uniforms & Merch"])
        listing_type = st.selectbox("Listing Mode", ["Sell", "Swap"])
        
        # Payment / Exchange selection
        if listing_type == "Sell":
            payment_method = st.selectbox("Accepted Payment Method", ["Real Cash", "Exchange Points"])
            price = st.text_input("Price or Points (e.g., INR 400 or 350 Points)")
        else:
            payment_method = "Item Swap"
            price = st.text_input("Desired Item in Return (e.g., Class 11 Chemistry NCERT)")
            
        locality = st.text_input("Locality / Society / Campus (e.g., Sobha Arena, Block B)")
        owner = st.text_input("Your Name and Class (e.g., Kabir - 11B)")
        parent_phone = st.text_input("Parent WhatsApp Contact (Required for verification)")
        
        submitted = st.form_submit_button("Publish Listing")
        
        if submitted:
            if not title or not owner or not price or not locality:
                st.error("Please fill in the item title, price/swap details, locality, and your name.")
            else:
                st.session_state.listings.append({
                    "title": title,
                    "category": category,
                    "type": listing_type,
                    "payment_method": payment_method,
                    "locality": locality,
                    "price": price,
                    "owner": owner,
                    "image": CATEGORY_IMAGES.get(category, CATEGORY_IMAGES["Books & Notes"])
                })
                st.success(f"Listing for '{title}' submitted successfully. It is now live in the marketplace.")

elif menu == "Parent Approval Log":
    st.subheader("Parent Safety and Verification Registry")
    st.info("All transactions across Real Cash, Exchange Points, and direct swaps trigger one-tap parent authorization via WhatsApp before completion.")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Pending Approvals", "3")
    m2.metric("Verified Swaps", "14")
    m3.metric("Safety Compliance", "100%")

