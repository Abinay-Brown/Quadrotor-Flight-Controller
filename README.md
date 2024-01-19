# Quadrotor-Flight-Controller

Flight Controller Software and Analysis Tools

+ Parts Selection:
  - Simonk Esc is used because arduino cannot operate popular BLHeli ESCs with dshot or oneshot protocol, so standard pwm is required.
  - 5inch props for standard performance and max thrust of 440g, 6inch props for ~600g thrust hight Thrust to mass ratio.
  - NRF transceiver used for telemetry and PID tuning during flight.
  - ICM20948 IMU since it comes with inbuilt magnetometer as opposed to using fake clones of HMC5883L (QMC5883L) with other IMUs.
  - BMP180 barometer for altitude control.
 
  
+ Electronics List
  - MT2204-2300kv motors
  - 12A Simonk ESC
  - 5045/6030 Props
  - NRF24L01 Trasceiver Module
  - Flysky 10 channel Transmitter and receiver
  - ICM 20948 Sparkfun 9DOF IMU (gyro+accel+mag)
  - BMP180 Barometer
  - Arduino Pro mini 328p 5V 16MHz
  - Matek systems Power Distribution Board with XT60 connector
 
+ Python-GUI
  - GUI tool for wireless motor control: To find start and stop motor pulse ranges
  - IMU plotter tool: TO plot live stability data for PID tuning

+ Madgwick Algorithm for sensor fusion:
  
