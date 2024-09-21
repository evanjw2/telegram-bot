from telegram import _update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from telegram import _chat
import random

# Card deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # 10's are for J, Q, K; 11 for Ace

# Function to deal cards
def deal_card():
    return random.choice(deck)

# Blackjack logic
def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

async def start_game(update: _update, context: CallbackContext) -> None:
    # Initializing hands for the player and dealer
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    context.user_data['player_hand'] = player_hand
    context.user_data['dealer_hand'] = dealer_hand

    await update.message.reply_text(f"Your hand: {player_hand} (Score: {calculate_score(player_hand)})")
    await update.message.reply_text(f"Dealer's visible card: {dealer_hand[0]}")

    await update.message.reply_text("Type /hit to draw a card, or /stand to end your turn.")

async def hit(update: _update, context: CallbackContext) -> None:
    player_hand = context.user_data['player_hand']
    player_hand.append(deal_card())
    score = calculate_score(player_hand)

    await update.message.reply_text(f"Your hand: {player_hand} (Score: {score})")

    if score > 21:
        await update.message.reply_text("Bust! You lose. Type /start to play again.")
    else:
        await update.message.reply_text("Type /hit to draw another card, or /stand to end your turn.")

async def stand(update: _update, context: CallbackContext) -> None:
    player_hand = context.user_data['player_hand']
    dealer_hand = context.user_data['dealer_hand']

    # Dealer's turn to play
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)

    await update.message.reply_text(f"Dealer's hand: {dealer_hand} (Score: {dealer_score})")

    if dealer_score > 21 or player_score > dealer_score:
        await update.message.reply_text("You win!")
    elif player_score < dealer_score:
        await update.message.reply_text("Dealer wins!")
    else:
        await update.message.reply_text("It's a tie!")

    await update.message.reply_text("Type /start to play again.")

async def main():
    # Initialize bot with token
    app = ApplicationBuilder().token("7621604261:AAG4z2RzO6kowotr8ZpoJ-SGvzsxGoncPM4").build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start_game))
    app.add_handler(CommandHandler("hit", hit))
    app.add_handler(CommandHandler("stand", stand))

    # Start the bot
    await app.start()
    await app.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
