import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# TODO: Modify this list to include the numerical columns
NUMERICAL_VARS = ['pclass','age','sibsp','parch','fare']

# Crear custom transformer
class MissingIndicator(BaseEstimator, TransformerMixin):

    def __init__(self, variables):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y):
        return self

    def transform(self, X):
        col_names = [f"{x}_nan" for x in NUMERICAL_VARS]
        aux = pd.DataFrame(X[self.variables]).isnull()*1
        aux.columns = col_names
        X = pd.concat([X, aux], axis=1)

        return X


# Leer el csv sin aplicar transformaciones
df = pd.read_csv("raw-data.csv")

# Imprimir los primeros datos
print(df.head(10))

mi = MissingIndicator(variables=NUMERICAL_VARS)
# Aplicar las transformaciones
df_mi = mi.transform(df)

# Imprimir resultados despues de las transformaciones
print(df_mi.head(20))