import pandas as pd

# Hardcoded auxiliary verb conjugations
auxiliary_conjugations = {
    'avoir': {
        'present': ['ai', 'as', 'a', 'avons', 'avez', 'ont'],
        'imparfait': ['avais', 'avais', 'avait', 'avions', 'aviez', 'avaient'],
        'futur': ['aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront'],
        'conditionnel': ['aurais', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient']
    },
    'etre': {
        'present': ['suis', 'es', 'est', 'sommes', 'êtes', 'sont'],
        'imparfait': ['étais', 'étais', 'était', 'étions', 'étiez', 'étaient'],
        'futur': ['serai', 'seras', 'sera', 'serons', 'serez', 'seront'],
        'conditionnel': ['serais', 'serais', 'serait', 'serions', 'seriez', 'seraient']
    }
}

# Hardcoded endings
passe_simple_endings = ['ai', 'as', 'a', 'âmes', 'âtes', 'èrent']
imparfait_endings = ['ais', 'ais', 'ait', 'ions', 'iez', 'aient']
futur_simple_endings = ['ai', 'as', 'a', 'ons', 'ez', 'ont']
conditionnel_endings = imparfait_endings


def generate_conjugation(auxiliary_type, nous_stem, participe_passe, infinitif_stem):
    aux = auxiliary_conjugations[auxiliary_type]
    
    # Passé Composé
    passe_compose = [f"{aux['present'][i]} {participe_passe}" for i in range(6)]
    
    # Passé Simple
    passe_simple = [f"{nous_stem}{passe_simple_endings[i]}" for i in range(6)]
    
    # Imparfait
    imparfait = [f"{nous_stem}{imparfait_endings[i]}" for i in range(6)]
    
    # Plus-que-parfait
    plus_que_parfait = [f"{aux['imparfait'][i]} {participe_passe}" for i in range(6)]
    
    # Futur Simple
    futur_simple = [f"{infinitif_stem}{futur_simple_endings[i]}" for i in range(6)]
    
    # Futur Antérieur
    futur_anterieur = [f"{aux['futur'][i]} {participe_passe}" for i in range(6)]
    
    # Conditionnel Présent
    conditionnel_present = [f"{infinitif_stem}{conditionnel_endings[i]}" for i in range(6)]
    
    # Conditionnel Passé
    conditionnel_passe = [f"{aux['conditionnel'][i]} {participe_passe}" for i in range(6)]
    
    return {
        'Passé Composé': passe_compose,
        'Passé Simple': passe_simple,
        'Imparfait': imparfait,
        'Plus-que-parfait': plus_que_parfait,
        'Futur Simple': futur_simple,
        'Futur Antérieur': futur_anterieur,
        'Conditionnel Présent': conditionnel_present,
        'Conditionnel Passé': conditionnel_passe
    }

# Input verb
infinitif_stem = input("Enter the infinitive form (e.g., 'manger'): ")
auxiliary_type = input("\nEnter auxiliary verb (avoir/etre): ")
nous_stem = input("\nEnter the 'nous' stem in present tense (e.g, 'mang' for 'manger'): ")
participe_passe = input("\nEnter the participe passé: ")

# Generate conjugations
conjugations = generate_conjugation(auxiliary_type, nous_stem, participe_passe, infinitif_stem)

# New structure: Pronouns as rows, Tenses as columns
pronouns = ['Je', 'Tu', 'Il/Elle/On', 'Nous', 'Vous', 'Ils/Elles']
tenses = ['Passé Composé', 'Passé Simple', 'Imparfait', 'Plus-que-parfait', 'Futur Simple', 'Futur Antérieur', 'Conditionnel Présent', 'Conditionnel Passé']
df = pd.DataFrame(index=pronouns, columns=tenses)

# Add conjugations to DataFrame
for tense in tenses:
    df[tense] = conjugations[tense]

# Save to Excel file
df.to_excel('verb.xlsx')
print("Conjugations written to verb.xlsx")
