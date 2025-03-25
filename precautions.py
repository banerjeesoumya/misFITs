import json

disease_remedies = {
    "URTI": [
        "Rest and stay hydrated",
        "Use saline nasal spray to clear congestion",
        "Take over-the-counter pain relievers for fever or aches",
        "Drink warm fluids like tea or soup"
    ],
    "Viral pharyngitis": [
        "Gargle with warm salt water",
        "Drink warm fluids to soothe the throat",
        "Use throat lozenges or sprays",
        "Rest and stay hydrated"
    ],
    "Anemia": [
        "Increase iron-rich foods like spinach, red meat, and lentils",
        "Take iron supplements if prescribed",
        "Avoid drinking tea or coffee with meals to enhance iron absorption",
        "Get regular check-ups for underlying causes"
    ],
    "HIV (initial infection)": [
        "Start antiretroviral therapy (ART) as soon as possible",
        "Maintain a balanced diet and exercise regularly",
        "Avoid sharing needles or unprotected sex",
        "Get regular check-ups to monitor immune function"
    ],
    "Localized edema": [
        "Elevate the affected area",
        "Reduce salt intake to minimize fluid retention",
        "Stay active and avoid prolonged sitting or standing",
        "Use compression stockings if recommended"
    ],
    "Anaphylaxis": [
        "Use an epinephrine auto-injector immediately",
        "Call emergency services",
        "Lie down and elevate legs if possible",
        "Avoid known allergens in the future"
    ],
    "Pulmonary embolism": [
        "Seek emergency medical help immediately",
        "Avoid long periods of immobility",
        "Stay hydrated and wear compression stockings if at risk",
        "Take anticoagulants as prescribed"
    ],
    "Influenza": [
        "Rest and stay hydrated",
        "Take antiviral medications if prescribed early",
        "Use fever reducers like acetaminophen",
        "Avoid contact with others to prevent spread"
    ],
    "Bronchitis": [
        "Stay hydrated and drink warm fluids",
        "Use a humidifier to soothe airways",
        "Avoid smoking and irritants",
        "Get plenty of rest and use cough suppressants if needed"
    ],
    "Allergic sinusitis": [
        "Use antihistamines or nasal sprays",
        "Avoid allergens like dust or pollen",
        "Try steam inhalation for congestion relief",
        "Stay hydrated to thin mucus"
    ],
    "Acute dystonic reactions": [
        "Seek immediate medical care",
        "Take anticholinergic medications as prescribed",
        "Avoid drugs that triggered the reaction",
        "Perform slow, controlled breathing to manage discomfort"
    ],
    "GERD": [
        "Avoid acidic and spicy foods",
        "Eat smaller, frequent meals",
        "Avoid lying down right after eating",
        "Elevate the head of your bed while sleeping"
    ],
    "Acute otitis media": [
        "Use warm compresses to ease ear pain",
        "Take over-the-counter pain relievers",
        "Avoid water exposure in the affected ear",
        "Consult a doctor if symptoms persist or worsen"
    ],
    "Pneumonia": [
        "Take prescribed antibiotics (if bacterial)",
        "Rest and stay hydrated",
        "Use a humidifier or steam to ease breathing",
        "Get vaccinated to prevent future infections"
    ],
    "Panic attack": [
        "Practice deep breathing exercises",
        "Use grounding techniques to stay present",
        "Avoid caffeine and stimulants",
        "Seek professional help for ongoing episodes"
    ],
    "Acute laryngitis": [
        "Rest your voice and avoid talking or whispering",
        "Drink plenty of fluids to stay hydrated",
        "Use a humidifier or inhale steam to moisturize your throat",
        "Gargle with warm salt water to soothe irritation"
    ],
    "Pericarditis": [
        "Rest and avoid strenuous activity",
        "Take NSAIDs like ibuprofen for pain and inflammation as directed",
        "Seek immediate medical care for severe chest pain or breathing difficulty"
    ],
    "Sarcoidosis": [
        "Get adequate rest and sleep",
        "Eat a healthy, balanced diet",
        "Avoid smoking and exposure to irritants",
        "Manage stress through relaxation techniques"
    ],
    "Possible NSTEMI / STEMI": [
        "Call emergency services immediately",
        "Chew and swallow aspirin if available and not contraindicated",
        "Rest and try to remain calm",
        "Be prepared to start CPR if needed"
    ],
    "Unstable angina": [
        "Call emergency services immediately",
        "Rest in a comfortable position",
        "Take nitroglycerin if prescribed",
        "Chew aspirin if recommended by a doctor"
    ],
    "Atrial fibrillation": [
        "Take medications as prescribed",
        "Avoid triggers like caffeine and alcohol",
        "Manage stress through relaxation techniques",
        "Seek medical care for severe symptoms"
    ],
    "Cluster headache": [
        "Use oxygen therapy if prescribed",
        "Apply cold compresses to affected area",
        "Avoid known triggers like alcohol",
        "Seek emergency care for severe, persistent pain"
    ],
    "Chronic rhinosinusitis": [
        "Use saline nasal irrigation",
        "Apply warm compresses to face",
        "Stay hydrated and get adequate rest",
        "Avoid irritants like smoke"
    ],
    "Inguinal hernia": [
        "Avoid heavy lifting and straining",
        "Support the hernia with your hand when coughing/sneezing",
        "Wear a supportive truss if recommended",
        "Seek emergency care for severe pain or vomiting"
    ],
    "Bronchospasm / acute asthma exacerbation": [
        "Use quick-relief inhaler as prescribed",
        "Sit upright and try to remain calm",
        "Remove yourself from any triggers",
        "Seek emergency care if symptoms worsen"
    ],
    "Acute pulmonary edema": [
        "Sit upright to ease breathing",
        "Take diuretics if prescribed",
        "Seek emergency medical help",
        "Avoid excess salt and fluid intake"
    ],
    "Pancreatic neoplasm": [
        "Consult an oncologist for treatment options",
        "Eat small, frequent meals",
        "Manage pain with prescribed medications",
        "Consider enzyme supplements if digestion is affected"
    ],
    "Bronchiectasis": [
        "Perform airway clearance exercises",
        "Stay hydrated to loosen mucus",
        "Use a humidifier to ease breathing",
        "Take prescribed antibiotics if an infection occurs"
    ],
    "PSVT": [
        "Perform vagal maneuvers like the Valsalva maneuver",
        "Take prescribed medications",
        "Avoid caffeine and other stimulants",
        "Seek emergency care for prolonged episodes"
    ],
    "Myasthenia gravis": [
        "Take anticholinesterase medications as prescribed",
        "Avoid overexertion and manage fatigue",
        "Eat small, frequent meals to ease swallowing",
        "Consult a doctor for immunosuppressive therapy if needed"
    ],
    "Epiglottitis": [
        "Seek emergency medical care immediately",
        "Avoid lying down to prevent airway obstruction",
        "Do not attempt to inspect the throat",
        "Take prescribed antibiotics if bacterial"
    ],
    "Stable angina": [
        "Take nitroglycerin as prescribed",
        "Avoid physical exertion during episodes",
        "Manage cholesterol and blood pressure",
        "Follow a heart-healthy diet"
    ],
    "Boerhaave syndrome": [
        "Seek emergency medical treatment",
        "Avoid eating or drinking until evaluated",
        "Receive IV fluids and antibiotics as needed",
        "Undergo surgical intervention if necessary"
    ],
    "Tuberculosis": [
        "Take the full course of prescribed antibiotics",
        "Avoid close contact with others to prevent spread",
        "Maintain good hygiene and cough etiquette",
        "Ensure proper ventilation in living spaces"
    ],
    "Pulmonary neoplasm": [
        "Consult an oncologist for treatment options",
        "Quit smoking and avoid pollutants",
        "Manage pain with medications",
        "Follow a nutritious diet to maintain strength"
    ],
     "Acute rhinosinusitis": [
        "Use saline nasal irrigation to clear sinuses",
        "Apply warm compresses to face to relieve pain and pressure",
        "Take over-the-counter pain relievers as needed",
        "Rest and stay hydrated",
        "Avoid irritants like smoke"
    ],
    "SLE (Systemic Lupus Erythematosus)": [
        "Avoid sun exposure and use sunscreen",
        "Get adequate rest and manage stress",
        "Take medications as prescribed",
        "Maintain a healthy diet and exercise routine",
        "Attend regular check-ups with healthcare provider"
    ],
    "Myocarditis": [
        "Rest and limit physical activity",
        "Take medications as prescribed by doctor",
        "Monitor for worsening symptoms like chest pain or difficulty breathing",
        "Follow a heart-healthy diet low in salt",
        "Avoid alcohol and tobacco"
    ],
    "Laryngospasm": [
        "Remove any stimuli causing the spasm",
        "Apply continuous positive airway pressure (CPAP) with 100% oxygen",
        "Perform jaw thrust maneuver",
        "Administer medications like propofol or succinylcholine if needed (by medical professionals)"
    ],
    "Spontaneous pneumothorax": [
        "Seek immediate medical attention if symptoms occur",
        "Rest and avoid strenuous activity",
        "Do not fly in airplanes or scuba dive until cleared by a doctor",
        "Stop smoking to reduce risk of recurrence",
        "Follow-up with healthcare provider as recommended"
    ],
    "Chagas disease": [
        "Use insecticide-treated bed nets when sleeping in endemic areas",
        "Inspect lodgings for signs of triatomine bugs",
        "Avoid consuming unpasteurized juices in endemic regions",
        "Use insect repellent on exposed skin",
        "Seek medical attention if bitten by a kissing bug"
    ],
    "Whooping cough": [
        "Take prescribed antibiotics as directed",
        "Use a cool mist humidifier to loosen mucus",
        "Drink plenty of fluids to prevent dehydration",
        "Keep the home free of irritants like smoke or dust",
        "Rest and avoid spreading the infection to others"
    ],
    "Spontaneous rib fracture": [
        "Apply ice to the affected area to reduce pain and swelling",
        "Take pain medication as recommended by a doctor",
        "Avoid activities that cause pain",
        "Practice deep breathing exercises to prevent lung complications",
        "Seek medical attention if severe pain or breathing difficulties occur"
    ],
    "Croup": [
        "Keep the child calm and sitting upright to ease breathing",
        "Use a cool mist humidifier in the child's room",
        "Offer plenty of fluids to prevent dehydration",
        "Avoid exposure to irritants like cigarette smoke",
        "Seek emergency care if the child has severe breathing difficulties"
    ],
    "Ebola": [
        "Isolate infected individuals immediately",
        "Use personal protective equipment when caring for patients",
        "Practice strict hygiene and disinfection procedures",
        "Avoid contact with bodily fluids of infected individuals",
        "Seek immediate medical care if symptoms develop after potential exposure"
    ],
    "Bronchiolitis": [
        "Ensure the child drinks plenty of fluids to prevent dehydration",
        "Use a rubber suction bulb to clear nasal congestion",
        "Elevate the child's head while sleeping to ease breathing",
        "Avoid exposure to tobacco smoke and other irritants",
        "Seek medical attention if breathing difficulties worsen"
    ]
}

with open('convert.txt', 'w') as convert_file: 
    convert_file.write(json.dumps(disease_remedies))