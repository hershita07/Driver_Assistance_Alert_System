# Driver_Assistance_Alert_System
## Requirements

Software: pytorch,CUDA  
Computational Environment: Edge cloud  
Hardware:  
* On Board Units (consisting GPRS module, 802.11p radio module, WiFi module, GPS module, Bluetooth module(RN4020),accelerometer,gyroscope)  
* Road Side Units(consisting GPRS module, 802.11p radio module, WiFi module, GPS module, Bluetooth module)  
* IP camera,mobile/HMI          
 
## Experiments

All the data that was transmitted and recieved from OBU to OBU or RSU-OBU and vice versa was analysed and alerts were formed accordingly with different set threshold values. So, an application was developed that could send below mentioned alerts.  
* ABRUPT LEFT
* ABRUPT RIGHT
* OVER SPEED WARNING
* EMERGENCY BREAK
* VRU ALERTS
<p align="center" width="70%">
    <img width="33%" src="https://github.com/hershita07/Pedestrian-Alert-System/blob/main/app.png">    
</p>  
Along with the application we also displayed the details about vehicles at the testbed on graphana dashboard.  
<p align="center" width="70%">
    <img width="33%" src="https://github.com/hershita07/Pedestrian-Alert-System/blob/main/grafana.png">    
</p>  


 

The connection via blutooth (RN4020)to the app did decrease the time delay that is usually faced in telegram alert generation.  
