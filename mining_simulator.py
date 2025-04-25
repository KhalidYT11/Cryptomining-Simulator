import time
import random
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

class MiningRig:
    """Represents a mining rig with a specific hash rate."""
    def __init__(self, hash_rate_mhps):
        self.hash_rate = max(0, float(hash_rate_mhps))  # Ensure non-negative hash rate

class CryptoEconomy:
    """Manages the cryptocurrency price."""
    def __init__(self, initial_price=50000.0, price_drift=0.0001, price_volatility=0.005):
        self.current_price = initial_price
        self.history = [initial_price]
        self.drift = price_drift
        self.volatility = price_volatility

    def update_price(self):
        """Simulates price fluctuations using numpy."""
        price_change_percentage = np.random.normal(self.drift, self.volatility)
        self.current_price *= (1 + price_change_percentage)
        self.history.append(self.current_price)
        return self.current_price

class Miner:
    """Represents the crypto miner with balance, mining rig, and mining operations."""
    BLOCK_REWARD = 0.001
    POWER_COST_PER_HOUR = 0.5

    def __init__(self, initial_balance=100.0, mining_rig=None):
        self.balance = initial_balance
        self.rig = mining_rig
        self.total_mined = 0.0
        self.balance_history = [initial_balance]
        self.time_history = [datetime.now()]
        self.last_update_time = time.time()

    def set_rig(self, rig):
        """Sets the mining rig for the miner."""
        self.rig = rig
        print(f"Mining rig set with hash rate: {self.rig.hash_rate:.2f} MH/s.")

    def mine_block(self, crypto_price):
        """Simulates the process of mining a block."""
        if self.rig and self.rig.hash_rate > 0:
            probability = self.rig.hash_rate / 1_000_000.0  # Adjust divisor for difficulty
            if random.random() < probability:
                reward = self.BLOCK_REWARD * crypto_price
                self.balance += reward
                self.total_mined += self.BLOCK_REWARD
                self._record_balance()
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Block mined! Received ${reward:.2f} ({self.BLOCK_REWARD:.8f} BTC). New balance: ${self.balance:.2f}")
                return True
            else:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Mining... (no block found)")
                return False
        else:
            print("Cannot mine without a mining rig or with zero hash rate.")
            return False

    def deduct_power_cost(self):
        """Deducts the cost of running the mining operation."""
        if self.rig and self.rig.hash_rate > 0:
            time_elapsed = time.time() - self.last_update_time
            hours_elapsed = time_elapsed / 3600
            cost = hours_elapsed * self.POWER_COST_PER_HOUR
            self.balance -= cost
            self._record_balance()
            self.last_update_time = time.time()
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Power cost deducted: ${cost:.2f}. New balance: ${self.balance:.2f}")
        self.last_update_time = time.time()

    def get_status(self, current_crypto_price):
        """Prints the current status of the miner."""
        print("\n--- Miner Status ---")
        print(f"Current Balance: ${self.balance:.2f}")
        print(f"Hash Rate: {self.rig.hash_rate:.2f} MH/s" if self.rig else "No mining rig set")
        print(f"Current Crypto Price: ${current_crypto_price:.2f}")
        print(f"Total Crypto Mined: {self.total_mined:.8f} BTC")
        print("-----------------------\n")

    def plot_balance(self):
        """Plots the balance history over time."""
        if len(self.time_history) > 1:
            dates = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in self.time_history]
            plt.plot(dates, self.balance_history)
            plt.xlabel("Time")
            plt.ylabel("Balance ($)")
            plt.title("Balance Over Time")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
        else:
            print("Not enough data to plot balance history yet.")

    def _record_balance(self):
        """Records the current balance and timestamp."""
        self.balance_history.append(self.balance)
        self.time_history.append(datetime.now())

def main():
    economy = CryptoEconomy()
    miner = Miner()

    while True:
        print("\n--- Crypto Mining Simulator ---")
        print("1. Set Mining Rig (Hash Rate)")
        print("2. Mine (Simulate)")
        print("3. Check Status")
        print("4. Plot Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                hash_rate = float(input("Enter desired hash rate (in MH/s): "))
                rig = MiningRig(hash_rate)
                miner.set_rig(rig)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '2':
            if miner.rig:
                mining_duration = 10  # Simulate mining for a few seconds
                print(f"Simulating mining for {mining_duration} seconds...")
                start_time = time.time()
                while time.time() - start_time < mining_duration:
                    current_price = economy.update_price()
                    miner.mine_block(current_price)
                    miner.deduct_power_cost()
                    time.sleep(random.uniform(0.1, 1.0)) # Simulate varying mining times
            else:
                print("Please set up a mining rig first (option 1).")
        elif choice == '3':
            miner.get_status(economy.current_price)
        elif choice == '4':
            miner.plot_balance()
        elif choice == '5':
            print("Exiting simulator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
