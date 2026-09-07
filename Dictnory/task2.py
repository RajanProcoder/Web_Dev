
prices = {
    "laptop": 50000,
    "mobile": 15000,
    "headphone": 2000,
    "keyboard": 1000
}

item_name = input("Kon sa item kharidna chahte ho? ").lower().strip()

# 1. Direct check karo ki item dictionary me hai ya nahi
if item_name in prices:
    original_price = prices[item_name]  # Direct value mil gayi! (No if/elif needed)
    
    # 10% Discount ka simple formula
    discount = original_price * 0.10
    final_price = original_price - discount
    
    print(f"\n✅ Item: {item_name.capitalize()}")
    print(f"💰 Original Price: ₹{original_price}")
    print(f"🎉 10% Discount: ₹{discount}")
    print(f"🏷️ Final Price: ₹{final_price}")

else:
    print("\n❌ Sorry brother, ye item available nahi hai!")