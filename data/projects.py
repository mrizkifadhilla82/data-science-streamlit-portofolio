PROJECTS = [
    {
        "id": "house-price-prediction",
        "title": "House Price Prediction",
        "domain": "Regression / MLOps",
        "status": "🟢 Deployed",
        "business_problem": """
            Real estate agents and property platforms struggle to price listings accurately.
            Manual valuation is slow, inconsistent, and heavily reliant on individual intuition —
            leading to underpriced or overpriced properties that hurt both sellers and buyers.
        """,
        "pain_points": [
            "Manual valuation takes 3–5 business days per property",
            "Estimates vary widely between agents (±20% deviation)",
            "No scalable system for hundreds of simultaneous listings",
            "Lack of data-driven insights for pricing strategy",
        ],
        "solution": """
            Built an end-to-end Machine Learning pipeline that predicts house prices based on
            80+ property features (area, quality, location, age, amenities). The model is served
            via a FastAPI REST endpoint containerized with Docker, enabling real-time predictions
            in milliseconds.
        """,
        "impact": [
            "Achieved an R² score of 0.895 on the validation dataset.",
            "Reduced property valuation time from 3–5 days to under 100 milliseconds.",
            "Successfully deployed as a scalable microservice using Docker and FastAPI.",
            "Enabled seamless integration with front-end dashboards via REST APIs.",
        ],
        "tools": ["Python", "Scikit-learn", "FastAPI", "Docker", "MLflow", "Joblib"],
        "github": "https://github.com/mrizkifadhilla82/mrizkifadhilla82",
        "demo": "/Prediction",
        "image_path": "house_cover.png",
    },
    {
        "id": "bank-churn-prediction",
        "title": "Bank Customer Churn Prediction",
        "domain": "Classification / ML",
        "status": "✅ Completed",
        "business_problem": """
            A bank is losing customers silently — churned customers (attrited) stop using services
            without warning. The bank cannot proactively retain them because there is no early
            detection system to identify at-risk customers before they leave.
        """,
        "pain_points": [
            "No early warning system for customer churn detection",
            "16% of customers are already churned — significant revenue loss",
            "Severe class imbalance (84% existing vs. 16% churned) makes detection harder",
            "Reactive retention strategy — too late after customers already churned",
        ],
        "solution": """
            Built a binary classification model using Logistic Regression and Random Forest,
            with SMOTE oversampling to handle the class imbalance. Analyzed 21 customer features
            (demographics, financial behavior, transaction history) to identify churn risk signals.
            The model enables proactive retention campaigns targeting high-risk customers.
        """,
        "impact": [
            "Random Forest model achieved 96% Recall and 99% AUC-ROC, outperforming Logistic Regression.",
            "Successfully addressed extreme class imbalance (84:16) using SMOTE techniques.",
            "Identified top churn drivers: Transaction Count, Months Inactive, and Total Transaction Amount.",
            "Enabled the business to proactively target at-risk customers, maximizing retention efforts.",
        ],
        "tools": ["Python", "XGBoost", "Scikit-learn", "Pandas", "Seaborn", "Matplotlib"],
        "github": "https://github.com/mrizkifadhilla82/mrizkifadhilla82",
        "demo": None,
        "notebook": "notebooks/Muhammad_Rizki_Fadhilla_DSML40_Day37.ipynb",
        "image_path": "bank_cover.jpg",
    },
    {
        "id": "ecommerce-rfm-analysis",
        "title": "E-Commerce RFM Customer Segmentation",
        "domain": "Analytics / Customer Segmentation",
        "status": "✅ Completed",
        "business_problem": """
            An e-commerce business treats all customers the same — sending identical promotions
            and offers regardless of purchase history. This leads to wasted marketing budget
            on inactive customers and missed opportunities to reward loyal, high-value ones.
        """,
        "pain_points": [
            "No customer segmentation — all customers receive identical marketing",
            "High marketing budget waste on inactive/low-value customers",
            "Unable to identify and reward top-tier loyal customers",
            "No data-driven approach to prioritize retention vs. acquisition efforts",
        ],
        "solution": """
            Implemented RFM (Recency, Frequency, Monetary) analysis on 4,870 e-commerce transactions
            across 31 countries. Used statistical analysis and regression modeling (Statsmodels)
            to segment customers into tiers: Champions, Loyal, At-Risk, and Lost — enabling
            targeted, personalized marketing campaigns.
        """,
        "impact": [
            "Successfully segmented 1,932 unique customers into actionable tiers (Champions, Loyal, At-Risk, Lost).",
            "Uncovered insights showing a small percentage of 'Champions' generate a disproportionate amount of revenue.",
            "Provided data-driven strategies to increase Customer Lifetime Value (CLV) based on specific RFM segments.",
            "Processed and analyzed 4,870 transactions across 31 different countries.",
        ],
        "tools": ["Python", "Pandas", "Seaborn", "Matplotlib", "NumPy"],
        "github": "https://github.com/mrizkifadhilla82/mrizkifadhilla82",
        "demo": None,
        "notebook": "notebooks/Muhammad_Rizki_Fadhilla_DSML40_Day17.ipynb",
        "image_path": "ecom_cover.jpg",
    },
]
