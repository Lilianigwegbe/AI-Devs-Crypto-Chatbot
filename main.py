"Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}
def crypto_bot():
    print("Yo, I’m CryptoBuddy! 🚀 Ask me about cryptos, and I’ll drop some knowledge!")
    print("Try: 'Which crypto is trending up?' or 'What’s the most sustainable coin?'")
    
    while True:
        user_query = input("\nWhat’s your crypto question? (Type 'exit' to quit): ").lower()
        
        if user_query == "exit":
            print("Peace out! Stay safe in the crypto jungle! ✌️")
            break
        
        # Initialize recommendation
        recommendation = None
        response = ""
        
        # Query handling
        if "trending up" in user_query or "rising" in user_query:
            # Find coins with rising price trend
            rising_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
            if rising_coins:
                # Prioritize high market cap for profitability
                high_cap_rising = [coin for coin in rising_coins if crypto_db[coin]["market_cap"] == "high"]
                if high_cap_rising:
                    recommendation = high_cap_rising[0]  # Pick first high-cap coin
                    response = f"Go for {recommendation}! 🚀 It’s trending up and has a huge market cap!"
                else:
                    recommendation = rising_coins[0]  # Fallback to any rising coin
                    response = f"{recommendation} is trending up! 📈 Solid pick for growth!"
            else:
                response = "No coins are trending up right now. 😕 Want to check sustainability instead?"
        
        elif "sustainable" in user_query or "eco-friendly" in user_query:
            # Find most sustainable coin
            recommendation = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            if crypto_db[recommendation]["sustainability_score"] > 7/10:
                response = f"Invest in {recommendation}! 🌱 It’s eco-friendly with a sustainability score of {crypto_db[recommendation]['sustainability_score']*10}/10!"
            else:
                response = f"{recommendation} is the greenest I’ve got, with a sustainability score of {crypto_db[recommendation]['sustainability_score']*10}/10. 🌿 Not perfect, but still decent!"
        
        elif "long-term growth" in user_query:
            # Combine profitability and sustainability
            candidates = [
                coin for coin, data in crypto_db.items()
                if data["price_trend"] == "rising" and data["sustainability_score"] > 5/10
            ]
            if candidates:
                recommendation = candidates[0]  # Pick first suitable coin
                response = f"For long-term growth, check out {recommendation}! 🚀 It’s trending up and has a sustainability score of {crypto_db[recommendation]['sustainability_score']*10}/10!"
            else:
                response = "No perfect long-term picks right now. 😕 Try asking for trending or sustainable coins!"
        
        else:
            response = "Hmmm, I didn’t catch that. Try asking about trending coins, sustainability, or long-term growth!"
        
        # Add disclaimer
        response += "\n⚠️ Crypto is risky—always do your own research!"
        print(response)

# Run the bot
crypto_bot()
    



