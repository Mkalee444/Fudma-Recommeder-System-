import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

class Recommender:
    def __init__(self):
        self.applicants = pd.read_csv('data/applicants.csv')
        self.courses = pd.read_csv('data/courses.csv')
        self.scaler = StandardScaler()
        self.model = self._train_model()

    def _train_model(self):
        # Feature engineering for courses
        X = self.courses[['JAMB_Cutoff', 'Math_Cutoff', 'Employability']]
        X_scaled = self.scaler.fit_transform(X)
        model = NearestNeighbors(n_neighbors=3, metric='cosine').fit(X_scaled)
        return model

    def recommend(self, applicant_id):
        # Get applicant data
        applicant = self.applicants[self.applicants['ApplicantID'] == applicant_id].iloc[0]
        
        # Filter eligible courses
        eligible = self.courses[
            (self.courses['JAMB_Cutoff'] <= applicant['JAMB_Score']) &
            (self.courses['Math_Cutoff'] <= applicant['Math_Score'])
        ]
        
        if eligible.empty:
            return "No eligible courses. Consider improving your scores."
        
        # Prepare applicant features for ML
        applicant_features = self.scaler.transform([[
            applicant['JAMB_Score'],
            applicant['Math_Score'],
            0.8  # Default employability weight (adjustable)
        ]])
        
        # Find closest matching courses
        _, indices = self.model.kneighbors(applicant_features)
        recommendations = eligible.iloc[indices[0]]
        
        # Add interest match score
        recommendations['Interest_Match'] = recommendations['Course'].apply(
            lambda x: 1 if applicant['Interest'] in x else 0.5
        )
        
        return recommendations.sort_values(by=['Interest_Match', 'Employability'], ascending=False)

