# Coffee Futures Pricing

This project aims to price Coffee Futures using three different methods:

1.  Cost of Carry Model
2.  Black-Scholes Model
3.  Monte Carlo Simulation

## Data

The project uses the following data:

*   Spot price of Coffee: 425.10 USD/lb (obtained from Bloomberg website)
*   Risk-free rate: 4.19% (obtained from US Department of Treasury website)
*   Storage cost: 1% (assumed)
*   Time to maturity: 6 months
*   Strike price: 426.10 USD/lb (slightly higher than the spot price)
*   Historical Volatility: Calculated from Coffee dataset downloaded using yfinance for the period of February 10, 2024, to February 10, 2025.


## Methodology

### 1. Cost of Carry Model

The Cost of Carry model is used to determine the theoretical price of a futures contract by considering the relationship between spot prices, interest rates, storage costs, and the time to maturity.

Formula:
Ft = St * exp((r + d) * T)

Where:

*   Ft: Futures price
*   St: Spot price
*   r: Risk-free rate
*   d: Storage cost
*   T: Time to maturity


### 2. Black-Scholes Model

The Black-Scholes model is a mathematical model used to calculate the theoretical price of European-style options. It considers factors such as the underlying asset's price, volatility, time to expiration, and risk-free interest rate.

Formula:
c = St * N(d1) - X * exp(-r * T) * N(d2)

Where:

*   c: Call option price
*   St: Spot price
*   X: Strike price
*   r: Risk-free rate
*   T: Time to maturity
*   vol: Volatility
*   N(): Cumulative standard normal distribution function
*   d1 = (ln(St/X) + (r + 0.5 * vol^2) * T) / (vol * sqrt(T))
*   d2 = d1 - vol * sqrt(T)

### 3. Monte Carlo Simulation

Monte Carlo simulation is a computational technique that uses random sampling to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of random variables. In the context of futures pricing, it can simulate the underlying asset's price movements over time and estimate the expected future price based on the distribution of simulated paths.

Steps:

1.  Define the underlying asset's price process.
2.  Generate a large number of random price paths.
3.  Calculate the payoff of the futures contract for each path.
4.  Average the payoffs to get the expected future price.
