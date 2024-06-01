import docx
import pandas as pd

def model():
    healthy_indices = set(list(range(1, 16)) + list(range(26, 31)))
    ill_indices = set(range(1, 41)) - healthy_indices


def create_docx():
    # Create a data frame
    si_units = {
        'Name': ['Second', 'Metre', 'Kilogram', 'Ampere', 'Kelvin', 'Mole', 'Candela'],
        'Symbol': ['s', 'm', 'kg', 'A', 'K', 'mol', 'cd'],
    '    Quantity': [
            'Time', 'Length', 'Mass', 'Electric current', 'Thermodynamic temperature',
            'Amount of substance', 'Luminous intensity'
        ],
        'Emojii': ['🕒', '📏', '🏋️', '⚡', '🌡️', '⚛️', '💡']
    }
    df = pd.DataFrame(si_units)

    # Initialise the Word document
    doc = docx.Document()

    # Initialise the table
    t = doc.add_table(rows=df.shape[0], cols=df.shape[1])

    # Add the body of the data frame to the table
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            cell = df.iat[i, j]
            t.cell(i, j).text = str(cell)

    # Save the Word doc
    doc.save('table1.docx')
