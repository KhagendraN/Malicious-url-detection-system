from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from config import RANDOM_SEED

def preprocess_data(df, target_col='type', test_size=0.2):
    """
    Preprocess data: drop missing, encode target, split, and scale.
    
    Args:
        df (pd.DataFrame): Dataframe with features and target.
        target_col (str): Name of the target column.
        test_size (float): Proportion of test set.
        
    Returns:
        tuple: X_train, X_test, y_train, y_test, le (LabelEncoder), scaler (StandardScaler)
    """
    # Drop rows with missing values
    df = df.dropna()
    
    # Encode target
    le = LabelEncoder()
    df[target_col] = le.fit_transform(df[target_col])
    
    # Select features (drop non-numeric and target)
    X = df.drop(['url', target_col], axis=1)
    y = df[target_col]
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=RANDOM_SEED)
    
    # Scale
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test, le, scaler
