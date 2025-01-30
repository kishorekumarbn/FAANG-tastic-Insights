# FAANG-tastic-Insights
Predicting Stock Prices with Regression and MLflow

📈 FAANG-tastic Insights: Predict Stock Prices with Regression and MLflow

Welcome to FAANG-tastic Insights, a stock price prediction web application built using Machine Learning, Streamlit, and MLflow. This project leverages regression models to predict the closing price of FAANG stocks (Facebook, Apple, Amazon, Netflix, Google), providing users with an intuitive interface for real-time predictions.
🚀 Features

🔹 Predict Stock Prices: Enter stock attributes (Open, High, Low, Volume) and get the predicted closing price.
🔹 Multiple Regression Models: Evaluated models include Linear Regression, Decision Tree, Random Forest, XGBoost, and LightGBM.
🔹 MLflow Integration: Model performance is logged, tracked, and compared using MLflow.
🔹 Scalable & Reusable: Separate pickled models and scalers ensure consistency across predictions.
🔹 Interactive Web App: Built with Streamlit for a seamless user experience.
🛠️ Tech Stack

    Python 🐍
    Pandas & NumPy 📊
    Scikit-Learn, XGBoost, LightGBM 🔥
    MLflow 📈
    Streamlit 🎨
    Pickle for Model Persistence 📂

📊 Model Performance

The best model is selected based on MAE, RMSE, and R² score:
Model	MAE	RMSE	R² Score
Linear Regression	✅ Best	✅ Best	✅ Best
Decision Tree	❌	❌	❌
Random Forest	❌	❌	❌
XGBoost	❌	❌	❌
LightGBM	❌	❌	❌

    📌 Note: The final selected model is stored as a pickle file (.pkl), along with a fitted scaler to preprocess user inputs.

🔧 Setup & Run

1️⃣ Clone the Repository

git clone https://github.com/kishorekumarbn/Stock-Price-Prediction-FAANG-tastic-Insights-.git

2️⃣ Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run MLflow Tracking Server (Optional)

mlflow ui

    Open http://127.0.0.1:5000 to view the MLflow dashboard.

5️⃣ Run the Streamlit App

streamlit run app.py

🎯 How It Works

1️⃣ Select a Company from the dropdown (Apple, Google, Facebook, Amazon, Netflix).
2️⃣ Enter Feature Values (Open, High, Low, Volume).
3️⃣ Predict the Closing Price using the best performing model.
4️⃣ View Results instantly on the interactive web app.
📌 Future Enhancements

🚀 Deploy on Cloud (AWS/GCP/Azure)
📊 Real-Time Stock Data Integration
📈 More Advanced ML/DL Models
🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.
🏆 Credits

💡 Developed by KISHORE KUMAR B N
📧 Contact: kishorekumarbn18@gmail.com
🌟 If you like this project, star ⭐ the repo and share it!
