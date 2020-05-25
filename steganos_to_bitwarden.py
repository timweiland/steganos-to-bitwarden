import pandas as pd

input_path = input("Steganos CSV input path: ")
output_path = input("Bitwarden CSV output path: ")

data = pd.read_csv(input_path, skipinitialspace=True)
df = data.copy()

# Drop unnecessary data
empty_cols = [col for col in df.columns if df[col].isnull().all()]
df = df.loc[df["type"] == 5]
df.drop(empty_cols,
        axis=1,
        inplace=True)
cols_to_drop=["last_password_change", "lastmodified", "type", "tags", "keyword", "autofill", "autofillenabled", "category", "username_field", "password_field"]
df = df.drop(columns=cols_to_drop)
df = df.dropna(how="all", axis=1)

# Add Bitwarden-specific columns
df["folder"]=''
df["favorite"]=''
df["type"]="login"
df["fields"]=''
df["login_totp"]=''

df = df.rename(columns={"title": "name", "username": "login_username", "password":"login_password","url":"login_uri","note":"notes"})
cols = ['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'login_uri', 'login_username','login_password','login_totp']
df = df[cols]

# We're done!
df.to_csv(output_path,index=False, encoding='utf-8')
