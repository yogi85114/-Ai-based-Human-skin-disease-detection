"""
Disease information database for the AI Skin Disease Prediction Chatbot.
Contains descriptions, symptoms, treatments, and severity for all 11 supported diseases
matching the actual dataset classes.
"""

DISEASE_INFO = {
    "Acne": {
        "full_name": "Acne Vulgaris",
        "description": "Acne is a common skin condition that occurs when hair follicles become clogged with oil and dead skin cells. It most commonly affects the face, chest, and back, and is especially prevalent during adolescence due to hormonal changes.",
        "symptoms": [
            "Whiteheads (closed clogged pores)",
            "Blackheads (open clogged pores)",
            "Red, tender bumps (papules)",
            "Pus-filled pimples (pustules)",
            "Large, solid, painful lumps under the skin (nodules)",
            "Painful, pus-filled lumps under the skin (cysts)"
        ],
        "causes": [
            "Excess oil (sebum) production",
            "Clogged hair follicles with oil and dead skin cells",
            "Bacterial infection (Cutibacterium acnes)",
            "Hormonal changes (puberty, menstrual cycle, PCOS)",
            "Certain medications (corticosteroids, lithium)"
        ],
        "treatment": [
            "Benzoyl peroxide and salicylic acid (OTC)",
            "Topical retinoids (tretinoin, adapalene)",
            "Topical or oral antibiotics",
            "Hormonal therapies (birth control pills, spironolactone)",
            "Isotretinoin for severe cystic acne",
            "Proper skincare routine (gentle cleansing, non-comedogenic products)"
        ],
        "severity": "Mild to Moderate",
        "see_doctor": "See a dermatologist if acne is severe (cystic/nodular), leaving scars, not responding to OTC treatments, or significantly affecting your self-esteem.",
        "emoji": "🔴"
    },

    "Eczema": {
        "full_name": "Eczema (Atopic Dermatitis)",
        "description": "Eczema is a chronic inflammatory skin condition that causes dry, itchy, and inflamed patches of skin. It is one of the most common skin conditions, often starting in childhood and sometimes persisting into adulthood.",
        "symptoms": [
            "Dry, cracked, scaly skin",
            "Intense itching, especially at night",
            "Red to brownish-gray patches",
            "Small, raised bumps that may leak fluid",
            "Thickened skin from repeated scratching",
            "Raw, swollen skin from scratching"
        ],
        "causes": [
            "Genetic predisposition",
            "Immune system overreaction",
            "Environmental triggers (allergens, irritants)",
            "Stress and hormonal changes"
        ],
        "treatment": [
            "Moisturizers and emollients applied regularly",
            "Topical corticosteroids for flare-ups",
            "Antihistamines for itch relief",
            "Avoiding known triggers and irritants",
            "Phototherapy (light therapy) for severe cases",
            "Immunosuppressants for chronic severe eczema"
        ],
        "severity": "Mild to Moderate",
        "see_doctor": "See a dermatologist if symptoms interfere with sleep or daily activities, if the skin becomes infected (oozing, crusting), or if over-the-counter treatments are not providing relief.",
        "emoji": "🔴"
    },

    "Infestations_Bites": {
        "full_name": "Skin Infestations & Insect Bites",
        "description": "Skin infestations include conditions like scabies (caused by mites), lice, and other parasitic infections. Insect bites from mosquitoes, fleas, bedbugs, and other insects cause localized skin reactions ranging from mild irritation to severe allergic responses.",
        "symptoms": [
            "Intense itching, especially at night (scabies)",
            "Small red bumps, blisters, or hives",
            "Burrow tracks visible under skin (scabies)",
            "Swelling or redness around bite site",
            "Rash that may spread or form clusters",
            "Visible parasites or eggs in hair/skin (lice)"
        ],
        "causes": [
            "Sarcoptes scabiei mite (scabies)",
            "Head lice, body lice, or pubic lice",
            "Mosquitoes, fleas, bedbugs, ticks",
            "Close contact with infected individuals",
            "Exposure to contaminated environments"
        ],
        "treatment": [
            "Permethrin cream or lotion (scabies/lice treatment)",
            "Oral ivermectin for severe scabies",
            "Antihistamines to relieve itching",
            "Topical corticosteroids to reduce inflammation",
            "Thorough laundering of all clothing and bedding",
            "Treating close contacts simultaneously"
        ],
        "severity": "Mild to Moderate",
        "see_doctor": "See a doctor if the infestation does not clear with OTC treatments, if symptoms worsen, or if you develop fever or signs of secondary bacterial infection.",
        "emoji": "🐛"
    },

    "Lupus": {
        "full_name": "Lupus (Systemic Lupus Erythematosus)",
        "description": "Lupus is a chronic autoimmune disease where the immune system attacks healthy tissue. The most distinctive skin manifestation is the butterfly-shaped rash (malar rash) across the cheeks and nose. Lupus can affect the skin, joints, kidneys, brain, and other organs.",
        "symptoms": [
            "Butterfly-shaped rash across cheeks and nose",
            "Photosensitivity (skin rash from sun exposure)",
            "Discoid rash — red, scaly, coin-shaped lesions",
            "Hair loss and thinning",
            "Mouth or nose ulcers",
            "Joint pain, swelling, and stiffness"
        ],
        "causes": [
            "Autoimmune dysfunction (immune system attacks own cells)",
            "Genetic predisposition",
            "Hormonal factors (more common in women)",
            "Environmental triggers (sunlight, infections, medications)",
            "Stress can trigger or worsen flares"
        ],
        "treatment": [
            "Hydroxychloroquine (antimalarial) to control symptoms",
            "NSAIDs for joint and muscle pain",
            "Corticosteroids during flares",
            "Immunosuppressants (azathioprine, methotrexate)",
            "Belimumab (biologic therapy)",
            "Strict sun protection (SPF 50+, protective clothing)"
        ],
        "severity": "High — Chronic Systemic Disease",
        "see_doctor": "Seek medical attention promptly if you have a persistent facial rash with joint pain, fatigue, or sensitivity to sunlight. Lupus requires specialist management by a rheumatologist and/or dermatologist.",
        "emoji": "🦋"
    },

    "Melanoma": {
        "full_name": "Melanoma (Malignant Melanoma)",
        "description": "Melanoma is the most serious type of skin cancer. It develops in the melanocytes — the cells that produce melanin, the pigment that gives skin its color. Early detection is critical as melanoma can spread to other organs if not treated promptly.",
        "symptoms": [
            "Asymmetric moles or lesions",
            "Borders that are irregular or ragged",
            "Color variation within a single mole",
            "Diameter larger than 6mm (pencil eraser size)",
            "Evolving size, shape, or color over time",
            "New dark spot or mole that looks different from others"
        ],
        "causes": [
            "Excessive UV radiation exposure (sun, tanning beds)",
            "History of severe sunburns",
            "Family history of melanoma",
            "Fair skin, light hair, and light eyes",
            "Large number of moles (50+)"
        ],
        "treatment": [
            "Surgical excision (primary treatment)",
            "Sentinel lymph node biopsy",
            "Immunotherapy (checkpoint inhibitors)",
            "Targeted therapy for specific mutations",
            "Radiation therapy for advanced cases",
            "Regular skin checks for monitoring"
        ],
        "severity": "High — Potentially Life-Threatening",
        "see_doctor": "IMMEDIATELY consult a dermatologist if you notice any new, changing, or unusual moles. Follow the ABCDE rule: Asymmetry, Border irregularity, Color variation, Diameter >6mm, Evolving appearance.",
        "emoji": "⚠️"
    },

    "Psoriasis": {
        "full_name": "Psoriasis",
        "description": "Psoriasis is a chronic autoimmune condition that causes rapid skin cell buildup, resulting in thick, silvery scales and itchy, dry, red patches. It is not contagious and tends to go through cycles of flare-ups and remission.",
        "symptoms": [
            "Red patches covered with thick silvery scales",
            "Dry, cracked skin that may bleed",
            "Itching, burning, or soreness",
            "Thickened, pitted, or ridged nails",
            "Swollen and stiff joints (psoriatic arthritis)",
            "Patches on scalp, elbows, knees, and lower back"
        ],
        "causes": [
            "Autoimmune disorder (immune system attacks healthy skin cells)",
            "Genetic predisposition",
            "Triggers: stress, infections, cold weather, certain medications",
            "Smoking and heavy alcohol consumption"
        ],
        "treatment": [
            "Topical corticosteroids and vitamin D analogues",
            "Phototherapy (UVB light therapy)",
            "Systemic medications (methotrexate, cyclosporine)",
            "Biologic drugs targeting specific immune pathways",
            "Moisturizers to reduce dryness and scaling",
            "Stress management and lifestyle modifications"
        ],
        "severity": "Moderate",
        "see_doctor": "Consult a dermatologist if psoriasis covers a large area, causes significant discomfort, affects your joints, or does not respond to over-the-counter treatments.",
        "emoji": "🟠"
    },

    "Rosacea": {
        "full_name": "Rosacea",
        "description": "Rosacea is a chronic inflammatory skin condition that primarily affects the face, causing redness, visible blood vessels, and sometimes small, red, pus-filled bumps. It typically affects middle-aged women with fair skin.",
        "symptoms": [
            "Persistent facial redness (flushing)",
            "Visible blood vessels (telangiectasia) on nose and cheeks",
            "Swollen red bumps resembling acne",
            "Eye problems: dryness, irritation, swollen eyelids",
            "Burning or stinging sensation on the face",
            "Enlarged nose (rhinophyma) in severe cases"
        ],
        "causes": [
            "Exact cause unknown — likely immune system and genetics",
            "Triggers: hot drinks, spicy foods, alcohol, sun exposure",
            "Temperature extremes and wind",
            "Stress, exercise, and certain medications",
            "Demodex mites and Helicobacter pylori may play a role"
        ],
        "treatment": [
            "Topical treatments (metronidazole, azelaic acid, ivermectin)",
            "Oral antibiotics (doxycycline) for inflammation",
            "Laser and light therapy for visible blood vessels",
            "Avoiding known triggers",
            "Gentle skincare with sunscreen (SPF 30+)",
            "Beta-blockers or brimonidine for flushing"
        ],
        "severity": "Moderate",
        "see_doctor": "See a dermatologist if you have persistent facial redness, bumps, or visible blood vessels. Early treatment can prevent the condition from worsening.",
        "emoji": "🔴"
    },

    "Tinea": {
        "full_name": "Tinea (Ringworm / Fungal Infection)",
        "description": "Tinea refers to a group of common fungal skin infections caused by dermatophytes. Despite the name 'ringworm', no worm is involved. It includes tinea corporis (body), tinea pedis (athlete's foot), tinea capitis (scalp), and tinea cruris (jock itch). It creates a ring-shaped, red, itchy rash.",
        "symptoms": [
            "Ring-shaped red or silver rash with clear center",
            "Scaly, cracked, or peeling skin",
            "Itching and discomfort",
            "Slightly raised, expanding borders",
            "Athlete's foot: scaling between toes, cracked heels",
            "Scalp infection: hair loss, dandruff-like scaling"
        ],
        "causes": [
            "Dermatophyte fungi (Trichophyton, Microsporum, Epidermophyton)",
            "Spread through direct contact with infected person or animal",
            "Contact with contaminated objects (towels, clothing, floors)",
            "Warm, moist environments promote fungal growth"
        ],
        "treatment": [
            "Topical antifungal creams (clotrimazole, miconazole, terbinafine)",
            "Oral antifungal medication for scalp or severe cases",
            "Keep affected area clean and dry",
            "Avoid sharing personal items",
            "Wash clothing and bedding in hot water",
            "Treatment typically lasts 2–4 weeks"
        ],
        "severity": "Mild",
        "see_doctor": "See a doctor if the rash does not improve with OTC antifungal treatment within 2 weeks, if it spreads rapidly, or if it affects the scalp (prescription antifungals may be needed).",
        "emoji": "🍄"
    },

    "Unknown_Normal": {
        "full_name": "Normal Skin / Unknown Condition",
        "description": "The uploaded image appears to show normal, healthy skin or a condition that falls outside the scope of the 10 disease categories the AI was trained on. This class represents skin that does not show clear signs of the target conditions.",
        "symptoms": [
            "No clear signs of disease detected",
            "May be normal healthy skin",
            "Could be a rare or unrelated skin condition",
            "Image quality or angle may affect classification"
        ],
        "causes": [
            "Healthy skin with no active condition",
            "Skin condition not covered by the current model",
            "Environmental factors (dry weather, minor irritation)",
            "Temporary skin changes (mild sunburn, minor rash)"
        ],
        "treatment": [
            "Maintain a regular moisturizing routine",
            "Use sunscreen (SPF 30+) daily",
            "Stay hydrated and eat a balanced diet",
            "Consult a dermatologist if any concerning changes appear"
        ],
        "severity": "None / Informational",
        "see_doctor": "If you have any concerns about your skin, or if a spot is changing, itching, or spreading, consult a certified dermatologist for a professional evaluation.",
        "emoji": "✅"
    },

    "Vitiligo": {
        "full_name": "Vitiligo",
        "description": "Vitiligo is a condition where the skin loses its pigment cells (melanocytes), resulting in discolored patches. It can affect any area of the body and is more noticeable in people with darker skin tones. It is not contagious or life-threatening.",
        "symptoms": [
            "Patchy loss of skin color (depigmentation)",
            "White or light patches on hands, face, and body folds",
            "Premature whitening of hair, eyelashes, or eyebrows",
            "Loss of color inside the mouth and nose",
            "Patches may spread over time",
            "Sensitivity to sunlight in affected areas"
        ],
        "causes": [
            "Autoimmune destruction of melanocytes",
            "Genetic factors",
            "Triggered by sunburn, stress, or chemical exposure",
            "Associated with other autoimmune conditions (thyroid disease)"
        ],
        "treatment": [
            "Topical corticosteroids to restore pigment",
            "Calcineurin inhibitor creams (tacrolimus, pimecrolimus)",
            "Phototherapy (narrowband UVB)",
            "Depigmentation therapy for extensive vitiligo",
            "Skin grafting for stable, localized patches",
            "Cosmetic camouflage and sunscreen protection"
        ],
        "severity": "Mild (cosmetic concern, not dangerous)",
        "see_doctor": "See a dermatologist for proper diagnosis and to discuss treatment options. While not dangerous, early treatment can help slow progression and restore pigment.",
        "emoji": "⚪"
    },

    "Warts Molluscum": {
        "full_name": "Warts & Molluscum Contagiosum",
        "description": "Warts are caused by the human papillomavirus (HPV) and appear as rough, raised bumps. Molluscum contagiosum is caused by a poxvirus and presents as small, dome-shaped, pearl-like bumps. Both are contagious through direct contact.",
        "symptoms": [
            "Small, rough, grainy bumps (warts)",
            "Flesh-colored, dome-shaped papules (molluscum)",
            "Central dimple or pit in molluscum bumps",
            "Black pinpoints (clotted blood vessels) in warts",
            "Occurring on hands, fingers, feet, and face",
            "May spread to other body areas or other people"
        ],
        "causes": [
            "HPV virus (warts) — over 100 strains",
            "Poxvirus (molluscum contagiosum)",
            "Spread through direct skin-to-skin contact",
            "Weakened immune system increases susceptibility"
        ],
        "treatment": [
            "Salicylic acid application (over-the-counter)",
            "Cryotherapy (freezing with liquid nitrogen)",
            "Cantharidin application by a dermatologist",
            "Curettage (scraping) for molluscum",
            "Immune-boosting treatments (imiquimod cream)",
            "Often resolves on its own within months to years"
        ],
        "severity": "Low",
        "see_doctor": "See a doctor if warts are painful, spreading rapidly, located on the face or genitals, or if you have a weakened immune system.",
        "emoji": "🟡"
    },

    "Uncertain Prediction": {
        "full_name": "Uncertain Prediction",
        "description": "The AI model could not confidently identify the skin condition from the uploaded image. This may be because the image quality is low, the condition is not in our database, or the image does not show a clear skin condition.",
        "symptoms": [],
        "causes": [
            "Low image quality or poor lighting",
            "Condition not covered by the current model",
            "Image shows multiple overlapping conditions"
        ],
        "treatment": [
            "Please upload a clearer, well-lit photo of the affected area",
            "Consult a dermatologist for proper in-person examination"
        ],
        "severity": "Unknown",
        "see_doctor": "Since the AI could not determine the condition, please consult a dermatologist for accurate diagnosis.",
        "emoji": "❓"
    }
}


def get_disease_info(disease_name):
    """Get disease info by name, with fallback for unknown conditions."""
    return DISEASE_INFO.get(disease_name, DISEASE_INFO["Uncertain Prediction"])
