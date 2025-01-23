# French Verb Conjugation Script

This script generates a conjugation table given a French verb input. It uses standard and predefined rules for conjugation patterns and auxiliary verbs to create conjugations for all subject pronouns across multiple tenses. The output is saved as an Excel file for easy reference and analysis.
Note: It generates a new .xlsx file for each verb for now. (Would come back to this later!)

---

## How to Use

1. **Install Dependencies**:
   - Ensure you have Python or Python3 installed.
   - Install the required library:
     ```bash
     pip install pandas
     ```

2. **Run the Script**:
   - Execute the script in your terminal or IDE.
   - Follow the prompts to enter:
     - Infinitive form of the verb.
     - Auxiliary verb (`avoir` or `être`).
     - Present-tense "nous" stem.
     - Participle passé.

3. **Output**:
   - The script will generate an Excel file (`verb.xlsx`) with the conjugation table.

---

## Example

### Input:
- Infinitive form: `manger`
- Auxiliary verb: `avoir`
- Nous stem: `mang`
- Participe passé: `mangé`

### Output:
Saves the result in an Excel file (`verb.xlsx`) with the following structure:

| Pronoun      | Passé Composé    | Passé Simple | Imparfait | Plus-que-parfait | Futur Simple | Futur Antérieur | Conditionnel Présent | Conditionnel Passé  |
|--------------|------------------|--------------|-----------|-------------------|--------------|-----------------|----------------------|---------------------|
| Je           | ai mangé         | mangeai      | mangeais  | avais mangé       | mangerai     | aurai mangé     | mangerais           | aurais mangé        |
| Tu           | as mangé         | mangeas      | mangeais  | avais mangé       | mangeras     | auras mangé     | mangerais           | aurais mangé        |
| Il/Elle/On   | a mangé          | mangea       | mangeait  | avait mangé       | mangera      | aura mangé      | mangerait           | aurait mangé        |
| Nous         | avons mangé      | mangeâmes    | mangions  | avions mangé      | mangerons    | aurons mangé    | mangerions          | aurions mangé       |
| Vous         | avez mangé       | mangeâtes    | mangiez   | aviez mangé       | mangerez     | aurez mangé     | mangeriez           | auriez mangé        |
| Ils/Elles    | ont mangé        | mangèrent    | mangeaient| avaient mangé     | mangeront    | auront mangé    | mangeraient         | auraient mangé      |

---

## Limitations

- Currently supports **regular verbs** only. No pronominals.
- Does not handle irregular conjugation rules for verbs like `aller`, `faire`, `venir`, etc.
- Some tense endings are hardcoded and not always correct e.g passe simple.

---

## Features

- **Dynamic Conjugation**:
  - Handles 8 French tenses: 
    - Passé Composé
    - Passé Simple
    - Imparfait
    - Plus-que-parfait
    - Futur Simple
    - Futur Antérieur
    - Conditionnel Présent
    - Conditionnel Passé
  - Supports both **avoir** and **être** auxiliary verbs.

---

## License

The code is free and open-source; available for public, personal and educational use!
