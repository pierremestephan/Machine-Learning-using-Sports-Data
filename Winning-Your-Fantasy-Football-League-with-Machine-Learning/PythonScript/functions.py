import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

def modeleval(predictions,y_test):
    # Difference between Predicted and Actual
    errors = abs(predictions - y_test)
    # Root Mean Square Error
    rmse = np.sqrt(mean_squared_error(y_test,predictions))
    # Residual Sum Squared 
    r_squared = 1 - np.sum((y_test - predictions)**2)/sum((y_test - np.mean(y_test))**2)
    # Mean Absolute Error
    mae = round(np.mean(errors), 2)
    # Mean Absolute Percent Error
    mape = 100 * np.mean(errors) / np.mean(y_test)
    # Accuracy of Random Forest
    accuracy = 100 - np.mean(mape)
    metrics = pd.DataFrame(data = {
        'rmse': [rmse],
        'r^2': [r_squared],
        'mae': [mae],
        'mape': [mape],
        'accuracy': [accuracy]})
    return metrics