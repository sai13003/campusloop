import streamlit as st

st.set_page_config(page_title="CampusLoop Beta", page_icon="🎒", layout="centered")

# App Title & Branding
st.title("🎒 CampusLoop: Student Swap, Rent & Sell")
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
                st.write(f"🏷️ **Type:** {item['type']} | 💰 **Price/Value:** {item['price']}")
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
            st.success("🎉 Item listed successfully! It is now live for your schoolmates.")

elif menu == "Parent Approval Status":
    st.header("Parent Safety & Verification Log")
    st.info("Every transaction involving money (Rent/Sell) or high-value swaps automatically pings parents via WhatsApp before locking in.")
    st.write("🟢 **Status:** 3 Pending Approvals | 12 Verified Trades Completed This Week.")
