import time
import random
from datetime import datetime

class CryptoMiningSimulator:
    def __init__(self, initial_balance=100.0):
        self.balance = initial_balance
        self.hash_rate = 0
        self.crypto_price = 50000.0  # Initial price
        self.block_reward = 0.001    # Reward per mined block
        self.mining_power_cost_per_hour = 0.5  # Cost to run mining
        self.last_update_time = time.time()
        self.total_mined = 0.0

    def set_hash_rate(self, hash_rate):
        """Sets the simulated hash rate."""
        if hash_rate >= 0:
            self.hash_rate = hash_rate
            print(f"Hash rate set to {self.hash_rate} MH/s.")
        else:
            print("Hash rate cannot be negative.")

    def mine_block(self):
        """Simulates the process of mining a block."""
        if self.hash_rate > 0:
            # Probability of finding a block is proportional to hash rate
            probability = self.hash_rate / 1000000.0  # Adjust divisor for difficulty
            if random.random() < probability:
                self.balance += self.block_reward * self.crypto_price
                self.total_mined += self.block_reward
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Block mined! Received {self.block_reward:.8f} BTC. New balance: ${self.balance:.2f}")
            else:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Mining... (no block found)")
        else:
            print("Cannot mine with zero hash rate.")

    def update_price(self):
        """Simulates random price fluctuations."""
        price_change = random.uniform(-0.01, 0.01) * self.crypto_price
        self.crypto_price += price_change
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Crypto price updated: ${self.crypto_price:.2f}")

    def deduct_power_cost(self):
        """Deducts the cost of running the mining operation."""
        time_elapsed = time.time() - self.last_update_time
        hours_elapsed = time_elapsed / 3600
        cost = hours_elapsed * self.mining_power_cost_per_hour
        self.balance -= cost
        self.last_update_time = time.time()
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Power cost deducted: ${cost:.2f}. New balance: ${self.balance:.2f}")

    def get_status(self):
        """Prints the current status of the simulator."""
        print("\n--- Mining Status ---")
        print(f"Current Balance: ${self.balance:.2f}")
        print(f"Hash Rate: {self.hash_rate} MH/s")
        print(f"Current Crypto Price: ${self.crypto_price:.2f}")
        print(f"Total Crypto Mined: {self.total_mined:.8f} BTC")
        print("-----------------------\n")

def main():
    simulator = CryptoMiningSimulator()

    while True:
        print("\n--- Crypto Mining Simulator ---")
        print("1. Set Hash Rate")
        print("2. Mine (Simulate)")
        print("3. Check Status")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                hash_rate = float(input("Enter desired hash rate (in MH/s): "))
                simulator.set_hash_rate(hash_rate)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '2':
            mining_duration = 10  # Simulate mining for a few seconds
            print(f"Simulating mining for {mining_duration} seconds...")
            start_time = time.time()
            while time.time() - start_time < mining_duration:
                simulator.mine_block()
                simulator.update_price()
                simulator.deduct_power_cost()
                time.sleep(random.uniform(0.1, 1.0)) # Simulate varying mining times
        elif choice == '3':
            simulator.get_status()
        elif choice == '4':
            print("Exiting simulator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
