# Crypto Mining Simulator (Python)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This Python script provides a simplified simulation of cryptocurrency mining, allowing you to explore the basic concepts of hash rate, block rewards, price fluctuations, and power costs without involving real hardware. This version features a cleaner code structure and utilizes the `numpy` and `matplotlib` libraries for enhanced price simulation and balance visualization.

## Features

* **Simulated Mining Rigs:** Define a virtual mining rig with a specific hash rate (in MH/s), influencing your chances of mining blocks.
* **Dynamic Cryptocurrency Price:** The price of the simulated cryptocurrency fluctuates over time using a model based on a slight upward drift and random volatility (powered by `numpy`).
* **Block Mining Simulation:** The simulator models the process of finding cryptocurrency blocks, with the probability of success determined by your mining rig's hash rate.
* **Balance Tracking:** Monitor your in-simulation balance in fiat currency (e.g., USD), which increases with mined blocks and decreases with power costs.
* **Power Cost Simulation:** A simulated hourly cost is deducted from your balance to represent electricity expenses.
* **Status Updates:** Get real-time information on your current balance, mining rig's hash rate, the current cryptocurrency price, and the total amount of cryptocurrency mined.
* **Balance Visualization:** Visualize your balance history over time using a line plot generated with `matplotlib`.

## How to Run

1.  **Save the Code:** Save the Python script (e.g., `mining_simulator_clean.py`).
2.  **Install Dependencies:** Ensure you have the required external libraries installed. Open your terminal or command prompt and run:
    ```bash
    pip install numpy matplotlib
    ```
3.  **Navigate to Directory:** Go to the directory where you saved the Python script.
4.  **Run the Script:** Execute the script using the command:
    ```bash
    python mining_simulator_clean.py
    ```
5.  **Follow the Menu:** The simulator will present a menu with the following options:
    * **1. Set Mining Rig (Hash Rate):** Enter the hash rate for your virtual mining rig.
    * **2. Mine (Simulate):** Run the mining simulation for a short period, during which the price will update, mining attempts will occur, and power costs will be deducted.
    * **3. Check Status:** Display the current status of your miner and the cryptocurrency market.
    * **4. Plot Balance:** Generate and display a plot of your balance over time.
    * **5. Exit:** Close the simulator.

## Important Notes

* **No Actual Mining:** This program **does not** perform any real cryptocurrency mining. It is a simulation for educational and entertainment purposes only.
* **Simulated Economy:** All economic factors, including price fluctuations, block rewards, and power costs, are simulated and do not reflect real-world market conditions.
* **Simplified Model:** This simulator provides a simplified representation of cryptocurrency mining and does not include complexities like network difficulty adjustments, mining pools, or different mining algorithms.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
