def car_info(manufacturer, model_name, **car):
    
    transportation = {
    'manufacturer'.title() : manufacturer,
    'models name'.title() : model_name
                     }
    for key,value in car.items():
        transportation[key] = value
        
    return transportation

car = car_info('subaru corportaion', 'subaru suv',
               color = 'red',
               tow_package = True)

print(car)
        
    