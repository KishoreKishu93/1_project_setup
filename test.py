from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData



customData_obj = CustomData(2.39,"Premium","J","SI2",62.2,58.0,8.51,8.47,5.32)


data =customData_obj.get_data_as_dataframe()
print(data)