# fourier-series-square-wave
Python implementation of Fourier series approximation for a square wave
# Fourier Series Approximation of a Square Wave

## 📌 Overview
This project demonstrates how to approximate a square wave using the Fourier series. It computes the Fourier coefficients (aₙ, bₙ) and reconstructs the waveform using **Python**, `scipy`, and `matplotlib`. The result is a comparison between the original square wave and its Fourier series approximation.

## 🚀 Features
- Computes Fourier coefficients using numerical integration.
- Reconstructs the square wave using a finite number of terms.
- Plots both the original square wave and its Fourier approximation.

## 🛠 Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/fourier-series-square-wave.git
   cd fourier-series-square-wave
2. Install dependencies:
   pip install numpy matplotlib scipy
   
3.Run the script:
  python fourier_series_square_wave.py
  
## 📊 Example Output
The script generates a plot comparing the original square wave and its Fourier series approximation (with 50 terms).

![Fourier Series Approximation](https://github.com/your-username/fourier-series-square-wave/blob/main/fourier_plot.png)

📝 Code Explanation
1.Define the square wave function using scipy.signal.square(x).
2.Compute Fourier coefficients (aₙ, bₙ) using numerical integration.
3.Reconstruct the Fourier series using cosine and sine terms.
4.Plot the original and approximated functions for visualization.

📜 License
This project is open-source and available under the MIT License.





