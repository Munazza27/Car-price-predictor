# Car-price-predictor
Car Price Predictor is a Flask web app that uses a machine learning model to estimate used car prices based on brand, model, year, fuel type, and kilometers driven





Car Price Predictor

A Flask-based machine learning web application that predicts the resale value of used cars based on attributes like brand, model, year, fuel type, and kilometers driven.  

This project demonstrates how to build, train, and deploy a machine learning model using **scikit-learn** and serve predictions through a simple web interface.
---->Features
- Interactive web form for entering car details
- Real-time price prediction using a trained Linear Regression model
- Machine learning pipeline with preprocessing (OneHotEncoder for categorical features)
- Optimized model selection using R² score across randomized splits
- Clean UI with prediction results displayed instantly
<img width="1808" height="805" alt="image" src="https://github.com/user-attachments/assets/c4656868-c4e0-46e8-a06f-ea9544f68049" />
---->Tech Stack
- Backend: Python, Flask  
- Frontend: HTML (Jinja2 templates)  
- Machine Learning: scikit-learn, pandas, numpy  
- Development Tools: Jupyter Notebook, VS Code
<img width="1907" height="1027" alt="Screenshot 2025-12-03 205238" src="https://github.com/user-attachments/assets/c0732c49-2a52-4825-bbd4-275f4685fc4b" />
<img width="1903" height="710" alt="Screenshot 2025-12-03 205327" src="https://github.com/user-attachments/assets/3b40070d-62f0-425a-956c-ae9c031a32e1" />
----->Model Details
- Trained on a dataset of car listings (`cleaned_car_data.csv`)  
- Pipeline includes column transformer for categorical encoding  
- Achieved an R² score of ~0.9 with optimal random state  


---

## 📁 Project Structure
