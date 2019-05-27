from sklearn import preprocessing
encoder = preprocessing.LabelEncoder()
encoder.fit(["human","tree","rock","scissors"])

